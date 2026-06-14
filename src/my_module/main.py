"""MCP server wiring.

This module exposes the computation in ``core.py`` over the Model Context
Protocol using `FastMCP <https://github.com/jlowin/fastmcp>`_.

Two things to note for the template:

1. ``hello_world`` from ``core.py`` is registered as an MCP **tool** with the
   ``@mcp.tool`` decorator — that's how you turn a plain Python function into
   something an LLM can call.
2. The contents of ``About.md`` are registered as an MCP **prompt** named
   ``about``. This is the custom prompt that tells the connecting LLM what this
   server is for and when to use it. Edit ``About.md`` to describe your server;
   no code change is required.
"""

from pathlib import Path

from fastmcp import FastMCP

from my_module import core

# Path to the About.md file shipped alongside this module.
ABOUT_PATH = Path(__file__).resolve().parent / "About.md"

mcp = FastMCP("my-module")


def _load_about() -> str:
    """Read About.md, falling back to a stub if it is missing."""
    try:
        return ABOUT_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        return "About.md was not found. Add one to describe this MCP server."


@mcp.tool
def hello_world(name: str = "world") -> str:
    """Return a friendly greeting. Example tool — replace with your own."""
    return core.hello_world(name)


@mcp.prompt
def about() -> str:
    """Describe what this MCP server does and when to use it.

    The text comes straight from ``About.md`` so non-developers can update it.
    """
    return _load_about()


def main() -> None:
    """Console-script entry point (see ``[project.scripts]`` in pyproject.toml)."""
    mcp.run()


if __name__ == "__main__":
    main()
