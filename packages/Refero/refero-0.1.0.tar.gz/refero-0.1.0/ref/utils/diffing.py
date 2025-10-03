from __future__ import annotations

import json
from typing import Any, Dict, Set, Tuple

import typer
from rich.table import Table
from rich.text import Text

from .. import diff_utils
from ..config import load as load_config
from ..console import console as rich_console

from .display import style_option_key

__all__ = [
    "changed_keys",
    "print_item_data_diff_table",
    "print_item_data_diff_inline",
    "print_item_data_diff_fastdmp",
    "print_item_data_diff_selected",
    "format_inline_three_way_diff",
    "format_fast_dmp_inline",
    "three_way_merge_item_data",
    "prompt_concurrent_action",
]


def changed_keys(a: Dict[str, Any], b: Dict[str, Any]) -> Set[str]:
    return diff_utils.changed_keys(a, b)


def print_item_data_diff_table(base: Dict[str, Any], local: Dict[str, Any], remote: Dict[str, Any]) -> None:
    local_changed = changed_keys(base, local)
    remote_changed = changed_keys(base, remote)
    union = sorted(local_changed | remote_changed)
    typer.echo("Detected concurrent changes (version changed remotely).")
    typer.echo(f"- Your changes: {', '.join(sorted(local_changed)) or '(none)'}")
    typer.echo(f"- Remote changes: {', '.join(sorted(remote_changed)) or '(none)'}")
    if not union:
        typer.echo("No differences.")
        return

    def _format_three_way_for_table(base_text: Any, local_text: Any, remote_text: Any, *, max_segment: int = 200) -> Tuple[str, str, str]:
        segments = diff_utils.compute_three_way_diff_segments(base_text, local_text, remote_text, max_segment=max_segment)
        parts_base: list[str] = []
        parts_remote: list[str] = []
        parts_local: list[str] = []
        for seg in segments:
            if seg["type"] == "ctx":
                parts_base.append(seg["base"])
                parts_remote.append(seg["remote"])
                parts_local.append(seg["local"])
            else:
                parts_base.append(typer.style(seg["base"], fg=typer.colors.WHITE, dim=True))
                parts_remote.append(typer.style(seg["remote"], fg=typer.colors.BLUE))
                parts_local.append(typer.style(seg["local"], fg=typer.colors.GREEN))
        return ("".join(parts_base), "".join(parts_remote), "".join(parts_local))

    for key in union:
        b_str, r_str, l_str = _format_three_way_for_table(base.get(key), local.get(key), remote.get(key))
        table = Table(title=str(key))
        table.add_column("base", justify="left", style="black")
        table.add_column("remote", justify="left", style="black", header_style="blue")
        table.add_column("yours", justify="left", style="black", header_style="green")
        table.add_row(Text.from_ansi(b_str), Text.from_ansi(r_str), Text.from_ansi(l_str))
        rich_console.print(table)


def format_inline_three_way_diff(base_text: Any, local_text: Any, remote_text: Any, context: int = 100, max_segment: int = 200) -> str:
    return diff_utils.format_inline_three_way_diff(base_text, local_text, remote_text, context=context, max_segment=max_segment)


def print_item_data_diff_inline(base: Dict[str, Any], local: Dict[str, Any], remote: Dict[str, Any]) -> None:
    local_changed = changed_keys(base, local)
    remote_changed = changed_keys(base, remote)
    union = sorted(local_changed | remote_changed)
    if not union:
        typer.echo("No differences.")
        return

    typer.echo(
        "Key-wise inline diff ("
        + typer.style("base", fg=typer.colors.WHITE, dim=True)
        + " → "
        + typer.style("remote", fg=typer.colors.BLUE)
        + " → "
        + typer.style("yours", fg=typer.colors.GREEN)
        + ")"
    )
    for key in union:
        base_value = base.get(key)
        local_value = local.get(key)
        remote_value = remote.get(key)
        line = format_inline_three_way_diff(base_value, local_value, remote_value)
        typer.echo("  " + typer.style(key, bold=True) + ":")
        typer.echo("    " + line)


def format_fast_dmp_inline(old_text: Any, new_text: Any, *, insert_color: typer.colors.Color | None = None) -> str:
    return diff_utils.format_fast_dmp_inline(old_text, new_text, insert_color=insert_color)


def print_item_data_diff_fastdmp(base: Dict[str, Any], local: Dict[str, Any], remote: Dict[str, Any]) -> None:
    local_changed = changed_keys(base, local)
    remote_changed = changed_keys(base, remote)
    union = sorted(local_changed | remote_changed)
    if not union:
        typer.echo("No differences.")
        return

    typer.echo("Key-wise fast-diff-match-patch inline diff (base→remote, base→yours):")
    for key in union:
        base_value = base.get(key)
        local_value = local.get(key)
        remote_value = remote.get(key)
        typer.echo("  " + typer.style(key, bold=True) + ":")
        typer.echo("    base → remote:")
        typer.echo("      " + format_fast_dmp_inline(base_value, remote_value, insert_color=typer.colors.BLUE))
        typer.echo("    base → yours:")
        typer.echo("      " + format_fast_dmp_inline(base_value, local_value, insert_color=typer.colors.GREEN))


def print_item_data_diff_selected(base: Dict[str, Any], local: Dict[str, Any], remote: Dict[str, Any]) -> None:
    cfg = load_config()
    style = cfg.diff_style
    if style == "table":
        print_item_data_diff_table(base, local, remote)
    elif style == "inline":
        print_item_data_diff_inline(base, local, remote)
    elif style == "pairwise":
        print_item_data_diff_fastdmp(base, local, remote)
    else:
        print_item_data_diff_inline(base, local, remote)


def three_way_merge_item_data(base: Dict[str, Any], local: Dict[str, Any], remote: Dict[str, Any]) -> Dict[str, Any]:
    result = json.loads(json.dumps(remote))
    for key in changed_keys(base, local):
        result[key] = local.get(key)
    return result


def prompt_concurrent_action(allow_merge: bool = False, allow_remote: bool = True, default: str = "y") -> str:
    parts: list[str] = []
    default_letter = (default or "y").strip().lower()[:1]
    y_color = typer.colors.GREEN
    m_color = typer.colors.YELLOW
    r_color = typer.colors.BLUE
    a_color = typer.colors.RED

    choice_yours = "[" + style_option_key("y", y_color) + "]ours"
    parts.append(choice_yours)
    if allow_remote:
        choice_remote = "[" + style_option_key("r", r_color) + "]emote"
        parts.append(choice_remote)
    if allow_merge:
        choice_merge = "[" + style_option_key("m", m_color) + "]erge"
        parts.append(choice_merge)
    choice_abort = "[" + style_option_key("a", a_color) + "]bort"
    parts.append(choice_abort)
    styled_default = "[" + style_option_key(default_letter, typer.colors.GREEN) + "]"
    prompt = "Choose action: " + ", ".join(parts) + ". " + styled_default
    choice_input = typer.prompt(prompt, default=default, show_default=False)
    choice = (choice_input or default).strip().lower()
    if choice.startswith("a"):
        return "abort"
    if allow_remote and choice.startswith("r"):
        return "remote"
    if allow_merge and choice.startswith("m"):
        return "merge"
    if choice.startswith("y"):
        return "yours"
    return "invalid"
