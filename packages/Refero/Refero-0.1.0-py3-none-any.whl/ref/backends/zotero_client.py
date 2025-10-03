from __future__ import annotations

from dataclasses import dataclass
import re
from collections.abc import Iterable, Mapping
from typing import Any, Dict, List, Optional, Tuple
import requests
import time

from pyzotero.zotero import Zotero


@dataclass(frozen=True)
class NormalizedItem:
    key: str
    citekey: str
    title: str
    creators: Tuple[str, ...]
    year: str
    doi: Optional[str]
    url: Optional[str]
    publication: str
    journalAbbreviation: str
    itemType: str
    collections: Tuple[str, ...]
    tags: Tuple[str, ...]


@dataclass(frozen=True)
class _ClientFilters:
    """Client-side filter values applied after quicksearch results."""

    author: str = ""
    title: str = ""
    year: str = ""
    doi: str = ""

    def any(self) -> bool:
        """Return True when at least one filter is active."""

        return any((self.author, self.title, self.year, self.doi))


@dataclass(frozen=True)
class _SearchPlan:
    """Search strategy describing server parameters and client filters."""

    params: Dict[str, Any]
    filters: _ClientFilters
    collection_key: Optional[str]


def _parse_citekey_from_extra(extra: Optional[str]) -> Optional[str]:
    if not extra:
        return None
    for line in extra.splitlines():
        low = line.strip().lower()
        if low.startswith("citation key:") or low.startswith("citationkey:"):
            return line.split(":", 1)[1].strip()
    return None


def _synthesize_citekey(data: Dict[str, Any]) -> str:
    title = (data.get("title") or "").split()[0:4]
    title_part = "".join([t[:3] for t in title]) or "item"
    year = _extract_year(data.get("date"))
    return f"{title_part}{year}"


def _extract_year(date_str: Optional[str]) -> str:
    if not date_str:
        return ""
    # Find the first 4-digit sequence that looks like a year
    m = re.search(r"\b(\d{4})\b", str(date_str))
    return m.group(1) if m else ""


def item_to_csl(normalized: NormalizedItem, data: Mapping[str, Any]) -> Dict[str, Any]:
    """Convert a Zotero item into a CSL-JSON mapping."""

    type_map = {
        "journalArticle": "article-journal",
        "book": "book",
        "bookSection": "chapter",
        "thesis": "thesis",
        "conferencePaper": "paper-conference",
        "report": "report",
        "webpage": "webpage",
    }
    authors: List[Dict[str, str]] = []
    for creator in data.get("creators", []) or []:
        family = creator.get("lastName") or creator.get("familyName")
        given = creator.get("firstName") or creator.get("givenName")
        if family or given:
            authors.append({"family": family or "", "given": given or ""})
    csl: Dict[str, Any] = {
        "id": normalized.citekey or normalized.key,
        "type": type_map.get(str(data.get("itemType", "")), "article"),
        "title": data.get("title"),
        "author": authors,
        "DOI": data.get("DOI"),
        "URL": data.get("url") or data.get("URL"),
    }
    year = _extract_year(data.get("date"))
    if year:
        try:
            csl["issued"] = {"date-parts": [[int(year)]]}
        except ValueError:
            pass
    if data.get("itemType") == "journalArticle":
        container = data.get("publicationTitle") or data.get("journalAbbreviation")
        if container:
            csl["container-title"] = container
        if data.get("volume"):
            csl["volume"] = data.get("volume")
        if data.get("issue"):
            csl["issue"] = data.get("issue")
        if data.get("pages"):
            csl["page"] = data.get("pages")
    return csl


