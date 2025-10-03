from __future__ import annotations

import shlex
import subprocess
import sys
from typing import List

__all__ = [
    "platform_open_command_str",
    "platform_clip_command_str",
    "build_open_command_args",
    "open_path",
]


_IS_LINUX = sys.platform.startswith("linux")
_IS_MAC = sys.platform.startswith("darwin")
_IS_WINDOWS = sys.platform.startswith("win")


def platform_open_command_str() -> str:
    if _IS_LINUX:
        return "xdg-open"
    if _IS_MAC:
        return "open"
    if _IS_WINDOWS:
        return "powershell -NoProfile -Command Start-Process"
    return "open"


def platform_clip_command_str() -> str:
    if _IS_LINUX:
        return "xclip -selection clipboard"
    if _IS_MAC:
        return "pbcopy"
    if _IS_WINDOWS:
        return "clip"
    return "pbcopy"


def build_open_command_args(target: str) -> List[str]:
    if _IS_WINDOWS:
        return [
            "powershell",
            "-NoProfile",
            "-Command",
            "Start-Process",
            target,
        ]
    command_str = platform_open_command_str()
    if " " in command_str:
        base = shlex.split(command_str)
    else:
        base = [command_str]
    return base + [target]


def open_path(target: str) -> bool:
    try:
        subprocess.run(build_open_command_args(target), check=False)
        return True
    except (FileNotFoundError, OSError):
        return False
