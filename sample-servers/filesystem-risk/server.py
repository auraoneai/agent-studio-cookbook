import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from mcp_stdio_fixture import run_server

run_server("filesystem-risk")