def item_to_bib(normalized: NormalizedItem, data: Mapping[str, Any]) -> str:
    """Convert a Zotero item into a BibTeX string."""

    type_map = {
        "journalArticle": "article",
        "book": "book",
        "bookSection": "incollection",
        "thesis": "phdthesis",
        "conferencePaper": "inproceedings",
        "report": "techreport",
        "webpage": "misc",
    }
    entry_type = type_map.get(str(data.get("itemType", "")), "misc")
    fields: Dict[str, Any] = {"title": data.get("title")}
    if normalized.creators:
        fields["author"] = " and ".join(normalized.creators)
    year = _extract_year(data.get("date"))
    if year:
        fields["year"] = year
    if data.get("DOI"):
        fields["doi"] = data.get("DOI")
    url_value = data.get("url") or data.get("URL")
    if url_value:
        fields["url"] = url_value
    if entry_type == "article":
        if data.get("publicationTitle"):
            fields["journal"] = data.get("publicationTitle")
        if data.get("volume"):
            fields["volume"] = data.get("volume")
        if data.get("issue"):
            fields["number"] = data.get("issue")
        if data.get("pages"):
            fields["pages"] = data.get("pages")
    if entry_type in {"book", "incollection"}:
        if data.get("publisher"):
            fields["publisher"] = data.get("publisher")
        if data.get("bookTitle") and entry_type == "incollection":
            fields["booktitle"] = data.get("bookTitle")
    key_value = (normalized.citekey or normalized.key or "item").replace(" ", "_")
    parts = [f"@{entry_type}{{{key_value},"]
    for field_name, value in fields.items():
        if value:
            parts.append(f"  {field_name} = {{{value}}},")
    parts.append("}")
    return "\n".join(parts)


def normalize_item(item: Dict[str, Any]) -> NormalizedItem:
    data = item.get("data", {})
    meta = item.get("meta", {})
    creators = data.get("creators", []) or []
    names: List[str] = []
    for c in creators:
        last = c.get("lastName") or c.get("familyName") or ""
        first = c.get("firstName") or c.get("givenName") or ""
        name = f"{last}, {first}".strip().strip(",")
        if name:
            names.append(name)
    tags = [t.get("tag", "") for t in (data.get("tags") or [])]
    citekey = (
        meta.get("citekey")
        or _parse_citekey_from_extra(data.get("extra"))
        or _synthesize_citekey(data)
    )
    year = _extract_year(data.get("date"))
    # Derive a human-friendly publication/container string
    publication = (
        data.get("publicationTitle")
        or data.get("journalAbbreviation")
        or data.get("proceedingsTitle")
        or data.get("conferenceName")
        or data.get("bookTitle")
        or data.get("websiteTitle")
        or data.get("seriesTitle")
        or ""
    )
    journal_abbr = data.get("journalAbbreviation") or ""
    return NormalizedItem(
        key=item.get("key", ""),
        citekey=citekey,
        title=data.get("title", ""),
        creators=tuple(names),
        year=year,
        doi=data.get("DOI"),
        url=data.get("url") or data.get("URL"),
        publication=publication,
        journalAbbreviation=journal_abbr,
        itemType=data.get("itemType", ""),
        collections=tuple(data.get("collections", []) or []),
        tags=tuple(tag for tag in tags if tag),
    )


class _BaseZoteroAPI:
    def __init__(self, client: "ZoteroClient") -> None:
        self.client = client

    def is_local(self) -> bool:
        raise NotImplementedError

    # The following methods are overridden by concrete strategies
    def export_csljson(self, keys: Iterable[str]) -> Any:
        raise NotImplementedError

    def export_bibtex(self, keys: Iterable[str]) -> str:
        raise NotImplementedError

    def create_items(self, items: List[Dict[str, Any]]) -> Dict[str, Any]:
        raise NotImplementedError

    def trash_items(self, keys: Iterable[str]) -> None:
        raise NotImplementedError

    def delete_items(self, keys: Iterable[str]) -> None:
        raise NotImplementedError

    def update_item_data_force(self, key: str, full_data: Dict[str, Any], strict: bool, force: bool) -> None:
        raise NotImplementedError


