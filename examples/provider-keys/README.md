# Provider Calls and Keys

The published CLI reads provider credentials from environment variables. It
does not provide a `providers set` credential-store command.

Verify command wiring without a key or network request:

```bash
agentstudio --json model \
  --provider openai \
  --model smoke-model \
  --prompt "Summarize this trace" \
  --dry-run
```

For an intentional live call, set the provider environment variable and remove
`--dry-run`:

```bash
export OPENAI_API_KEY="<redacted>"

agentstudio --json model \
  --provider openai \
  --model <available-model-id> \
  --prompt "Summarize this trace"
```

Supported environment variables in `auraone-agent-studio-open==0.1.1` are
`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, and optional
`OLLAMA_URL`. Live commands send the prompt to the selected provider or Ollama
endpoint. The CLI does not persist keys, but shell history, process
environments, provider logs, and command output remain separate review
boundaries.
