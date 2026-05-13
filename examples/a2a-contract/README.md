# A2A Contract

Validates an A2A agent card and exports a CI-friendly report.

```bash
agentstudio a2a validate ./fixtures/agent-card.json
agentstudio a2a run ./fixtures/agent-card.json --transcript ./fixtures/task-transcript.json --format junit --out reports/a2a.xml
```

Expected evidence:

- Required card fields pass.
- Capability negotiation is shown in the A2A panel.
- Task lifecycle transitions are validated.
- JUnit XML can be uploaded by CI.
