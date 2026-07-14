# OTLP or Phoenix to Regression

This recipe imports a telemetry export you supply into a local Agent Studio
trace store, then writes canonical replay JSON.

```bash
agentstudio import-trace <phoenix-export.json> \
  --format phoenix \
  --store telemetry-debug.ast

agentstudio store dump-replay telemetry-debug.ast \
  --out regressions/telemetry-debug.json
```

Run deterministic assertions after creating a matching assertion file:

```bash
agentstudio replay regressions/telemetry-debug.json \
  --assert regressions/telemetry-debug.assertions.yaml \
  --report reports/telemetry-debug.md
```

To extract eval cases instead of replay JSON:

```bash
agentstudio otel-bridge extract <otlp-or-phoenix.json> \
  --out eval-cases.jsonl
```

The CLI also exposes `agentstudio otlp receive` for an explicitly started local
receiver. File import is the narrower default: it does not open a listening port
or contact an observability backend. Review trace exports for sensitive prompts,
outputs, headers, and identifiers before import.
