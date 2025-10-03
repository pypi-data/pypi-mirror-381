"""Command-line interface for the Grounding tooling."""

from __future__ import annotations

import typer
from rich.console import Console

from . import __version__
from .commands.auth import auth_app
from .commands.configure import config_app
from .commands.agent import agent_app
from .commands.server import server_app

app = typer.Typer(help="Grounding CLI", rich_markup_mode="markdown")
console = Console()

app.add_typer(auth_app, name="auth")
app.add_typer(config_app, name="config")
app.add_typer(agent_app, name="agent")
app.add_typer(server_app, name="server")


@app.callback()
def main_callback() -> None:
    """Top-level callback to ensure the CLI initialises."""


@app.command()
def version() -> None:
    """Print the installed CLI version."""

    console.print(f"Grounding CLI version [bold]{__version__}[/bold]")


if __name__ == "__main__":
    app()
