"""CLI resource resolution utilities for handling ID/name references.

This module provides CLI-specific resource resolution functionality,
including interactive pickers and ambiguity handling.

Authors:
    Raymond Christopher (raymond.christopher@gdplabs.id)
"""

from collections.abc import Callable
from typing import Any

import click

from glaip_sdk.cli.utils import resolve_resource


def resolve_resource_reference(
    ctx: Any,
    _client: Any,
    reference: str,
    resource_type: str,
    get_by_id_func: Callable,
    find_by_name_func: Callable,
    label: str,
    select: int | None = None,
    interface_preference: str | None = None,
) -> Any | None:
    """Resolve resource reference (ID or name) with ambiguity handling.

    This is a common pattern used across all resource types.

    Args:
        ctx: Click context
        client: API client
        reference: Resource ID or name
        resource_type: Type of resource
        get_by_id_func: Function to get resource by ID
        find_by_name_func: Function to find resources by name
        label: Label for error messages
        select: Selection index for ambiguous matches

    Returns:
        Resolved resource object

    Raises:
        click.ClickException: If resolution fails
    """
    try:
        return resolve_resource(
            ctx,
            reference,
            get_by_id=get_by_id_func,
            find_by_name=find_by_name_func,
            label=label,
            select=select,
            interface_preference=interface_preference,
        )
    except Exception as e:
        raise click.ClickException(f"Failed to resolve {resource_type.lower()}: {e}")
