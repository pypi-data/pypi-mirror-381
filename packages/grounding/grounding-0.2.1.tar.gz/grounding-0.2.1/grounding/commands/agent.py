"""Agent integration helpers for the Grounding CLI."""

from __future__ import annotations

from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from ..api import GroundingAPI, GroundingAPIError
from ..config import delete_token, get_token, list_tokens, set_token
from ..settings import DEFAULT_MCP_URL

console = Console()

agent_app = typer.Typer(help="Manage MCP agent tokens and configuration snippets.")


@agent_app.command("list")
def list_agents(
    remote: bool = typer.Option(False, help="Also query Supabase for tokens."),
    show_billing: bool = typer.Option(False, help="Show billing mode for each token."),
) -> None:
    """List locally stored agent tokens."""

    tokens = list_tokens()
    if tokens:
        table = Table(title="Stored agent tokens", show_header=True, header_style="bold")
        table.add_column("Agent")
        table.add_column("Token prefix")
        table.add_column("Token ID", overflow="fold")
        if show_billing:
            table.add_column("Billing Mode")
        table.add_column("Note")
        for name, payload in tokens.items():
            row = [
                name,
                str(payload.get("token_prefix", payload.get("token", ""))[:12]),
                str(payload.get("token_id", "")),
            ]
            if show_billing:
                billing_mode = payload.get("billing_mode", "—")
                row.append(billing_mode)
            row.append(payload.get("note", ""))
            table.add_row(*row)
        console.print(table)
    else:
        console.print("[yellow]No local agent tokens stored.[/yellow]")

    if remote:
        try:
            api = GroundingAPI()
            remote_tokens = api.list_agent_tokens()
        except GroundingAPIError as error:
            console.print(f"[red]Failed to query Supabase:[/red] {error}")
            return
        table = Table(title="Supabase tokens", show_header=True, header_style="bold")
        table.add_column("Token ID", overflow="fold")
        table.add_column("Agent")
        table.add_column("Prefix")
        table.add_column("Active")
        if show_billing:
            table.add_column("Billing Mode")
        table.add_column("Stored locally")
        table.add_column("Created at")
        for item in remote_tokens:
            stored = next((name for name, payload in tokens.items() if payload.get("token_id") == item.get("id")), None)
            row = [
                str(item.get("id")),
                item.get("agent_id") or "—",
                item.get("token_prefix") or "—",
                "yes" if item.get("is_active", True) else "no",
            ]
            if show_billing:
                metadata = item.get("metadata", {})
                billing_mode = metadata.get("billing_mode", "—") if isinstance(metadata, dict) else "—"
                row.append(billing_mode)
            row.extend([
                stored or "no",
                item.get("created_at") or "—",
            ])
            table.add_row(*row)
        console.print(table)


