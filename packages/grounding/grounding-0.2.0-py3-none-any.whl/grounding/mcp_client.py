"""MCP client library for integrating Grounding with LLM SDKs."""

from __future__ import annotations

import asyncio
import json
import re
from typing import Any, Dict, List, Optional, AsyncIterator
from contextlib import asynccontextmanager

try:
    from mcp import ClientSession
    from mcp.client.streamable_http import streamablehttp_client
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False


class GroundingMCPError(Exception):
    """Base exception for Grounding MCP client errors."""
    pass


def _sanitize_openai_name(name: str) -> str:
    """
    Sanitize tool name for OpenAI requirements.

    OpenAI requires: alphanumeric + underscore only, max 64 characters.
    Reference: https://platform.openai.com/docs/guides/function-calling
    """
    safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    return safe_name[:64]


def _sanitize_anthropic_name(name: str) -> str:
    """
    Sanitize tool name for Anthropic requirements.

    Anthropic requires: ^[a-zA-Z0-9_-]{1,64}$
    Reference: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use
    """
    safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    return safe_name[:64]


class GroundingMCP:
    """Base class for Grounding MCP client integration."""

    def __init__(
        self,
        token: str,
        url: str = "https://api.grounding.dev/mcp",
    ):
        """
        Initialize the Grounding MCP client.

        Args:
            token: Your Grounding API token (fg_xxxxx.yyyyy format)
            url: MCP server URL (default: https://api.grounding.dev/mcp)
        """
        if not MCP_AVAILABLE:
            raise GroundingMCPError(
                "MCP SDK not installed. Run: pip install 'grounding[mcp]'"
            )

        self.token = token
        self.url = url
        self._session: Optional[ClientSession] = None

    @asynccontextmanager
    async def connect(self) -> AsyncIterator[ClientSession]:
        """
        Connect to the Grounding MCP server.

        Usage:
            async with grounding.connect() as session:
                tools = await session.list_tools()
        """
        async with streamablehttp_client(
            url=self.url,
            headers={"Authorization": f"Bearer {self.token}"}
        ) as (read, write, _):
            async with ClientSession(read, write) as session:
                await session.initialize()
                yield session

    async def get_tools(self) -> List[Dict[str, Any]]:
        """
        Get all available tools from the Grounding MCP server.

        Returns:
            List of tool definitions in MCP format
        """
        async with self.connect() as session:
            tools_response = await session.list_tools()
            return [
                {
                    "name": tool.name,
                    "description": tool.description,
                    "inputSchema": tool.inputSchema,
                }
                for tool in tools_response.tools
            ]

    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Any:
        """
        Call a tool on the Grounding MCP server.

        Args:
            name: Tool name
            arguments: Tool arguments

        Returns:
            Tool execution result

        Raises:
            GroundingMCPError: If tool execution fails
        """
        try:
            async with self.connect() as session:
                result = await session.call_tool(name, arguments)
                return result
        except Exception as e:
            raise GroundingMCPError(f"Tool execution failed for '{name}': {e}")


