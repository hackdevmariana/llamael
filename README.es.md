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

### Instalación de Ollama

Ollama es el motor de inteligencia artificial local que utiliza llamael para generar y modificar código.

#### GNU/Linux (Debian, Ubuntu y derivados)

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

Después, asegúrate de que el servicio esté corriendo:

```bash
ollama serve
```

Y prueba el modelo base:

```bash
ollama run llama3
```

#### MacOS

```bash
brew install ollama/tap/ollama
ollama run llama3
```

#### Windows

Descarga el instalador desde [https://ollama.ai/download](https://ollama.ai/download)
Instálalo y abre una terminal nueva.

Ejecuta:

```bash
ollama run llama3
```

Una vez que Ollama esté instalado y ejecutando el modelo llama3, ya puedes usar todos los comandos de `llamael`.

## Uso básico

Ejemplo de generación de código:

```bash
python -m llamael gen "Crea una función en Python que calcule la media de una lista"
```

Ejemplo de modificación de archivo:

```bash
python -m llamael mod main.py "Convierte este código a usar pandas"
```

También puedes usarlo para inicializar una estructura base de proyecto:

```bash
python -m llamael init
```

## Instalación como comando global

Para poder ejecutar simplemente llamael desde cualquier lugar:

```bash
pip install -e .
```

Y luego, ejecutarlo:

```bash
llamael gen "Crea una clase Usuario con nombre y correo electrónico"
```

## Subcomandos disponibles

| Subcomando | Descripción                                         |
| ---------- | --------------------------------------------------- |
| `gen`      | Genera código a partir de un prompt                 |
| `mod`      | Modifica un fichero existente según una instrucción |
| `init`     | Crea la estructura base de un proyecto Python       |
| `translate` | Traduce un fichero       |

## Ideas futuras

- Integración con Git para commits automáticos
- Generación de tests unitarios con IA
- Plantillas de proyectos personalizables
- Modo interactivo estilo ChatGPT

## Licencia

Distribuido bajo la licencia GPLv3.
Consulta `LICENSE` para más información.