@agent_app.command()
def create(
    name: str = typer.Argument(..., help="Friendly name for the agent token."),
    label: Optional[str] = typer.Option(None, help="Label stored in Supabase metadata (visible in dashboard)."),
    note: Optional[str] = typer.Option(None, help="Optional description stored locally only."),
    store: bool = typer.Option(True, help="Persist the full token locally."),
    billing_mode: Optional[str] = typer.Option(None, help="Billing mode: 'subscription' or 'credits'"),
) -> None:
    """Create a new MCP API token for an agent."""

    try:
        api = GroundingAPI()
    except GroundingAPIError as error:
        console.print(f"[red]Failed to initialize API:[/red] {error}")
        raise typer.Exit(code=1)

    # Get billing status to determine available options
    try:
        billing_status = api.get_billing_status()
    except GroundingAPIError as error:
        console.print(f"[yellow]Warning: Could not fetch billing status:[/yellow] {error}")
        billing_status = {"subscription": None, "credits": None}

    subscription = billing_status.get("subscription")
    credits = billing_status.get("credits")
    has_subscription = subscription is not None
    has_credits = credits and credits.get("balance_cents", 0) > 0

    # Determine billing mode if not provided
    if billing_mode is None and (has_subscription or has_credits):
        console.print("\n[bold cyan]Billing Options:[/bold cyan]")

        if has_subscription:
            tier = subscription.get("tier", "unknown")
            limit = subscription.get("call_limit", "unlimited")
            period = subscription.get("call_limit_period", "month")
            console.print(f"  [bold]1)[/bold] Use subscription quota ([green]{tier}[/green] - {limit} calls/{period})")

        if has_credits:
            balance = credits.get("balance_cents", 0) / 100
            currency = credits.get("currency", "usd").upper()
            console.print(f"  [bold]2)[/bold] Use prepaid credits ([green]{currency} ${balance:.2f}[/green])")

        if has_subscription and has_credits:
            console.print("\n[dim]Subscription quota is recommended for regular usage.[/dim]")
            console.print("[dim]Prepaid credits are useful for temporary or overflow usage.[/dim]")
            choice = typer.prompt("\nSelect billing mode", type=int, default=1)
            billing_mode = 'subscription' if choice == 1 else 'credits'
        elif has_subscription:
            billing_mode = 'subscription'
            console.print("\n[dim]Using subscription quota (no prepaid credits available).[/dim]")
        elif has_credits:
            billing_mode = 'credits'
            console.print("\n[dim]Using prepaid credits (no active subscription).[/dim]")
    elif billing_mode is None:
        # Default to credits if nothing available (will fail later if no credits exist)
        billing_mode = 'credits'
        console.print("\n[yellow]No subscription or credits detected. Token will be created but may not work until you add credits or subscribe.[/yellow]")

    # Validate billing mode
    if billing_mode not in ('subscription', 'credits'):
        console.print(f"[red]Invalid billing mode '{billing_mode}'. Must be 'subscription' or 'credits'.[/red]")
        raise typer.Exit(code=1)

    # Prompt for label if not provided
    if label is None:
        label = typer.prompt("Label (optional, visible in dashboard)", default="", show_default=False)
        if label.strip() == "":
            label = None

    try:
        payload = api.issue_agent_token(name)
    except GroundingAPIError as error:
        console.print(f"[red]Failed to create agent token:[/red] {error}")
        raise typer.Exit(code=1)

    token = payload.get("token")
    token_id = payload.get("token_id") or payload.get("id")
    token_prefix = payload.get("token_prefix")

    # Set billing mode for the token
    if token_id:
        try:
            api.set_agent_token_billing_mode(token_id, billing_mode)
            console.print(f"[green]✓ Billing mode set to: [bold]{billing_mode}[/bold][/green]")
        except GroundingAPIError as error:
            console.print(f"[yellow]Warning: Failed to set billing mode:[/yellow] {error}")

    # Update metadata with label if provided
    if label and token_id:
        try:
            api.update_agent_token_metadata(token_id, label=label)
            console.print(f"[green]✓ Label '[bold]{label}[/bold]' saved to Supabase.[/green]")
        except GroundingAPIError as error:
            console.print(f"[yellow]Warning: Failed to save label to Supabase:[/yellow] {error}")

    console.print("\n[green]Token created successfully.[/green]")
    if token:
        console.print(f"[bold]Token:[/bold] {token}")
    else:
        console.print("[yellow]Supabase did not return a token. Check RLS policies and RPC implementation.[/yellow]")

    if store and token:
        stored_payload = {
            "token": token,
            "token_id": token_id,
            "token_prefix": token_prefix,
            "billing_mode": billing_mode,
        }
        if note:
            stored_payload["note"] = note
        set_token(name, stored_payload)
        console.print(f"Token stored locally under name [bold]{name}[/bold].")


@agent_app.command()
def forget(name: str = typer.Argument(..., help="Agent token to remove from local storage.")) -> None:
    """Remove a stored agent token from the local config."""

    if get_token(name) is None:
        console.print(f"[yellow]No token stored under '{name}'.[/yellow]")
        return
    delete_token(name)
    console.print(f"Removed token '{name}' from local storage.")


