"""CLI utilities for glaip-sdk.

Authors:
    Raymond Christopher (raymond.christopher@gdplabs.id)
"""

from __future__ import annotations

import io
import json
import os
import platform
import shlex
import shutil
import subprocess
import tempfile
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

import click
from rich.console import Console, Group
from rich.markdown import Markdown
from rich.pretty import Pretty
from rich.text import Text

# Optional interactive deps (fuzzy palette)
try:
    from prompt_toolkit.completion import Completion
    from prompt_toolkit.shortcuts import prompt

    _HAS_PTK = True
except Exception:
    _HAS_PTK = False

try:
    import questionary
except Exception:
    questionary = None

if TYPE_CHECKING:
    from glaip_sdk import Client
from glaip_sdk.cli.commands.configure import load_config
from glaip_sdk.rich_components import AIPPanel, AIPTable
from glaip_sdk.utils import is_uuid
from glaip_sdk.utils.rendering.renderer import (
    CapturingConsole,
    RendererConfig,
    RichStreamRenderer,
)

console = Console()


# ----------------------------- Context helpers ---------------------------- #


def get_ctx_value(ctx: Any, key: str, default: Any = None) -> Any:
    """Safely resolve a value from click's context object."""
    if ctx is None:
        return default

    obj = getattr(ctx, "obj", None)
    if obj is None:
        return default

    if isinstance(obj, dict):
        return obj.get(key, default)

    getter = getattr(obj, "get", None)
    if callable(getter):
        try:
            return getter(key, default)
        except TypeError:
            return default

    return getattr(obj, key, default) if hasattr(obj, key) else default


# ----------------------------- Pager helpers ----------------------------- #


def _prepare_pager_env(
    clear_on_exit: bool = True,
) -> None:  # pragma: no cover - terminal UI setup
    """
    Configure LESS flags for a predictable, high-quality UX:
      -R  : pass ANSI color escapes
      -S  : chop long lines (horizontal scroll with ←/→)
    (No -F, no -X) so we open a full-screen pager and clear on exit.
    Toggle wrapping with AIP_PAGER_WRAP=1 to drop -S.
    Power users can override via AIP_LESS_FLAGS.
    """
    os.environ.pop("LESSSECURE", None)
    if os.getenv("LESS") is None:
        want_wrap = os.getenv("AIP_PAGER_WRAP", "0") == "1"
        base = "-R" if want_wrap else "-RS"
        default_flags = base if clear_on_exit else (base + "FX")
        os.environ["LESS"] = os.getenv("AIP_LESS_FLAGS", default_flags)


def _render_ansi(
    renderable: Any,
) -> str:  # pragma: no cover - rendering requires real terminal
    """Render a Rich renderable to an ANSI string suitable for piping to 'less'."""
    buf = io.StringIO()
    tmp_console = Console(
        file=buf,
        force_terminal=True,
        color_system=console.color_system or "auto",
        width=console.size.width or 100,
        legacy_windows=False,
        soft_wrap=False,
        record=False,
    )
    tmp_console.print(renderable)
    return buf.getvalue()


def _pager_header() -> str:  # pragma: no cover - terminal UI helper
    v = (os.getenv("AIP_PAGER_HEADER", "1") or "1").strip().lower()
    if v in {"0", "false", "off"}:
        return ""
    return "\n".join(
        [
            "TABLE VIEW — ↑/↓ PgUp/PgDn, ←/→ horiz scroll (with -S), /search, n/N next/prev, h help, q quit",
            "───────────────────────────────────────────────────────────────────────────────────────────────",
            "",
        ]
    )


def _should_use_pager() -> bool:
    """Check if we should attempt to use a system pager."""
    if not (console.is_terminal and os.isatty(1)):
        return False
    if (os.getenv("TERM") or "").lower() == "dumb":
        return False
    return True


def _resolve_pager_command() -> tuple[list[str] | None, str | None]:
    """Resolve the pager command and path to use."""
    pager_cmd = None
    pager_env = os.getenv("PAGER")
    if pager_env:
        parts = shlex.split(pager_env)
        if parts and os.path.basename(parts[0]).lower() == "less":
            pager_cmd = parts

    less_path = shutil.which("less")
    return pager_cmd, less_path


