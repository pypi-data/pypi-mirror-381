from __future__ import annotations

from typing import Any, Dict, List, Optional

import typer

from ..backends.zotero_client import ZoteroClient

__all__ = [
    "build_collection_index",
    "collection_path_from_index",
    "collection_paths_for_item",
    "resolve_collection",
    "resolve_collections_list",
    "split_csv_string",
    "parse_editor_kv_csv",
    "ordered_union",
    "normalize_flag_inputs",
    "merge_collections",
    "merge_tags",
]


def resolve_collection(zot: ZoteroClient, collection: Optional[str]) -> Optional[str]:
    if not collection:
        return None
    collections = zot.collections()
    keys = {c.get("key") for c in collections}
    if collection in keys:
        return collection
    target = str(collection).strip().lower()
    names = [
        (c.get("data", {}).get("name", ""), c.get("key"))
        for c in collections
    ]
    exact = [(name, key) for (name, key) in names if str(name).strip().lower() == target]
    if len(exact) == 1:
        return exact[0][1]
    if len(exact) > 1:
        choices = ", ".join(f"{name} ({key})" for name, key in exact)
        raise typer.BadParameter(f"Ambiguous collection name '{collection}': {choices}")
    partial = [(name, key) for (name, key) in names if target in str(name).strip().lower()]
    if len(partial) == 1:
        return partial[0][1]
    if len(partial) > 1:
        choices = ", ".join(f"{name} ({key})" for name, key in partial)
        raise typer.BadParameter(f"Ambiguous collection name '{collection}': {choices}")
    raise typer.BadParameter(f"Collection not found: {collection}")


def build_collection_index(zot: ZoteroClient) -> Dict[str, Dict[str, Optional[str]]]:
    collections = zot.collections()
    index: Dict[str, Dict[str, Optional[str]]] = {}
    for collection in collections:
        data = collection.get("data") if isinstance(collection.get("data"), dict) else collection
        if not isinstance(data, dict):
            continue
        key = str(collection.get("key") or data.get("key") or "").strip()
        if not key:
            continue
        name = str(data.get("name") or "").strip()
        parent = (
            data.get("parentCollection")
            or data.get("parent")
            or data.get("parentKey")
            or None
        )
        index[key] = {"name": name, "parent": str(parent) if parent else None}
    return index


def collection_path_from_index(index: Dict[str, Dict[str, Optional[str]]], col_key: str) -> str:
    if not col_key:
        return ""
    names: List[str] = []
    seen: set[str] = set()
    current = col_key
    while current and current not in seen:
        seen.add(current)
        info = index.get(current)
        if not info:
            break
        name = (info.get("name") or "").strip()
        if name:
            names.append(name)
        current = info.get("parent") or None
    names.reverse()
    return " -> ".join(names)


def collection_paths_for_item(zot: ZoteroClient, collection_keys: List[str]) -> List[str]:
    index = build_collection_index(zot)
    paths: List[str] = []
    for key in collection_keys or []:
        path = collection_path_from_index(index, key)
        if path:
            paths.append(path)
    return sorted(paths)


def split_csv_string(value: str) -> List[str]:
    parts = [part.strip() for part in (value or "").split(",") if part.strip()]
    seen: set[str] = set()
    ordered: List[str] = []
    for part in parts:
        if part not in seen:
            seen.add(part)
            ordered.append(part)
    return ordered


def parse_editor_kv_csv(text: str, field_names: List[str]) -> Dict[str, List[str]]:
    allowed = [str(name).strip().lower() for name in field_names]
    result: Dict[str, List[str]] = {}
    for raw_line in (text or "").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        lower_line = line.lower()
        for name in allowed:
            prefix = name + ":"
            if lower_line.startswith(prefix):
                values = line.split(":", 1)[1].strip()
                result[name] = split_csv_string(values)
                break
    return result


def ordered_union(existing_lists: List[List[str]]) -> List[str]:
    ordered: List[str] = []
    seen: set[str] = set()
    for values in existing_lists:
        for value in values or []:
            if value not in seen:
                seen.add(value)
                ordered.append(value)
    return ordered


def normalize_flag_inputs(values: List[str]) -> List[str]:
    normalized: List[str] = []
    seen: set[str] = set()
    for value in values or []:
        chunks = [chunk.strip() for chunk in str(value).split(",") if str(chunk).strip()]
        for chunk in chunks:
            if chunk not in seen:
                seen.add(chunk)
                normalized.append(chunk)
    return normalized


def resolve_collections_list(zot: ZoteroClient, inputs: List[str]) -> List[str]:
    keys: List[str] = []
    for item in inputs or []:
        key = resolve_collection(zot, item)
        if key not in keys:
            keys.append(key)
    return keys


def merge_collections(
    zot: ZoteroClient,
    existing_keys: List[str],
    add_inputs: List[str],
    remove_inputs: List[str],
) -> List[str]:
    to_add = resolve_collections_list(zot, add_inputs)
    to_remove = set(resolve_collections_list(zot, remove_inputs))
    final: List[str] = []
    seen: set[str] = set()
    for key in list(existing_keys or []) + [candidate for candidate in to_add if candidate not in (existing_keys or [])]:
        if key in to_remove:
            continue
        if key not in seen:
            seen.add(key)
            final.append(key)
    return final


def merge_tags(existing_texts: List[str], add_inputs: List[str], remove_inputs: List[str]) -> List[str]:
    add_norm = normalize_flag_inputs(add_inputs)
    remove_norm = set(normalize_flag_inputs(remove_inputs))
    seen = set(existing_texts or [])
    merged: List[str] = list(existing_texts or [])
    for tag in add_norm:
        if tag not in seen:
            merged.append(tag)
            seen.add(tag)
    if remove_norm:
        merged = [tag for tag in merged if tag not in remove_norm]
    return merged

