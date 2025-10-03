"""Authentication-related CLI commands."""

from __future__ import annotations

import datetime as dt
from typing import Optional

import typer
import requests
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from .. import __version__
from ..config import get_session, set_session, get_setting, set_setting
from ..oauth import OAuthConfig, OAuthError, perform_pkce_flow
from ..settings import (
    DEFAULT_API_URL,
    DEFAULT_OAUTH_SCOPES,
    DEFAULT_REDIRECT_HOST,
    DEFAULT_REDIRECT_PORT,
    DEFAULT_SUPABASE_ANON_KEY,
    DEFAULT_SUPABASE_CLIENT_ID,
    DEFAULT_SUPABASE_PROVIDER,
    DEFAULT_SUPABASE_URL,
)

console = Console()

auth_app = typer.Typer(help="Manage authentication for the Grounding platform.")


@auth_app.command()
def login(
    supabase_url: Optional[str] = typer.Option(
        None,
        help="Override the Supabase project URL.",
        envvar="GROUNDING_SUPABASE_URL",
    ),
    provider: str = typer.Option(
        DEFAULT_SUPABASE_PROVIDER,
        help="OAuth provider to use for login (e.g. github, google).",
    ),
    scopes: str = typer.Option(
        DEFAULT_OAUTH_SCOPES,
        help="OAuth scopes requested during login.",
    ),
    client_id: Optional[str] = typer.Option(
        DEFAULT_SUPABASE_CLIENT_ID,
        help="Optional Supabase client ID for multi-provider setups.",
    ),
    no_browser: bool = typer.Option(
        False,
        help="Do not attempt to automatically open the browser.",
    ),
    manual: bool = typer.Option(
        False,
        help="Disable the embedded callback server and require manual code entry.",
    ),
) -> None:
    """Authenticate with Grounding using a browser-based PKCE flow."""

    resolved_url = (
        supabase_url
        or get_setting("supabase_url")
        or DEFAULT_SUPABASE_URL
    )
    if not resolved_url:
        raise typer.BadParameter(
            "Supabase URL is not configured. Provide --supabase-url or set the GROUNDING_SUPABASE_URL environment variable."
        )

    set_setting("supabase_url", resolved_url)
    set_setting("supabase_provider", provider)
    set_setting("oauth_scopes", scopes)
    if client_id:
        set_setting("supabase_client_id", client_id)

    oauth_config = OAuthConfig(
        supabase_url=resolved_url,
        provider=provider,
        scopes=scopes,
        redirect_host=DEFAULT_REDIRECT_HOST,
        redirect_port=DEFAULT_REDIRECT_PORT,
        anon_key=DEFAULT_SUPABASE_ANON_KEY,
        client_id=client_id,
        use_local_server=not manual,
        open_browser=not no_browser,
    )

    console.print("Starting browser-based login flow…")

    try:
        session = perform_pkce_flow(oauth_config)
    except OAuthError as error:
        console.print(f"[red]Login failed:[/red] {error}")
        raise typer.Exit(code=1)

    set_session(session)
    console.print("[green]Login succeeded.[/green]")

    # Prompt for billing preference
    console.print("\n[bold]Choose your billing preference:[/bold]")
    console.print("  1. Subscription (default) - Use your subscription limits")
    console.print("  2. Credits - Use your credit balance")
    console.print("  3. Auto - Try subscription first, fallback to credits")

    choice = Prompt.ask(
        "\nSelect billing mode",
        choices=["1", "2", "3"],
        default="1"
    )

    billing_preference_map = {
        "1": "subscription",
        "2": "credits",
        "3": "auto"
    }

    billing_preference = billing_preference_map[choice]

    # Update billing preference via API
    try:
        api_url = get_setting("api_url") or DEFAULT_API_URL
        response = requests.put(
            f"{api_url}/payment/billing/preference",
            headers={
                "Authorization": f"Bearer {session.access_token}",
                "Content-Type": "application/json"
            },
            json={"billingPreference": billing_preference}
        )

        if response.status_code == 200:
            console.print(f"[green]✓[/green] Billing preference set to: [bold]{billing_preference}[/bold]")
        else:
            console.print(f"[yellow]Warning: Could not set billing preference (HTTP {response.status_code}). Response: {response.text}[/yellow]")
            console.print(f"[yellow]You can change it later in the dashboard.[/yellow]")
    except Exception as e:
        console.print(f"[yellow]Warning: Could not set billing preference ({e}). You can change it later in the dashboard.[/yellow]")


@auth_app.command()
def logout() -> None:
    """Clear the stored Grounding session."""

    set_session(None)
    console.print("Logged out of Grounding.")


@auth_app.command()
def status() -> None:
    """Display the current authentication status."""

    session = get_session()
    if not session:
        console.print("[yellow]Not logged in.[/yellow]")
        return

    table = Table(show_header=False, box=None)
    table.add_row("CLI version", __version__)
    user = session.user or {}
    table.add_row("User ID", str(user.get("id", "unknown")))
    table.add_row("Email", user.get("email", "unknown"))
    if session.expires_at:
        expiry = dt.datetime.fromtimestamp(session.expires_at)
        table.add_row("Token expires", expiry.isoformat())
    console.print(table)


__all__ = ["auth_app"]