def _run_less_pager(
    pager_cmd: list[str] | None, less_path: str | None, tmp_path: str
) -> None:
    """Run less pager with appropriate command and flags."""
    if pager_cmd:
        subprocess.run([*pager_cmd, tmp_path], check=False)
    else:
        flags = os.getenv("LESS", "-RS").split()
        subprocess.run([less_path, *flags, tmp_path], check=False)


def _run_more_pager(tmp_path: str) -> None:
    """Run more pager as fallback."""
    more_path = shutil.which("more")
    if more_path:
        subprocess.run([more_path, tmp_path], check=False)
    else:
        raise FileNotFoundError("more command not found")


def _run_pager_with_temp_file(
    pager_runner: Callable[[str], None], ansi_text: str
) -> bool:
    """Run a pager using a temporary file containing the content."""
    _prepare_pager_env(clear_on_exit=True)
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tmp:
        tmp.write(_pager_header())
        tmp.write(ansi_text)
        tmp_path = tmp.name
    try:
        pager_runner(tmp_path)
        return True
    except Exception:
        # If pager fails, return False to indicate paging was not successful
        return False
    finally:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass


def _page_with_system_pager(
    ansi_text: str,
) -> bool:  # pragma: no cover - spawns real pager
    """Prefer 'less' with a temp file so stdin remains the TTY."""
    if not _should_use_pager():
        return False

    pager_cmd, less_path = _resolve_pager_command()

    if pager_cmd or less_path:
        return _run_pager_with_temp_file(
            lambda tmp_path: _run_less_pager(pager_cmd, less_path, tmp_path), ansi_text
        )

    # Windows 'more' is poor with ANSI; let Rich fallback handle it
    if platform.system().lower().startswith("win"):
        return False

    # POSIX 'more' fallback (may or may not honor ANSI)
    return _run_pager_with_temp_file(_run_more_pager, ansi_text)


def _get_view(ctx: Any) -> str:
    view = get_ctx_value(ctx, "view")
    if view:
        return view

    fallback = get_ctx_value(ctx, "format")
    return fallback or "rich"


# ----------------------------- Client config ----------------------------- #


def get_client(ctx: Any) -> Client:
    """Get configured client from context, env, and config file (ctx > env > file)."""
    from glaip_sdk import Client

    file_config = load_config() or {}
    context_config_obj = getattr(ctx, "obj", None)
    context_config = context_config_obj or {}

    raw_timeout = os.getenv("AIP_TIMEOUT", "0") or "0"
    try:
        timeout_value = float(raw_timeout)
    except ValueError:
        timeout_value = None

    env_config = {
        "api_url": os.getenv("AIP_API_URL"),
        "api_key": os.getenv("AIP_API_KEY"),
        "timeout": timeout_value if timeout_value else None,
    }
    env_config = {k: v for k, v in env_config.items() if v not in (None, "", 0)}

    # Merge config sources: context > env > file
    config = {
        **file_config,
        **env_config,
        **{k: v for k, v in context_config.items() if v is not None},
    }

    if not config.get("api_url") or not config.get("api_key"):
        raise click.ClickException(
            "Missing api_url/api_key. Run `aip configure` or set AIP_* env vars."
        )

    return Client(
        api_url=config.get("api_url"),
        api_key=config.get("api_key"),
        timeout=float(config.get("timeout") or 30.0),
    )


# ----------------------------- Secret masking ---------------------------- #

_DEFAULT_MASK_FIELDS = {
    "api_key",
    "apikey",
    "token",
    "access_token",
    "secret",
    "client_secret",
    "password",
    "private_key",
    "bearer",
}


def _mask_value(v: Any) -> str:
    s = str(v)
    if len(s) <= 8:
        return "••••"
    return f"{s[:4]}••••••••{s[-4:]}"


def _mask_any(value: Any, mask_fields: set[str]) -> Any:
    """Recursively mask sensitive fields in mappings / lists."""

    if isinstance(value, dict):
        masked: dict[Any, Any] = {}
        for key, raw in value.items():
            if isinstance(key, str) and key.lower() in mask_fields and raw is not None:
                masked[key] = _mask_value(raw)
            else:
                masked[key] = _mask_any(raw, mask_fields)
        return masked

    if isinstance(value, list):
        return [_mask_any(item, mask_fields) for item in value]

    return value


def _maybe_mask_row(row: dict[str, Any], mask_fields: set[str]) -> dict[str, Any]:
    """Mask a single row (legacy function, now uses _mask_any)."""
    if not mask_fields:
        return row
    return _mask_any(row, mask_fields)


