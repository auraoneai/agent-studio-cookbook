# Agent Studio Cookbook

Repo-ready examples for Agent Studio Open. Each example is intentionally small,
local-first, and safe to run with synthetic fixtures.

## Examples

| Example | What it demonstrates |
| --- | --- |
| `examples/mcp-filesystem-risk` | MCP stdio connection, risk scan, replay, and trace card export. |
| `examples/claude-desktop` | Bring a Claude Desktop stdio MCP server into Agent Studio Open. |
| `examples/cursor` | Inspect and replay a Cursor workspace MCP configuration. |
| `examples/cody` | Debug a Cody-compatible remote HTTP MCP server. |
| `examples/a2a-contract` | A2A card validation and JUnit contract-test export. |
| `examples/otel-to-regression` | OTEL / Phoenix import and convert-to-regression flow. |
| `examples/provider-keys` | Provider key setup and model compare smoke check. |
| `examples/ci-export` | GitHub Action, JUnit, and PR comment export. |

## Runnable Sample MCP Servers

Each directory under `sample-servers/` exposes a tiny stdio MCP fixture for
Agent Studio smoke tests:

- `filesystem-risk`
- `crm-refunds`
- `calendar-scheduler`
- `vector-search`
- `sql-readonly`
- `browser-automation`
- `support-tickets`
- `payments-readonly`
- `feature-flags`
- `docs-search`

Run any sample with:

```bash
agentstudio --json connect stdio --command python --arg sample-servers/crm-refunds/server.py
```

## Baseline flow

```bash
agentstudio connect --stdio "npx -y @modelcontextprotocol/server-filesystem ./fixtures"
agentstudio risk-scan ./server --format json --out reports/risk.json
agentstudio record --session filesystem-smoke --tool list_directory --json '{"path":"."}'
agentstudio replay filesystem-smoke.ast --export trace-card --out reports/filesystem-smoke.md
```

Browser edition can use the HTTP/SSE examples but cannot spawn stdio servers or
run the local OTLP receiver.
