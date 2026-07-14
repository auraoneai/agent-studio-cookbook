# A2A Contract

This recipe validates an A2A-style agent card and a recorded task lifecycle
transcript that you supply. The cookbook does not bundle either file.

```bash
agentstudio a2a <agent-card.json> \
  --transcript <contract-transcript.json> \
  --format markdown \
  --out reports/a2a-contract.md
```

The published CLI uses one `a2a` command; it does not expose nested `validate`
or `run` subcommands and does not contact the endpoint declared in the card.
The output contains profile findings and a redacted transcript.

For a dedicated CI gate, use the separately published
`a2a-contract-test` GitHub Action. This profile is not an official A2A
compliance or certification program.
