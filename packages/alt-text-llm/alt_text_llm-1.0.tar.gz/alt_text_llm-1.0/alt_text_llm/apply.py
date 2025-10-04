"""Apply labeled alt text to markdown files."""

import json
import re
from collections import defaultdict
from pathlib import Path

from rich.console import Console
from rich.text import Text

from alt_text_llm import utils


def _escape_markdown_alt_text(alt_text: str) -> str:
    """
    Escape special characters in alt text for markdown.

    Args:
        alt_text: The alt text to escape

    Returns:
        Escaped alt text safe for markdown
    """
    # Escape backslashes first to avoid double-escaping
    alt_text = alt_text.replace("\\", "\\\\")
    # Escape dollar signs to prevent LaTeX interpretation
    alt_text = alt_text.replace("$", "\\$")
    return alt_text


def _escape_html_alt_text(alt_text: str) -> str:
    """
    Escape special characters in alt text for HTML.

    Args:
        alt_text: The alt text to escape

    Returns:
        Escaped alt text safe for HTML attributes
    """
    # Escape HTML special characters
    alt_text = alt_text.replace("&", "&amp;")
    alt_text = alt_text.replace("<", "&lt;")
    alt_text = alt_text.replace(">", "&gt;")
    alt_text = alt_text.replace('"', "&quot;")
    return alt_text


def _apply_markdown_image_alt(
    line: str, asset_path: str, new_alt: str
) -> tuple[str, str | None]:
    """
    Apply alt text to a markdown image syntax.

    Args:
        line: The line containing the image
        asset_path: The asset path to match
        new_alt: The new alt text to apply

    Returns:
        Tuple of (modified line, old alt text or None)
    """
    # Match markdown image syntax: ![alt](path)
    # Need to escape special regex chars in asset_path
    escaped_path = re.escape(asset_path)
    pattern = rf"!\[([^\]]*)\]\({escaped_path}\s*\)"

    match = re.search(pattern, line)
    if not match:
        return line, None

    old_alt = match.group(1) if match.group(1) else None
    # Escape special characters in alt text
    escaped_alt = _escape_markdown_alt_text(new_alt)
    # Replace the alt text - use lambda to avoid backslash interpretation in replacement
    new_line = re.sub(
        pattern, lambda m: f"![{escaped_alt}]({asset_path})", line, count=1
    )
    return new_line, old_alt


def _apply_html_image_alt(
    line: str, asset_path: str, new_alt: str
) -> tuple[str, str | None]:
    """
    Apply alt text to an HTML img tag.

    Args:
        line: The line containing the img tag
        asset_path: The asset path to match
        new_alt: The new alt text to apply

    Returns:
        Tuple of (modified line, old alt text or None)
    """
    # Escape special regex chars in asset_path
    escaped_path = re.escape(asset_path)

    # Match img tag with this src (handles both > and /> endings)
    # Capture group 1: attributes, Group 2: whitespace before closing, Group 3: closing slash
    img_pattern = rf'<img\s+([^>]*src="{escaped_path}"[^/>]*?)(\s*)(/?)>'

    match = re.search(img_pattern, line, re.IGNORECASE | re.DOTALL)
    if not match:
        return line, None

    img_attrs = match.group(1).rstrip()  # Remove trailing whitespace
    old_alt: str | None = None
    whitespace_before_close = match.group(2)  # Whitespace before closing
    closing_slash = match.group(3)  # Either "/" or ""

    # Check if alt attribute exists
    alt_pattern = r'alt="([^"]*)"'
    alt_match = re.search(alt_pattern, img_attrs, re.IGNORECASE)

    # Escape special characters in alt text for HTML
    escaped_alt = _escape_html_alt_text(new_alt)

    if alt_match:
        old_alt = alt_match.group(1)
        # Replace existing alt - use lambda to avoid backslash interpretation
        new_attrs = re.sub(
            alt_pattern,
            lambda m: f'alt="{escaped_alt}"',
            img_attrs,
            count=1,
            flags=re.IGNORECASE,
        )
    else:
        # Add alt attribute (insert before src or at the end)
        # Use lambda to avoid backslash interpretation in replacement
        new_attrs = re.sub(
            rf'(src="{escaped_path}")',
            lambda m: f'alt="{escaped_alt}" {m.group(1)}',
            img_attrs,
            count=1,
            flags=re.IGNORECASE,
        )

    # Reconstruct the img tag with proper closing, preserving original whitespace
    old_tag = f"<img {img_attrs}{whitespace_before_close}{closing_slash}>"
    new_tag = f"<img {new_attrs}{whitespace_before_close}{closing_slash}>"
    new_line = line.replace(old_tag, new_tag)
    return new_line, old_alt


