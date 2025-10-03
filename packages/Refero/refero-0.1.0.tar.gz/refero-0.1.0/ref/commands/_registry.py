"""Shared command registration helpers for the CLI."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Iterator, Optional, Tuple

import typer

CommandCallback = Callable[..., None]


@dataclass(frozen=True)
class CommandBinding:
    """Describe how a Typer command should be registered."""

    callback: CommandCallback
    name: Optional[str] = None
    aliases: Tuple[str, ...] = ()

    def primary_name(self) -> Optional[str]:
        return self.name

    def iter_aliases(self) -> Iterator[str]:
        yield from self.aliases


def register_bindings(app: typer.Typer, bindings: Iterable[CommandBinding]) -> None:
    """Register one or more command bindings with the Typer app."""

    for binding in bindings:
        primary = binding.primary_name()
        decorator = app.command(name=primary) if primary else app.command()
        decorator(binding.callback)
        for alias in binding.iter_aliases():
            app.command(name=alias)(binding.callback)

