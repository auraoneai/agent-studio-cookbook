# MCP Filesystem Risk

Demonstrates connecting to a local filesystem MCP server, reviewing broad path
permissions, recording a safe list operation, and exporting a trace card.

```bash
agentstudio --json connect stdio --command python --arg ../../sample-servers/filesystem-risk/server.py
agentstudio risk-scan ./server --fail-on high --format json --out reports/risk.json
agentstudio import-trace ../../../agent-studio-open/cli/tests/fixtures/openai_events.jsonl --format openai --store filesystem-smoke.ast
agentstudio export trace-card ../../../agent-trace-card/examples/refund_trace.json --out reports/filesystem-smoke.md
```

Expected evidence:

- Manifest Inspector lists filesystem tools.
- Risk scan flags broad paths if the server is configured too loosely.
- Replay succeeds with mocked output.
- Trace card redacts local absolute paths.
