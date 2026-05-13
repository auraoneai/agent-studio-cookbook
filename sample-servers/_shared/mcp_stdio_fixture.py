from __future__ import annotations

import json
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Tool:
    name: str
    description: str


SERVERS: dict[str, list[Tool]] = {
    "filesystem-risk": [Tool("list_directory", "List files in an allowed workspace."), Tool("read_file", "Read a text file.")],
    "crm-refunds": [Tool("lookup_order", "Look up a customer order."), Tool("refund_order", "Queue a refund workflow.")],
    "calendar-scheduler": [Tool("find_slots", "Find available calendar slots."), Tool("book_meeting", "Book a meeting.")],
    "vector-search": [Tool("semantic_search", "Search a vector index."), Tool("fetch_chunk", "Fetch a source chunk.")],
    "sql-readonly": [Tool("describe_table", "Describe a SQL table."), Tool("select_rows", "Run a read-only SELECT.")],
    "browser-automation": [Tool("open_page", "Open a browser page."), Tool("extract_text", "Extract visible text.")],
    "support-tickets": [Tool("create_ticket", "Create a support ticket."), Tool("update_ticket", "Update ticket state.")],
    "payments-readonly": [Tool("lookup_payment", "Look up a payment."), Tool("list_disputes", "List payment disputes.")],
    "feature-flags": [Tool("get_flag", "Read a feature flag."), Tool("set_flag", "Update a test feature flag.")],
    "docs-search": [Tool("search_docs", "Search documentation."), Tool("open_doc", "Open a documentation page.")],
}


def run_server(name: str) -> None:
    tools = SERVERS[name]
    while True:
        try:
            request = read_message()
        except EOFError:
            break
        method = request.get("method")
        if method == "initialize":
            result = {
                "protocolVersion": "2024-11-05",
                "serverInfo": {"name": f"agent-studio-cookbook-{name}", "version": "0.1.0"},
                "capabilities": {"tools": {}, "resources": {}, "prompts": {}},
            }
        elif method == "tools/list":
            result = {
                "tools": [
                    {
                        "name": tool.name,
                        "description": tool.description,
                        "inputSchema": {"type": "object", "additionalProperties": True},
                    }
                    for tool in tools
                ]
            }
        elif method == "resources/list":
            result = {"resources": [{"uri": f"cookbook://{name}/sample", "name": f"{name} sample resource"}]}
        elif method == "prompts/list":
            result = {"prompts": [{"name": f"{name}_smoke", "description": f"Smoke prompt for {name}"}]}
        else:
            result = {}
        write_message({"jsonrpc": "2.0", "id": request.get("id"), "result": result})


def read_message() -> dict:
    headers = b""
    while b"\r\n\r\n" not in headers:
        chunk = sys.stdin.buffer.read(1)
        if not chunk:
            raise EOFError
        headers += chunk
    length = 0
    for line in headers.decode("ascii", errors="replace").splitlines():
        if line.lower().startswith("content-length:"):
            length = int(line.split(":", 1)[1].strip())
            break
    if length <= 0:
        raise ValueError("missing Content-Length")
    return json.loads(sys.stdin.buffer.read(length).decode("utf-8"))


def write_message(payload: dict) -> None:
    data = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    sys.stdout.buffer.write(b"Content-Length: " + str(len(data)).encode("ascii") + b"\r\n\r\n" + data)
    sys.stdout.buffer.flush()
