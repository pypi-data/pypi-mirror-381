"""Setup utilities for initializing FastAPI application state and resources.

This module contains functions for setting up the application's
state, templates, static files, and file watching.
"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from markdpy.config.models import ServerConfig
from markdpy.renderer import MarkdownRenderer
from markdpy.server.utils.handlers import handle_file_change
from markdpy.server.websocket import ConnectionManager
from markdpy.watcher import FileObserver


def setup_app_state(app: FastAPI, config: ServerConfig) -> None:
    """Initialize application state with configuration and services.

    This function sets up:
    - Server configuration
    - Markdown renderer with base path
    - WebSocket connection manager
    - File observer for live reload (if enabled)
    - Jinja2 templates
    - Static file serving

    Args:
        app: FastAPI application instance
        config: Server configuration
    """
    # Store config on app state
    app.state.config = config

    # Pass base_path to renderer for link processing
    base_path = config.serve_path if config.serve_path.is_dir() else config.serve_path.parent
    app.state.renderer = MarkdownRenderer(base_path=base_path)
    app.state.ws_manager = ConnectionManager()
    app.state.file_observer = None

    # Setup file watcher if reload enabled
    if config.reload_enabled:
        observer = FileObserver(
            watch_path=(
                config.serve_path if config.serve_path.is_dir() else config.serve_path.parent
            ),
            callback=lambda event: handle_file_change(app, event),
            debounce_ms=150,
            recursive=True,
        )
        app.state.file_observer = observer

    # Setup templates - now in package directory
    package_dir = Path(__file__).parent.parent  # markdpy/server/utils -> markdpy
    templates_path = package_dir / "templates"
    app.state.templates = Jinja2Templates(directory=str(templates_path))

    # Mount static files - now in package directory
    static_path = package_dir / "static"
    if static_path.exists():
        app.mount("/static", StaticFiles(directory=str(static_path)), name="static")
