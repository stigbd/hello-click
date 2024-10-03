"""Tests for the CLI."""

from click.testing import CliRunner

from hello_click import cli


def test_hello_world() -> None:
    """Should print the help message."""
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert "Usage: hello-click [OPTIONS] COMMAND [ARGS]" in result.output
    assert "Do nothing, just a placeholder for the subcommands." in result.output
    assert "Options:" in result.output
    assert "Commands:" in result.output
    assert "command-1" in result.output
    assert "command-2" in result.output


def test_hello_world_with_version() -> None:
    """Should print the version message."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "hello-click, version 0.1.0\n" in result.output
