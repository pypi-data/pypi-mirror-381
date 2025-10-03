# llama-scan

A tool for converting PDFs to text files using Ollama.

## Features

- Convert PDFs to text files locally, no token costs.
- Use the latest multimodal models supported by Ollama.
- Turn images and diagrams into detailed text descriptions.

## Requirements

- Python 3.10+
- Ollama installed and running locally

### Installing Ollama and the Default Model

1. Install [Ollama](https://ollama.com/)
2. Pull the default model:
```bash
ollama run qwen2.5vl:latest
```

## Installation

Install using pip:
```bash
pip install llama-scan
```

or uv:
```bash
uv tool install llama-scan
```

## Usage

Basic usage:
```bash
llama-scan path/to/your/file.pdf
```

### Options

- `--output`, `-o`: Output directory (default: "output")
- `--model`, `-m`: Ollama model to use (default: "qwen2.5vl:latest")
- `--start`, `-s`: Start page number (default: 0)
- `--end`, `-e`: End page number (default: 0)
- `--custom-instructions`, `-c`: Optional path to a text file containing additional instructions (default: None)
- `--server-url`, `-u`: Ollama server URL (default: "http://localhost:11434")
- `--width`, `-w`: Width of the resized images (0 to skip resizing; default: 0)
- `--keep-images`, `-k`: Keep the intermediate image files (default: False)
- `--stdout`, `-s`: Write merged output to stdout (default: False)

### Examples

Process specific pages:
```bash
llama-scan document.pdf --start 1 --end 5
```

Use a different Ollama model:
```bash
llama-scan document.pdf --model qwen2.5vl:3b
```
