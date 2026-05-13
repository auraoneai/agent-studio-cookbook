# OTEL to Regression

Imports OpenTelemetry GenAI spans or Phoenix JSON and converts a failed span to a
tool-call replay artifact.

```bash
agentstudio observe import ./fixtures/phoenix-export.json --format phoenix
agentstudio observe convert --span span_failed_refund --out regressions/refund-retry.json
agentstudio replay regressions/refund-retry.json --format markdown --out reports/refund-retry.md
```

Desktop-only live receiver flow:

```bash
agentstudio observe start --http 4318 --grpc 4317
OTEL_EXPORTER_OTLP_ENDPOINT=http://127.0.0.1:4318 npm test
```

Browser edition supports file import only.
