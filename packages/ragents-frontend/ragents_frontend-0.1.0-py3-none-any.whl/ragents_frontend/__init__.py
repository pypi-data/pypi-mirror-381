"""RAGents Frontend - Python package for serving the Next.js frontend."""

from pathlib import Path

__version__ = "0.1.0"

# Get the package root directory
PACKAGE_ROOT = Path(__file__).parent

# Frontend build directory (contains .next and public folders)
FRONTEND_BUILD_DIR = PACKAGE_ROOT / "frontend_build"
NEXT_BUILD_DIR = FRONTEND_BUILD_DIR / ".next"
PUBLIC_DIR = FRONTEND_BUILD_DIR / "public"


def get_frontend_build_path() -> Path:
    """Get the path to the Next.js production build."""
    return FRONTEND_BUILD_DIR


def get_next_build_path() -> Path:
    """Get the path to the .next build directory."""
    return NEXT_BUILD_DIR


def get_public_path() -> Path:
    """Get the path to the public assets directory."""
    return PUBLIC_DIR


__all__ = [
    "__version__",
    "get_frontend_build_path",
    "get_next_build_path",
    "get_public_path",
    "FRONTEND_BUILD_DIR",
    "NEXT_BUILD_DIR",
    "PUBLIC_DIR",
]
