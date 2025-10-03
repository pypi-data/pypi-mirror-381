from pathlib import Path

import pytest
from click.testing import CliRunner

from yaml_lex import cli


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def temp_yaml_file(tmp_path: Path):
    file = tmp_path / "test.yml"
    yield file  # let test write content
    # cleanup handled by tmp_path


def test_cli_on_file(runner, temp_yaml_file):
    temp_yaml_file.write_text(
        '- caption: "This is a very long caption that should be wrapped"\n'
    )
    result = runner.invoke(cli, [str(temp_yaml_file), "--char-limit", "20"])
    assert result.exit_code == 0
    assert "caption" in result.output
    assert "wrapped" in result.output


def test_cli_inplace(runner, temp_yaml_file):
    temp_yaml_file.write_text(
        '- content: "This is some very long content that will be wrapped"\n'
    )
    result = runner.invoke(
        cli, [str(temp_yaml_file), "--inplace", "--char-limit", "20"]
    )
    assert result.exit_code == 0
    text = temp_yaml_file.read_text()
    assert "content" in text
    assert "\n" in text


def test_cli_folder(runner, tmp_path: Path):
    f1 = tmp_path / "a.yml"
    f2 = tmp_path / "b.yml"
    f1.write_text('- caption: "Short"\n')
    f2.write_text('- caption: "This is another long caption that will be wrapped"\n')

    result = runner.invoke(cli, [str(tmp_path), "--inplace", "--char-limit", "20"])
    assert result.exit_code == 0
    assert "Formatted" in result.output