class _LocalZoteroAPI(_BaseZoteroAPI):
    def is_local(self) -> bool:
        return True

    def export_csljson(self, keys: Iterable[str]) -> List[Dict[str, Any]]:
        items = [self.client.get_item(k) for k in keys]
        return [
            item_to_csl(normalize_item(item), item.get("data", {}) or {})
            for item in items
        ]

    def export_bibtex(self, keys: Iterable[str]) -> str:
        items = [self.client.get_item(k) for k in keys]
        return "\n\n".join(
            item_to_bib(normalize_item(item), item.get("data", {}) or {})
            for item in items
        )

    def create_items(self, items: List[Dict[str, Any]]) -> Dict[str, Any]:
        endpoint = getattr(self.client.zot, "endpoint", None) or "http://localhost:23119/api"
        user_id = 0 if self.client.library_id in (None, 0) else self.client.library_id
        url = f"{endpoint.rstrip('/')}/users/{user_id}/items"
        try:
            headers = {"Zotero-API-Version": "3", "Content-Type": "application/json"}
            resp = requests.post(url, json=items, headers=headers, timeout=30)
            if resp.status_code in (400, 404, 405):
                text = (resp.text or "").strip()
                raise RuntimeError(
                    f"Local Zotero API rejected item creation (HTTP {resp.status_code}).\n"
                    "- No write support in server_localAPI.js until now, see https://groups.google.com/g/zotero-dev/c/ElvHhIFAXrY/m/fA7SKKwsAgAJ\n"
                    "- Alternatively, switch ref to web mode with a write-enabled API key.\n"
                    f"Response: {text}"
                )
            resp.raise_for_status()
            data = resp.json() if resp.content else None
            if isinstance(data, list):
                successful: Dict[str, Any] = {}
                for idx, item in enumerate(data):
                    successful[str(idx)] = item
                return {"successful": successful, "failed": {}}
            if isinstance(data, dict):
                return data
            return {"successful": {}, "failed": {}}
        except requests.RequestException as exc:
            raise RuntimeError(f"Local Zotero API request failed: {exc}")

    def trash_items(self, keys: Iterable[str]) -> None:
        items = [self.client.get_item(k) for k in keys]
        self.client.zot.delete_item(items)

    def delete_items(self, keys: Iterable[str]) -> None:
        items = [self.client.get_item(k) for k in keys]
        self.client.zot.delete_item(items)

    def update_item_data_force(self, key: str, full_data: Dict[str, Any], strict: bool, force: bool) -> None:
        current = self.client.get_item(key)
        current_data = current.get("data", {}) or {}
        updates = dict(full_data or {})
        updates.pop("version", None)
        updates.pop("key", None)
        merged = dict(updates) if strict else {**current_data, **updates}
        item_for_update: Dict[str, Any] = {
            "key": current.get("key", key),
            "version": current.get("version"),
        }
        item_for_update.update(merged)
        self.client.zot.update_item(item_for_update)


