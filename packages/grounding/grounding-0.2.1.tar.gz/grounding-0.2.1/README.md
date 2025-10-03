# Grounding CLI

**Grounding** provides real-time UI context to AI agents through feature grounding - giving agents precise, queryable information about application interfaces instead of relying on screenshots or outdated documentation.

The `grounding` CLI lets you:
- **Authenticate** with the Grounding platform
- **Create MCP tokens** for your AI agents
- **Connect agents** to live UI data (button locations, keyboard shortcuts, UI element hierarchies)
- **Query application features** in real-time without screenshots

By integrating Grounding's MCP server, your agents can:
- 🎯 **Find UI elements** by semantic description ("Gmail compose button")
- ⌨️ **Discover keyboard shortcuts** for any application
- 🗺️ **Navigate interfaces** using structured, queryable UI data
- 🔄 **Stay up-to-date** with live application state instead of stale screenshots

## Installation

```bash
pip install grounding
```

> Tip: `pipx install grounding` keeps the CLI isolated from your system Python.

## First-time setup

1. Supabase connection info ships with the CLI via environment variables (`GROUNDING_SUPABASE_URL`, `GROUNDING_SUPABASE_ANON_KEY`). If you need to override them, run `grounding config supabase` with your project values.

2. Log in with your Grounding developer account using an OAuth PKCE flow. The CLI opens a browser window; if that fails it prints the URL so you can copy/paste manually.

    ```bash
    grounding auth login
    ```

3. Verify the session:

    ```bash
    grounding auth status
    ```

## Managing MCP agent tokens

Create a token for each automation agent you operate. The CLI stores the full token locally (chmod 600) so you can reuse it later.

```bash
grounding agent create my-agent
# → prints fg_xxxxx.yyyyy and stores it locally

# Import a token minted from the dashboard
grounding agent import my-agent fg_abcdef12.verysecrettoken

# List local and remote tokens
grounding agent list --remote

# Remove a stored token
grounding agent forget my-agent

# Revoke or rotate a token directly from the CLI
grounding agent revoke my-agent
grounding agent rotate my-agent
```

### For SDK Integration (OpenAI, Anthropic, Google)

**All major LLM providers now have native MCP support!** You can integrate with minimal or zero code:

#### OpenAI - Native MCP (Zero Code!)
```python
from openai import OpenAI

client = OpenAI()
response = client.responses.create(
    model="o4-mini",
    input=[{"role": "user", "content": [{"type": "input_text", "text": "Find Gmail compose"}]}],
    tools=[{
        "type": "mcp",
        "server_label": "grounding",
        "server_url": "https://api.grounding.dev/mcp/sse/",
        "allowed_tools": ["list_surfaces", "get_feature", "find_feature", "list_keyboard_shortcuts"],
        "require_approval": "never"
    }]
)
```

#### Anthropic - Native MCP (Zero Code!)
```python
from anthropic import Anthropic

client = Anthropic()
response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "Find Gmail compose"}],
    mcp_servers=[{
        "type": "url",
        "url": "https://api.grounding.dev/mcp",
        "name": "grounding",
        "authorization_token": "fg_xxxxx.yyyyy"
    }],
    extra_headers={"anthropic-beta": "mcp-client-2025-04-04"}
)
```

#### Google Gemini - Native MCP (Minimal Code!)
```python
from google import genai
from google.genai import types
from mcp import ClientSession
from mcp.client.http import http_client

client = genai.Client()
async with http_client(url="https://api.grounding.dev/mcp", headers={"Authorization": "Bearer fg_xxxxx.yyyyy"}) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        response = await client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents="Find Gmail compose",
            config=types.GenerateContentConfig(tools=[session])
        )
```

**Need manual control?** Install our helper library:
```bash
pip install 'grounding[openai]'    # For OpenAI manual control
pip install 'grounding[anthropic]' # For Anthropic manual control
pip install 'grounding[google]'    # For Google Gemini manual control
```

See [SDK Integration Guide](docs/SDK_INTEGRATION.md) for complete examples, multi-turn conversations, and when to use native vs. helper library approaches.

### For GUI Tools (Claude Desktop, Cline, VS Code)

These configurations work with GUI-based AI assistants that support MCP.

Generate a ready-to-paste MCP client configuration snippet for your agent:

```bash
grounding agent config my-agent --format claude-desktop
```

Formats:

- `claude-desktop` – Configuration for Claude Desktop (macOS/Windows)
- `cline` – Configuration for Cline VS Code extension
- `vscode` – Configuration for VS Code native MCP support
- `generic` – Generic MCP client configuration for any compatible client

### Example configurations

**Claude Desktop** (default format):
```bash
grounding agent config my-agent --format claude-desktop
```
Output includes the config file path and JSON to add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "grounding": {
      "type": "http",
      "url": "https://api.grounding.dev/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_TOKEN_HERE"
      }
    }
  }
}
```

**Cline** (VS Code extension):
```bash
grounding agent config my-agent --format cline
```
Output includes instructions to configure via Cline's MCP Servers UI.

**VS Code** (native MCP):
```bash
grounding agent config my-agent --format vscode
```
Output can be added to `.vscode/mcp.json` (workspace) or global user configuration.

## Supabase prerequisites

The CLI uses two Postgres functions (exposed as Supabase RPC endpoints) to mint and revoke MCP tokens:

- `issue_mcp_agent_token(agent_name text)` – returns a JSON payload containing `token`, `token_id`, `token_prefix`, and metadata.
- `revoke_mcp_agent_token(token_id uuid)` – marks an existing token as inactive.

Ensure these functions run with `security definer` privileges and enforce that `auth.uid()` matches the token `developer_id`.

## Environment variables

The CLI respects the following overrides:

| Variable | Purpose |
| --- | --- |
| `GROUNDING_SUPABASE_URL` | Default Supabase project URL. |
| `GROUNDING_SUPABASE_ANON_KEY` | Public anon key. |
| `GROUNDING_SUPABASE_CLIENT_ID` | Optional Supabase client ID for PKCE refresh. |
| `GROUNDING_SUPABASE_PROVIDER` | Default OAuth provider (e.g. `github`, `google`). |
| `GROUNDING_OAUTH_SCOPES` | Space-delimited scope list for the auth flow. |
| `GROUNDING_REDIRECT_PORT` | Local port for the PKCE callback server. |
| `GROUNDING_MCP_URL` | Hosted MCP endpoint for snippet generation. |

When publishing the CLI to PyPI, remember to include the Node assets via `python -m build` and verify the resulting wheel contains `grounding/server/node/*` files.

## Running the bundled MCP server (optional)

The primary deployment model is to call the hosted MCP endpoint with your issued tokens. For smoke testing or air-gapped environments you can launch the bundled Node server:

```bash
grounding server start --agent my-agent
```

On first run this command installs Node dependencies into a cache directory under `~/.cache/grounding/server`. Provide `--token` to pass a raw token string instead of referencing a stored agent.
