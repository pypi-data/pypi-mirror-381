"""Configuration commands for the Grounding CLI."""

from __future__ import annotations

from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from ..config import get_setting, set_setting
from ..settings import DEFAULT_SUPABASE_URL

console = Console()

config_app = typer.Typer(help="Manage stored configuration values.")


@config_app.command()
def supabase(
    url: Optional[str] = typer.Option(
        None,
        help="Supabase project URL (https://...supabase.co).",
        envvar="GROUNDING_SUPABASE_URL",
    ),
    anon_key: Optional[str] = typer.Option(
        None,
        help="Supabase anon key used for REST requests.",
        envvar="GROUNDING_SUPABASE_ANON_KEY",
    ),
) -> None:
    """Persist Supabase configuration required for API calls."""

    resolved_url = url or get_setting("supabase_url") or DEFAULT_SUPABASE_URL
    if not resolved_url:
        raise typer.BadParameter("Provide --url or set GROUNDING_SUPABASE_URL to your Supabase project URL.")
    set_setting("supabase_url", resolved_url)
    console.print(f"Supabase URL set to [bold]{resolved_url}[/bold].")

    if anon_key:
        set_setting("supabase_anon_key", anon_key)
        console.print("Supabase anon key stored securely in the local config file.")
    elif not get_setting("supabase_anon_key"):
        console.print("[yellow]Anon key not provided. API calls may fail until it is set.[/yellow]")


@config_app.command()
def show() -> None:
    """Show the persisted configuration values."""

    table = Table(show_header=False, box=None)
    table.add_row("supabase_url", get_setting("supabase_url") or "<unset>")
    anon = get_setting("supabase_anon_key")
    table.add_row("supabase_anon_key", "<set>" if anon else "<unset>")
    console.print(table)


__all__ = ["config_app"]
