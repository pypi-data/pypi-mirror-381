"""Command line interface for running the MCP knowledge base server."""
from __future__ import annotations

import argparse
import asyncio
import logging
import os
from pathlib import Path
from typing import Iterable, List, Optional

from mcp_kb.config import DOCS_FOLDER_NAME, resolve_knowledge_base_root
from mcp_kb.cli.args import add_chroma_arguments, build_chroma_listener, parse_bool
from mcp_kb.ingest.chroma import ChromaIngestor
from mcp_kb.knowledge.bootstrap import install_default_documentation
from mcp_kb.security.path_validation import PathRules
from mcp_kb.server.app import create_fastmcp_app
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def _build_argument_parser() -> argparse.ArgumentParser:
    """Create and return the argument parser used by ``main``."""

    parser = argparse.ArgumentParser(description="Run the MCP knowledge base server")
    parser.add_argument(
        "--root",
        dest="root",
        default=None,
        help="Optional path to the knowledge base root (defaults to environment configuration)",
    )
    parser.add_argument(
        "--transport",
        dest="transports",
        action="append",
        choices=["stdio", "sse", "http"],
        help="Transport protocol to enable (repeatable). Defaults to stdio only.",
    )
    parser.add_argument(
        "--host",
        dest="host",
        default=None,
        help="Host interface for HTTP/SSE transports (default 127.0.0.1).",
    )
    parser.add_argument(
        "--port",
        dest="port",
        type=int,
        default=None,
        help="Port for HTTP/SSE transports (default 8000).",
    )

    add_chroma_arguments(parser)
    return parser


async def _run_transports(server: FastMCP, transports: List[str]) -> None:
    """Run all selected transport protocols concurrently."""

    coroutines = []
    for name in transports:
        if name == "stdio":
            coroutines.append(server.run_stdio_async())
        elif name == "sse":
            coroutines.append(server.run_sse_async())
        elif name == "http":
            coroutines.append(server.run_streamable_http_async())
        else:  # pragma: no cover - argparse restricts values
            raise ValueError(f"Unsupported transport: {name}")

    await asyncio.gather(*coroutines)


def run_server(arguments: Iterable[str] | None = None) -> None:
    """Entry point used by both CLI invocations and unit tests."""

    parser = _build_argument_parser()
    options = parser.parse_args(arguments)
    root_path = resolve_knowledge_base_root(options.root)
    rules = PathRules(root=root_path, protected_folders=(DOCS_FOLDER_NAME,))
    install_default_documentation(root_path)
    listeners: List[ChromaIngestor] = []
    try:
        listener = build_chroma_listener(options, root_path)
    except Exception as exc:  # pragma: no cover - configuration errors
        raise SystemExit(f"Failed to configure Chroma ingestion: {exc}") from exc
    if listener is not None:
        listeners.append(listener)
        logger.info(
            "Chroma ingestion enabled (client=%s, collection=%s)",
            options.chroma_client,
            options.chroma_collection,
        )
    server = create_fastmcp_app(
        rules,
        host=options.host,
        port=options.port,
        listeners=listeners,
    )
    transports = options.transports or ["stdio"]
    logger.info(f"Running server on {options.host}:{options.port} with transports {transports}")
    logger.info(f"Data root is {root_path}")
    print("--------------------------------",root_path,"--------------------------------")
    asyncio.run(_run_transports(server, transports))


def main() -> None:
    """CLI hook that executes :func:`run_server`."""

    run_server()


if __name__ == "__main__":
    main()
