# MCP Filesystem Risk

This runnable recipe connects to the bundled filesystem-risk stdio fixture and
then statically scans its source.

Run from the cookbook repository root:

```bash
mkdir -p reports

agentstudio --json connect stdio \
  --command python \
  --arg sample-servers/filesystem-risk/server.py

agentstudio risk-scan sample-servers/filesystem-risk \
  --format json \
  --fail-on critical \
  --out reports/filesystem-risk.json
```

The connection returns a synthetic MCP manifest. The scan records lower-severity
review findings but uses `critical` so the tutorial command completes
successfully. Change the threshold to `high` to exercise a failing CI gate.

The fixture does not read or write the filesystem. Its deliberately broad tool
descriptions exist to exercise inspection and risk-review workflows.
