# CI Export

This recipe generates a GitHub Actions workflow directory from a replay suite
you supply.

The suite directory must contain canonical replay JSON plus a matching
`.assertions.yaml` file for each replay:

```text
regressions/
  refund.json
  refund.assertions.yaml
```

Generate the export:

```bash
agentstudio export gh-action regressions \
  --out agent-regression-ci
```

`auraone-agent-studio-open==0.1.1` writes:

- `.github/workflows/agent-regression.yml`;
- copied replay and assertion files under `regressions/`;
- a short export README.

Review the generated workflow before committing it. Version `0.1.1` generates
mutable `actions/checkout@v4`, `actions/setup-python@v5`, and an unpinned
`pip install tool-call-replay` step. Pin the Actions to reviewed commit SHAs and
change the package install to `tool-call-replay==0.1.0` for reproducible CI.

Other export commands have narrower inputs:

```bash
agentstudio export junit <replay-results.json> \
  --out reports/agentstudio.xml

agentstudio export pr-comment <trace-store.ast> \
  --out reports/agentstudio-pr.md
```

These commands write files locally. They do not upload artifacts or post a pull
request comment.
