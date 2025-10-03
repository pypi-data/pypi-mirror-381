"""Shared CLI argument wiring for knowledge base utilities.

This module centralizes the definition of common command-line options and
helpers so that multiple entry points (e.g., server and reindex commands) can
remain small and focused while sharing consistent behavior.
"""
from __future__ import annotations

import os
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Optional

from mcp_kb.ingest.chroma import SUPPORTED_CLIENTS, ChromaConfiguration, ChromaIngestor


def parse_bool(value: str | bool | None) -> bool:
    """Return ``True`` when ``value`` represents an affirmative boolean string.

    The function accepts case-insensitive variants such as "true", "t",
    "yes", and "1". ``None`` yields ``False``.
    """

    if isinstance(value, bool):
        return value
    if value is None:
        return False
    return value.lower() in {"1", "true", "t", "yes", "y"}


def add_chroma_arguments(parser: ArgumentParser) -> None:
    """Register Chroma ingestion arguments on ``parser``.

    Environment variables are used as defaults where available so that
    deployments can configure ingestion without repeating flags.
    """

    default_chroma_client = os.getenv("MCP_KB_CHROMA_CLIENT", "persistent").lower()
    default_collection = os.getenv("MCP_KB_CHROMA_COLLECTION", "knowledge-base")
    default_embedding = os.getenv("MCP_KB_CHROMA_EMBEDDING", "default")
    default_data_dir = os.getenv("MCP_KB_CHROMA_DATA_DIR")
    default_host = os.getenv("MCP_KB_CHROMA_HOST")
    default_port_env = os.getenv("MCP_KB_CHROMA_PORT")
    default_port = int(default_port_env) if default_port_env else None
    default_ssl = parse_bool(os.getenv("MCP_KB_CHROMA_SSL", "true"))
    default_tenant = os.getenv("MCP_KB_CHROMA_TENANT")
    default_database = os.getenv("MCP_KB_CHROMA_DATABASE")
    default_api_key = os.getenv("MCP_KB_CHROMA_API_KEY")
    default_custom_auth = os.getenv("MCP_KB_CHROMA_CUSTOM_AUTH")
    default_id_prefix = os.getenv("MCP_KB_CHROMA_ID_PREFIX")

    parser.add_argument(
        "--chroma-client",
        dest="chroma_client",
        choices=SUPPORTED_CLIENTS,
        default=default_chroma_client,
        help="Client implementation for mirroring data to ChromaDB (default: persistent).",
    )
    parser.add_argument(
        "--chroma-collection",
        dest="chroma_collection",
        default=default_collection,
        help="Chroma collection name used to store documents.",
    )
    parser.add_argument(
        "--chroma-embedding",
        dest="chroma_embedding",
        default=default_embedding,
        help="Embedding function name registered with chromadb.utils.embedding_functions.",
    )
    parser.add_argument(
        "--chroma-data-dir",
        dest="chroma_data_dir",
        default=default_data_dir,
        help="Storage directory for the persistent Chroma client.",
    )
    parser.add_argument(
        "--chroma-host",
        dest="chroma_host",
        default=default_host,
        help="Target host for HTTP or cloud Chroma clients.",
    )
    parser.add_argument(
        "--chroma-port",
        dest="chroma_port",
        type=int,
        default=default_port,
        help="Port for the HTTP Chroma client.",
    )
    parser.add_argument(
        "--chroma-ssl",
        dest="chroma_ssl",
        type=parse_bool,
        default=default_ssl,
        help="Toggle SSL for the HTTP Chroma client (default: true).",
    )
    parser.add_argument(
        "--chroma-tenant",
        dest="chroma_tenant",
        default=default_tenant,
        help="Tenant identifier for Chroma Cloud deployments.",
    )
    parser.add_argument(
        "--chroma-database",
        dest="chroma_database",
        default=default_database,
        help="Database name for Chroma Cloud deployments.",
    )
    parser.add_argument(
        "--chroma-api-key",
        dest="chroma_api_key",
        default=default_api_key,
        help="API key used to authenticate against Chroma Cloud.",
    )
    parser.add_argument(
        "--chroma-custom-auth",
        dest="chroma_custom_auth",
        default=default_custom_auth,
        help="Optional custom auth credentials for self-hosted HTTP deployments.",
    )
    parser.add_argument(
        "--chroma-id-prefix",
        dest="chroma_id_prefix",
        default=default_id_prefix,
        help="Prefix applied to document IDs stored in Chroma (default: kb::).",
    )


def build_chroma_listener(options: Namespace, root: Path) -> Optional[ChromaIngestor]:
    """Construct a Chroma listener from parsed CLI options when enabled.

    Returns ``None`` when the configured client type is ``off``.
    """

    configuration = ChromaConfiguration.from_options(
        root=root,
        client_type=options.chroma_client,
        collection_name=options.chroma_collection,
        embedding=options.chroma_embedding,
        data_directory=options.chroma_data_dir,
        host=options.chroma_host,
        port=options.chroma_port,
        ssl=options.chroma_ssl,
        tenant=options.chroma_tenant,
        database=options.chroma_database,
        api_key=options.chroma_api_key,
        custom_auth_credentials=options.chroma_custom_auth,
        id_prefix=options.chroma_id_prefix,
    )
    if not configuration.enabled:
        return None
    return ChromaIngestor(configuration)

