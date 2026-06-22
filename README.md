# mcp_test

A minimal MCP server with one tool that reads from a mock database.

## Local development

```bash
uv sync
uv run python -m mcp_test.server
```

The server listens on `http://127.0.0.1:8080/mcp` (Streamable HTTP).

## Deploy on Render

Push this repository to GitHub/GitLab/Bitbucket and connect it in the Render dashboard, or apply the `render.yaml` blueprint.