class GroundingMCPOpenAIResponses(GroundingMCP):
    """
    Grounding MCP client for OpenAI Responses API integration.

    Supports the new Responses API (client.responses.create()).
    Reference: https://platform.openai.com/docs/guides/function-calling
    """

    def __init__(self, token: str, url: str = "https://api.grounding.dev/mcp"):
        """
        Initialize the Grounding MCP client for OpenAI Responses API.

        Args:
            token: Your Grounding API token
            url: MCP server URL

        Example:
            from openai import OpenAI
            from grounding import GroundingMCPOpenAIResponses

            client = OpenAI()
            grounding = GroundingMCPOpenAIResponses(token="fg_xxxxx.yyyyy")

            async def main():
                # Get tools for Responses API
                tools = await grounding.get_tools_for_responses()

                # Create input list
                input_list = [
                    {"role": "user", "content": "Find Gmail compose button"}
                ]

                # Make initial request
                response = client.responses.create(
                    model="gpt-5",
                    tools=tools,
                    input=input_list
                )

                # Process function calls
                input_list += response.output

                for item in response.output:
                    if item.type == "function_call":
                        result = await grounding.execute_function_call(item)
                        input_list.append(result)

                # Get final response
                response = client.responses.create(
                    model="gpt-5",
                    tools=tools,
                    input=input_list
                )
        """
        super().__init__(token, url)

    def _convert_to_responses_tool(self, mcp_tool: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert MCP tool format to OpenAI Responses API tools format.

        Reference: https://platform.openai.com/docs/guides/function-calling
        """
        return {
            "type": "function",
            "name": _sanitize_openai_name(mcp_tool["name"]),
            "description": mcp_tool["description"],
            "parameters": mcp_tool["inputSchema"],
        }

    async def get_tools_for_responses(self) -> List[Dict[str, Any]]:
        """
        Get tools in OpenAI Responses API format.

        Use this for the 'tools' parameter in client.responses.create().

        Returns:
            List of tools in OpenAI Responses API format

        Reference: https://platform.openai.com/docs/guides/function-calling
        """
        mcp_tools = await self.get_tools()
        return [self._convert_to_responses_tool(tool) for tool in mcp_tools]

    async def execute_function_call(self, function_call: Any) -> Dict[str, Any]:
        """
        Execute an OpenAI Responses API function call via the Grounding MCP server.

        Args:
            function_call: Function call object from response.output (type == "function_call")

        Returns:
            Function call output in Responses API format with:
            - type: "function_call_output"
            - call_id: The call_id from the function call
            - output: The stringified result

        Raises:
            GroundingMCPError: If arguments are malformed or tool execution fails

        Reference: https://platform.openai.com/docs/guides/function-calling
        """
        # Parse arguments - Responses API provides JSON string in arguments field
        try:
            if isinstance(function_call.arguments, str):
                arguments = json.loads(function_call.arguments)
            else:
                arguments = function_call.arguments
        except json.JSONDecodeError as e:
            raise GroundingMCPError(
                f"Invalid JSON in function call arguments for '{function_call.name}': {e}"
            )

        # Execute the tool via MCP
        result = await self.call_tool(function_call.name, arguments)

        # Serialize result content properly
        content = result
        if hasattr(result, 'content'):
            content = result.content

        # Ensure output is a string (as per Responses API spec)
        if not isinstance(content, str):
            output = json.dumps(content)
        else:
            output = content

        # Return in Responses API format
        return {
            "type": "function_call_output",
            "call_id": function_call.call_id,
            "output": output,
        }

    async def execute_function_calls(self, function_calls: List[Any]) -> List[Dict[str, Any]]:
        """
        Execute multiple OpenAI Responses API function calls.

        Args:
            function_calls: List of function call objects from response.output

        Returns:
            List of function call outputs in Responses API format
        """
        return await asyncio.gather(*[
            self.execute_function_call(fc) for fc in function_calls
        ])


class GroundingMCPOpenAIChatCompletions(GroundingMCP):
    """
    Grounding MCP client for OpenAI Chat Completions API integration.

    Supports the Chat Completions API (client.chat.completions.create()).
    Reference: https://platform.openai.com/docs/api-reference/chat/create
    """

    def __init__(self, token: str, url: str = "https://api.grounding.dev/mcp"):
        """
        Initialize the Grounding MCP client for OpenAI Chat Completions API.

        Args:
            token: Your Grounding API token
            url: MCP server URL

        Example:
            from openai import OpenAI
            from grounding import GroundingMCPOpenAIChatCompletions

            client = OpenAI()
            grounding = GroundingMCPOpenAIChatCompletions(token="fg_xxxxx.yyyyy")

            async def main():
                # Get tools for Chat Completions API
                tools = await grounding.get_tools_for_chat()

                # Create messages
                messages = [
                    {"role": "user", "content": "Find Gmail compose button"}
                ]

                # Make initial request
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    tools=tools
                )

                # Process tool calls
                message = response.choices[0].message
                if message.tool_calls:
                    messages.append(message)

                    for tool_call in message.tool_calls:
                        result = await grounding.execute_tool_call(tool_call)
                        messages.append(result)

                    # Get final response
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=messages,
                        tools=tools
                    )
        """
        super().__init__(token, url)

    def _convert_to_chat_tool(self, mcp_tool: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert MCP tool format to OpenAI Chat Completions API tools format.

        Reference: https://platform.openai.com/docs/api-reference/chat/create
        """
        return {
            "type": "function",
            "function": {
                "name": _sanitize_openai_name(mcp_tool["name"]),
                "description": mcp_tool["description"],
                "parameters": mcp_tool["inputSchema"],
            }
        }

    def _convert_to_chat_function(self, mcp_tool: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert MCP tool format to OpenAI legacy functions format.

        For use with the deprecated 'functions' parameter in Chat Completions API.
        """
        return {
            "name": _sanitize_openai_name(mcp_tool["name"]),
            "description": mcp_tool["description"],
            "parameters": mcp_tool["inputSchema"],
        }

    async def get_tools_for_chat(self) -> List[Dict[str, Any]]:
        """
        Get tools in OpenAI Chat Completions API format.

        Use this for the 'tools' parameter in client.chat.completions.create().

        Returns:
            List of tools in OpenAI Chat Completions format

        Reference: https://platform.openai.com/docs/api-reference/chat/create
        """
        mcp_tools = await self.get_tools()
        return [self._convert_to_chat_tool(tool) for tool in mcp_tools]

    async def get_functions_for_chat(self) -> List[Dict[str, Any]]:
        """
        Get tools in OpenAI legacy functions format (deprecated).

        Use this for older code using the 'functions' parameter in Chat Completions API.

        Returns:
            List of functions in legacy OpenAI format

        Reference: https://platform.openai.com/docs/api-reference/chat/create
        """
        mcp_tools = await self.get_tools()
        return [self._convert_to_chat_function(tool) for tool in mcp_tools]

    async def execute_tool_call(self, tool_call: Any) -> Dict[str, Any]:
        """
        Execute an OpenAI Chat Completions API tool call via the Grounding MCP server.

        Args:
            tool_call: Tool call object from response.choices[0].message.tool_calls

        Returns:
            Tool message in Chat Completions API format with:
            - tool_call_id: The id from the tool call
            - role: "tool"
            - name: The function name
            - content: The stringified result

        Raises:
            GroundingMCPError: If arguments are malformed or tool execution fails

        Reference: https://platform.openai.com/docs/api-reference/chat/create
        """
        # Parse arguments - Chat Completions API provides JSON string in function.arguments
        try:
            if isinstance(tool_call.function.arguments, str):
                arguments = json.loads(tool_call.function.arguments)
            else:
                arguments = tool_call.function.arguments
        except json.JSONDecodeError as e:
            raise GroundingMCPError(
                f"Invalid JSON in tool call arguments for '{tool_call.function.name}': {e}"
            )

        # Execute the tool via MCP
        result = await self.call_tool(tool_call.function.name, arguments)

        # Serialize result content properly
        # MCP SDK returns CallToolResult with content array of TextContent objects
        if hasattr(result, 'content') and result.content:
            # Extract text from TextContent objects
            content_parts = []
            for item in result.content:
                if hasattr(item, 'text'):
                    content_parts.append(item.text)
                elif hasattr(item, 'type') and item.type == 'text' and hasattr(item, 'text'):
                    content_parts.append(item.text)
                elif isinstance(item, dict) and 'text' in item:
                    content_parts.append(item['text'])
            content = '\n'.join(content_parts) if content_parts else str(result.content)
        else:
            content = str(result)

        # Return in Chat Completions API format
        return {
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": tool_call.function.name,
            "content": content,
        }

    async def execute_tool_calls(self, tool_calls: List[Any]) -> List[Dict[str, Any]]:
        """
        Execute multiple OpenAI Chat Completions API tool calls.

        Args:
            tool_calls: List of tool call objects from response.choices[0].message.tool_calls

        Returns:
            List of tool messages in Chat Completions API format
        """
        return await asyncio.gather(*[
            self.execute_tool_call(tc) for tc in tool_calls
        ])


class GroundingMCPClaude(GroundingMCP):
    """
    Grounding MCP client for Anthropic Claude SDK integration.

    Supports Claude Messages API with tool use.
    Reference: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use
    """

    def __init__(self, token: str, url: str = "https://api.grounding.dev/mcp"):
        """
        Initialize the Grounding MCP client for Claude.

        Args:
            token: Your Grounding API token
            url: MCP server URL

        Example:
            from anthropic import Anthropic
            from grounding import GroundingMCPClaude

            client = Anthropic()
            grounding = GroundingMCPClaude(token="fg_xxxxx.yyyyy")

            async def main():
                tools = await grounding.get_claude_tools()
                response = client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    messages=[{"role": "user", "content": "Find Gmail compose"}],
                    tools=tools
                )
        """
        super().__init__(token, url)

    def _convert_to_claude_tool(self, mcp_tool: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert MCP tool format to Claude tool format.

        Anthropic requires tool names to match ^[a-zA-Z0-9_-]{1,64}$
        Reference: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use
        """
        return {
            "name": _sanitize_anthropic_name(mcp_tool["name"]),
            "description": mcp_tool["description"],
            "input_schema": mcp_tool["inputSchema"],
        }

    async def get_claude_tools(self) -> List[Dict[str, Any]]:
        """
        Get tools in Claude Messages API format.

        Returns:
            List of tools in Claude format

        Reference: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use
        """
        mcp_tools = await self.get_tools()
        return [self._convert_to_claude_tool(tool) for tool in mcp_tools]

    async def execute_tool_use(self, tool_use: Any) -> Dict[str, Any]:
        """
        Execute a Claude tool use via the Grounding MCP server.

        Args:
            tool_use: Claude tool use object from response.content blocks

        Returns:
            Tool execution result for Claude (tool_result block) with:
            - type: "tool_result"
            - tool_use_id: The id from the tool_use block
            - content: String or array of content blocks (text, image, document)
            - is_error: Optional boolean, true if execution failed

        Raises:
            GroundingMCPError: If tool execution fails

        Reference: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use
        """
        is_error = False

        try:
            # Execute the tool via MCP
            result = await self.call_tool(tool_use.name, tool_use.input)
        except Exception as e:
            # If tool execution fails, return error in tool_result
            return {
                "type": "tool_result",
                "tool_use_id": tool_use.id,
                "content": f"Error executing tool '{tool_use.name}': {str(e)}",
                "is_error": True,
            }

        # Serialize result content properly
        content = result
        if hasattr(result, 'content'):
            content = result.content

        # Claude supports multiple content formats:
        # 1. String: "content": "15 degrees"
        # 2. Array: "content": [{"type": "text", "text": "15 degrees"}]
        # 3. Mixed: "content": [{"type": "text", ...}, {"type": "image", ...}]

        # If content is already a list (array of content blocks), use as-is
        if isinstance(content, list):
            # Verify it's a valid content block array
            for block in content:
                if not isinstance(block, dict) or 'type' not in block:
                    # Invalid format, convert entire list to JSON string
                    content = json.dumps(content)
                    break
        # If content is a dict, check if it's a single content block
        elif isinstance(content, dict) and 'type' in content:
            # Single content block, wrap in array
            content = [content]
        # Otherwise, ensure it's a string
        elif not isinstance(content, str):
            content = json.dumps(content)

        tool_result = {
            "type": "tool_result",
            "tool_use_id": tool_use.id,
            "content": content,
        }

        # Only include is_error if it's true (optional field)
        if is_error:
            tool_result["is_error"] = True

        return tool_result

    async def execute_tool_uses(self, tool_uses: List[Any]) -> List[Dict[str, Any]]:
        """
        Execute multiple Claude tool uses.

        Args:
            tool_uses: List of tool use objects

        Returns:
            List of tool execution results
        """
        return await asyncio.gather(*[
            self.execute_tool_use(tu) for tu in tool_uses
        ])


