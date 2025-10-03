from __future__ import annotations

import json
from typing import Any, Dict, List, Set
import typer
import fast_diff_match_patch as fast_diff  

__all__ = [
    "json_equal",
    "changed_keys",
    "collapse_one_line",
    "trim_middle",
    "to_str_for_diff",
    "format_normal_value",
    "format_inline_three_way_diff",
    "compute_three_way_diff_segments",
    "format_fast_dmp_inline",
]


def to_str_for_diff(value: Any, *, ensure_ascii: bool = False, sort_keys: bool = True, indent: int | None = None) -> str:
    """Serialize any value to a string suitable for diffing.

    - Strings passed through as-is
    - JSON-serialize other values (sorted keys for stable comparisons)
    """
    if isinstance(value, str):
        return value
    try:
        return json.dumps(value, ensure_ascii=ensure_ascii, sort_keys=sort_keys, indent=indent)
    except Exception:
        return str(value)


def collapse_one_line(text: str, *, collapse: bool = False) -> str:
    """Collapse or preserve newlines/whitespace.

    - When ``collapse=True``: collapse to a single, console-friendly line with
      visible newline markers.
    - When ``collapse=False`` (default): preserve original newlines and spacing.
    """
    if not collapse:
        return text
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return " ".join(normalized.replace("\n", " ⏎ ").split())


