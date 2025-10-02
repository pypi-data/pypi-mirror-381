"""FastAPI server to serve the RAGents frontend."""

from pathlib import Path
from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import uvicorn

from . import FRONTEND_BUILD_DIR, NEXT_BUILD_DIR, PUBLIC_DIR


def create_app(
    frontend_build_dir: Optional[Path] = None,
) -> FastAPI:
    """
    Create a FastAPI app that serves the Next.js frontend.

    Args:
        frontend_build_dir: Path to the frontend build directory. If None, uses the bundled build.

    Returns:
        FastAPI application instance
    """
    app = FastAPI(
        title="RAGents Frontend",
        description="Frontend interface for RAG agents",
        version="0.1.0"
    )

    build_path = frontend_build_dir or FRONTEND_BUILD_DIR
    next_path = build_path / ".next"
    public_path = build_path / "public"

    if not next_path.exists():
        raise RuntimeError(
            f"Next.js build not found at {next_path}. "
            "Make sure the frontend is built and included in the package."
        )

    # Health check endpoint
    @app.get("/api/health")
    async def health():
        return {
            "status": "ok",
            "frontend_build_path": str(build_path),
            "next_build_exists": next_path.exists(),
            "public_exists": public_path.exists()
        }

    # Serve Next.js static files from /_next
    static_path = next_path / "static"
    if static_path.exists():
        app.mount("/_next/static", StaticFiles(directory=str(static_path)), name="next_static")

    # Serve public assets if they exist
    if public_path.exists():
        app.mount("/public", StaticFiles(directory=str(public_path)), name="public")

    # Catch-all route to serve the Next.js app
    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        """Serve the Next.js frontend for all routes."""
        # For now, return a simple response
        # In production, you'd use Next.js standalone server or export
        return HTMLResponse("""
            <html>
                <head><title>RAGents Frontend</title></head>
                <body>
                    <h1>RAGents Frontend</h1>
                    <p>Next.js build is bundled. To serve properly, you need to:</p>
                    <ol>
                        <li>Use Next.js standalone output mode, or</li>
                        <li>Use static export (next export), or</li>
                        <li>Run Next.js server directly via Node.js</li>
                    </ol>
                    <p>Build path: {}</p>
                </body>
            </html>
        """.format(str(build_path)))

    return app


def serve(
    host: str = "0.0.0.0",
    port: int = 3000,
    frontend_build_dir: Optional[Path] = None,
    reload: bool = False,
):
    """
    Start the frontend server.

    Args:
        host: Host to bind to
        port: Port to bind to
        frontend_build_dir: Custom frontend build directory path
        reload: Enable auto-reload for development
    """
    app = create_app(frontend_build_dir=frontend_build_dir)

    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=reload,
    )


if __name__ == "__main__":
    serve()
