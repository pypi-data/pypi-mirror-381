"""Shared search filter helpers used by CLI commands.

This module centralizes the Typer option declarations for item search filters
and provides an immutable data structure for downstream consumers.
"""

from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Sequence
from typing import Optional, Tuple

import typer
from typer.models import ArgumentInfo, OptionInfo

__all__ = [
    "SearchFilters",
    "SearchFilterOptions",
    "build_search_filter_options",
    "build_search_filters",
    "PICK_FILTER_OPTIONS",
    "LIST_FILTER_OPTIONS",
    "EXPORT_FILTER_OPTIONS",
]


@dataclass(frozen=True)
class SearchFilters:
    """Immutable container describing Zotero item search filters."""

    positional_terms: Tuple[str, ...]
    query: Optional[str]
    limit: Optional[int]
    collection: Optional[str]
    tag: Optional[str]
    author: Optional[str]
    title: Optional[str]
    year: Optional[str]
    doi: Optional[str]


@dataclass(frozen=True)
class SearchFilterOptions:
    """Typer option descriptors used for the shared search filters."""

    positional: ArgumentInfo
    query: OptionInfo
    limit: OptionInfo
    collection: OptionInfo
    tag: OptionInfo
    author: OptionInfo
    title: OptionInfo
    year: OptionInfo
    doi: OptionInfo


def build_search_filter_options(*, limit_default: Optional[int], limit_help: str) -> SearchFilterOptions:
    """Construct the Typer option metadata for search filters.

    Args:
        limit_default: Default value for the ``--limit`` option.
        limit_help: Help text describing the limit behaviour for the caller.

    Returns:
        A ``SearchFilterOptions`` instance with reusable Typer descriptors.
    """

    return SearchFilterOptions(
        positional=typer.Argument(None, help="Search query (positional)"),
        query=typer.Option(None, "--query", "-q", help="Search query"),
        limit=typer.Option(limit_default, "--limit", "-l", help=limit_help),
        collection=typer.Option(None, "--collection", "-c", help="Collection key"),
        tag=typer.Option(None, "--tag", "-g", help="Filter by tag"),
        author=typer.Option(None, "--author", "-a", help="Filter by author substring"),
        title=typer.Option(None, "--title", "-t", help="Filter by title substring"),
        year=typer.Option(None, "--year", "-y", help="Filter by year (exact or prefix)"),
        doi=typer.Option(None, "--doi", "-d", help="Filter by DOI substring"),
    )


def build_search_filters(
    positional_terms: Optional[Sequence[str]],
    query: Optional[str],
    limit: Optional[int],
    collection: Optional[str],
    tag: Optional[str],
    author: Optional[str],
    title: Optional[str],
    year: Optional[str],
    doi: Optional[str],
) -> SearchFilters:
    """Normalize Typer inputs into a reusable :class:`SearchFilters` object."""

    def _normalize_text(value: Optional[str]) -> Optional[str]:
        if value is None:
            return None
        trimmed = value.strip()
        return trimmed or None

    limit_value: Optional[int] = None
    if limit is not None:
        limit_value = limit if limit > 0 else None

    terms = tuple(token for token in (positional_terms or []) if isinstance(token, str) and token.strip())
    return SearchFilters(
        positional_terms=terms,
        query=_normalize_text(query),
        limit=limit_value,
        collection=_normalize_text(collection),
        tag=_normalize_text(tag),
        author=_normalize_text(author),
        title=_normalize_text(title),
        year=_normalize_text(year),
        doi=_normalize_text(doi),
    )


PICK_FILTER_OPTIONS = build_search_filter_options(
    limit_default=None,
    limit_help="Max items to fetch for picking (defaults to config picker_limit)",
)


LIST_FILTER_OPTIONS = build_search_filter_options(
    limit_default=50,
    limit_help="Max items to return",
)


EXPORT_FILTER_OPTIONS = build_search_filter_options(
    limit_default=None,
    limit_help="Max items to export when filters are used (defaults to config picker_limit)",
)