class _WebZoteroAPI(_BaseZoteroAPI):
    def is_local(self) -> bool:
        return False

    def export_csljson(self, keys: Iterable[str]) -> List[Dict[str, Any]]:
        zot = self.client.zot
        zot.add_parameters(format="csljson")
        return list(zot.get_subset(list(keys)))

    def export_bibtex(self, keys: Iterable[str]) -> str:
        zot = self.client.zot
        zot.add_parameters(format="bibtex")
        return "\n\n".join(zot.get_subset(list(keys)))

    def create_items(self, items: List[Dict[str, Any]]) -> Dict[str, Any]:
        return self.client.zot.create_items(items)

    def trash_items(self, keys: Iterable[str]) -> None:
        self._delete_items(keys)

    def delete_items(self, keys: Iterable[str]) -> None:
        self._delete_items(keys)

    def update_item_data_force(self, key: str, full_data: Dict[str, Any], strict: bool, force: bool) -> None:
        import requests as _rq

        user_id = int(self.client.library_id)
        base = self._base_url()
        url = f"{base}/users/{user_id}/items/{key}"
        user_updates = dict(full_data or {})
        user_updates.pop("version", None)
        user_updates.pop("key", None)

        max_attempts = 10
        attempt = 0
        override_latest: Optional[Dict[str, Any]] = None
        last_response: Optional[_rq.Response] = None

        while attempt < max_attempts:
            attempt += 1

            latest_item = override_latest if override_latest is not None else self._get_item(key)
            override_latest = None

            payload: Dict[str, Any] = {
                "key": latest_item.get("key", key),
                "version": latest_item.get("version"),
            }

            base_data = dict(latest_item.get("data", {}) or {})
            if strict:
                payload.update(user_updates)
            else:
                merged = dict(base_data)
                merged.update(user_updates)
                payload.update(merged)

            version_value = payload.get("version")
            try:
                version_int = int(version_value)
            except (TypeError, ValueError):
                version_int = None

            headers = self._headers(None if force else version_int)
            response = _rq.put(
                url,
                json=payload,
                headers=headers,
                timeout=30,
            )
            last_response = response

            if response.status_code in (200, 201, 204):
                return

            if response.status_code == 412:
                # Try to use server-provided latest snapshot, if present
                diag = None
                try:
                    if response.headers.get("content-type", "").startswith("application/json"):
                        diag = response.json()
                except Exception:
                    diag = None

                latest_list = diag.get("latest") if isinstance(diag, dict) else None
                if isinstance(latest_list, list) and latest_list:
                    latest_candidate = latest_list[0]
                    if isinstance(latest_candidate, dict):
                        override_latest = latest_candidate
                        continue

                delay = min(2.0, 0.2 * (2 ** (attempt - 1)))
                time.sleep(delay)
                continue

            response.raise_for_status()

        if last_response is not None:
            detail = (last_response.text or "").strip()
            raise RuntimeError(
                f"Web API update failed after retries (HTTP {last_response.status_code})\n"
                f"- URL: {url}\n- Method: PUT\n- Response: {detail}"
            )

        raise RuntimeError("Web API update failed after retries")

    # ---- Internal helpers ----
    def _base_url(self) -> str:
        if self.client._endpoint_override:
            return str(self.client._endpoint_override).rstrip("/")
        return "https://api.zotero.org"

    def _headers(self, unmodified_since_version: Optional[int] = None) -> Dict[str, str]:
        headers: Dict[str, str] = {
            "Zotero-API-Version": "3",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        }
        if self.client.api_key:
            headers["Zotero-API-Key"] = str(self.client.api_key)
        if isinstance(unmodified_since_version, int):
            headers["If-Unmodified-Since-Version"] = str(unmodified_since_version)
        return headers

    def _latest_library_version(self) -> int:
        import requests as _rq

        url = f"{self._base_url()}/users/{int(self.client.library_id)}/items"
        response = _rq.get(
            url,
            params={"limit": 1, "_": str(int(time.time() * 1000))},
            headers=self._headers(),
            timeout=30,
        )
        response.raise_for_status()
        header_value = response.headers.get("Last-Modified-Version") or response.headers.get("Last-Modified-" "Version")
        try:
            return int(header_value) if header_value is not None else 0
        except Exception:
            return 0

    def _get_item(self, key: str) -> Dict[str, Any]:
        import requests as _rq

        url = f"{self._base_url()}/users/{int(self.client.library_id)}/items/{key}"
        response = _rq.get(
            url,
            params={"_": str(int(time.time() * 1000))},
            headers=self._headers(),
            timeout=30,
        )
        response.raise_for_status()
        return response.json()

    def _delete_items(self, keys: Iterable[str]) -> None:
        import requests as _rq

        key_list = list(keys)
        if not key_list:
            return
        base = self._base_url()
        url = f"{base}/users/{int(self.client.library_id)}/items"
        item_keys = ",".join(key_list)

        def _attempt(version: Optional[int]) -> _rq.Response:
            return _rq.delete(
                url,
                params={"itemKey": item_keys},
                headers=self._headers(version),
                timeout=30,
            )

        version = self._latest_library_version()
        response = _attempt(version if version else None)
        if response.status_code == 412:
            version = self._latest_library_version()
            response = _attempt(version if version else None)
        if response.status_code >= 400:
            response.raise_for_status()



