# Cursor MCP Workspace Connection

Use this recipe when a workspace contains Cursor MCP configuration and you want
Agent Studio Open to inspect the same tool surface.

```bash
agentstudio connect stdio --command node --arg ./mcp-server.js --json
agentstudio import-trace ./cursor-events.jsonl --format openai --store cursor-debug.ast
agentstudio store search cursor-debug.ast refund
```

The VS Code extension companion can deep-link the same workspace connection into
the desktop app with `auraone://agent-studio/open`.
