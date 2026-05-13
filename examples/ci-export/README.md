# CI Export

Exports a recorded session as GitHub Actions, JUnit XML, and PR comment
Markdown.

```bash
agentstudio export ./traces/refund.ast --github-action --out .github/workflows/agentstudio.yml
agentstudio export ./traces/refund.ast --junit --out reports/agentstudio.xml
agentstudio export ./traces/refund.ast --pr-comment --out reports/agentstudio-pr.md
```

The generated workflow should call `tool-call-replay` directly. CI does not need
the desktop runtime.
