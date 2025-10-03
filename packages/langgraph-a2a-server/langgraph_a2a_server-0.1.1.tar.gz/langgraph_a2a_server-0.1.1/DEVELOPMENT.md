# Development Guide

## Setup Development Environment

### Prerequisites

- Python 3.10 or higher
- uv (recommended) or pip

### Installation with uv

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install the package in editable mode with dev dependencies
uv pip install -e ".[dev]"
```

### Installation with pip

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install the package in editable mode with dev dependencies
pip install -e ".[dev]"
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=langgraph_a2a_server --cov-report=html

# Run specific test file
pytest tests/test_executor.py
```

## Code Quality

```bash
# Format code
ruff format .

# Lint code
ruff check .

# Fix linting issues automatically
ruff check --fix .
```

## Running Examples

```bash
# Run the simple agent example
python examples/simple_agent.py
```

Then visit:
- Agent Card: http://127.0.0.1:9000/.well-known/agent.json
- API Documentation: http://127.0.0.1:9000/docs (FastAPI only)

## Building the Package

```bash
# Build distribution packages
uv pip install build
python -m build

# This will create:
# - dist/langgraph_a2a_server_server-*.tar.gz (source distribution)
# - dist/langgraph_a2a_server_server-*.whl (wheel distribution)
```

## Publishing to PyPI

```bash
# Install twine
uv pip install twine

# Upload to PyPI (requires PyPI credentials)
python -m twine upload dist/*

# Upload to TestPyPI first (recommended)
python -m twine upload --repository testpypi dist/*
```

## Project Structure

```
langgraph-a2a-server/
├── src/
│   └── langgraph_a2a_server/
│       ├── __init__.py      # Package initialization
│       ├── executor.py       # A2A executor implementation
│       └── server.py         # A2A server implementation
├── tests/
│   ├── __init__.py
│   ├── test_executor.py     # Executor tests
│   └── test_server.py       # Server tests
├── examples/
│   └── simple_agent.py      # Simple example
├── pyproject.toml           # Project configuration
├── README.md                # User documentation
├── DEVELOPMENT.md           # This file
├── LICENSE                  # MIT License
└── .gitignore               # Git ignore rules
```

## Adding New Features

1. Create a new branch for your feature
2. Implement the feature with tests
3. Ensure all tests pass and code is formatted
4. Update documentation if needed
5. Submit a pull request

## Debugging

To enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Common Issues

### Import errors

Make sure you've installed the package in editable mode:
```bash
uv pip install -e ".[dev]"
```

### Tests not found

Make sure pytest is installed:
```bash
uv pip install pytest pytest-asyncio
```

## Resources

- [A2A Protocol Specification](https://github.com/google/a2a)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
