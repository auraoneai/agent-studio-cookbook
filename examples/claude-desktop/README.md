# Claude Desktop MCP Connection

Use this recipe when a server already works in Claude Desktop and you want the
same server inside Agent Studio Open for manifest inspection, risk scanning, and
replay export.

```bash
agentstudio connect stdio --command npx --arg -y --arg @modelcontextprotocol/server-filesystem --arg ./fixtures --json
agentstudio risk-scan ./server --format json --out reports/claude-desktop-risk.json
```

Desktop is required because Claude Desktop-style local MCP servers usually use
stdio.
