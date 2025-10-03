"""Commands for interacting with the bundled MCP server."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from ..config import get_setting, get_token
from ..server import get_server_root
from ..settings import DEFAULT_MCP_HOST, DEFAULT_MCP_PORT, DEFAULT_SUPABASE_URL

console = Console()

server_app = typer.Typer(help="Run the local MCP server bundled with the CLI.")


def _ensure_node_available() -> str:
    node_path = shutil.which("node")
    if not node_path:
        raise typer.BadParameter("Node.js 18+ is required but not found on PATH.")
    return node_path


def _ensure_dependencies(server_root: Path, install: bool) -> None:
    node_modules = server_root / "node_modules"
    if node_modules.exists():
        return
    if not install:
        console.print("[yellow]node_modules missing and --no-install set. Dependencies may be missing.[/yellow]")
        return
    console.print("Installing Node.js dependencies (one-time setup)…")
    result = subprocess.run(
        ["npm", "install", "--production"],
        cwd=server_root,
        stdout=sys.stdout,
        stderr=sys.stderr,
        check=False,
    )
    if result.returncode != 0:
        raise typer.BadParameter("npm install failed. Inspect the output above for details.")


@server_app.command()
def start(
    agent: Optional[str] = typer.Option(
        None,
        help="Name of the stored agent token to expose to the server.",
    ),
    token: Optional[str] = typer.Option(
        None,
        help="Token string to expose to the server (overrides --agent).",
    ),
    host: str = typer.Option(DEFAULT_MCP_HOST, help="Host to bind the MCP server."),
    port: int = typer.Option(DEFAULT_MCP_PORT, help="Port to bind the MCP server."),
    install_dependencies: bool = typer.Option(
        True, help="Install Node dependencies if missing."
    ),
) -> None:
    """Start the bundled MCP server locally."""

    node_path = _ensure_node_available()
    server_root = get_server_root()
    _ensure_dependencies(server_root, install_dependencies)

    env = os.environ.copy()
    supabase_url = get_setting("supabase_url")
    # MCP server needs service_role key to access mcp_api_tokens table
    supabase_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("GROUNDING_SUPABASE_SERVICE_ROLE_KEY")
    if supabase_url:
        env.setdefault("SUPABASE_URL", supabase_url)
    if supabase_key:
        env.setdefault("SUPABASE_SERVICE_ROLE_KEY", supabase_key)
    else:
        console.print("[yellow]Warning: SUPABASE_SERVICE_ROLE_KEY not set. Server may not be able to validate tokens.[/yellow]")

    token_value = token
    if agent and not token_value:
        stored = get_token(agent)
        if stored:
            token_value = stored.get("token")
        else:
            console.print(f"[yellow]No stored token named '{agent}'. Server will start without a default Authorization header.[/yellow]")
    if token_value:
        env.setdefault("GROUNDING_AGENT_TOKEN", token_value)

    env.setdefault("MCP_SERVER_HOST", host)
    env.setdefault("MCP_SERVER_PORT", str(port))

    console.print(f"Launching MCP server from {server_root} on http://{host}:{port}/mcp")
    command = [node_path, "index.js"]

    process = subprocess.Popen(
        command,
        cwd=server_root,
        env=env,
    )
    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()
        process.wait()


__all__ = ["server_app"]