@agent_app.command()
def config(
    name: str = typer.Argument(..., help="Agent token to format."),
    format: str = typer.Option(
        "claude-desktop", help="Output format (claude-desktop|cline|vscode|openai|anthropic|gemini|generic)."
    ),
    endpoint: str = typer.Option(
        DEFAULT_MCP_URL,
        help="MCP server endpoint URL for hosted usage.",
    ),
) -> None:
    """Print MCP client configuration for an agent token."""

    token = get_token(name)
    if not token:
        console.print(f"[red]No stored token named '{name}'. Run `grounding agent create {name}` first.")
        raise typer.Exit(code=1)

    full_token = token.get("token")
    if not full_token:
        console.print("[red]Stored token is missing the secret component.[/red]")
        raise typer.Exit(code=1)

    if format == "openai":
        console.print("[bold]OpenAI SDK Integration[/bold]")
        console.print()
        console.print("[dim]# Installation:[/dim]")
        console.print("pip install 'grounding[openai]'")
        console.print()
        console.print("[dim]# Usage:[/dim]")
        console.print(f"""
import asyncio
from openai import OpenAI
from grounding import GroundingMCPOpenAI

client = OpenAI()  # Reads OPENAI_API_KEY from environment
grounding = GroundingMCPOpenAI(token="{full_token}", url="{endpoint}")

async def main():
    # Get Grounding tools for OpenAI
    tools = await grounding.get_openai_tools()

    # Make a request with tools (use your preferred model)
    response = client.chat.completions.create(
        model="gpt-4o",  # or any OpenAI model
        messages=[{{"role": "user", "content": "Find the Gmail compose button"}}],
        tools=tools
    )

    # Execute tool calls if any
    message = response.choices[0].message
    if message.tool_calls:
        tool_results = await grounding.execute_tool_calls(message.tool_calls)

        # Continue conversation with tool results
        messages = [
            {{"role": "user", "content": "Find the Gmail compose button"}},
            message,
            *tool_results
        ]
        final_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        print(final_response.choices[0].message.content)

asyncio.run(main())
""")
    elif format == "anthropic":
        console.print("[bold]Anthropic Claude SDK Integration[/bold]")
        console.print()
        console.print("[dim]# Installation:[/dim]")
        console.print("pip install 'grounding[anthropic]'")
        console.print()
        console.print("[dim]# Usage:[/dim]")
        console.print(f"""
import asyncio
from anthropic import Anthropic
from grounding import GroundingMCPClaude

client = Anthropic()  # Reads ANTHROPIC_API_KEY from environment
grounding = GroundingMCPClaude(token="{full_token}", url="{endpoint}")

async def main():
    # Get Grounding tools for Claude
    tools = await grounding.get_claude_tools()

    # Make a request with tools (use your preferred model)
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",  # or any Claude model
        max_tokens=1024,
        messages=[{{"role": "user", "content": "Find the Gmail compose button"}}],
        tools=tools
    )

    # Execute tool uses if any
    if response.stop_reason == "tool_use":
        tool_uses = [block for block in response.content if block.type == "tool_use"]
        tool_results = await grounding.execute_tool_uses(tool_uses)

        # Continue conversation with tool results
        final_response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[
                {{"role": "user", "content": "Find the Gmail compose button"}},
                {{"role": "assistant", "content": response.content}},
                {{"role": "user", "content": tool_results}}
            ],
            tools=tools
        )
        print(final_response.content)

asyncio.run(main())
""")
    elif format == "gemini":
        console.print("[bold]Google Gemini SDK Integration[/bold]")
        console.print()
        console.print("[dim]# Installation:[/dim]")
        console.print("pip install 'grounding[google]'")
        console.print()
        console.print("[dim]# Usage:[/dim]")
        console.print(f"""
import asyncio
import os
from google import genai

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
grounding = GroundingMCPGemini(token="{full_token}", url="{endpoint}")

async def main():
    # Get Grounding tools for Gemini
    tools = await grounding.get_gemini_tools()

    # Generate content with tools (use your preferred model)
    response = client.models.generate_content(
        model='gemini-1.5-pro',  # or gemini-1.5-flash, gemini-2.0-flash, etc.
        contents="Find the Gmail compose button",
        config={{"tools": tools}}
    )

    # Execute function calls if any
    if response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if hasattr(part, 'function_call'):
                result = await grounding.execute_function_call(part.function_call)
                # Continue conversation with function response
                response = client.models.generate_content(
                    model='gemini-1.5-pro',
                    contents=[
                        {{"role": "user", "parts": [{{"text": "Find the Gmail compose button"}}]}},
                        {{"role": "model", "parts": response.candidates[0].content.parts}},
                        {{"role": "function", "parts": [{{"function_response": result}}]}}
                    ]
                )

    print(response.text)

asyncio.run(main())
""")
    elif format == "claude-desktop":
        import json
        config = {
            "mcpServers": {
                "grounding": {
                    "type": "http",
                    "url": endpoint,
                    "headers": {
                        "Authorization": f"Bearer {full_token}"
                    }
                }
            }
        }
        console.print("[bold]Claude Desktop Configuration[/bold]")
        console.print("Add this to your Claude Desktop config file:")
        console.print("[dim]macOS: ~/Library/Application Support/Claude/claude_desktop_config.json[/dim]")
        console.print("[dim]Windows: %APPDATA%\\Claude\\claude_desktop_config.json[/dim]")
        console.print()
        console.print(json.dumps(config, indent=2))
    elif format == "cline":
        import json
        config = {
            "mcpServers": {
                "grounding": {
                    "type": "http",
                    "url": endpoint,
                    "headers": {
                        "Authorization": f"Bearer {full_token}"
                    }
                }
            }
        }
        console.print("[bold]Cline MCP Configuration[/bold]")
        console.print("Add this to cline_mcp_settings.json:")
        console.print("[dim]Access via Cline extension → MCP Servers icon → Configure MCP Servers[/dim]")
        console.print()
        console.print(json.dumps(config, indent=2))
    elif format == "vscode":
        import json
        config = {
            "mcpServers": {
                "grounding": {
                    "type": "http",
                    "url": endpoint,
                    "headers": {
                        "Authorization": f"Bearer {full_token}"
                    }
                }
            }
        }
        console.print("[bold]VS Code MCP Configuration[/bold]")
        console.print("Add this to your MCP configuration:")
        console.print("[dim]Workspace: .vscode/mcp.json[/dim]")
        console.print("[dim]Global: Run 'MCP: Open User Configuration' command[/dim]")
        console.print()
        console.print(json.dumps(config, indent=2))
    elif format == "generic":
        import json
        config = {
            "mcpServers": {
                "grounding": {
                    "type": "http",
                    "url": endpoint,
                    "headers": {
                        "Authorization": f"Bearer {full_token}"
                    }
                }
            }
        }
        console.print("[bold]Generic MCP Client Configuration[/bold]")
        console.print("Use this configuration block with any MCP-compatible client:")
        console.print()
        console.print(json.dumps(config, indent=2))
    else:
        console.print(f"[red]Unknown format '{format}'.[/red]")
        console.print("Supported formats:")
        console.print("  [bold]GUI Tools:[/bold] claude-desktop, cline, vscode")
        console.print("  [bold]SDK Integration:[/bold] openai, anthropic, gemini")
        console.print("  [bold]Other:[/bold] generic")
        raise typer.Exit(code=1)


