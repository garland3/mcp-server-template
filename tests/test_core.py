"""Tests for the core computation.

At least one real test that passes under ``pytest`` is a hard requirement for
every MCP repo. Keep tests pointed at ``core.py`` so they run fast and need no
MCP runtime.
"""

from my_module.core import hello_world


def test_hello_world_default():
    assert hello_world() == "Hello, world!"


def test_hello_world_with_name():
    assert hello_world("Team") == "Hello, Team!"
