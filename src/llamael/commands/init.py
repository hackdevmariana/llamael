import click
import os

@click.command()
def init():
    """Create a basic Python project structure."""
    click.echo("Creando estructura base de proyecto...")
    os.makedirs("src", exist_ok=True)
    os.makedirs("tests", exist_ok=True)
    open("src/__init__.py", "a").close()
    open("tests/__init__.py", "a").close()
    click.echo("Proyecto base creado.")
