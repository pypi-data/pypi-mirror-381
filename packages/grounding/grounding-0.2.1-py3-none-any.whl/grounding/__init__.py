"""Grounding CLI package."""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("grounding")
except PackageNotFoundError:  # pragma: no cover - not installed
    __version__ = "0.2.0"

# MCP client library (optional - requires 'grounding[mcp]' installation)
try:
    from .mcp_client import (
        GroundingMCP,
        GroundingMCPOpenAIChatCompletions,
        GroundingMCPOpenAIResponses,
        GroundingMCPClaude,
        GroundingMCPGemini,
        GroundingMCPError,
    )
    __all__ = [
        "__version__",
        "GroundingMCP",
        "GroundingMCPOpenAIChatCompletions",
        "GroundingMCPOpenAIResponses",
        "GroundingMCPClaude",
        "GroundingMCPGemini",
        "GroundingMCPError",
    ]
except ImportError:
    # MCP dependencies not installed
    __all__ = ["__version__"]