def _apply_wikilink_image_alt(
    line: str, asset_path: str, new_alt: str
) -> tuple[str, str | None]:
    """
    Apply alt text to a wikilink-style image syntax (e.g. Obsidian).

    Args:
        line: The line containing the image
        asset_path: The asset path to match
        new_alt: The new alt text to apply

    Returns:
        (modified line, old alt text or None)
    """
    # Match wikilink image syntax: ![[path]] or ![[path|alt]]
    # Need to escape special regex chars in asset_path
    escaped_path = re.escape(asset_path)
    pattern = rf"!\[\[{escaped_path}(?:\|([^\]]*))?\]\]"

    match = re.search(pattern, line)
    if not match:
        return line, None

    old_alt = match.group(1) if match.group(1) else None
    # Escape special characters in alt text (wikilinks are still markdown)
    escaped_alt = _escape_markdown_alt_text(new_alt)
    # Replace with new alt text - use lambda to avoid backslash interpretation
    new_line = re.sub(
        pattern, lambda m: f"![[{asset_path}|{escaped_alt}]]", line, count=1
    )
    return new_line, old_alt


def _display_unused_entries(
    unused_entries: set[tuple[str, str]], console: Console
) -> None:
    if not unused_entries:
        return

    console.print(
        f"[yellow]Note: {len(unused_entries)} {'entry' if len(unused_entries) == 1 else 'entries'} without 'final_alt' will be skipped:[/yellow]"
    )
    for markdown_file, asset_basename in sorted(unused_entries):
        console.print(f"[dim]  {markdown_file}: {asset_basename}[/dim]")


def _read_file_lines(md_path: Path) -> tuple[str, list[str]]:
    """
    Read a file and split it into lines.

    Args:
        md_path: Path to the markdown file

    Returns:
        Tuple of (original text, list of lines)
    """
    source_text = md_path.read_text(encoding="utf-8")
    lines = source_text.splitlines()
    return source_text, lines


def _try_all_image_formats(
    line: str, asset_path: str, new_alt: str
) -> tuple[str, str | None]:
    """
    Try applying alt text to all supported image formats.

    Args:
        line: The line to modify
        asset_path: The asset path to match
        new_alt: The new alt text to apply

    Returns:
        Tuple of (modified line, old alt text or None)
    """
    # Normalize alt text by replacing line breaks with ellipses
    # Use + to collapse multiple consecutive line breaks into one ellipsis
    normalized_alt = re.sub(r"(\r\n|\r|\n)+", " ... ", new_alt)

    # Try markdown image first
    modified_line, old_alt = _apply_markdown_image_alt(
        line, asset_path, normalized_alt
    )

    # If no change, try wikilink image
    if modified_line == line:
        modified_line, old_alt = _apply_wikilink_image_alt(
            line, asset_path, normalized_alt
        )

    # If no change, try HTML image
    if modified_line == line:
        modified_line, old_alt = _apply_html_image_alt(
            line, asset_path, normalized_alt
        )

    return modified_line, old_alt


def _write_modified_lines(
    md_path: Path, lines: list[str], original_text: str, dry_run: bool
) -> None:
    """
    Write modified lines back to file.

    Args:
        md_path: Path to the markdown file
        lines: Modified lines to write
        original_text: Original file text (to preserve trailing newline)
        dry_run: If True, don't actually write to file
    """
    if dry_run:
        return

    new_content = "\n".join(lines)
    # Preserve trailing newline if original had one
    if original_text.endswith("\n"):
        new_content += "\n"
    md_path.write_text(new_content, encoding="utf-8")


def _apply_caption_to_file(
    md_path: Path,
    caption_item: utils.AltGenerationResult,
    console: Console,
    dry_run: bool = False,
) -> tuple[str | None, str] | None:
    """
    Apply a caption to all instances of an asset in a markdown file.

    Args:
        md_path: Path to the markdown file
        caption_item: The AltGenerationResult with final_alt to apply
        console: Rich console for output
        dry_run: If True, don't actually modify files

    Returns:
        Tuple of (old_alt, new_alt) if successful, None otherwise
    """
    assert caption_item.final_alt is not None, "final_alt must be set"

    source_text, lines = _read_file_lines(md_path)

    modified_count = 0
    last_old_alt: str | None = None

    # Search all lines for the asset and replace
    for line_idx, original_line in enumerate(lines):
        modified_line, old_alt = _try_all_image_formats(
            original_line, caption_item.asset_path, caption_item.final_alt
        )

        if modified_line != original_line:
            lines[line_idx] = modified_line
            modified_count += 1
            last_old_alt = old_alt

    if modified_count == 0:
        console.print(
            f"[orange]Warning: Could not find asset '{caption_item.asset_path}' in {md_path}[/orange]"
        )
        return None

    _write_modified_lines(md_path, lines, source_text, dry_run)
    return (last_old_alt, caption_item.final_alt)


