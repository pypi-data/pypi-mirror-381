"""Reusable picker utilities built on top of fzf integration."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Callable, Dict, List, Optional, Tuple, TypeVar, Union

import typer

from . import fzf as fzf_utils
from .fzf import fzf_multiselect_lines
from .session import PickerSession, ensure_picker_session
from ..backends.zotero_client import NormalizedItem, ZoteroClient, normalize_item
from ..utils.collections import (
    build_collection_index,
    collection_path_from_index,
    split_csv_string,
)

T = TypeVar("T")

DEFAULT_PICKER_CREATOR_PREVIEW = 30
DEFAULT_PICKER_TITLE_PREVIEW = 80

PickerItem = Tuple[Dict[str, Any], Optional[NormalizedItem]]

__all__ = [
    "PickerSession",
    "ensure_picker_session",
    "run_multiselect_picker",
    "load_picker_items",
    "normalize_picker_item",
    "format_picker_item_line",
    "build_picker_line",
    "select_tags",
    "select_collections",
    "select_related_items",
]


def run_multiselect_picker(
    preselected_values: Sequence[T],
    other_values: Sequence[T],
    *,
    prompt: str,
    header: str,
    formatter: Callable[[T, bool], str],
    marker: str,
    capture_query: bool,
    context: Optional[str],
) -> Tuple[Optional[List[str]], Optional[str]]:
    """Run the shared multiselect picker with consistent formatting."""

    def _format_line(value: T, selected: bool) -> str:
        body = str(formatter(value, selected))
        prefix = marker if selected else " " * len(marker)
        return f"{prefix} {body}".rstrip()

    lines = [_format_line(value, True) for value in preselected_values]
    lines.extend(_format_line(value, False) for value in other_values)
    try:
        return fzf_multiselect_lines(
            lines,
            prompt=prompt,
            header=header,
            marker=marker,
            preselect_all=True,
            print_query=capture_query,
            with_help=True,
            context=context or prompt,
        )
    except FileNotFoundError:
        typer.echo("fzf not found for picker mode", err=True)
        raise typer.Exit(code=1)


def _resolve_picker_key(
    item: Dict[str, Any],
    normalized: Optional[NormalizedItem],
) -> Optional[str]:
    """Derive the canonical item key for picker usage."""

    key_candidate = (normalized.key if normalized and normalized.key else None)
    if key_candidate:
        return key_candidate
    raw_key = item.get("key")
    if isinstance(raw_key, str):
        trimmed = raw_key.strip()
        if trimmed:
            return trimmed
    return None


def load_picker_items(
    zot: Union[ZoteroClient, PickerSession],
    *,
    limit: Optional[int] = None,
    include_keys: Sequence[str] = (),
    exclude_keys: Sequence[str] = (),
) -> Dict[str, PickerItem]:
    """Load Zotero items for picker flows and normalize them when possible."""

    session = ensure_picker_session(zot)
    exclude_set = {value for value in exclude_keys if value}
    items_by_key: Dict[str, PickerItem] = {}
    fetch_limit = limit if isinstance(limit, int) and limit > 0 else None
    for item in session.list_items(limit=fetch_limit):
        normalized = normalize_picker_item(item)
        key_candidate = _resolve_picker_key(item, normalized)
        if not key_candidate or key_candidate in exclude_set:
            continue
        if key_candidate not in items_by_key:
            items_by_key[key_candidate] = (item, normalized)

    for explicit_key in include_keys:
        if not explicit_key or explicit_key in exclude_set:
            continue
        if explicit_key in items_by_key:
            continue
        try:
            item = session.get_item(explicit_key)
        except Exception:
            item = {"key": explicit_key, "data": {}}
        normalized = normalize_picker_item(item)
        key_candidate = _resolve_picker_key(item, normalized) or explicit_key
        if key_candidate in exclude_set or key_candidate in items_by_key:
            continue
        items_by_key[key_candidate] = (item, normalized)

    return items_by_key


def normalize_picker_item(item: Dict[str, Any]) -> Optional[NormalizedItem]:
    """Normalize a Zotero item for picker display, suppressing normalization errors."""

    try:
        return normalize_item(item)
    except Exception:
        return None


def format_picker_item_line(
    normalized: Optional[NormalizedItem],
    fallback_key: str,
    *,
    max_creators: int = DEFAULT_PICKER_CREATOR_PREVIEW,
    max_title: int = DEFAULT_PICKER_TITLE_PREVIEW,
) -> str:
    """Format a picker display line using normalized metadata when available."""

    key_text = fallback_key.strip() or "(unknown)"
    if not normalized:
        return f"{key_text} | (unavailable)"
    venue_source = (
        normalized.journalAbbreviation or normalized.publication or ""
    ).strip()
    venue = f" [{venue_source}]" if venue_source else ""
    creators = "; ".join(normalized.creators)[:max_creators]
    title = normalized.title[:max_title]
    year = normalized.year or ""
    key_display = normalized.key or key_text
    body = f"{year:<4}{venue} {creators}: {title}".strip()
    return f"{key_display} | {body}".rstrip()


def build_picker_line(
    item: Dict[str, Any],
    normalized: Optional[NormalizedItem],
    *,
    fallback_key: Optional[str] = None,
    max_creators: int = DEFAULT_PICKER_CREATOR_PREVIEW,
    max_title: int = DEFAULT_PICKER_TITLE_PREVIEW,
) -> str:
    """Compose a picker line from raw and normalized item data."""

    if isinstance(fallback_key, str) and fallback_key.strip():
        key_hint = fallback_key
    else:
        raw_key = item.get("key")
        key_hint = raw_key if isinstance(raw_key, str) else ""
    return format_picker_item_line(
        normalized,
        key_hint,
        max_creators=max_creators,
        max_title=max_title,
    )


def select_tags(
    zot: Union[ZoteroClient, PickerSession],
    preselected: Sequence[str],
    *,
    limit: Optional[int] = None,
) -> Optional[List[str]]:
    """Launch the tag picker and return the chosen tag strings."""

    session = ensure_picker_session(zot)
    preselected_list = list(preselected)
    all_tags = sorted(session.tags() or [])
    other_raw = [tag for tag in all_tags if tag not in preselected_list]
    if isinstance(limit, int) and limit > 0:
        other_raw = other_raw[:limit]
    header_text = (
        f"★ = currently set ({len(preselected_list)}). {fzf_utils._base_hint_text()}. "
        "Type new tags (comma-separated) and press Enter to add."
    )
    selected_lines, query = run_multiselect_picker(
        preselected_list,
        other_raw,
        prompt="tags",
        header=header_text,
        formatter=lambda tag, _: tag,
        marker="★",
        capture_query=True,
        context="tags",
    )
    if selected_lines is None:
        return None
    selected: List[str] = []
    if query and query.strip():
        selected.extend([tag for tag in split_csv_string(query) if tag])
    for line in selected_lines:
        tag = line.strip("★ ")
        if tag and tag not in selected:
            selected.append(tag)
    return selected


def select_collections(
    zot: Union[ZoteroClient, PickerSession],
    preselected_keys: Sequence[str],
) -> Optional[List[str]]:
    """Launch the collection picker and return the selected collection keys."""

    session = ensure_picker_session(zot)
    preselected_list = list(preselected_keys)
    col_index = build_collection_index(session)

    def _col_path_with_key(collection_key: str) -> str:
        path = collection_path_from_index(col_index, collection_key)
        return f"{path} | {collection_key}" if path else f"(No Name) | {collection_key}"

    all_col_keys = sorted(col_index.keys())
    other_keys = [key for key in all_col_keys if key not in preselected_list]
    header_text = f"★ = currently set ({len(preselected_list)}). {fzf_utils._base_hint_text()}"
    selected_lines, _ = run_multiselect_picker(
        preselected_list,
        other_keys,
        prompt="collections",
        header=header_text,
        formatter=lambda key, _: _col_path_with_key(key),
        marker="★",
        capture_query=False,
        context="collections",
    )
    if selected_lines is None:
        return None
    selected_keys: List[str] = []
    for line in selected_lines:
        if "|" not in line:
            continue
        key_part = line.split("|", 1)[1].strip()
        if key_part and key_part not in selected_keys:
            selected_keys.append(key_part)
    return selected_keys


def select_related_items(
    zot: Union[ZoteroClient, PickerSession],
    preselected_keys: Sequence[str],
    exclude_key: str,
    *,
    limit: Optional[int] = None,
) -> Optional[List[str]]:
    """Launch the related-items picker and return the chosen item keys."""

    session = ensure_picker_session(zot)
    clean_preselected = [key for key in preselected_keys if key and key != exclude_key]
    items_by_key = load_picker_items(
        session,
        limit=limit,
        include_keys=clean_preselected,
        exclude_keys=(exclude_key,),
    )

    case_index = {existing.lower(): existing for existing in items_by_key}
    resolved_preselected: List[str] = []
    for candidate in clean_preselected:
        if not candidate:
            continue
        if candidate in items_by_key:
            resolved_preselected.append(candidate)
            continue
        mapped = case_index.get(candidate.lower())
        if mapped:
            resolved_preselected.append(mapped)
            continue
        items_by_key[candidate] = ({"key": candidate, "data": {}}, None)
        case_index[candidate.lower()] = candidate
        resolved_preselected.append(candidate)

    preselected_sorted = sorted({key for key in resolved_preselected}, key=str.lower)
    preselected_set = set(preselected_sorted)
    other_keys = [
        key
        for key in sorted(items_by_key.keys(), key=str.lower)
        if key not in preselected_set
    ]

    def _format_line(item_key: str, _: bool) -> str:
        item, normalized = items_by_key.get(item_key, ({"key": item_key, "data": {}}, None))
        return build_picker_line(
            item,
            normalized,
            fallback_key=item_key,
        )

    header_text = (
        f"★ = currently related ({len(preselected_sorted)}). {fzf_utils._base_hint_text()}"
    )
    selected_lines, _ = run_multiselect_picker(
        preselected_sorted,
        other_keys,
        prompt="related",
        header=header_text,
        formatter=_format_line,
        marker="★",
        capture_query=False,
        context="related",
    )
    if selected_lines is None:
        return None
    selected_keys: List[str] = []
    for line in selected_lines:
        if "|" not in line:
            continue
        candidate = line.split("|", 1)[0].strip()
        if candidate and candidate != exclude_key and candidate not in selected_keys:
            selected_keys.append(candidate)
    return selected_keys