@agent_app.command("import")
def import_token(
    name: str = typer.Argument(..., help="Friendly name to store the imported token."),
    token: str = typer.Argument(..., help="Full token string (prefix.secret) provided by the dashboard."),
    note: Optional[str] = typer.Option(None, help="Optional note to store locally."),
) -> None:
    """Register an existing agent token that was created outside the CLI."""

    try:
        api = GroundingAPI()
        record = api.verify_agent_token(token)
    except GroundingAPIError as error:
        console.print(f"[red]Failed to verify token:[/red] {error}")
        raise typer.Exit(code=1)

    existing = get_token(name)
    if existing and existing.get("token_id") != record.get("id"):
        console.print(f"[yellow]Warning: overwriting local entry '{name}'.[/yellow]")

    local_note = note if note is not None else (existing.get("note") if existing else None)
    stored_payload = {
        "token": token,
        "token_id": record.get("id"),
        "token_prefix": record.get("token_prefix"),
        "note": local_note,
    }
    if record.get("agent_id"):
        stored_payload["agent_id"] = record.get("agent_id")
    set_token(name, stored_payload)
    console.print(f"Imported token for agent '{record.get('agent_id') or name}' under name [bold]{name}[/bold].")


@agent_app.command()
def revoke(
    name: str = typer.Argument(..., help="Name of the stored token to revoke."),
    forget_local: bool = typer.Option(True, help="Remove the token from local storage after revocation."),
) -> None:
    """Revoke a token in Supabase and optionally remove it locally."""

    token = get_token(name)
    if not token or not token.get("token_id"):
        console.print(f"[red]No token metadata found for '{name}'.[/red]")
        raise typer.Exit(code=1)

    try:
        api = GroundingAPI()
        api.revoke_agent_token(token["token_id"])
    except GroundingAPIError as error:
        console.print(f"[red]Failed to revoke token:[/red] {error}")
        raise typer.Exit(code=1)

    console.print(f"[green]Token '{name}' revoked in Supabase.[/green]")
    if forget_local:
        delete_token(name)
        console.print("Local record removed.")


