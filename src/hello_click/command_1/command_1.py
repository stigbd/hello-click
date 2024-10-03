import click


@click.command()
@click.option("--name", prompt="Your name", help="The person to greet.")
def command_1(name: str) -> None:
    """A simple Click command that echos your name."""
    click.echo(f"Hello, {name}!")
