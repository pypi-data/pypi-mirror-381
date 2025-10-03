"""Editing command package orchestrating core, label, and relation flows."""

from __future__ import annotations

from .core import CORE_COMMANDS, abstract, edit, extra, note, picker_edit
from .labels import LABEL_COMMANDS, collection_cmd, label, tag
from .relations import RELATION_COMMANDS, relate

COMMANDS = CORE_COMMANDS + LABEL_COMMANDS + RELATION_COMMANDS

__all__ = [
    "edit",
    "picker_edit",
    "abstract",
    "extra",
    "note",
    "label",
    "collection_cmd",
    "tag",
    "relate",
    "COMMANDS",
]

