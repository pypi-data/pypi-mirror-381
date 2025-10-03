import re
import textwrap
from pathlib import Path
from typing import Any, Generator, Optional

import click  # type: ignore
import yaml  # type: ignore
from rich.console import Console  # type: ignore

console: Console = Console()

CHAR_LIMIT_DEFAULT: int = 88
CONTENT_INDENT: int = 2


class LiteralStr(str):
    """Marker class to force PyYAML to emit block scalar style (|-)."""

    pass


def literal_str_representer(dumper: yaml.Dumper, data: LiteralStr) -> yaml.ScalarNode:
    """PyYAML representer for LiteralStr to use block scalar."""
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(LiteralStr, literal_str_representer)

MD_TABLE_RE: re.Pattern = re.compile(r"^\s*\|.*\|.*$")
MD_TABLE_HEADER_RE: re.Pattern = re.compile(r"^\s*\|.*[-:]+.*\|.*$")


def contains_markdown_table(value: Any) -> bool:
    """Check if the string contains Markdown table syntax.

    Args:
        value (Any): The string to check.

    Returns:
        bool: True if a Markdown table is detected, False otherwise.

    Examples:
        >>> contains_markdown_table('| Col1 | Col2 |\\n| --- | --- |\\n| A | B |')
        True
        >>> contains_markdown_table('Just a normal text')
        False
    """
    if not isinstance(value, str):
        return False
    for line in value.splitlines():
        if MD_TABLE_RE.match(line) and MD_TABLE_HEADER_RE.match(line):
            return True
    return False


def wrap_block(text: str, char_limit: int) -> str:
    """Wrap text at char_limit preserving paragraph breaks.

    Args:
        text (str): Text to wrap.
        char_limit (int): Maximum characters per line.

    Returns:
        str: Wrapped text with preserved paragraphs.

    Examples:
        >>> wrap_block('This is a long paragraph that should be wrapped.', 10)
        'This is a\\nlong\\nparagraph\\nthat\\nshould be\\nwrapped.'
    """
    lines = []
    for para in text.splitlines():
        if not para.strip():
            lines.append("")
        else:
            wrapped = textwrap.fill(
                para, width=char_limit, break_long_words=False, break_on_hyphens=False
            )
            lines.append(wrapped)
    return "\n".join(lines)


def wrap_value(key: Optional[str], value: Any, char_limit: int) -> Any:
    """Wrap string values according to key-specific rules.

    Args:
        key (Optional[str]): YAML key name.
        value (Any): The value to wrap.
        char_limit (int): Maximum characters per line.

    Returns:
        Any: Wrapped string or original value.

    Rules:
        - content → always block unless contains Markdown table
        - caption/title → flatten & wrap if effective length exceeds char_limit
        - other long single-line strings → wrap

    Examples:
        >>> wrap_value('content', 'Some content', 20)
        'Some content'
        >>> wrap_value('caption', 'This is a very long caption that should be wrapped', 20)
        'This is a very long\\ncaption that should\\nbe wrapped'
    """
    if not isinstance(value, str):
        return value

    has_md_table = contains_markdown_table(value)

    # content → always block unless Markdown table
    if key == "content" and not has_md_table:
        return LiteralStr(wrap_block(value.rstrip(), char_limit))

    # caption or title → flatten & wrap if effective length exceeds char_limit
    if key in ("caption", "title"):
        flat_value = " ".join(value.splitlines()).strip()
        if len(flat_value) > char_limit:
            return LiteralStr(wrap_block(flat_value, char_limit))

    # other single-line long strings → wrap
    if len(value) > char_limit and "\n" not in value:
        return LiteralStr(wrap_block(value, char_limit))

    return value