class ZoteroClient:
    def __init__(
        self,
        library_id: int,
        library_type: str = "user",
        api_key: Optional[str] = None,
        endpoint: Optional[str] = None,
        local: bool = True,
    ) -> None:
        self.library_id = library_id
        self.library_type = library_type
        self.api_key = api_key
        self._endpoint_override = endpoint
        self._local_flag = local
        self.zot = Zotero(
            library_id,
            library_type,
            api_key=api_key,
            local=local,
        )
        if endpoint:
            self.zot.endpoint = endpoint
        self._api: _BaseZoteroAPI = _LocalZoteroAPI(self) if local else _WebZoteroAPI(self)

    def ping(self) -> bool:
        try:
            list(self.zot.items(limit=1))
            return True
        except Exception:
            return False

    def _build_search_plan(
        self,
        *,
        q: Optional[str],
        collection: Optional[str],
        tag: Optional[str],
        itemType: Optional[str],
        author: Optional[str],
        title: Optional[str],
        year: Optional[str],
        doi: Optional[str],
    ) -> _SearchPlan:
        """Construct search parameters and client filters for list_items."""

        params: Dict[str, Any] = {}
        collection_key = collection
        if q:
            params.update({"q": q, "qmode": "everything"})
        if tag:
            params["tag"] = tag
        if itemType:
            params["itemType"] = itemType

        server_flags: Dict[str, bool] = {
            "author": False,
            "title": False,
            "year": False,
            "doi": False,
        }

        if doi:
            params = {"q": doi, "qmode": "everything"}
            collection_key = None
            server_flags["doi"] = True
        elif not q:
            author_provided = bool(author)
            title_provided = bool(title)
            year_provided = bool(year)

            if author_provided and not title_provided and not year_provided:
                params.update({"q": author, "qmode": "titleCreatorYear"})
                server_flags["author"] = True
            elif title_provided and not author_provided and not year_provided:
                params.update({"q": title, "qmode": "titleCreatorYear"})
                server_flags["title"] = True
            elif year_provided and not author_provided and not title_provided:
                params.update({"q": str(year), "qmode": "titleCreatorYear"})
                server_flags["year"] = True
            elif author_provided and title_provided and not year_provided:
                params.update({"q": author, "qmode": "titleCreatorYear"})
                server_flags["author"] = True
            elif author_provided and year_provided and not title_provided:
                params.update({"q": author, "qmode": "titleCreatorYear"})
                server_flags["author"] = True
            elif year_provided and title_provided and not author_provided:
                params.update({"q": str(year), "qmode": "titleCreatorYear"})
                server_flags["year"] = True
            elif author_provided and title_provided and year_provided:
                params.update({"q": author, "qmode": "titleCreatorYear"})
                server_flags["author"] = True

        filters_author = "" if server_flags["author"] else (author or "").strip().lower()
        filters_title = "" if server_flags["title"] else (title or "").strip().lower()
        year_text = str(year) if year is not None else ""
        filters_year = "" if server_flags["year"] else year_text.strip()
        filters_doi = "" if server_flags["doi"] else (doi or "").strip().lower()

        if doi:
            filters_author = ""
            filters_title = ""
            filters_year = ""

        filters = _ClientFilters(
            author=filters_author,
            title=filters_title,
            year=filters_year,
            doi=filters_doi,
        )
        return _SearchPlan(params=dict(params), filters=filters, collection_key=collection_key)

    def _fetch_server_items(
        self,
        collection_key: Optional[str],
        params: Mapping[str, Any],
        limit: int,
    ) -> List[Dict[str, Any]]:
        """Fetch items directly from Zotero when no client filtering is needed."""

        options = dict(params)
        if collection_key:
            return list(self.zot.collection_items(collection_key, limit=limit, **options))
        return list(self.zot.items(limit=limit, **options))

    def _collect_client_filtered_items(self, plan: _SearchPlan, limit: int) -> List[Dict[str, Any]]:
        """Gather items with client-side filtering until the requested limit is met."""

        matches: List[Dict[str, Any]] = []
        page_size = self._determine_page_size(limit)
        for batch in self._page_results(plan.collection_key, plan.params, page_size):
            for item in batch:
                if self._item_matches_filters(item, plan.filters):
                    matches.append(item)
                    if len(matches) >= limit:
                        return matches
        return matches

    def _determine_page_size(self, limit: int) -> int:
        """Return the number of items to retrieve per request when paging."""

        return min(max(limit, 50), 200)

    def _page_results(
        self,
        collection_key: Optional[str],
        params: Mapping[str, Any],
        page_size: int,
    ) -> Iterable[List[Dict[str, Any]]]:
        """Yield successive result pages from the Zotero API."""

        start = 0
        while True:
            batch = self._fetch_page(collection_key, params, page_size, start)
            if not batch:
                break
            yield batch
            if len(batch) < page_size:
                break
            start += page_size

    def _fetch_page(
        self,
        collection_key: Optional[str],
        params: Mapping[str, Any],
        page_size: int,
        start: int,
    ) -> List[Dict[str, Any]]:
        """Request a single page of items from Zotero."""

        options = dict(params)
        if collection_key:
            return list(
                self.zot.collection_items(
                    collection_key,
                    limit=page_size,
                    start=start,
                    **options,
                )
            )
        return list(self.zot.items(limit=page_size, start=start, **options))

    def _item_matches_filters(self, item: Dict[str, Any], filters: _ClientFilters) -> bool:
        """Return True when the item satisfies all active client-side filters."""

        normalized = normalize_item(item)
        data = item.get("data", {})
        meta = item.get("meta", {})

        if filters.title:
            if filters.title not in (normalized.title or "").lower():
                return False

        if filters.author:
            creator_names = [creator.lower() for creator in normalized.creators]
            for creator in (data.get("creators") or []):
                last = (creator.get("lastName") or creator.get("familyName") or "").lower()
                first = (creator.get("firstName") or creator.get("givenName") or "").lower()
                name = f"{last}, {first}".strip().strip(",")
                if name:
                    creator_names.append(name)
            creator_summary = str(meta.get("creatorSummary", "")).lower()
            has_author_match = any(filters.author in name for name in creator_names) or (
                filters.author in creator_summary if creator_summary else False
            )
            if not has_author_match:
                return False

        if filters.year:
            if not (normalized.year or "").startswith(filters.year):
                return False

        if filters.doi:
            doi_value = (normalized.doi or data.get("DOI") or "").strip().lower()
            if not doi_value or filters.doi not in doi_value:
                return False
        return True

    def list_items(
        self,
        limit: int = 200,
        q: Optional[str] = None,
        collection: Optional[str] = None,
        tag: Optional[str] = None,
        itemType: Optional[str] = None,
        author: Optional[str] = None,
        title: Optional[str] = None,
        year: Optional[str] = None,
        doi: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        plan = self._build_search_plan(
            q=q,
            collection=collection,
            tag=tag,
            itemType=itemType,
            author=author,
            title=title,
            year=year,
            doi=doi,
        )

        if not plan.filters.any():
            return self._fetch_server_items(plan.collection_key, plan.params, limit)
        return self._collect_client_filtered_items(plan, limit)

    def get_item(self, key: str) -> Dict[str, Any]:
        return self.zot.item(key)

    def children(self, key: str) -> List[Dict[str, Any]]:
        return list(self.zot.children(key))

    def collections(self) -> List[Dict[str, Any]]:
        # Fetch all collections (pyzotero defaults to paging)
        results: List[Dict[str, Any]] = []
        start = 0
        page_size = 200
        while True:
            batch = list(self.zot.collections(limit=page_size, start=start))
            if not batch:
                break
            results.extend(batch)
            if len(batch) < page_size:
                break
            start += page_size
        return results

    def get_collection(self, key: str) -> Dict[str, Any]:
        """Fetch a single collection by key."""
        return self.zot.collection(key)

    def tags(self) -> List[str]:
        return list(self.zot.tags())

    def export_csljson(self, keys: Iterable[str]) -> List[Dict[str, Any]]:
        return self._api.export_csljson(keys)


    def export_bibtex(self, keys: Iterable[str]) -> str:
        return self._api.export_bibtex(keys)


    def create_items(self, items: List[Dict[str, Any]]) -> Dict[str, Any]:
        return self._api.create_items(items)

    def item_template(self, item_type: str) -> Dict[str, Any]:
        """Return a Zotero item template, with a local-API-safe fallback.

        Some local API builds do not support /items/new; in that case, fall back to
        a minimal template that is acceptable to create_items.
        """
        try:
            return self.zot.item_template(item_type)
        except Exception:
            base: Dict[str, Any] = {
                "itemType": item_type,
                "title": "",
                "creators": [],
                "abstractNote": "",
                "date": "",
                "url": "",
                "DOI": "",
                "language": "",
                "accessDate": "",
                "rights": "",
                "extra": "",
                "tags": [],
                "collections": [],
            }
            # Common container fields used by our importers
            base.setdefault("publicationTitle", "")
            base.setdefault("journalAbbreviation", "")
            base.setdefault("volume", "")
            base.setdefault("issue", "")
            base.setdefault("pages", "")
            # arXiv-related optional fields
            base.setdefault("archive", "")
            base.setdefault("archiveLocation", "")
            return base

    def is_local(self) -> bool:
        return self._api.is_local()

    def trash_items(self, keys: Iterable[str]) -> None:
        """Move one or more items to Zotero Trash."""
        self._api.trash_items(keys)

    def delete_items(self, keys: Iterable[str]) -> None:
        """Delete items (moves to Trash in Zotero)."""
        self._api.delete_items(keys)

    def update_item_data(self, key: str, data_updates: Dict[str, Any]) -> None:
        """Update an item's data fields.

        Fetches the current item, applies shallow updates to its 'data' dict,
        and calls the underlying Zotero update API. The item's current version
        is preserved to satisfy concurrency headers.
        """
        # Fetch full item to retain key and version
        current = self.get_item(key)
        cur_data = current.get("data", {}) or {}
        # Apply shallow updates; caller can provide nested structures as needed
        merged = dict(cur_data)
        merged.update(data_updates or {})
        # Build the item dict expected by pyzotero.update_item: include key and version,
        # with all item fields flattened at the top level (Web API rejects a nested 'data')
        item_for_update: Dict[str, Any] = {
            "key": current.get("key", key),
            "version": current.get("version"),
        }
        item_for_update.update(merged)
        self.zot.update_item(item_for_update)

    def update_child_item_fields(self, key: str, fields: Dict[str, Any]) -> None:
        """Update fields on a non-top-level child item (e.g., a note or attachment).

        Unlike update_item_data, which merges into the parent item's 'data' dict,
        this method updates fields on the child item itself by sending a flattened
        item structure expected by the Zotero APIs (key, version, and top-level fields).
        """
        # Reuse the robust updater which handles web-mode PUT with proper
        # version headers and retries on concurrency conflicts. For local
        # mode it will delegate to pyzotero.update_item with a fresh version.
        self.update_item_data_force(key, dict(fields or {}), strict=False)

    def update_item_data_force(
        self,
        key: str,
        full_data: Dict[str, Any],
        strict: bool = False,
        force: bool = False,
    ) -> None:
        """Forcefully update an item's data using the latest known versions.
        """
        self._api.update_item_data_force(key, full_data, strict, force)
