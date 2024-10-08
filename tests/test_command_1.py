"""Test command_1."""

from click.testing import CliRunner

from hello_click.command_1 import command_1


def test_command_1() -> None:
    """Should print 'Hello, Alice!'."""
    runner = CliRunner()
    result = runner.invoke(command_1, ["--name", "Alice"])
    assert result.exit_code == 0
    assert "Hello, Alice!" in result.output
