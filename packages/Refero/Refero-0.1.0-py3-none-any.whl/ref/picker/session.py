"""Session-scoped Zotero helpers for picker workflows."""

from __future__ import annotations

import copy
from typing import Any, Dict, List, Optional, Tuple, Union

from ..backends.zotero_client import ZoteroClient

__all__ = ["PickerSession", "ensure_picker_session"]


class PickerSession:
    """Provide memoized Zotero lookups during a picker session.

    The cache lives for the lifetime of the session instance and prevents
    repeated calls to expensive Zotero endpoints while several pickers run
    back-to-back in one CLI workflow.
    """

    def __init__(self, zotero: ZoteroClient) -> None:
        self._zotero = zotero
        self._tag_cache: Optional[List[str]] = None
        self._list_cache: Dict[
            Tuple[
                Optional[int],
                Optional[str],
                Optional[str],
                Optional[str],
                Optional[str],
                Optional[str],
                Optional[str],
                Optional[str],
                Optional[str],
            ],
            List[Dict[str, Any]],
        ] = {}

    def tags(self) -> List[str]:
        """Return cached Zotero tags for the active session."""

        if self._tag_cache is None:
            fetched = self._zotero.tags()
            self._tag_cache = list(fetched or [])
        return copy.deepcopy(self._tag_cache)

    def list_items(
        self,
        limit: Optional[int] = 200,
        q: Optional[str] = None,
        collection: Optional[str] = None,
        tag: Optional[str] = None,
        itemType: Optional[str] = None,
        author: Optional[str] = None,
        title: Optional[str] = None,
        year: Optional[str] = None,
        doi: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Return cached Zotero items keyed on the query parameters."""

        cache_key = (
            limit,
            q,
            collection,
            tag,
            itemType,
            author,
            title,
            year,
            doi,
        )
        if cache_key not in self._list_cache:
            items = self._zotero.list_items(
                limit=limit,
                q=q,
                collection=collection,
                tag=tag,
                itemType=itemType,
                author=author,
                title=title,
                year=year,
                doi=doi,
            )
            self._list_cache[cache_key] = copy.deepcopy(items)
        return copy.deepcopy(self._list_cache[cache_key])

    def invalidate_tags(self) -> None:
        """Reset the cached tag list."""

        self._tag_cache = None

    def invalidate_list_items(self) -> None:
        """Reset cached list-items queries."""

        self._list_cache.clear()

    def invalidate_all(self) -> None:
        """Reset every cached lookup."""

        self.invalidate_tags()
        self.invalidate_list_items()

    def __getattr__(self, name: str) -> Any:  # type: ignore[override]
        return getattr(self._zotero, name)


def ensure_picker_session(
    zotero: Union[ZoteroClient, PickerSession]
) -> PickerSession:
    """Return a picker session, preserving existing session instances."""

    if isinstance(zotero, PickerSession):
        return zotero
    return PickerSession(zotero)
