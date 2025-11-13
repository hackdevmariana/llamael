import click
import os
from llamael.utils.ollama import run_ollama

@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_file", required=False)
@click.option("--from-lang", "-f", default="es", help="Idioma original (por defecto: es)")
@click.option("--to-lang", "-t", default="en", help="Idioma destino (por defecto: en)")
def translate(input_file, output_file, from_lang, to_lang):
    """Translate a file from one language to another using Ollama."""
    click.echo(f"Translating {input_file} from {from_lang} to {to_lang}...\n")

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    prompt = (
        f"Translate the following text from {from_lang} to {to_lang}. "
        f"Preserve the Markdown formatting, headers, and code:\n\n{text}"
    )

    if not output_file:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}.{to_lang}{ext}"

    run_ollama(prompt, output_file)
    click.echo(f"Translation saved in {output_file}")
