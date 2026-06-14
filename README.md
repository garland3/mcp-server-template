# my-module

> **Template repo.** This is the team's starting point for new MCP servers.
> Clone it, rename `my_module`, and fill in the blanks below. It already
> satisfies all six MCP repo requirements: layout, pinned Python, this README,
> an `about` prompt, a passing test, and the `.gitignore`.

## 1. What does this do, and when should I use it?

This is a template MCP (Model Context Protocol) server built on
[FastMCP](https://github.com/jlowin/fastmcp). It exposes one example tool,
`hello_world`, which returns a greeting, plus an `about` prompt that tells the
connecting LLM what the server is for. Use it as the skeleton for any new MCP —
replace the example tool with your real computation in `core.py`.

## 2. How do I install it from nothing?

Assumes zero setup. Install [uv](https://docs.astral.sh/uv/) if you don't have
it, then:

```bash
# 1. Install uv (skip if already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Clone the repo
git clone https://github.com/garland3/mcp-server-template.git
cd mcp-server-template

# 3. Install dependencies (creates a .venv automatically)
uv sync --extra dev

# 4. Confirm it works
uv run pytest          # tests should pass
uv run my-module       # starts the MCP server (Ctrl-C to stop)
```

## 3. How do I connect it?

Point your MCP client at the example config in
[`mcp.json`](./mcp.json). Edit the `--directory` path to the absolute path of
this repo on your machine:

```json
{
  "mcpServers": {
    "my-module": {
      "command": "uv",
      "args": ["run", "--directory", "/absolute/path/to/this/repo", "my-module"]
    }
  }
}
```

Drop that into your client's MCP settings (e.g. Claude Desktop's
`claude_desktop_config.json`) and restart the client. The server will offer the
`hello_world` tool and the `about` prompt.

## 4. Screenshot

Replace the image below with a screenshot of *your* MCP working in a client.

![Screenshot of the MCP server working](docs/screenshot.png)

---

## Project layout

```
root
├── pyproject.toml        # dependencies + install (Python >=3.11)
├── mcp.json              # example connection config
├── README.md             # this file
├── .gitignore            # keeps credentials/large data out of the repo
├── src/
│   └── my_module/
│       ├── main.py       # MCP server wiring (FastMCP)
│       ├── core.py       # the actual computation
│       └── About.md      # text served as the `about` MCP prompt
└── tests/
    └── test_core.py      # at least one test that runs
```

Keep computation in `core.py` and MCP wiring in `main.py`. The `about` prompt is
loaded from `About.md`, so you can update what the LLM is told about the server
without touching any code.
