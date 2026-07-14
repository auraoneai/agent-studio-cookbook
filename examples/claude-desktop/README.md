# Claude Desktop MCP Command Mapping

Use this recipe to translate the `command` and `args` from an MCP server entry
you already reviewed in Claude Desktop. Agent Studio does not read or import the
Claude Desktop configuration automatically.

First verify the command shape with a bundled local fixture:

```bash
agentstudio --json connect stdio \
  --command python \
  --arg sample-servers/docs-search/server.py
```

Then map the reviewed third-party command explicitly:

```bash
agentstudio --json connect stdio \
  --command <configured-command> \
  --arg <configured-arg-1> \
  --arg <configured-arg-2>
```

Every `--arg` is passed as a separate process argument. The CLI launches the
specified executable, so review the command, working directory, credentials,
and filesystem permissions before connecting. Local stdio servers require the
CLI or desktop application; the browser application cannot spawn them.

This project is not affiliated with Anthropic or Claude Desktop.
