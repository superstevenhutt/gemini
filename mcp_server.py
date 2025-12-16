
from __future__ import annotations

import logging
from datetime import datetime, timezone
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)  # logs to stderr by default

mcp = FastMCP("Demo MCP Server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers and return the sum."""
    return a + b

@mcp.tool()
def now_utc_iso() -> str:
    """Return the current UTC time as an ISO-8601 string."""
    return datetime.now(timezone.utc).isoformat()

if __name__ == "__main__":
    # stdio transport is what we want for notebook subprocess testing
    mcp.run()
