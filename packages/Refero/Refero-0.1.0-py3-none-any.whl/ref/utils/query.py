from __future__ import annotations

from typing import Iterable, Optional, Sequence

__all__ = ["coalesce_query", "normalize_tokens"]


def normalize_tokens(tokens: Optional[Iterable[str]]) -> Optional[str]:
    if not tokens:
        return None
    normalized = [str(token).strip() for token in tokens if str(token).strip()]
    if not normalized:
        return None
    return " ".join(normalized)


def coalesce_query(option_query: Optional[str], positional_tokens: Optional[Sequence[str]]) -> Optional[str]:
    if option_query is not None:
        return option_query
    return normalize_tokens(positional_tokens)
