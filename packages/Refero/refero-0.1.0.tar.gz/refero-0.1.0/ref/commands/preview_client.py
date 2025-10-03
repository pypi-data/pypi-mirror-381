from __future__ import annotations

"""Helper client that proxies keys to a running preview daemon via shared pipes.

This module is intended to be invoked by fzf's --preview command. It looks for
two file descriptors in the environment (REF_PREVIEW_DAEMON_IN_FD and
REF_PREVIEW_DAEMON_OUT_FD). If present, it sends a requested Zotero key to the
daemon and prints one line of JSON as the preview output. If the FDs are not
available (no daemon), it falls back to fetching from Zotero directly.
"""

import json
import os
import shutil
import subprocess
import sys
import socket
from typing import NoReturn

from ._registry import CommandBinding


def _read_env_fd(name: str) -> int:
    value = os.environ.get(name)
    if value is None:
        raise RuntimeError(f"Missing environment variable: {name}")
    try:
        return int(value)
    except ValueError as exc:  # noqa: B904
        raise RuntimeError(f"Invalid file descriptor for {name}: {value}") from exc


def _print_payload(payload: str, pretty: bool) -> None:
    if not payload:
        print("", end="")
        return

    if pretty:
        try:
            from rich.json import JSON as RichJSON  # local import to keep fast path light
            from rich.console import Console as _Console

            # Force color even when piped to fzf
            _preview_console = _Console(force_terminal=True)

            try:
                data = json.loads(payload)
                renderable = RichJSON.from_data(data)
                _preview_console.print(renderable)
                return
            except json.JSONDecodeError:
                # Fallback to raw payload as plain text if it's not valid JSON
                pass
        except Exception:
            # If Rich is unavailable for any reason, fall back to Python pretty
            try:
                data = json.loads(payload)
                payload = json.dumps(data, ensure_ascii=False, indent=2)
            except json.JSONDecodeError:
                pass

    print(payload)


def _print_text_from_payload(payload: str) -> None:
    """Render a compact single-line preview from a JSON payload string.

    Falls back to printing the raw payload on JSON decode errors.
    """
    try:
        data = json.loads(payload)
        if not isinstance(data, dict):
            print(payload)
            return
        if data.get("error"):
            # Show the error message as-is
            print(str(data.get("error")))
            return

        title = str(data.get("title") or "")
        year = str(data.get("year") or "")
        creators = data.get("creators") or []
        if isinstance(creators, list):
            authors = "; ".join(str(x) for x in creators if str(x).strip())
        else:
            authors = str(creators)
        tags = data.get("tags") or []
        if isinstance(tags, list):
            tags_str = ",".join(str(t) for t in tags if str(t).strip())
        else:
            tags_str = str(tags)

        which = (
            str(data.get("journalAbbreviation") or "")
            or str(data.get("publication") or "")
            or str(data.get("itemType") or "")
        )
        line = f"{year} • {which} • {authors} • {tags_str} • {title}"
        print(line)
    except Exception:
        # If anything goes wrong, just print the raw payload
        print(payload)


def _fallback_render(key: str, pretty: bool) -> None:
    # Lazy-import heavy modules so daemon-backed fast path remains lightweight
    try:
        from .listing import normalize_item, build_item_collection_display  # type: ignore
        from ..utils.collections import build_collection_index  # type: ignore
        from ..utils.zotero import zot_from_config  # type: ignore

        zot = zot_from_config()
        item = zot.get_item(key)
        normalized = normalize_item(item)
        collection_index = build_collection_index(zot)
        display = build_item_collection_display(normalized, collection_index)
        data = dict(normalized.__dict__)
        data["collection_paths"] = list(display.paths)
        payload = json.dumps(data, ensure_ascii=False)
    except Exception as exc:  # noqa: BLE001
        payload = json.dumps(
            {
                "key": key,
                "error": (
                    str(exc)
                    or "Zotero preview unavailable. Ensure Zotero is running and your ref config connects to the local API."
                ),
            },
            ensure_ascii=False,
        )
    _print_payload(payload, pretty)


