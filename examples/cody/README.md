# Cody MCP Debugging Recipe

Use this recipe for Cody-compatible MCP servers where the first debug target is
tool schema conformance and replay stability.

```bash
agentstudio connect http http://127.0.0.1:8787/mcp --json
agentstudio import-trace ./cody-openai-events.jsonl --format openai --store cody-debug.ast
agentstudio export pr-comment cody-debug.ast --out reports/cody-trace-comment.md
```

Remote HTTP/SSE servers can also be exercised from the browser edition. Stdio
servers require the desktop app.
