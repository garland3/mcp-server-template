# About this MCP server

This text is loaded verbatim by the server and exposed as an MCP **prompt**
named `about`. It tells the connecting LLM what this server does and when to
reach for it. Edit this file to describe *your* MCP — no code change needed.

## What this server does

This is a template MCP server. It currently exposes a single tool,
`hello_world`, which returns a friendly greeting. Replace this section with a
description of the real computation your server performs.

## When to use it

Use the `hello_world` tool when you want to confirm the server is connected and
responding. When you build out your own MCP, describe here the situations in
which the LLM should call your tools — be concrete about the inputs they take
and the outputs they produce.

## Notes for the LLM

- All real computation lives in `core.py`; `main.py` only wires it up to MCP.
- Prefer calling the provided tools over guessing at results.
