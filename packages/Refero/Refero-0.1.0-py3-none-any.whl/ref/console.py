from __future__ import annotations

from typing import Any

from rich.console import Console
from rich.text import Text


# Shared Rich consoles for stdout and stderr
console = Console()
console_err = Console(stderr=True)


def echo(message: Any = "", *, err: bool = False) -> None:
    """Rich-backed drop-in for simple echoing.

    - Prints to stderr if err=True.
    - Treats strings as literal text (markup disabled) but preserves ANSI colors.
    - Passes through Rich renderables unchanged.
    """
    target = console_err if err else console
    # If this is already a Rich renderable, just print it directly
    if isinstance(message, (Text,)):
        target.print(message)
        return
    # Default: print literal text without interpreting Rich markup; ANSI preserved
    target.print(message, markup=False)


