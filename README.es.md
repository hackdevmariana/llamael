# llamael

Asistente de programación en la terminal con [Ollama](https://ollama.ai) y [Click](https://click.palletsprojects.com/).

**llamael** te permite generar y modificar código mediante prompts de lenguaje natural, sin salir de tu consola.

## Instalación

Clona el repositorio y crea un entorno virtual:

```bash
git clone https://github.com/hackdevmariana/llamael.git
cd llamael
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Asegúrate de tener Ollama:

```bash
ollama run llama3
```