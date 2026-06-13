"""Core computation for the MCP server.

Keep the *actual work* in this file, free of any MCP wiring. That makes it easy
to unit-test (see ``tests/test_core.py``) and to reuse from other code. The MCP
server in ``main.py`` simply imports these functions and exposes them as tools.
"""


def hello_world(name: str = "world") -> str:
    """Return a friendly greeting.

    This is the template's example computation. Replace it with your own.

    Args:
        name: Who to greet. Defaults to ``"world"``.

    Returns:
        A greeting string, e.g. ``"Hello, world!"``.
    """
    return f"Hello, {name}!"