def trim_middle(text: str, max_len: int, *, keep: str = "ends") -> str:
    """Trim a long string to ``max_len`` with ellipsis, controlling which part to keep.

    - keep="ends": keep the head and tail, elide the middle (previous behavior)
    - keep="middle": keep the middle, elide from both ends equally
    """
    if max_len <= 0:
        return ""
    if len(text) <= max_len:
        return text

    ellipsis = "..."
    if max_len <= len(ellipsis):
        return ellipsis[:max_len]

    if keep == "middle":
        # Keep the central window and elide both ends with ellipses: '...<middle>...'
        # Need room for two ellipses
        if max_len <= 2 * len(ellipsis):
            return ellipsis if max_len >= len(ellipsis) else ellipsis[:max_len]
        window = max_len - 2 * len(ellipsis)
        start = max((len(text) - window) // 2, 0)
        middle = text[start:start + window]
        return ellipsis + middle + ellipsis

    # Default: keep both ends and elide center
    head = max_len // 2 - 2
    if head < 0:
        head = 0
    tail = max_len - head - len(ellipsis)
    if tail < 0:
        tail = 0
    return text[:head] + ellipsis + text[-tail:]


def json_equal(a: Any, b: Any) -> bool:
    """Compare two values by JSON representation with stable key ordering."""
    return json.dumps(a, sort_keys=True, ensure_ascii=False) == json.dumps(b, sort_keys=True, ensure_ascii=False)


def changed_keys(a: Dict[str, Any], b: Dict[str, Any]) -> Set[str]:
    """Return the set of keys whose values differ under json_equal."""
    keys = set(a.keys()) | set(b.keys())
    out: Set[str] = set()
    for k in keys:
        if not json_equal(a.get(k), b.get(k)):
            out.add(k)
    return out


def format_normal_value(value: Any, *, max_len: int = 200, collapse: bool = False) -> str:
    """Serialize a value for the Normal diff and trim.

    - Converts to string/JSON
    - Optionally collapses to one line with visible newlines when ``collapse=True``
    - Trims the middle if longer than ``max_len``
    """
    s = to_str_for_diff(value, ensure_ascii=False, sort_keys=True)
    s = collapse_one_line(s, collapse=collapse)
    s = trim_middle(s, max_len)
    return s


def compute_three_way_diff_segments(
    base_text: Any,
    local_text: Any,
    remote_text: Any,
    *,
    max_segment: int = 200,
    collapse: bool = False,
) -> List[Dict[str, str]]:
    """Compute normalized three-way diff segments for base/remote/local.

    Returns a list of segments. Each segment is a dict with keys:
    - type: "ctx" for unchanged context, "change" for changed section
    - base, remote, local: collapsed and trimmed strings for each side

    The function performs the core span identification shared by inline and table styles.
    """
    if fast_diff is None:
        raise RuntimeError("fast-diff-match-patch not available, install with `pip install fast-diff-match-patch`")

    a_raw = to_str_for_diff(base_text, ensure_ascii=False, sort_keys=True)
    l_raw = to_str_for_diff(local_text, ensure_ascii=False, sort_keys=True)
    r_raw = to_str_for_diff(remote_text, ensure_ascii=False, sort_keys=True)

    if collapse:
        a = a_raw.replace("\r\n", "\n").replace("\r", "\n")
        l = l_raw.replace("\r\n", "\n").replace("\r", "\n")
        r = r_raw.replace("\r\n", "\n").replace("\r", "\n")
    else:
        a = a_raw
        l = l_raw
        r = r_raw

    if a == l == r:
        one = collapse_one_line(a, collapse=collapse)
        return [{"type": "ctx", "base": one, "remote": one, "local": one}]

    try:
        chunks_ar = fast_diff.diff(a, r, counts_only=False, cleanup="Semantic", timelimit=0.05)
    except TypeError:
        chunks_ar = fast_diff.diff(a, r)
    try:
        chunks_al = fast_diff.diff(a, l, counts_only=False, cleanup="Semantic", timelimit=0.05)
    except TypeError:
        chunks_al = fast_diff.diff(a, l)

    def _collect_change_intervals(chunks: list[tuple[str, str]]) -> list[tuple[int, int]]:
        intervals: list[tuple[int, int]] = []
        base_idx = 0
        for op, seg in chunks:
            if op == "=":
                base_idx += len(seg)
            elif op == "-":
                start = base_idx
                base_idx += len(seg)
                intervals.append((start, base_idx))
            elif op == "+":
                intervals.append((base_idx, base_idx))
        return intervals

    base_len = len(a)
    intervals = _collect_change_intervals(chunks_ar) + _collect_change_intervals(chunks_al)
    if not intervals:
        one = collapse_one_line(a, collapse=collapse)
        return [{"type": "ctx", "base": one, "remote": one, "local": one}]
    intervals.sort()

    merged: list[tuple[int, int]] = []
    for s0, e0 in intervals:
        if not merged:
            merged.append((s0, e0))
            continue
        ps, pe = merged[-1]
        if s0 <= pe:
            merged[-1] = (ps, max(pe, e0))
        else:
            merged.append((s0, e0))

    def _extract_other_for_base_span(chunks: list[tuple[str, str]], base_s: int, base_e: int) -> str:
        pieces: list[str] = []
        base_idx = 0
        for op, seg in chunks:
            if op == "=":
                seg_len = len(seg)
                seg_start = base_idx
                seg_end = base_idx + seg_len
                over_s = max(base_s, seg_start)
                over_e = min(base_e, seg_end)
                if over_s < over_e:
                    pieces.append(seg[over_s - seg_start: over_e - seg_start])
                base_idx += seg_len
            elif op == "-":
                base_idx += len(seg)
            elif op == "+":
                if base_s <= base_idx <= base_e:
                    pieces.append(seg)
        return "".join(pieces)

    segments: List[Dict[str, str]] = []
    cursor = 0
    for s_idx, e_idx in merged:
        if cursor < s_idx:
            ctx = collapse_one_line(a[cursor:s_idx], collapse=collapse)
            segments.append({"type": "ctx", "base": ctx, "remote": ctx, "local": ctx})

        a_mid = a[s_idx:e_idx]
        r_mid = _extract_other_for_base_span(chunks_ar, s_idx, e_idx)
        l_mid = _extract_other_for_base_span(chunks_al, s_idx, e_idx)

        a_mid_disp = collapse_one_line(trim_middle(a_mid, max_segment), collapse=collapse)
        r_mid_disp = collapse_one_line(trim_middle(r_mid, max_segment), collapse=collapse)
        l_mid_disp = collapse_one_line(trim_middle(l_mid, max_segment), collapse=collapse)

        segments.append({"type": "change", "base": a_mid_disp, "remote": r_mid_disp, "local": l_mid_disp})
        cursor = e_idx

    if cursor < base_len:
        tail = collapse_one_line(a[cursor:], collapse=collapse)
        segments.append({"type": "ctx", "base": tail, "remote": tail, "local": tail})

    return segments

def format_inline_three_way_diff(base_text: Any, local_text: Any, remote_text: Any, *, context: int = 100, max_segment: int = 200, collapse: bool = False) -> str:
    """Return a compact one-line inline triple diff with multiple bracketed segments.

    Example: one [two → 2 → second] four … eleven [twelve → 12 → 12th] thirteen
    """
    segments = compute_three_way_diff_segments(base_text, local_text, remote_text, max_segment=max_segment, collapse=collapse)

    parts: list[str] = []
    for seg in segments:
        if seg["type"] == "ctx":
            parts.append(seg["base"])  # context same on all
        else:
            base_col = typer.style(seg["base"], fg=typer.colors.WHITE, dim=True)
            remote_col = typer.style(seg["remote"], fg=typer.colors.BLUE)
            yours_col = typer.style(seg["local"], fg=typer.colors.GREEN)
            parts.append("[" + base_col + " → " + remote_col + " → " + yours_col + "]")

    return "".join(parts)


def format_fast_dmp_inline(old_text: Any, new_text: Any, *, context: int = 80, max_len: int = 200, insert_color: typer.colors.Color | None = None, collapse: bool = False) -> str:
    """Return a compact one-line inline diff using fast-diff-match-patch.

    Shows surrounding context and highlights changes inline with colors:
    - deletions in RED inside [- ... -]
    - insertions in GREEN inside [+ ... +]
    - unchanged text shown dimmed
    """
    if fast_diff is None:
        # Fallback: simple inline showing trimmed old/new
        a = collapse_one_line(to_str_for_diff(old_text, ensure_ascii=False, sort_keys=True), collapse=collapse)
        b = collapse_one_line(to_str_for_diff(new_text, ensure_ascii=False, sort_keys=True), collapse=collapse)
        a = trim_middle(a, max_len)
        b = trim_middle(b, max_len)
        ins_col = insert_color or typer.colors.GREEN
        return "[" + typer.style(a, fg=typer.colors.RED) + " → " + typer.style(b, fg=ins_col) + "]"

    a_raw = to_str_for_diff(old_text, ensure_ascii=False, sort_keys=True)
    b_raw = to_str_for_diff(new_text, ensure_ascii=False, sort_keys=True)
    if collapse:
        a = a_raw.replace("\r\n", "\n").replace("\r", "\n")
        b = b_raw.replace("\r\n", "\n").replace("\r", "\n")
    else:
        a = a_raw
        b = b_raw

    if a == b:
        one = collapse_one_line(a, collapse=collapse)
        return trim_middle(one, max_len)

    # Compute diff; request counts_only=False to get substrings
    try:
        chunks = fast_diff.diff(a, b, counts_only=False, cleanup="Semantic", timelimit=0.05)
    except TypeError:
        # Older versions may use positional args or different options
        chunks = fast_diff.diff(a, b)

    # Build a single-line with small context around the first changed chunk
    parts: list[str] = []
    total_len = 0
    seen_change = False

    def _append(text: str) -> None:
        nonlocal total_len
        if not text:
            return
        remaining = max_len - total_len
        if remaining <= 0:
            return
        if len(text) > remaining:
            text = text[: max(0, remaining - 1)] + "…"
        parts.append(text)
        total_len += len(text)

    # Collapse long equal runs to show only local context
    for (op, seg) in chunks:
        if op == "=":
            if not seen_change:
                # Head context before first change
                head = collapse_one_line(seg, collapse=collapse)
                if len(head) > context:
                    head = "…" + head[-context:]
                _append(head)
            else:
                tail = collapse_one_line(seg, collapse=collapse)
                if len(tail) > context:
                    tail = tail[:context] + "…"
                _append(tail)
        elif op == "-":
            seen_change = True
            mid = collapse_one_line(seg, collapse=collapse)
            _append("[" + typer.style(mid, fg=typer.colors.RED) + "]")
        elif op == "+":
            seen_change = True
            mid = collapse_one_line(seg, collapse=collapse)
            ins_col = insert_color or typer.colors.GREEN
            _append("[" + typer.style(mid, fg=ins_col) + "]")
        else:
            # Unknown op; be robust
            seen_change = True
            mid = collapse_one_line(str(seg), collapse=collapse)
            _append("[" + mid + "]")

    return "".join(parts)
