import click
from llamael.commands import gen, mod, init, translate

@click.group()
def cli():
    """llamael - Asistente de programación con Ollama"""
    pass

# Registrar comandos
cli.add_command(gen.gen)
cli.add_command(mod.mod)
cli.add_command(init.init)
cli.add_command(translate.translate)

if __name__ == "__main__":
    cli()
