import click
from llamael.utils.ollama import run_ollama

@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.argument("prompt")
def mod(file, prompt):
    """Modifies an existing file according to a prompt."""
    click.echo(f"Modificando {file}...\n")
    with open(file) as f:
        code = f.read()
    full_prompt = f"{prompt}\n\nCódigo actual:\n{code}"
    run_ollama(full_prompt)
