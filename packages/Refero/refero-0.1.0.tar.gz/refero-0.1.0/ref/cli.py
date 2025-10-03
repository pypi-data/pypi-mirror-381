from __future__ import annotations

"""CLI entrypoint wiring the Typer commands for ``ref``."""

import os
from typing import Optional

import typer
from typer.core import TyperGroup

from .commands import editing, listing, management
from .commands import preview_client as preview_client_module
from .commands._registry import register_bindings
from .utils.editor import NoteEditorMode
from .utils.query import coalesce_query


class DefaultToListGroup(TyperGroup):
    """Typer command group that defaults to the ``list`` command."""

    def get_command(self, ctx, cmd_name):  # type: ignore[override]
        return super().get_command(ctx, cmd_name)

    def resolve_command(self, ctx, args):  # type: ignore[override]
        if args and args[0] in self.commands:
            return super().resolve_command(ctx, args)

        args = list(args or [])
        if any(arg in ("-h", "--help") for arg in args):
            return super().resolve_command(ctx, args)

        new_args = ["list"]
        passthrough_options = {
            "--query",
            "-q",
            "--limit",
            "-l",
            "--collection",
            "-c",
            "--tag",
            "-g",
            "--author",
            "-a",
            "--title",
            "-t",
            "--year",
            "-y",
            "--doi",
            "-d",
        }

        index = 0
        bare_tokens: list[str] = []
        while index < len(args):
            token = args[index]
            if token in self.commands:
                break
            if token in passthrough_options:
                new_args.append(token)
                if index + 1 < len(args) and not args[index + 1].startswith("-"):
                    new_args.append(args[index + 1])
                    index += 2
                    continue
                index += 1
                continue
            if token.startswith("-"):
                new_args.append(token)
                if index + 1 < len(args) and not args[index + 1].startswith("-"):
                    new_args.append(args[index + 1])
                    index += 2
                    continue
                index += 1
                continue
            bare_tokens.append(token)
            index += 1

        joined_query = coalesce_query(None, bare_tokens)
        if joined_query is not None:
            new_args += ["-q", joined_query]

        return super().resolve_command(ctx, new_args)


app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    cls=DefaultToListGroup,
    context_settings={
        "allow_extra_args": True,
        "ignore_unknown_options": True,
        "help_option_names": ["-h", "--help"],
    },
)


@app.callback()
def _global_options(
    note_editor: Optional[str] = typer.Option(
        None,
        "--note-editor",
        help="Editor mode for notes: text | markdown",
        case_sensitive=False,
    ),
):
    """Configure global CLI options.

    Args:
        note_editor: Override the preferred editor mode for notes.
    """

    if note_editor:
        value = str(note_editor).strip().lower()
        if value not in {NoteEditorMode.TEXT, NoteEditorMode.MARKDOWN}:
            raise typer.BadParameter("--note-editor must be one of: text, markdown")
        os.environ["REF_NOTE_EDITOR"] = value


for module in (listing, editing, management, preview_client_module):
    register_bindings(app, getattr(module, "COMMANDS", ()))


__all__ = ["app"]