def _fallback_render_text(key: str) -> None:
    """Fetch and render a compact one-line preview when no daemon is available."""
    try:
        from .listing import normalize_item  # type: ignore
        from ..utils.zotero import zot_from_config  # type: ignore
        from ..utils.display import format_tags  # type: ignore

        zot = zot_from_config()
        item = zot.get_item(key)
        normalized = normalize_item(item)
        creators_str = "; ".join(normalized.creators)
        tags_str = format_tags(normalized.tags)
        which = (
            normalized.journalAbbreviation or normalized.publication or normalized.itemType
        )
        line = f"{normalized.year} • {which} • {creators_str} • {tags_str} • {normalized.title}"
        print(line)
    except Exception as exc:  # noqa: BLE001
        print(str(exc) or "preview failed")


def main(argv: list[str]) -> NoReturn:
    if not argv:
        raise SystemExit("Usage: preview_client [--text|-t] <key>")
    text_mode = False
    args = list(argv)
    if args and args[0] in ("--text", "-t"):
        text_mode = True
        args = args[1:]
    if not args:
        raise SystemExit("Usage: preview_client [--text|-t] <key>")
    key = args[0]

    pretty = os.environ.get("REF_PREVIEW_DAEMON_PRETTY") == "1"

    in_fd_str = os.environ.get("REF_PREVIEW_DAEMON_IN_FD")
    out_fd_str = os.environ.get("REF_PREVIEW_DAEMON_OUT_FD")
    tcp_host = os.environ.get("REF_PREVIEW_TCP_HOST")
    tcp_port = os.environ.get("REF_PREVIEW_TCP_PORT")
    tcp_token = os.environ.get("REF_PREVIEW_TCP_TOKEN")

    # Prefer FD transport if available (Unix), else TCP if available, else fallback
    if in_fd_str and out_fd_str:
        in_fd = _read_env_fd("REF_PREVIEW_DAEMON_IN_FD")
        out_fd = _read_env_fd("REF_PREVIEW_DAEMON_OUT_FD")
        writer = os.fdopen(in_fd, "w", buffering=1, closefd=False)
        reader = os.fdopen(out_fd, "r", buffering=1, closefd=False)

        try:
            writer.write(key + "\n")
            writer.flush()
        except (BrokenPipeError, OSError):
            if text_mode:
                _fallback_render_text(key)
            else:
                _fallback_render(key, pretty)
            raise SystemExit(0)

        try:
            payload = reader.readline()
        except (BrokenPipeError, OSError):
            if text_mode:
                _fallback_render_text(key)
            else:
                _fallback_render(key, pretty)
            raise SystemExit(0)

        payload = payload.rstrip("\n")
        if not payload:
            if text_mode:
                _fallback_render_text(key)
            else:
                _fallback_render(key, pretty)
            raise SystemExit(0)

        if text_mode:
            _print_text_from_payload(payload)
        else:
            _print_payload(payload, pretty)
        raise SystemExit(0)

    if tcp_host and tcp_port:
        try:
            port = int(tcp_port)
        except Exception:
            port = 0
        if port <= 0:
            if text_mode:
                _fallback_render_text(key)
            else:
                _fallback_render(key, pretty)
            raise SystemExit(0)
        try:
            with socket.create_connection((tcp_host, port), timeout=1.0) as s:
                token = tcp_token or ""
                line = f"{token} {key}\n".encode("utf-8", errors="replace")
                s.sendall(line)
                # Read a single line response
                chunks = []
                while True:
                    data = s.recv(4096)
                    if not data:
                        break
                    chunks.append(data)
                    if b"\n" in data:
                        break
                payload = b"".join(chunks).decode("utf-8", errors="replace").splitlines()[0] if chunks else ""
        except Exception:
            payload = ""

        if not payload:
            if text_mode:
                _fallback_render_text(key)
            else:
                _fallback_render(key, pretty)
            raise SystemExit(0)

        if text_mode:
            _print_text_from_payload(payload)
        else:
            _print_payload(payload, pretty)
        raise SystemExit(0)

    # No daemon environment available; fallback directly
    if text_mode:
        _fallback_render_text(key)
    else:
        _fallback_render(key, pretty)
    raise SystemExit(0)


if __name__ == "__main__":
    main(sys.argv[1:])


def preview_client(key: str, text: bool = False) -> None:
    """CLI wrapper to run the preview client for fzf.

    Args:
        key: Zotero item key to preview.
        text: Render compact one-line text instead of JSON.
    """
    argv = (["--text", key] if text else [key])
    main(argv)


COMMANDS = (
    CommandBinding(callback=preview_client, name="preview-client"),
)
