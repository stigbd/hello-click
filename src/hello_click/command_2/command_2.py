import click


@click.command()
def command_2() -> None:
    """A simple command that prints a greeting."""
    click.echo("Hello, World!")
