from __future__ import annotations

import builtins
import json
from collections.abc import Sequence
from typing import Any, Dict

import typer

from ..config import load as load_config

__all__ = [
    "active_color_styles",
    "format_collection_paths",
    "format_listing_line",
    "format_tags",
    "header_filter",
    "match_filter",
    "style_option_key",
]


def active_color_styles() -> Dict[str, str]:
    """Return the active color styles (key/title/author/venue)."""
    cfg = load_config()
    schemes = cfg.color_schemes or {}
    name = cfg.color_scheme
    if not name or name not in schemes:
        valid = ", ".join(sorted(schemes.keys())) or "(none)"
        raise RuntimeError(f"Unknown color_scheme '{name}'. Valid schemes: {valid}")
    scheme = schemes[name] or {}
    return {
        "key": str(scheme.get("key", "bright_white")),
        "title": str(scheme.get("title", "")),
        "author": str(scheme.get("author", "")),
        "venue": str(scheme.get("venue", "")),
    }


def header_filter(data: Dict[str, Any]) -> str:
    cfg = load_config()
    fmt = cfg.fzf_header_format
    if isinstance(fmt, str) and fmt:
        try:
            return fmt.format(doc=data)
        except Exception:
            pass
    title = data.get("title", "")
    author = data.get("author", "")
    year = data.get("year", "")
    tags_raw = data.get("tags", [])
    tags = ",".join(tags_raw) if isinstance(tags_raw, builtins.list) else (
        tags_raw if isinstance(tags_raw, str) else ""
    )
    return (
        f"{title} :: {author} :: «{year}» :: :{tags} :: {data.get('key', '')} :: "
        f"{data.get('citekey', '')}"
    )


def match_filter(data: Dict[str, Any]) -> str:
    cfg = load_config()
    fmt = cfg.match_format
    if isinstance(fmt, str) and fmt:
        try:
            return fmt.format(doc=data)
        except Exception:
            pass
    return json.dumps(data, ensure_ascii=False)


def style_option_key(letter: str, color) -> str:
    return typer.style(letter, fg=color, bold=True)


def format_tags(tags: Sequence[str]) -> str:
    """Return a comma-separated representation of tag strings."""

    return ",".join(
        tag for tag in (str(tag).strip() for tag in tags) if tag
    )


def format_collection_paths(
    paths: Sequence[str],
    *,
    stylize: bool = False,
    separator: str = " / ",
) -> str:
    """Render one or more collection paths for display."""

    rendered: list[str] = []
    for raw in paths:
        if not raw:
            continue
        segments = [segment.strip() for segment in str(raw).split("->") if segment.strip()]
        if not segments:
            continue
        if stylize:
            highlight = "\033[90m >> \033[1;36m".join(segments)
            rendered.append(highlight)
        else:
            rendered.append(" -> ".join(segments))
    return separator.join(rendered)


def format_listing_line(
    *,
    key: str,
    title: str,
    authors: str,
    venue: str,
    year: str,
    tags: str,
    key_style: str = "",
    title_style: str = "",
    author_style: str = "",
    venue_style: str = "",
    collection_paths: str = "",
) -> str:
    """Format a list line with optional styling for key, title, author, and venue."""

    def _apply_style(value: str, style: str) -> str:
        return f"[{style}]{value}[/]" if style else value

    prefix = f"{collection_paths} :: " if collection_paths else ""
    return (
        prefix
        + f"{_apply_style(key, key_style)} :: "
        + f"{_apply_style(title, title_style)} :: "
        + f"{_apply_style(authors, author_style)} :: "
        + f"{_apply_style(venue, venue_style)} :: "
        + f"{year} :: :{tags}"
    )
