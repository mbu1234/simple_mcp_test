"""MCP server exposing a single tool backed by a mock database."""

import os

from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse
from typing import Annotated

from mcp_test.database import get_user_by_id

mcp = FastMCP("mcp-test")


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> JSONResponse:
    return JSONResponse({"status": "healthy", "service": "mcp-test"})



@mcp.tool
def get_user(
    user_id: Annotated[int, "The numeric ID of the user to look up. Example: 1"]
) -> dict:
    """Look up a user in the mock database by numeric user_id."""
    return get_user_by_id(user_id)


def main() -> None:
    port = int(os.environ.get("PORT", "8080"))
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
