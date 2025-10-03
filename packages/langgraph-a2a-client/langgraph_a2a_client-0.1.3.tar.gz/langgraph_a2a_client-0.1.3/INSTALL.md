# Installation and Development Guide

## Installation

### Using pip

```bash
pip install langgraph-a2a-client
```

### Using uv (recommended)

```bash
uv pip install langgraph-a2a-client
```

### From source

```bash
git clone https://github.com/yourusername/langgraph-a2a-client-as-tool.git
cd langgraph-a2a-client-as-tool
uv pip install -e .
```

## Development Setup

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Setup development environment

1. Clone the repository:
```bash
git clone https://github.com/yourusername/langgraph-a2a-client-as-tool.git
cd langgraph-a2a-client-as-tool
```

2. Install development dependencies with uv:
```bash
uv pip install -e ".[dev]"
```

### Running tests

```bash
pytest
```

With coverage:
```bash
pytest --cov=langgraph_a2a_client --cov-report=html
```

### Code formatting and linting

Format code:
```bash
ruff format .
```

Lint code:
```bash
ruff check .
```

Fix linting issues automatically:
```bash
ruff check --fix .
```

## Building the package

```bash
uv build
```

This will create distribution files in the `dist/` directory.

## Publishing to PyPI

```bash
uv publish
```

Make sure you have configured your PyPI credentials before publishing.
