from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Mapping, Optional, Sequence

from ..utils.system import platform_clip_command_str, platform_open_command_str

__all__ = [
    "PickerBindingSpec",
    "PickerBinding",
    "DEFAULT_PICKER_BINDINGS",
    "binding_specs_by_raw",
    "parse_binding_list",
]


@dataclass(frozen=True)
class PickerBindingSpec:
    """Declarative metadata for a picker binding."""

    key: str
    action: str
    description: str
    show_in_help: bool = True

    def raw(self) -> str:
        return f"{self.key}:{self.action}"


@dataclass(frozen=True)
class PickerBinding:
    """Concrete binding entry derived from configuration."""

    key: str
    action: str
    raw: str
    description: Optional[str] = None

    def help_line(self) -> Optional[str]:
        if not self.description:
            return None
        return f"{_format_key(self.key)}: {self.description}"


def _format_key(value: str) -> str:
    parts = [part for part in (value or "").split("-") if part]
    return "-".join(part.capitalize() for part in parts)


def _normalize_action(value: str) -> str:
    return value.strip()


def _humanize_action(action: str) -> Optional[str]:
    text = action.lower()
    if not text:
        return None
    lookups = (
        ("jump", "Jump to key"),
        ("zotero://select", "Open in Zotero"),
        (" ref open ", "Open attachment"),
        (" ref picker-edit ", "Edit metadata"),
        (" ref label ", "Edit tags+collections"),
        (" ref relate ", "Relate items"),
        (" ref note ", "Edit note"),
        ("export", ".bib export"),
        ("delete", "Delete"),
        ("pbcopy", "Copy key"),
        ("xclip", "Copy key"),
        (" clip", "Copy key"),
    )
    for needle, label in lookups:
        if needle in f" {text} ":
            return label
    return None


def _parse_binding(raw: str) -> Optional[PickerBinding]:
    if not raw:
        return None
    key, _, rest = raw.partition(":")
    if not key:
        return None
    action = _normalize_action(rest)
    return PickerBinding(key=key.strip(), action=action, raw=raw)

_OPEN_CMD = platform_open_command_str()
_CLIP_CMD = platform_clip_command_str()

DEFAULT_PICKER_BINDINGS: Sequence[PickerBindingSpec] = (
    PickerBindingSpec("ctrl-s", "jump", "Jump to key"),
    PickerBindingSpec(
        "ctrl-r",
        f"execute({_OPEN_CMD} zotero://select/library/items/{{5}})",
        "Open in Zotero",
    ),
    PickerBindingSpec("ctrl-o", "execute(ref open {5})", "Open attachment"),
    PickerBindingSpec("ctrl-e", "execute(ref picker-edit {5})", "Edit metadata"),
    PickerBindingSpec("ctrl-t", "execute(ref label {+5} --pick)", "Edit tags+collections"),
    PickerBindingSpec("ctrl-l", "execute(ref relate {5} --pick)", "Relate items"),
    PickerBindingSpec("ctrl-k", "execute(ref note {5})", "Edit note"),
    PickerBindingSpec(
        "ctrl-a",
        "execute(ref export {5} --format bibtex --out {6}.bib)",
        ".bib export",
    ),
    PickerBindingSpec("ctrl-d", "execute(ref delete {+5})+abort", "Delete"),
    PickerBindingSpec(
        "alt-y",
        f"execute-silent(echo -n {{5}} | {_CLIP_CMD})+abort",
        "Copy key",
    ),
)


def binding_specs_by_raw(specs: Sequence[PickerBindingSpec]) -> Mapping[str, PickerBindingSpec]:
    return {spec.raw(): spec for spec in specs}


def parse_binding_list(
    values: Iterable[str],
    *,
    specs: Mapping[str, PickerBindingSpec] | None = None,
) -> List[PickerBinding]:
    specs = specs or {}
    bindings: List[PickerBinding] = []
    for raw in values:
        parsed = _parse_binding(str(raw))
        if not parsed:
            continue
        spec = specs.get(parsed.raw)
        description = spec.description if spec else _humanize_action(parsed.action)
        bindings.append(
            PickerBinding(
                key=parsed.key,
                action=parsed.action,
                raw=parsed.raw,
                description=description,
            )
        )
    return bindings
