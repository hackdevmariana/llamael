import click
from llamael.utils.ollama import run_ollama

@click.command()
@click.argument("prompt")
def gen(prompt):
    """Generates code from a prompt."""
    click.echo("Generando código con Ollama...\n")
    run_ollama(prompt)
