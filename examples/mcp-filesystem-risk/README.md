# MCP Filesystem Risk

Demonstrates connecting to a local filesystem MCP server, reviewing broad path
permissions, recording a safe list operation, and exporting a trace card.

```bash
agentstudio connect --stdio "npx -y @modelcontextprotocol/server-filesystem ./fixtures" --sandbox --allow-read ./fixtures
agentstudio risk-scan ./server --fail-on high --format json --out reports/risk.json
agentstudio record --session filesystem-smoke --tool list_directory --json '{"path":"."}'
agentstudio export filesystem-smoke.ast --trace-card --out reports/filesystem-smoke.md
```

Expected evidence:

- Manifest Inspector lists filesystem tools.
- Risk scan flags broad paths if the server is configured too loosely.
- Replay succeeds with mocked output.
- Trace card redacts local absolute paths.
