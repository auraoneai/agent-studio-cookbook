# Provider Keys

Stores provider keys locally and runs a model compare smoke check.

```bash
agentstudio providers set anthropic --env ANTHROPIC_API_KEY
agentstudio providers set openai --env OPENAI_API_KEY
agentstudio providers set ollama --base-url http://127.0.0.1:11434/v1
agentstudio providers test --all
agentstudio compare ./traces/refund.ast --models anthropic:claude-sonnet,openai:gpt-4.1 --out reports/compare.md
```

Keys are not written to trace cards, telemetry, JUnit exports, or intake packet
previews.
