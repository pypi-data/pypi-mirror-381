# RAGents Frontend

A Python package that bundles the RAGents Next.js frontend for easy integration into Python applications.

## Installation

### Using uv (recommended)

```bash
uv pip install -e .
```

### Using pip

```bash
pip install -e .
```

## Usage

### As a Python Module

```python
from ragents_frontend import get_frontend_path, FRONTEND_DIR
from ragents_frontend.server import create_app, serve

# Get the frontend directory path
frontend_path = get_frontend_path()
print(f"Frontend is located at: {frontend_path}")

# Create a FastAPI app with the frontend
app = create_app()

# Or serve directly
serve(host="0.0.0.0", port=3000)
```

### As a CLI Tool

```bash
# Run the frontend server
python -m ragents_frontend

# With custom options
python -m ragents_frontend --host 127.0.0.1 --port 8080

# With auto-reload for development
python -m ragents_frontend --reload

# With a custom frontend directory
python -m ragents_frontend --frontend-dir /path/to/frontend
```

### Integration with Existing FastAPI Apps

```python
from fastapi import FastAPI
from ragents_frontend.server import create_app

# Your existing FastAPI app
main_app = FastAPI()

# Mount the frontend
frontend_app = create_app()
main_app.mount("/", frontend_app)

# Your API routes
@main_app.get("/api/data")
def get_data():
    return {"message": "Hello from API"}
```

## Development

### Prerequisites

- Python 3.9+
- Node.js 18+ (for building the frontend)
- uv (recommended) or pip

### Building the Package

1. Build the Next.js frontend first:
```bash
cd ../ragents-frontend
npm install
npm run build
```

2. Build the Python package:
```bash
cd ragents_frontend
uv build
```

### Development Installation

```bash
uv pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

## Package Structure

```
ragents_frontend/
├── src/
│   └── ragents_frontend/
│       ├── __init__.py          # Package entry point
│       ├── __main__.py          # CLI entry point
│       ├── server.py            # FastAPI server implementation
│       ├── frontend/            # Bundled Next.js frontend
│       └── frontend_lib/        # Frontend library code
├── pyproject.toml               # Package configuration
└── README.md                    # This file
```

## License

MIT License

## Author

Mehran Moazeni (mehran1414@gmail.com)
