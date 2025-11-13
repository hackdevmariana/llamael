import subprocess

def run_ollama(prompt: str, output_file: str = None, model: str = "llama3"):
    """Ejecuta un prompt con Ollama y opcionalmente guarda la salida."""
    command = f'echo "{prompt}" | ollama run {model}'
    if output_file:
        with open(output_file, "w", encoding="utf-8") as out:
            subprocess.run(command, shell=True, stdout=out)
    else:
        subprocess.run(command, shell=True)
