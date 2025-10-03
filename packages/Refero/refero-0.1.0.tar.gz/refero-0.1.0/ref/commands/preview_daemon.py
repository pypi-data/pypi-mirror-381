from __future__ import annotations

"""Preview daemon for fzf preview integration.

This daemon receives Zotero item keys over a request pipe and writes a single-line
JSON payload per key to the response pipe. It optionally preloads a set of keys at
startup to warm the cache for snappy previews.

Environment variables used by this module:

- REF_PREVIEW_DAEMON_REQ_R_FD: read-end FD number for incoming key requests.
- REF_PREVIEW_DAEMON_RESP_W_FD: write-end FD number for outgoing JSON payloads.
- REF_PREVIEW_DAEMON_PRELOAD: optional comma-separated list of keys to preload.

The client-side helper is implemented in ``ref/commands/preview_client.py``.
"""

import json
import os
import sys
from typing import Dict, Iterable, Optional, Tuple
import socket
import socketserver
import threading
import json as _json

from .listing import normalize_item, build_item_collection_display
from ..utils.collections import build_collection_index
from ..utils.zotero import zot_from_config


def _coerce_fd_from_env(name: str) -> int:
    value = os.environ.get(name)
    if value is None:
        raise RuntimeError(f"Missing environment variable: {name}")
    try:
        return int(value)
    except ValueError as exc:  # noqa: B904
        raise RuntimeError(f"Invalid file descriptor for {name}: {value}") from exc


def _iter_preload_keys_from_env() -> Iterable[str]:
    raw = os.environ.get("REF_PREVIEW_DAEMON_PRELOAD")
    if not raw:
        return ()
    return (k.strip() for k in raw.split(",") if k.strip())


def _render_payload(key: str, *, zot=None, collection_index=None) -> str:
    """Return a compact single-line JSON payload for a given item key.

    On errors, returns a JSON object with an "error" field.
    """
    try:
        if zot is None:
            zot = zot_from_config()
        item = zot.get_item(key)
        normalized = normalize_item(item)
        if collection_index is None:
            collection_index = build_collection_index(zot)
        display = build_item_collection_display(normalized, collection_index)
        data = dict(normalized.__dict__)
        data["collection_paths"] = list(display.paths)
        text = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    except Exception as exc:  # noqa: BLE001
        text = json.dumps({"key": key, "error": str(exc) or "preview failed"}, ensure_ascii=False)
    # ensure single-line payload for client .readline()
    return text.replace("\n", " ")


def _serve(req_fd: int, resp_fd: int, *, preload_keys: Iterable[str]) -> int:
    """Main request/response loop; returns exit status code."""
    cache: Dict[str, str] = {}

    # Initialize Zotero client and shared indices once
    try:
        zot = zot_from_config()
    except Exception:
        zot = None  # fallback in _render_payload handles this case

    collection_index = None
    if zot is not None:
        try:
            collection_index = build_collection_index(zot)
        except Exception:
            collection_index = None

    # Preload known keys
    for key in preload_keys:
        if key and key not in cache:
            cache[key] = _render_payload(key, zot=zot, collection_index=collection_index)

    # Start serving requests
    reader = os.fdopen(req_fd, "r", buffering=1, closefd=False)
    writer = os.fdopen(resp_fd, "w", buffering=1, closefd=False)

    try:
        for line in reader:
            key = line.strip()
            if not key:
                writer.write("{}\n")
                writer.flush()
                continue
            payload = cache.get(key)
            if payload is None:
                payload = _render_payload(key, zot=zot, collection_index=collection_index)
                cache[key] = payload
            writer.write(payload + "\n")
            writer.flush()
    except (BrokenPipeError, OSError):
        # Client side closed; exit gracefully
        return 0
    finally:
        try:
            writer.flush()
        except Exception:
            pass
        try:
            writer.close()
        except Exception:
            pass
        try:
            reader.close()
        except Exception:
            pass
    return 0


def _serve_tcp(*, preload_keys: Iterable[str]) -> int:
    """Serve preview requests over a localhost TCP socket.

    Protocol: client connects, sends a single line "<token> <key>\n"; server responds
    with a single-line JSON payload and closes the connection.
    """
    # Shared state
    cache: Dict[str, str] = {}

    try:
        zot = zot_from_config()
    except Exception:
        zot = None
    try:
        collection_index = build_collection_index(zot) if zot is not None else None
    except Exception:
        collection_index = None

    for key in preload_keys:
        if key and key not in cache:
            cache[key] = _render_payload(key, zot=zot, collection_index=collection_index)

    host = os.environ.get("REF_PREVIEW_DAEMON_HOST") or "127.0.0.1"
    port_raw = os.environ.get("REF_PREVIEW_DAEMON_PORT")
    try:
        port = int(port_raw) if port_raw else 0
    except Exception:
        port = 0
    token = os.environ.get("REF_PREVIEW_DAEMON_TOKEN") or ""
    meta_path = os.environ.get("REF_PREVIEW_DAEMON_META")

    class _Handler(socketserver.BaseRequestHandler):  # type: ignore[type-arg]
        def handle(self) -> None:  # noqa: D401 - simple handler
            try:
                data = self.request.recv(4096)
                if not data:
                    return
                try:
                    line = data.decode("utf-8", errors="replace").strip()
                except Exception:
                    return
                # Expect: "<token> <key>"
                parts = line.split(" ", 1)
                if len(parts) != 2:
                    return
                recv_token, key = parts[0], parts[1].strip()
                if token and recv_token != token:
                    self.request.sendall(b"{}\n")
                    return
                payload = cache.get(key)
                if payload is None:
                    payload = _render_payload(key, zot=zot, collection_index=collection_index)
                    cache[key] = payload
                self.request.sendall((payload + "\n").encode("utf-8", errors="replace"))
            except Exception:
                try:
                    self.request.sendall(b"{}\n")
                except Exception:
                    pass

    class _TCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):  # type: ignore[misc]
        allow_reuse_address = True
        daemon_threads = True

    with _TCPServer((host, port), _Handler) as srv:
        # Write meta with chosen host/port to a file for the parent process
        addr: Tuple[str, int] = srv.server_address  # type: ignore[assignment]
        if isinstance(addr, tuple) and len(addr) >= 2 and meta_path:
            try:
                payload = {"host": addr[0], "port": int(addr[1]), "token": token}
                with open(meta_path, "w", encoding="utf-8") as fp:
                    _json.dump(payload, fp, ensure_ascii=False)
            except Exception:
                pass
        try:
            srv.serve_forever(poll_interval=0.2)
        except KeyboardInterrupt:
            return 0
        except Exception:
            return 1
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    mode = (os.environ.get("REF_PREVIEW_DAEMON_MODE") or "").strip().lower()
    preload = list(_iter_preload_keys_from_env())
    if mode == "tcp":
        return _serve_tcp(preload_keys=preload)
    # Default FD mode
    req_fd = _coerce_fd_from_env("REF_PREVIEW_DAEMON_REQ_R_FD")
    resp_fd = _coerce_fd_from_env("REF_PREVIEW_DAEMON_RESP_W_FD")
    return _serve(req_fd, resp_fd, preload_keys=preload)


if __name__ == "__main__":  # pragma: no cover - direct module execution
    raise SystemExit(main(sys.argv[1:]))
