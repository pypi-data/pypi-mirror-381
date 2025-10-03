"""Debug test for keyboard shortcut tools."""

import asyncio
import os
from dotenv import load_dotenv
import sys

sys.path.insert(0, os.path.dirname(__file__))

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

load_dotenv()

async def test_connection():
    """Test basic MCP connection."""
    print("\n" + "=" * 80)
    print("Testing MCP Connection")
    print("=" * 80)

    token = os.getenv("GROUNDING_TOKEN")
    if not token:
        print("❌ GROUNDING_TOKEN not set")
        return

    print(f"✅ Token found: {token[:15]}...")
    url = "http://localhost:3333/mcp"
    print(f"✅ URL: {url}")

    try:
        print("\n🔌 Connecting to MCP server...")
        async with streamablehttp_client(
            url=url,
            headers={"Authorization": f"Bearer {token}"}
        ) as (read, write, _):
            print("✅ HTTP client connected")

            async with ClientSession(read, write) as session:
                print("✅ Client session created")

                print("🔄 Initializing session...")
                init_result = await session.initialize()
                print(f"✅ Session initialized!")
                print(f"📊 Server info: {init_result}")

                # List tools
                print("\n🔧 Listing available tools...")
                tools = await session.list_tools()
                print(f"✅ Found {len(tools.tools)} tools:")
                for tool in tools.tools:
                    print(f"   - {tool.name}: {tool.description}")

                # Test 1: list_keyboard_shortcuts
                print("\n🎯 Test 1: list_keyboard_shortcuts (ChatGPT on Windows)...")
                result = await session.call_tool(
                    "list_keyboard_shortcuts",
                    {
                        "applicationName": "ChatGPT",
                        "os": "Windows",
                        "applicationType": "web_application",
                        "limit": 5
                    }
                )
                print(f"✅ Tool call successful!")
                print(f"📊 Result:\n{result.content[0].text}")

                # Test 2: get_keyboard_shortcut
                print("\n🎯 Test 2: get_keyboard_shortcut ('Open new chat')...")
                result = await session.call_tool(
                    "get_keyboard_shortcut",
                    {
                        "action": "Open new chat",
                        "applicationName": "ChatGPT",
                        "os": "Windows"
                    }
                )
                print(f"✅ Tool call successful!")
                print(f"📊 Result:\n{result.content[0].text}")

                # Test 3: find_keyboard_shortcut
                print("\n🎯 Test 3: find_keyboard_shortcut (search for 'chat')...")
                result = await session.call_tool(
                    "find_keyboard_shortcut",
                    {
                        "applicationName": "ChatGPT",
                        "os": "Windows",
                        "action": "chat",
                        "limit": 5
                    }
                )
                print(f"✅ Tool call successful!")
                print(f"📊 Result:\n{result.content[0].text}")

    except Exception as e:
        print(f"\n❌ Error: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_connection())
