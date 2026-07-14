# Remote HTTP MCP Debugging

Use this recipe for a reviewed Cody-compatible or other remote HTTP MCP endpoint.
The cookbook does not bundle a remote server.

```bash
agentstudio --json connect http https://mcp.example.com/mcp
```

The command performs MCP initialization and manifest discovery over the supplied
URL. Add the published CLI's `--header`, `--bearer-token`,
`--oauth-access-token`, or mTLS options only when required by that endpoint.
Avoid placing secrets directly in shell history.

After importing a trace into a local store, render review Markdown:

```bash
agentstudio import-trace <events.jsonl> \
  --format openai \
  --store remote-debug.ast

agentstudio export pr-comment remote-debug.ast \
  --out reports/remote-debug.md
```

`export pr-comment` writes Markdown only; it does not post to GitHub. Remote
connection commands make network requests and share the configured
authentication material with the supplied endpoint.

This project is not affiliated with Sourcegraph or Cody.
