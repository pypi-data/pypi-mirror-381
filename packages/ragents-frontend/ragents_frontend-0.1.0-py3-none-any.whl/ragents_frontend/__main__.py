"""CLI entry point for the ragents-frontend package."""

import argparse
from pathlib import Path

from .server import serve


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="RAGents Frontend Server"
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host to bind to (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=3000,
        help="Port to bind to (default: 3000)"
    )
    parser.add_argument(
        "--frontend-build-dir",
        type=Path,
        help="Custom frontend build directory path"
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload for development"
    )

    args = parser.parse_args()

    print(f"Starting RAGents Frontend server on {args.host}:{args.port}")
    serve(
        host=args.host,
        port=args.port,
        frontend_build_dir=args.frontend_build_dir,
        reload=args.reload,
    )


if __name__ == "__main__":
    main()
