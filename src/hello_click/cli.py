import click

from .command_1 import command_1
from .command_2 import command_2


@click.group(name="hello-click")
@click.version_option()
def cli():
    """A simple Click group to demonstrate Click."""


cli.add_command(command_1)
cli.add_command(command_2)