@agent_app.command()
def update_label(
    name: str = typer.Argument(..., help="Name of the stored token to update."),
    label: str = typer.Option(..., help="New label to save in Supabase metadata."),
) -> None:
    """Update the label for an existing token in Supabase."""

    token = get_token(name)
    if not token or not token.get("token_id"):
        console.print(f"[red]No stored token named '{name}'.[/red]")
        raise typer.Exit(code=1)

    try:
        api = GroundingAPI()
        api.update_agent_token_metadata(token["token_id"], label=label)
        console.print(f"[green]Label updated to '[bold]{label}[/bold]' in Supabase.[/green]")
    except GroundingAPIError as error:
        console.print(f"[red]Failed to update label:[/red] {error}")
        raise typer.Exit(code=1)


@agent_app.command()
def rotate(
    name: str = typer.Argument(..., help="Name of the stored token to rotate."),
    note: Optional[str] = typer.Option(None, help="Optional note for the new token."),
) -> None:
    """Revoke the existing token and issue a new one with the same friendly name."""

    token = get_token(name)
    if not token or not token.get("token_id"):
        console.print(f"[red]No stored token named '{name}'.[/red]")
        raise typer.Exit(code=1)

    agent_label = token.get("agent_id") or name

    try:
        api = GroundingAPI()
        api.revoke_agent_token(token["token_id"])
        console.print(f"Revoked existing token for '{name}'.")
        new_payload = api.issue_agent_token(agent_label)
    except GroundingAPIError as error:
        console.print(f"[red]Rotation failed:[/red] {error}")
        raise typer.Exit(code=1)

    stored_payload = {
        "token": new_payload.get("token"),
        "token_id": new_payload.get("token_id") or new_payload.get("id"),
        "token_prefix": new_payload.get("token_prefix"),
        "agent_id": agent_label,
        "note": note or token.get("note"),
    }
    set_token(name, stored_payload)
    console.print("[green]Rotation complete. New token stored locally and printed below.[/green]")
    if new_payload.get("token"):
        console.print(f"[bold]{new_payload['token']}[/bold]")


@agent_app.command("set-billing")
def set_billing(
    name: str = typer.Argument(..., help="Name of the stored token"),
    mode: str = typer.Option(..., "--mode", help="Billing mode: 'subscription' or 'credits'"),
) -> None:
    """Change the billing mode for an existing agent token.

    This allows you to switch between using your subscription quota
    or prepaid credits for a specific token.
    """
    token = get_token(name)
    if not token or not token.get("token_id"):
        console.print(f"[red]No stored token named '{name}'.[/red]")
        console.print("Run [bold]grounding agent list[/bold] to see available tokens.")
        raise typer.Exit(code=1)

    # Validate billing mode
    if mode not in ('subscription', 'credits'):
        console.print(f"[red]Invalid billing mode '{mode}'.[/red]")
        console.print("Valid options: [bold]subscription[/bold] or [bold]credits[/bold]")
        raise typer.Exit(code=1)

    try:
        api = GroundingAPI()

        # Get current billing status to show user what they have
        try:
            billing_status = api.get_billing_status()
            subscription = billing_status.get("subscription")
            credits_data = billing_status.get("credits")

            if mode == 'subscription' and not subscription:
                console.print("[yellow]Warning: You don't have an active subscription.[/yellow]")
                console.print("The token will be set to subscription mode, but calls may fail until you subscribe.")
                if not typer.confirm("Continue anyway?", default=False):
                    raise typer.Exit(code=0)

            if mode == 'credits' and (not credits_data or credits_data.get("balance_cents", 0) <= 0):
                console.print("[yellow]Warning: You don't have any prepaid credits.[/yellow]")
                console.print("The token will be set to credits mode, but calls may fail until you add credits.")
                if not typer.confirm("Continue anyway?", default=False):
                    raise typer.Exit(code=0)
        except GroundingAPIError:
            # If we can't fetch billing status, just warn and continue
            console.print("[yellow]Warning: Could not verify your billing status.[/yellow]")

        # Update the billing mode
        api.set_agent_token_billing_mode(token["token_id"], mode)
        console.print(f"[green]✓ Billing mode for '{name}' updated to: [bold]{mode}[/bold][/green]")

        # Update local storage
        token["billing_mode"] = mode
        set_token(name, token)

        if mode == 'subscription':
            console.print("[dim]This token will now use your subscription quota.[/dim]")
        else:
            console.print("[dim]This token will now deduct from your prepaid credits.[/dim]")

    except GroundingAPIError as error:
        console.print(f"[red]Failed to update billing mode:[/red] {error}")
        raise typer.Exit(code=1)


__all__ = ["agent_app"]