class GroundingMCPGemini(GroundingMCP):
    """
    Grounding MCP client for Google Gen AI SDK (google-genai) integration.

    Supports Gemini's native function calling with proper multi-turn conversation flow.

    IMPORTANT: This class is designed for the NEW Google Gen AI SDK (google-genai),
    NOT the deprecated google-generativeai SDK. Use:
        - pip install google-genai
        - from google import genai

    Reference: https://ai.google.dev/gemini-api/docs/function-calling
    """

    def __init__(self, token: str, url: str = "https://api.grounding.dev/mcp"):
        """
        Initialize the Grounding MCP client for Gemini.

        Requires the NEW Google Gen AI SDK (google-genai):
            pip install google-genai

        Args:
            token: Your Grounding API token (fg_xxxxx.yyyyy format)
            url: MCP server URL (default: https://api.grounding.dev/mcp)

        Example:
            from grounding import GroundingMCPGemini

            grounding = GroundingMCPGemini(token="fg_xxxxx.yyyyy")
            tools = await grounding.get_gemini_tools()

        For complete examples with multi-turn conversations and function calling,
        see: docs/SDK_INTEGRATION.md
        """
        super().__init__(token, url)

    def _convert_to_gemini_tool(self, mcp_tool: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert MCP tool format to Gemini function declaration format.

        Reference: https://ai.google.dev/gemini-api/docs/function-calling
        """
        # Gemini uses function declarations with JSON Schema parameters
        return {
            "name": _sanitize_openai_name(mcp_tool["name"]),  # Use OpenAI sanitization (similar rules)
            "description": mcp_tool["description"],
            "parameters": mcp_tool["inputSchema"],
        }

    async def get_gemini_tools(self) -> List[Dict[str, Any]]:
        """
        Get tools in Gemini format, wrapped in Tool objects.

        Returns:
            List of Tool objects with function_declarations for Gemini.
            Use this for the 'tools' parameter in GenerateContentConfig.

        Example:
            tools = await grounding.get_gemini_tools()
            config = types.GenerateContentConfig(tools=tools)

        Reference: https://ai.google.dev/gemini-api/docs/function-calling
        """
        mcp_tools = await self.get_tools()
        function_declarations = [self._convert_to_gemini_tool(tool) for tool in mcp_tools]

        # Wrap function declarations in Tool object as per Gemini spec
        # Reference: lines 40-42 of gemini-sdk-tool-call-docs.md
        return [{"function_declarations": function_declarations}]

    async def execute_function_call(self, function_call: Any) -> Dict[str, Any]:
        """
        Execute a Gemini function call via the Grounding MCP server.

        This method executes the function and returns a Content object with the
        function response wrapped in the format expected by Gemini.

        Args:
            function_call: Gemini function call object from
                          response.candidates[0].content.parts[0].function_call

        Returns:
            A Content object (dict) with role="user" containing the function response.
            This should be appended to your contents list for the next model call.

        Raises:
            GroundingMCPError: If tool execution fails

        Example:
            function_call = response.candidates[0].content.parts[0].function_call
            if function_call:
                # Append model's response
                contents.append(response.candidates[0].content)

                # Execute function and append response
                function_response = await grounding.execute_function_call(function_call)
                contents.append(function_response)

                # Call model again with updated conversation
                response = client.models.generate_content(...)

        Reference: https://ai.google.dev/gemini-api/docs/function-calling
                   See lines 163-171 of gemini-sdk-tool-call-docs.md
        """
        # Extract arguments from function_call.args
        # Reference: lines 53-56 of gemini-sdk-tool-call-docs.md
        try:
            if hasattr(function_call, 'args'):
                arguments = dict(function_call.args)
            elif isinstance(function_call, dict):
                arguments = function_call.get('args', {})
            else:
                arguments = {}
        except (TypeError, AttributeError) as e:
            raise GroundingMCPError(
                f"Invalid function call structure for '{getattr(function_call, 'name', 'unknown')}': {e}"
            )

        # Execute the tool via MCP
        result = await self.call_tool(function_call.name, arguments)

        # Serialize result content properly
        content = result
        if hasattr(result, 'content'):
            content = result.content

        # Ensure content is JSON-serializable
        if not isinstance(content, (str, int, float, bool, list, dict, type(None))):
            content = str(content)

        # Wrap response in a dict as per Gemini spec
        # Reference: line 166 of gemini-sdk-tool-call-docs.md
        # response={"result": result}
        response_data = {"result": content}

        # Return in Gemini's expected format using Part.from_function_response pattern
        # Reference: lines 164-171 of gemini-sdk-tool-call-docs.md
        # Note: We return the dict structure that matches types.Part.from_function_response()
        # wrapped in types.Content with role="user"
        return {
            "role": "user",
            "parts": [
                {
                    "function_response": {
                        "name": function_call.name,
                        "response": response_data,
                    }
                }
            ]
        }

    async def execute_function_calls(self, function_calls: List[Any]) -> List[Dict[str, Any]]:
        """
        Execute multiple Gemini function calls (parallel function calling).

        This is used when Gemini requests multiple independent function calls
        in a single response.

        Args:
            function_calls: List of function call objects from response parts

        Returns:
            List of Content objects with function responses. Append all of these
            to your contents list for the next model call.

        Example:
            # Extract all function calls from response
            function_calls = [
                part.function_call
                for part in response.candidates[0].content.parts
                if hasattr(part, 'function_call')
            ]

            if function_calls:
                # Append model's response
                contents.append(response.candidates[0].content)

                # Execute all functions in parallel
                responses = await grounding.execute_function_calls(function_calls)
                contents.extend(responses)

                # Call model again
                response = client.models.generate_content(...)

        Reference: https://ai.google.dev/gemini-api/docs/function-calling
                   See lines 228-312 for parallel function calling
        """
        return await asyncio.gather(*[
            self.execute_function_call(fc) for fc in function_calls
        ])

    @staticmethod
    def get_function_calls_from_response(response: Any) -> List[Any]:
        """
        Extract function calls from a Gemini response.

        Helper method to get all function_call objects from a response.
        Useful for handling both single and parallel function calling.

        Args:
            response: Gemini API response object

        Returns:
            List of function_call objects (may be empty if no functions called)

        Example:
            response = client.models.generate_content(...)
            function_calls = grounding.get_function_calls_from_response(response)

            if function_calls:
                # Process function calls
                contents.append(response.candidates[0].content)
                responses = await grounding.execute_function_calls(function_calls)
                contents.extend(responses)

        Reference: https://ai.google.dev/gemini-api/docs/function-calling
                   See lines 53-56 for accessing function calls
        """
        try:
            parts = response.candidates[0].content.parts
            return [
                part.function_call
                for part in parts
                if hasattr(part, 'function_call') and part.function_call
            ]
        except (AttributeError, IndexError):
            return []


__all__ = [
    "GroundingMCP",
    "GroundingMCPOpenAIChatCompletions",
    "GroundingMCPOpenAIResponses",
    "GroundingMCPClaude",
    "GroundingMCPGemini",
    "GroundingMCPError",
]