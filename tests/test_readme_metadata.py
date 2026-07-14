from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_readme_discovery_sections():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for section in (
        "## At a Glance",
        "## Prerequisite",
        "## Verified Quickstart",
        "## Runtime, Data, and Network Boundary",
        "## Limitations",
        "## Publication Status",
        "## Next Action",
    ):
        assert section in readme


def test_readme_truthful_release_state():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "The cookbook has no PyPI package and no GitHub Release." in readme
    assert '`auraone-agent-studio-open==0.1.1`' in readme