def _resolve_mask_fields() -> set[str]:
    if os.getenv("AIP_MASK_OFF", "0") in ("1", "true", "on", "yes"):
        return set()
    env_fields = (os.getenv("AIP_MASK_FIELDS") or "").strip()
    if env_fields:
        parts = [p.strip().lower() for p in env_fields.split(",") if p.strip()]
        return set(parts)
    return set(_DEFAULT_MASK_FIELDS)


# ----------------------------- Fuzzy palette ----------------------------- #


def _extract_display_fields(row: dict[str, Any]) -> tuple[str, str, str, str]:
    """Extract display fields from row data."""
    name = str(row.get("name", "")).strip()
    _id = str(row.get("id", "")).strip()
    type_ = str(row.get("type", "")).strip()
    fw = str(row.get("framework", "")).strip()
    return name, _id, type_, fw


def _build_primary_parts(name: str, type_: str, fw: str) -> list[str]:
    """Build primary display parts from name, type, and framework."""
    parts = []
    if name:
        parts.append(name)
    if type_:
        parts.append(type_)
    if fw:
        parts.append(fw)
    return parts


def _get_fallback_columns(columns: list[tuple]) -> list[tuple]:
    """Get first two visible columns for fallback display."""
    return columns[:2]


def _is_standard_field(k: str) -> bool:
    """Check if field is a standard field to skip."""
    return k in ("id", "name", "type", "framework")


def _extract_fallback_values(row: dict[str, Any], columns: list[tuple]) -> list[str]:
    """Extract fallback values from columns."""
    fallback_parts = []
    for k, _hdr, _style, _w in columns:
        if _is_standard_field(k):
            continue
        val = str(row.get(k, "")).strip()
        if val:
            fallback_parts.append(val)
        if len(fallback_parts) >= 2:
            break
    return fallback_parts


def _build_display_parts(
    name: str, _id: str, type_: str, fw: str, row: dict[str, Any], columns: list[tuple]
) -> list[str]:
    """Build complete display parts list."""
    parts = _build_primary_parts(name, type_, fw)

    if not parts:
        # Use fallback columns
        fallback_columns = _get_fallback_columns(columns)
        parts.extend(_extract_fallback_values(row, fallback_columns))

    if _id:
        parts.append(f"[{_id}]")

    return parts


def _row_display(row: dict[str, Any], columns: list[tuple]) -> str:
    """
    Build a compact text label for the palette.
    Prefers: name • type • framework • [id] (when available)
    Falls back to first 2 columns + [id].
    """
    name, _id, type_, fw = _extract_display_fields(row)
    parts = _build_display_parts(name, _id, type_, fw, row, columns)
    return " • ".join(parts) if parts else (_id or "(row)")


def _check_fuzzy_pick_requirements() -> bool:
    """Check if fuzzy picking requirements are met."""
    return _HAS_PTK and console.is_terminal and os.isatty(1)


def _build_unique_labels(
    rows: list[dict[str, Any]], columns: list[tuple]
) -> tuple[list[str], dict[str, dict[str, Any]]]:
    """Build unique display labels and reverse mapping."""
    labels = []
    by_label: dict[str, dict[str, Any]] = {}

    for r in rows:
        label = _row_display(r, columns)
        # Ensure uniqueness: if duplicate, suffix with …#n
        if label in by_label:
            i = 2
            base = label
            while f"{base} #{i}" in by_label:
                i += 1
            label = f"{base} #{i}"
        labels.append(label)
        by_label[label] = r

    return labels, by_label


class _FuzzyCompleter:
    """Fuzzy completer for prompt_toolkit."""

    def __init__(self, words: list[str]) -> None:
        self.words = words

    def get_completions(self, document: Any, _complete_event: Any) -> Any:
        word = document.get_word_before_cursor()
        if not word:
            return

        word_lower = word.lower()
        for label in self.words:
            label_lower = label.lower()
            if self._fuzzy_match(word_lower, label_lower):
                yield Completion(label, start_position=-len(word))

    def _fuzzy_match(self, search: str, target: str) -> bool:
        """True fuzzy matching: checks if all characters in search appear in order in target."""
        if not search:
            return True

        search_idx = 0
        for char in target:
            if search_idx < len(search) and search[search_idx] == char:
                search_idx += 1
                if search_idx == len(search):
                    return True
        return False


