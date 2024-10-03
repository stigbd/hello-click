from click.testing import CliRunner
from hello_click.command_2 import command_2


def test_command_2():
    runner = CliRunner()
    result = runner.invoke(command_2)
    assert result.exit_code == 0
    assert "Hello, World!" in result.output
