"""Test keyboard shortcut tools using the Grounding MCP client library."""

import asyncio
import os
from dotenv import load_dotenv

# Add parent directory to path to import grounding
import sys
sys.path.insert(0, os.path.dirname(__file__))

from mcp_client import GroundingMCP

# Load environment variables
load_dotenv()

async def test_list_keyboard_shortcuts():
    """Test list_keyboard_shortcuts tool."""
    print("\n" + "=" * 80)
    print("Testing list_keyboard_shortcuts")
    print("=" * 80)

    token = os.getenv("GROUNDING_TOKEN")
    if not token:
        print("❌ GROUNDING_TOKEN not set in environment")
        return

    grounding = GroundingMCP(
        token=token,
        # url="http://localhost:3333/mcp"  # Use this for local testing
        # Default is production: https://api.grounding.dev/mcp
    )

    try:
        async with grounding.connect() as session:
            print("✅ Connected to MCP server")

            # List available tools
            tools = await session.list_tools()
            print(f"\n📦 Available tools: {[t.name for t in tools.tools]}")

            # Call list_keyboard_shortcuts
            print("\n🔧 Calling list_keyboard_shortcuts...")
            result = await session.call_tool(
                "list_keyboard_shortcuts",
                {
                    "applicationName": "Gmail",
                    "os": "macOS",
                    "applicationType": "web_application",
                    "limit": 5
                }
            )

            print(f"\n✅ Result received!")
            print(f"📊 Result:\n{result.content[0].text}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        raise


async def test_get_keyboard_shortcut():
    """Test get_keyboard_shortcut tool."""
    print("\n" + "=" * 80)
    print("Testing get_keyboard_shortcut")
    print("=" * 80)

    token = os.getenv("GROUNDING_TOKEN")
    if not token:
        print("❌ GROUNDING_TOKEN not set in environment")
        return

    grounding = GroundingMCP(
        token=token,
        # url="http://localhost:3333/mcp"  # Use this for local testing
        # Default is production: https://api.grounding.dev/mcp
    )

    try:
        async with grounding.connect() as session:
            print("✅ Connected to MCP server")

            # Call get_keyboard_shortcut
            print("\n🔧 Calling get_keyboard_shortcut...")
            result = await session.call_tool(
                "get_keyboard_shortcut",
                {
                    "action": "Compose new email",
                    "applicationName": "Gmail",
                    "os": "macOS"
                }
            )

            print(f"\n✅ Result received!")
            print(f"📊 Result:\n{result.content[0].text}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        raise


async def test_find_keyboard_shortcut():
    """Test find_keyboard_shortcut tool."""
    print("\n" + "=" * 80)
    print("Testing find_keyboard_shortcut")
    print("=" * 80)

    token = os.getenv("GROUNDING_TOKEN")
    if not token:
        print("❌ GROUNDING_TOKEN not set in environment")
        return

    grounding = GroundingMCP(
        token=token,
        # url="http://localhost:3333/mcp"  # Use this for local testing
        # Default is production: https://api.grounding.dev/mcp
    )

    try:
        async with grounding.connect() as session:
            print("✅ Connected to MCP server")

            # Call find_keyboard_shortcut
            print("\n🔧 Calling find_keyboard_shortcut...")
            result = await session.call_tool(
                "find_keyboard_shortcut",
                {
                    "applicationName": "Gmail",
                    "os": "macOS",
                    "action": "send",
                    "limit": 5
                }
            )

            print(f"\n✅ Result received!")
            print(f"📊 Result:\n{result.content[0].text}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        raise


async def main():
    """Run all tests."""
    print("\n" + "=" * 80)
    print("KEYBOARD SHORTCUT TOOLS TEST SUITE (via Grounding MCP Library)")
    print("=" * 80)

    await test_list_keyboard_shortcuts()
    await test_get_keyboard_shortcut()
    await test_find_keyboard_shortcut()

    print("\n" + "=" * 80)
    print("ALL TESTS COMPLETED")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