def _perform_fuzzy_search(
    answer: str, labels: list[str], by_label: dict[str, dict[str, Any]]
) -> dict[str, Any] | None:
    """Perform fuzzy search fallback and return best match."""
    # Exact label match
    if answer in by_label:
        return by_label[answer]

    # Fuzzy search fallback
    best_match = None
    best_score = -1

    for label in labels:
        score = _fuzzy_score(answer.lower(), label.lower())
        if score > best_score:
            best_score = score
            best_match = label

    return by_label[best_match] if best_match and best_score > 0 else None


def _fuzzy_pick(
    rows: list[dict[str, Any]], columns: list[tuple], title: str
) -> dict[str, Any] | None:  # pragma: no cover - requires interactive prompt toolkit
    """
    Open a minimal fuzzy palette using prompt_toolkit.
    Returns the selected row (dict) or None if cancelled/missing deps.
    """
    if not _check_fuzzy_pick_requirements():
        return None

    # Build display labels and mapping
    labels, by_label = _build_unique_labels(rows, columns)

    # Create fuzzy completer
    completer = _FuzzyCompleter(labels)

    try:
        answer = prompt(
            message=f"Find {title.rstrip('s')}: ",
            completer=completer,
            complete_in_thread=True,
            complete_while_typing=True,
        )
    except (KeyboardInterrupt, EOFError):
        return None

    return _perform_fuzzy_search(answer, labels, by_label) if answer else None


def _fuzzy_score(search: str, target: str) -> int:
    """
    Calculate fuzzy match score.
    Higher score = better match.
    Returns -1 if no match possible.
    """
    if not search:
        return 0

    # Check if it's a fuzzy match first
    search_idx = 0
    for char in target:
        if search_idx < len(search) and search[search_idx] == char:
            search_idx += 1
            if search_idx == len(search):
                break

    if search_idx < len(search):
        return -1  # Not a fuzzy match

    # Calculate score based on:
    # 1. Exact substring match gets bonus points
    # 2. Consecutive character matches get bonus points
    # 3. Shorter search terms get bonus points

    score = 0

    # Exact substring bonus
    if search.lower() in target.lower():
        score += 100

    # Consecutive character bonus
    consecutive = 0
    max_consecutive = 0
    search_idx = 0
    for char in target:
        if search_idx < len(search) and search[search_idx] == char:
            consecutive += 1
            max_consecutive = max(max_consecutive, consecutive)
            search_idx += 1
        else:
            consecutive = 0

    score += max_consecutive * 10

    # Length bonus (shorter searches get higher scores)
    score += (len(target) - len(search)) * 2

    return score


# ----------------------------- Pretty outputs ---------------------------- #


def _coerce_result_payload(result: Any) -> Any:
    try:
        to_dict = getattr(result, "to_dict", None)
        if callable(to_dict):
            return to_dict()
    except Exception:
        return result
    return result


def _apply_mask_if_configured(payload: Any) -> Any:
    mask_fields = _resolve_mask_fields()
    if not mask_fields:
        return payload
    try:
        return _mask_any(payload, mask_fields)
    except Exception:
        return payload


def _ensure_displayable(payload: Any) -> Any:
    if isinstance(payload, dict | list | str | int | float | bool) or payload is None:
        return payload

    if hasattr(payload, "__dict__"):
        try:
            return dict(payload)
        except Exception:
            try:
                return dict(payload.__dict__)
            except Exception:
                pass

    try:
        return str(payload)
    except Exception:
        return repr(payload)


def _render_markdown_output(data: Any) -> None:
    try:
        console.print(Markdown(str(data)))
    except ImportError:
        click.echo(str(data))


def output_result(
    ctx: Any,
    result: Any,
    title: str = "Result",
    panel_title: str | None = None,
    success_message: str | None = None,
) -> None:
    fmt = _get_view(ctx)

    data = _coerce_result_payload(result)
    data = _apply_mask_if_configured(data)
    data = _ensure_displayable(data)

    if fmt == "json":
        click.echo(json.dumps(data, indent=2, default=str))
        return

    if fmt == "plain":
        click.echo(str(data))
        return

    if fmt == "md":
        _render_markdown_output(data)
        return

    if success_message:
        console.print(Text(f"[green]✅ {success_message}[/green]"))

    if panel_title:
        console.print(
            AIPPanel(
                Pretty(data),
                title=panel_title,
                border_style="blue",
            )
        )
    else:
        console.print(Text(f"[cyan]{title}:[/cyan]"))
        console.print(Pretty(data))


