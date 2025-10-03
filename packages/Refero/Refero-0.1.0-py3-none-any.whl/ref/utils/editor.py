from __future__ import annotations

import os
import shlex
import subprocess
import tempfile
from pathlib import Path
from typing import Callable, Optional

import typer

from ..config import load as load_config

__all__ = [
    "NoteEditorMode",
    "get_note_editor_mode",
    "edit_text_in_editor",
    "edit_via_editor",
]


class NoteEditorMode(str):
    TEXT = "text"
    MARKDOWN = "markdown"


def get_note_editor_mode() -> str:
    """Return the configured note editor mode."""
    env = os.environ.get("REF_NOTE_EDITOR", "").strip().lower()
    if env in {NoteEditorMode.TEXT, NoteEditorMode.MARKDOWN}:
        return env
    try:
        cfg = load_config()
        value = cfg.note_editor
        if value in {NoteEditorMode.TEXT, NoteEditorMode.MARKDOWN}:
            return value
    except Exception:
        pass
    return NoteEditorMode.TEXT


def edit_text_in_editor(prefix: str, header: str, template: str) -> Optional[str]:
    """Write text to a temp file, open $EDITOR, and return the edited text."""
    fd, tmp_path_str = tempfile.mkstemp(prefix=prefix, suffix=".md")
    tmp_path = Path(tmp_path_str)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(header)
            handle.write(template)
        editor = os.environ.get("VISUAL") or os.environ.get("EDITOR") or "vi"
        cmd = shlex.split(editor) + [str(tmp_path)]
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as exc:
            typer.echo(f"Editor exited with non-zero status: {exc}", err=True)
            raise typer.Exit(code=1) from exc
        return tmp_path.read_text(encoding="utf-8")
    finally:
        try:
            if tmp_path.exists():
                tmp_path.unlink()
        except Exception:
            pass


def edit_via_editor(
    prefix: str,
    header: str,
    load: Callable[[], str],
    save: Callable[[str], None],
) -> None:
    """Generic edit flow: load, edit in $EDITOR, and persist changes."""
    current = load() or ""
    edited = edit_text_in_editor(prefix=prefix, header=header, template=current)
    if edited is None:
        return
    if edited.rstrip("\n") == current.rstrip("\n"):
        typer.echo("No changes; nothing to update")
        return
    save(edited.rstrip("\n"))
    typer.echo("Updated")
