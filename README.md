# Agent Studio Cookbook

The Agent Studio Cookbook is a source-only collection of synthetic MCP stdio
servers and command recipes for inspecting, recording, replaying, and exporting
agent integration evidence with Agent Studio Open.

## At a Glance

| | |
| --- | --- |
| Job | Provide small integration recipes and local MCP fixtures for agent debugging workflows. |
| Built for | Agent developers, MCP/A2A integrators, eval engineers, and CI owners. |
| Differentiator | Bundled stdio fixtures are synthetic, dependency-free, and safe to inspect without provider credentials. |
| Produces | MCP manifest JSON, risk reports, local trace stores, replay files, and CI export directories through the Agent Studio CLI. |

## Prerequisite

The cookbook itself is not a Python package. Install the current published
Agent Studio CLI:

```bash
python -m pip install "auraone-agent-studio-open==0.1.1"
```

Python 3.11 or newer is required by that package.

## Verified Quickstart

Run from the cookbook repository root:

```bash
agentstudio self-test

agentstudio --json connect stdio \
  --command python \
  --arg sample-servers/crm-refunds/server.py
```

The bundled server starts as a local subprocess and returns an MCP manifest with
two synthetic tools. It does not contact a CRM or issue a refund.

## Recipe Index

| Recipe | Purpose | Bundled input |
| --- | --- | --- |
| [`mcp-filesystem-risk`](examples/mcp-filesystem-risk/README.md) | Connect to and statically scan a deliberately broad filesystem fixture. | Yes |
| [`claude-desktop`](examples/claude-desktop/README.md) | Translate an existing Claude Desktop stdio command into Agent Studio CLI arguments. | Mapping template |
| [`cursor`](examples/cursor/README.md) | Translate a Cursor MCP command and optionally import a user-provided trace export. | Mapping template |
| [`cody`](examples/cody/README.md) | Inspect a user-provided remote HTTP MCP endpoint and export local review Markdown. | Mapping template |
| [`a2a-contract`](examples/a2a-contract/README.md) | Validate a user-provided A2A card and recorded transcript. | No card or transcript |
| [`otel-to-regression`](examples/otel-to-regression/README.md) | Import a user-provided OTLP/Phoenix export into a local trace store and replay file. | No telemetry export |
| [`provider-keys`](examples/provider-keys/README.md) | Verify provider command wiring with a no-network dry run, then opt into live calls. | Dry run only |
| [`ci-export`](examples/ci-export/README.md) | Generate a workflow directory from a user-provided replay suite. | No replay suite |

The recipe READMEs are executable command maps. They do not bundle third-party
application configurations, provider credentials, A2A cards, or production
trace exports.

## Synthetic MCP Servers

Each directory under `sample-servers/` starts the same small MCP stdio protocol
fixture with a different tool inventory:

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

The fixtures return synthetic JSON responses and do not perform the real side
effects implied by their tool names.

## Runtime, Data, and Network Boundary

- Bundled sample servers communicate over local stdio and use Python's standard
  library.
- `agentstudio connect stdio` launches the command supplied by the user. Review
  that executable and its arguments before running it.
- Remote HTTP, SSE, WebSocket, provider, OAuth, and OTLP recipes can make
  network requests when the user supplies an endpoint or removes `--dry-run`.
- Imported traces and generated `.ast`, replay, Markdown, XML, and workflow
  files stay local until the user explicitly uploads, commits, or sends them.
- Recipes do not guarantee that third-party application formats or endpoints
  remain compatible.

## Limitations

- The cookbook is a source repository, not an installable package or hosted
  service.
- Most recipes require a user-supplied third-party configuration, endpoint,
  trace export, or credential before they can exercise a real integration.

## Publication Status

Verified on 2026-07-13:

- Source repository: [`auraoneai/agent-studio-cookbook`](https://github.com/auraoneai/agent-studio-cookbook)
- The cookbook has no PyPI package and no GitHub Release.
- Runnable commands were verified against
  [`auraone-agent-studio-open==0.1.1`](https://pypi.org/project/auraone-agent-studio-open/0.1.1/).
- Bundled servers are tutorial fixtures, not evidence of product adoption or
  third-party endorsement.

## Next Action

Run the CRM fixture quickstart, inspect the returned tool descriptions, then
choose the recipe that matches an integration artifact you already control.
