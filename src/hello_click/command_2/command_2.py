"""A simple command that prints a greeting."""

import click


@click.command()
def command_2() -> None:
    """Print a greeting."""
    click.echo("Hello, World!")
