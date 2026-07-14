# Cursor MCP Workspace Mapping

Use this recipe to translate a reviewed Cursor workspace MCP command and,
separately, import a trace export you already possess. Agent Studio does not
discover Cursor configuration files automatically.

Validate the stdio mapping with a bundled fixture:

```bash
agentstudio --json connect stdio \
  --command python \
  --arg sample-servers/feature-flags/server.py
```

For a reviewed workspace server, replace the command and repeat `--arg` for each
argument:

```bash
agentstudio --json connect stdio \
  --command node \
  --arg ./mcp-server.js
```

To import a user-provided normalized event export:

```bash
agentstudio import-trace <cursor-events.jsonl> \
  --format openai \
  --store cursor-debug.ast

agentstudio store search cursor-debug.ast refund
```

The `openai` importer accepts the published CLI's normalized JSONL event subset;
it is not a general Cursor log parser. Imported data remains in the local
SQLite-based `.ast` store until explicitly exported.

This project is not affiliated with Cursor.