def _load_and_parse_captions(
    captions_path: Path,
) -> tuple[list[utils.AltGenerationResult], set[tuple[str, str]]]:
    """
    Load captions from JSON and parse into AltGenerationResult objects.

    Args:
        captions_path: Path to the captions JSON file

    Returns:
        Tuple of (captions to apply, unused entries)
    """
    with open(captions_path, encoding="utf-8") as f:
        captions_data = json.load(f)

    captions_to_apply: list[utils.AltGenerationResult] = []
    unused_entries: set[tuple[str, str]] = set()

    for item in captions_data:
        if item.get("final_alt") and item.get("final_alt").strip():
            captions_to_apply.append(
                utils.AltGenerationResult(
                    markdown_file=item["markdown_file"],
                    asset_path=item["asset_path"],
                    suggested_alt=item["suggested_alt"],
                    model=item["model"],
                    context_snippet=item["context_snippet"],
                    line_number=int(item["line_number"]),
                    final_alt=item["final_alt"],
                )
            )
        else:
            unused_entries.add(
                (
                    item["markdown_file"],
                    Path(item["asset_path"]).name,
                )
            )

    return captions_to_apply, unused_entries


def _group_captions_by_file(
    captions: list[utils.AltGenerationResult],
) -> dict[str, list[utils.AltGenerationResult]]:
    """
    Group captions by their markdown file.

    Args:
        captions: List of captions to group

    Returns:
        Dictionary mapping file paths to lists of captions
    """
    by_file: dict[str, list[utils.AltGenerationResult]] = defaultdict(list)
    for item in captions:
        by_file[item.markdown_file].append(item)
    return by_file


def _display_caption_result(
    result: tuple[str | None, str],
    item: utils.AltGenerationResult,
    console: Console,
    dry_run: bool,
) -> None:
    """
    Display the result of applying a caption.

    Args:
        result: Tuple of (old_alt, new_alt)
        item: The caption item that was applied
        console: Rich console for output
        dry_run: Whether this is a dry run
    """
    old_alt, new_alt = result
    status = "Would apply" if dry_run else "Applied"
    old_text = f'"{old_alt}"' if old_alt else "(no alt)"

    # Build message with Text to avoid markup parsing issues
    message = Text("  ")
    message.append(f"{status}:", style="green")
    message.append(f' {old_text} → "{new_alt}"')
    console.print(message)


def _process_file_captions(
    md_path: Path,
    items: list[utils.AltGenerationResult],
    console: Console,
    dry_run: bool,
) -> int:
    """
    Process all captions for a single file.

    Args:
        md_path: Path to the markdown file
        items: List of captions to apply to this file
        console: Rich console for output
        dry_run: If True, don't actually modify files

    Returns:
        Number of successfully applied captions
    """
    if not md_path.exists():
        console.print(f"[yellow]Warning: File not found: {md_path}[/yellow]")
        return 0

    console.print(f"\n[dim]Processing {md_path} ({len(items)} captions)[/dim]")

    applied_count = 0
    for item in items:
        result = _apply_caption_to_file(
            md_path=md_path,
            caption_item=item,
            console=console,
            dry_run=dry_run,
        )

        if result:
            applied_count += 1
            _display_caption_result(result, item, console, dry_run)

    return applied_count


def apply_captions(
    captions_path: Path,
    console: Console,
    dry_run: bool = False,
) -> int:
    """
    Apply captions from a JSON file to markdown files.

    Args:
        captions_path: Path to the captions JSON file
        console: Rich console for output
        dry_run: If True, show what would be done without modifying files

    Returns:
        Number of successfully applied captions
    """
    captions_to_apply, unused_entries = _load_and_parse_captions(captions_path)

    _display_unused_entries(unused_entries, console)

    if not captions_to_apply:
        console.print(
            f"[yellow]No captions with 'final_alt' found in {captions_path}[/yellow]"
        )
        return 0

    console.print(
        f"[blue]Found {len(captions_to_apply)} captions to apply{' (dry run)' if dry_run else ''}[/blue]"
    )

    by_file = _group_captions_by_file(captions_to_apply)

    applied_count = 0
    for md_file, items in by_file.items():
        md_path = Path(md_file)
        applied_count += _process_file_captions(
            md_path, items, console, dry_run
        )

    return applied_count


def apply_from_captions_file(
    captions_file: Path, dry_run: bool = False
) -> None:
    """
    Load captions from file and apply them to markdown files.

    Args:
        captions_file: Path to the captions JSON file
        dry_run: If True, show what would be done without modifying files
    """
    console = Console()

    if not captions_file.exists():
        console.print(
            f"[red]Error: Captions file not found: {captions_file}[/red]"
        )
        return

    applied_count = apply_captions(captions_file, console, dry_run=dry_run)

    # Summary
    if dry_run:
        console.print(
            f"\n[blue]Dry run complete: {applied_count} captions would be applied[/blue]"
        )
    else:
        console.print(
            f"\n[green]Successfully applied {applied_count} captions[/green]"
        )