# ----------------------------- List rendering ---------------------------- #

# Threshold no longer used - fuzzy palette is always default for TTY
# _PICK_THRESHOLD = int(os.getenv("AIP_PICK_THRESHOLD", "5") or "5")


def _normalise_rows(
    items: list[Any], transform_func: Callable[[Any], dict[str, Any]] | None
) -> list[dict[str, Any]]:
    try:
        rows: list[dict[str, Any]] = []
        for item in items:
            if transform_func:
                rows.append(transform_func(item))
            elif hasattr(item, "to_dict"):
                rows.append(item.to_dict())
            elif hasattr(item, "__dict__"):
                rows.append(vars(item))
            elif isinstance(item, dict):
                rows.append(item)
            else:
                rows.append({"value": item})
        return rows
    except Exception:
        return []


def _mask_rows_if_configured(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    mask_fields = _resolve_mask_fields()
    if not mask_fields:
        return rows
    try:
        return [_maybe_mask_row(row, mask_fields) for row in rows]
    except Exception:
        return rows


def _render_plain_list(
    rows: list[dict[str, Any]], title: str, columns: list[tuple]
) -> None:
    if not rows:
        click.echo(f"No {title.lower()} found.")
        return
    for row in rows:
        row_str = " | ".join(str(row.get(key, "N/A")) for key, _, _, _ in columns)
        click.echo(row_str)


def _render_markdown_list(
    rows: list[dict[str, Any]], title: str, columns: list[tuple]
) -> None:
    if not rows:
        click.echo(f"No {title.lower()} found.")
        return
    headers = [header for _, header, _, _ in columns]
    click.echo(f"| {' | '.join(headers)} |")
    click.echo(f"| {' | '.join('---' for _ in headers)} |")
    for row in rows:
        row_str = " | ".join(str(row.get(key, "N/A")) for key, _, _, _ in columns)
        click.echo(f"| {row_str} |")


def _should_sort_rows(rows: list[dict[str, Any]]) -> bool:
    return (
        os.getenv("AIP_TABLE_NO_SORT", "0") not in ("1", "true", "on")
        and rows
        and isinstance(rows[0], dict)
        and "name" in rows[0]
    )


def _create_table(columns: list[tuple[str, str, str, int | None]], title: str) -> Any:
    table = AIPTable(title=title, expand=True)
    for _key, header, style, width in columns:
        table.add_column(header, style=style, width=width)
    return table


def _build_table_group(
    rows: list[dict[str, Any]], columns: list[tuple], title: str
) -> Group:
    table = _create_table(columns, title)
    for row in rows:
        table.add_row(*[str(row.get(key, "N/A")) for key, _, _, _ in columns])
    footer = Text(f"\n[dim]Total {len(rows)} items[/dim]")
    return Group(table, footer)


def _should_page_output(row_count: int, is_tty: bool) -> bool:
    pager_env = (os.getenv("AIP_PAGER", "auto") or "auto").lower()
    if pager_env in ("0", "off", "false"):
        return False
    if pager_env in ("1", "on", "true"):
        return is_tty
    try:
        term_h = console.size.height or 24
        approx_lines = 5 + row_count
        return is_tty and (approx_lines >= term_h * 0.5)
    except Exception:
        return is_tty


def _handle_json_output(items: list[Any], rows: list[dict[str, Any]]) -> None:
    """Handle JSON output format."""
    data = (
        rows
        if rows
        else [it.to_dict() if hasattr(it, "to_dict") else it for it in items]
    )
    click.echo(json.dumps(data, indent=2, default=str))


def _handle_plain_output(
    rows: list[dict[str, Any]], title: str, columns: list[tuple]
) -> None:
    """Handle plain text output format."""
    _render_plain_list(rows, title, columns)


def _handle_markdown_output(
    rows: list[dict[str, Any]], title: str, columns: list[tuple]
) -> None:
    """Handle markdown output format."""
    _render_markdown_list(rows, title, columns)


def _handle_empty_items(title: str) -> None:
    """Handle case when no items are found."""
    console.print(Text(f"[yellow]No {title.lower()} found.[/yellow]"))


def _handle_fuzzy_pick_selection(
    rows: list[dict[str, Any]], columns: list[tuple], title: str
) -> bool:
    """Handle fuzzy picker selection, returns True if selection was made."""
    picked = (
        _fuzzy_pick(rows, columns, title)
        if console.is_terminal and os.isatty(1)
        else None
    )
    if picked:
        table = _create_table(columns, title)
        table.add_row(*[str(picked.get(key, "N/A")) for key, _, _, _ in columns])
        console.print(table)
        console.print(Text("\n[dim]Tip: use `aip agents get <ID>` for details[/dim]"))
        return True
    return False


def _handle_table_output(
    rows: list[dict[str, Any]], columns: list[tuple], title: str
) -> None:
    """Handle table output with paging."""
    content = _build_table_group(rows, columns, title)
    if _should_page_output(len(rows), console.is_terminal and os.isatty(1)):
        ansi = _render_ansi(content)
        if not _page_with_system_pager(ansi):
            with console.pager(styles=True):
                console.print(content)
    else:
        console.print(content)


def output_list(
    ctx: Any,
    items: list[Any],
    title: str,
    columns: list[tuple[str, str, str, int | None]],
    transform_func: Callable | None = None,
) -> None:
    """Display a list with fuzzy palette by default on TTY, Rich table as fallback."""
    fmt = _get_view(ctx)
    rows = _normalise_rows(items, transform_func)
    rows = _mask_rows_if_configured(rows)

    if fmt == "json":
        _handle_json_output(items, rows)
        return

    if fmt == "plain":
        _handle_plain_output(rows, title, columns)
        return

    if fmt == "md":
        _handle_markdown_output(rows, title, columns)
        return

    if not items:
        _handle_empty_items(title)
        return

    if _should_sort_rows(rows):
        try:
            rows = sorted(rows, key=lambda r: str(r.get("name", "")).lower())
        except Exception:
            pass

    if _handle_fuzzy_pick_selection(rows, columns, title):
        return

    _handle_table_output(rows, columns, title)


# ------------------------- Output flags decorator ------------------------ #


def _set_view(ctx: Any, _param: Any, value: str) -> None:
    if not value:
        return
    ctx.ensure_object(dict)
    ctx.obj["view"] = value


def _set_json(ctx: Any, _param: Any, value: bool) -> None:
    if not value:
        return
    ctx.ensure_object(dict)
    ctx.obj["view"] = "json"


def output_flags() -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator to allow output format flags on any subcommand."""

    def decorator(f: Callable[..., Any]) -> Callable[..., Any]:
        f = click.option(
            "--json",
            "json_mode",
            is_flag=True,
            expose_value=False,
            help="Shortcut for --view json",
            callback=_set_json,
        )(f)
        f = click.option(
            "-o",
            "--output",
            "--view",
            "view_opt",
            type=click.Choice(["rich", "plain", "json", "md"]),
            expose_value=False,
            help="Output format",
            callback=_set_view,
        )(f)
        return f

    return decorator


# ------------------------- Ambiguity handling --------------------------- #


def coerce_to_row(item: Any, keys: list[str]) -> dict[str, Any]:
    """Coerce an item (dict or object) to a row dict with specified keys.

    Args:
        item: The item to coerce (dict or object with attributes)
        keys: List of keys/attribute names to extract

    Returns:
        Dict with the extracted values, "N/A" for missing values
    """
    result = {}
    for key in keys:
        if isinstance(item, dict):
            value = item.get(key, "N/A")
        else:
            value = getattr(item, key, "N/A")
        result[key] = str(value) if value is not None else "N/A"
    return result


def build_renderer(
    _ctx: Any,
    *,
    save_path: str | os.PathLike[str] | None,
    theme: str = "dark",
    verbose: bool = False,
    _tty_enabled: bool = True,
    live: bool | None = None,
    snapshots: bool | None = None,
) -> tuple[RichStreamRenderer, Console | CapturingConsole]:
    """Build renderer and capturing console for CLI commands.

    Args:
        ctx: Click context
        save_path: Path to save output to (enables capturing)
        theme: Color theme ("dark" or "light")
        verbose: Whether to enable verbose mode
        tty_enabled: Whether TTY is available

    Returns:
        Tuple of (renderer, capturing_console)
    """
    # Use capturing console if saving output
    working_console = console
    if save_path:
        working_console = CapturingConsole(console, capture=True)

    # Configure renderer based on verbose mode and explicit overrides
    if live is None:
        live_enabled = not verbose  # Disable live mode in verbose (unless overridden)
    else:
        live_enabled = bool(live)

    renderer_cfg = RendererConfig(
        theme=theme,
        style="debug" if verbose else "pretty",
        live=live_enabled,
        show_delegate_tool_panels=True,
        append_finished_snapshots=bool(snapshots)
        if snapshots is not None
        else RendererConfig.append_finished_snapshots,
    )

    # Create the renderer instance
    renderer = RichStreamRenderer(
        working_console.original_console
        if isinstance(working_console, CapturingConsole)
        else working_console,
        cfg=renderer_cfg,
        verbose=verbose,
    )

    return renderer, working_console


def _build_resource_labels(resources: list[Any]) -> tuple[list[str], dict[str, Any]]:
    """Build unique display labels for resources."""
    labels = []
    by_label: dict[str, Any] = {}

    for resource in resources:
        name = getattr(resource, "name", "Unknown")
        _id = getattr(resource, "id", "Unknown")

        # Create display label
        label_parts = []
        if name and name != "Unknown":
            label_parts.append(name)
        label_parts.append(f"[{_id[:8]}...]")  # Show first 8 chars of ID
        label = " • ".join(label_parts)

        # Ensure uniqueness
        if label in by_label:
            i = 2
            base = label
            while f"{base} #{i}" in by_label:
                i += 1
            label = f"{base} #{i}"

        labels.append(label)
        by_label[label] = resource

    return labels, by_label


def _fuzzy_pick_for_resources(
    resources: list[Any], resource_type: str, _search_term: str
) -> Any | None:  # pragma: no cover - interactive selection helper
    """
    Fuzzy picker for resource objects, similar to _fuzzy_pick but without column dependencies.

    Args:
        resources: List of resource objects to choose from
        resource_type: Type of resource (e.g., "agent", "tool")
        search_term: The search term that led to multiple matches

    Returns:
        Selected resource object or None if cancelled/no selection
    """
    if not _check_fuzzy_pick_requirements():
        return None

    # Build labels and mapping
    labels, by_label = _build_resource_labels(resources)

    # Create fuzzy completer
    completer = _FuzzyCompleter(labels)

    try:
        answer = prompt(
            message=f"Find 🤖 {resource_type.title()}: ",
            completer=completer,
            complete_in_thread=True,
            complete_while_typing=True,
        )
    except (KeyboardInterrupt, EOFError):
        return None

    return _perform_fuzzy_search(answer, labels, by_label) if answer else None


def _resolve_by_id(ref: str, get_by_id: Callable) -> Any | None:
    """Resolve resource by UUID if ref is a valid UUID."""
    if is_uuid(ref):
        return get_by_id(ref)
    return None


def _resolve_by_name_multiple_with_select(matches: list[Any], select: int) -> Any:
    """Resolve multiple matches using select parameter."""
    idx = int(select) - 1
    if not (0 <= idx < len(matches)):
        raise click.ClickException(f"--select must be 1..{len(matches)}")
    return matches[idx]


def _resolve_by_name_multiple_fuzzy(
    ctx: Any, ref: str, matches: list[Any], label: str
) -> Any:
    """Resolve multiple matches using fuzzy picker interface."""
    picked = _fuzzy_pick_for_resources(matches, label.lower(), ref)
    if picked:
        return picked
    # Fallback to original ambiguity handler if fuzzy picker fails
    return handle_ambiguous_resource(ctx, label.lower(), ref, matches)


def _resolve_by_name_multiple_questionary(
    ctx: Any, ref: str, matches: list[Any], label: str
) -> Any:
    """Resolve multiple matches using questionary interface."""
    return handle_ambiguous_resource(ctx, label.lower(), ref, matches)


def resolve_resource(
    ctx: Any,
    ref: str,
    *,
    get_by_id: Callable,
    find_by_name: Callable,
    label: str,
    select: int | None = None,
    interface_preference: str = "fuzzy",
) -> Any | None:
    """Resolve resource reference (ID or name) with ambiguity handling.

    Args:
        ctx: Click context
        ref: Resource reference (ID or name)
        get_by_id: Function to get resource by ID
        find_by_name: Function to find resources by name
        label: Resource type label for error messages
        select: Optional selection index for ambiguity resolution
        interface_preference: "fuzzy" for fuzzy picker, "questionary" for up/down list

    Returns:
        Resolved resource object
    """
    # Try to resolve by ID first
    result = _resolve_by_id(ref, get_by_id)
    if result is not None:
        return result

    # If get_by_id returned None, the resource doesn't exist
    if is_uuid(ref):
        raise click.ClickException(f"{label} '{ref}' not found")

    # Find resources by name
    matches = find_by_name(name=ref)
    if not matches:
        raise click.ClickException(f"{label} '{ref}' not found")

    if len(matches) == 1:
        return matches[0]

    # Multiple matches found, handle ambiguity
    if select:
        return _resolve_by_name_multiple_with_select(matches, select)

    # Choose interface based on preference
    if interface_preference == "fuzzy":
        return _resolve_by_name_multiple_fuzzy(ctx, ref, matches, label)
    else:
        return _resolve_by_name_multiple_questionary(ctx, ref, matches, label)


def _handle_json_view_ambiguity(matches: list[Any]) -> Any:
    """Handle ambiguity in JSON view by returning first match."""
    return matches[0]


def _handle_questionary_ambiguity(
    resource_type: str, ref: str, matches: list[Any]
) -> Any:
    """Handle ambiguity using questionary interactive interface."""
    if not (questionary and os.getenv("TERM") and os.isatty(0) and os.isatty(1)):
        raise click.ClickException("Interactive selection not available")

    # Escape special characters for questionary
    safe_resource_type = resource_type.replace("{", "{{").replace("}", "}}")
    safe_ref = ref.replace("{", "{{").replace("}", "}}")

    picked_idx = questionary.select(
        f"Multiple {safe_resource_type}s match '{safe_ref}'. Pick one:",
        choices=[
            questionary.Choice(
                title=f"{getattr(m, 'name', '—').replace('{', '{{').replace('}', '}}')} — {getattr(m, 'id', '').replace('{', '{{').replace('}', '}}')}",
                value=i,
            )
            for i, m in enumerate(matches)
        ],
        use_indicator=True,
        qmark="🧭",
        instruction="↑/↓ to select • Enter to confirm",
    ).ask()
    if picked_idx is None:
        raise click.ClickException("Selection cancelled")
    return matches[picked_idx]


def _handle_fallback_numeric_ambiguity(
    resource_type: str, ref: str, matches: list[Any]
) -> Any:
    """Handle ambiguity using numeric prompt fallback."""
    # Escape special characters for display
    safe_resource_type = resource_type.replace("{", "{{").replace("}", "}}")
    safe_ref = ref.replace("{", "{{").replace("}", "}}")

    console.print(
        Text(
            f"[yellow]Multiple {safe_resource_type}s found matching '{safe_ref}':[/yellow]"
        )
    )
    table = AIPTable(
        title=f"Select {safe_resource_type.title()}",
    )
    table.add_column("#", style="dim", width=3)
    table.add_column("ID", style="dim", width=36)
    table.add_column("Name", style="cyan")
    for i, m in enumerate(matches, 1):
        table.add_row(str(i), str(getattr(m, "id", "")), str(getattr(m, "name", "")))
    console.print(table)
    choice_str = click.prompt(
        f"Select {safe_resource_type} (1-{len(matches)})",
    )
    try:
        choice = int(choice_str)
    except ValueError:
        raise click.ClickException("Invalid selection")
    if 1 <= choice <= len(matches):
        return matches[choice - 1]
    raise click.ClickException("Invalid selection")


def _should_fallback_to_numeric_prompt(exception: Exception) -> bool:
    """Determine if we should fallback to numeric prompt for this exception."""
    # Re-raise cancellation - user explicitly cancelled
    if "Selection cancelled" in str(exception):
        return False

    # Fall back to numeric prompt for other exceptions
    return True


def handle_ambiguous_resource(
    ctx: Any, resource_type: str, ref: str, matches: list[Any]
) -> Any:
    """Handle multiple resource matches gracefully."""
    if _get_view(ctx) == "json":
        return _handle_json_view_ambiguity(matches)

    try:
        return _handle_questionary_ambiguity(resource_type, ref, matches)
    except Exception as e:
        if _should_fallback_to_numeric_prompt(e):
            try:
                return _handle_fallback_numeric_ambiguity(resource_type, ref, matches)
            except Exception:
                # If fallback also fails, re-raise the original exception
                raise e
        else:
            # Re-raise cancellation exceptions
            raise