def process_node(
    node: Any, parent_key: Optional[str] = None, char_limit: int = CHAR_LIMIT_DEFAULT
) -> Any:
    """Recursively process a YAML node applying wrap rules.

    Args:
        node: dict, list, or scalar.
        parent_key: Key of parent dict for context.
        char_limit: Maximum characters per line.

    Returns:
        Any: Processed YAML node.

    Examples:
        >>> process_node({'caption': 'A very long caption that should wrap'}, char_limit=20)
        {'caption': 'A very long caption\\nthat should wrap'}
        >>> process_node(['Short', 'This is a long string'], char_limit=10)
        ['Short', 'This is a\\nlong\\nstring']
        >>> process_node('Simple', parent_key='title', char_limit=5)
        'Simple'
    """
    if isinstance(node, dict):
        return {
            k: process_node(wrap_value(k, v, char_limit), k, char_limit)
            for k, v in node.items()
        }
    elif isinstance(node, list):
        return [
            process_node(i, parent_key=parent_key, char_limit=char_limit) for i in node
        ]
    else:
        return wrap_value(parent_key, node, char_limit)


def format_yaml_file(
    file_path: Path,
    inplace: bool = True,
    output_file: Optional[Path] = None,
    char_limit: int = CHAR_LIMIT_DEFAULT,
) -> None:
    """Format a YAML file with wrapping rules.

    Args:
        file_path (Path): Path to input YAML file.
        inplace (bool): Whether to overwrite the file.
        output_file (Optional[Path]): Optional output file path.
        char_limit (int): Maximum characters per line.

    Examples:
        >>> import tempfile, os
        >>> tmp = tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8', suffix='.yml')
        >>> tmp.write('- caption: "This is a very long caption that should be wrapped"\\n')
        64
        >>> tmp.close()
        >>> format_yaml_file(Path(tmp.name), inplace=False, char_limit=20)  # doctest: +ELLIPSIS
        - caption: |-
            This is a very long
            caption that should
            be wrapped
        <BLANKLINE>
        >>> os.unlink(tmp.name)
    """
    try:
        data: Any = yaml.safe_load(file_path.read_text(encoding="utf-8"))
    except Exception as e:
        console.print(f"[red]Failed to read {file_path}: {e}[/red]")
        return

    processed: Any = process_node(data, None, char_limit)
    target_file: Optional[Path] = output_file or (file_path if inplace else None)

    yaml_text: str = yaml.dump(
        processed,
        sort_keys=False,
        allow_unicode=True,
        width=char_limit,
        indent=CONTENT_INDENT,
        default_flow_style=False,
    )

    if target_file is None:
        console.print(yaml_text)
    else:
        try:
            target_file.write_text(yaml_text, encoding="utf-8")
            console.print(f"[green]Formatted:[/green] {target_file}")
        except Exception as e:
            console.print(f"[red]Failed to write {target_file}: {e}[/red]")


def find_yaml_files(folder: Path) -> Generator[Path, None, None]:
    """Recursively find all .yml files in a folder.

    Args:
        folder (Path): Folder path to search.

    Returns:
        Generator[Path, None, None]: All YAML files under the folder.
    """
    return folder.rglob("*.yml")  # type: ignore


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--inplace", is_flag=True, default=False, help="Format files in place.")
@click.option(
    "--output",
    type=click.Path(),
    default=None,
    help="Output file (only for single file input).",
)
@click.option(
    "--char-limit",
    type=int,
    default=CHAR_LIMIT_DEFAULT,
    help="Maximum line length for wrapping.",
)
def cli(path: str, inplace: bool, output: Optional[str], char_limit: int) -> None:
    """Format a YAML file or all `.yml` files in a folder."""
    path_obj: Path = Path(path)
    if path_obj.is_file():
        out_path: Optional[Path] = Path(output) if output else None
        console.print(f"[cyan]Processing file:[/cyan] {path_obj}")
        format_yaml_file(
            path_obj, inplace=inplace, output_file=out_path, char_limit=char_limit
        )
    elif path_obj.is_dir():
        if output:
            raise click.BadParameter("Cannot specify --output when input is a folder")
        console.print(f"[cyan]Processing folder recursively:[/cyan] {path_obj}")
        for file in find_yaml_files(path_obj):
            format_yaml_file(file, inplace=True, char_limit=char_limit)
    else:
        raise click.BadParameter(f"Path is neither file nor folder: {path}")


if __name__ == "__main__":
    cli()  # type: ignore
