"""Integration layer that mirrors knowledge base updates into ChromaDB."""
from __future__ import annotations

import importlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Set, Tuple, Type, TYPE_CHECKING
from langchain_text_splitters import TokenTextSplitter

from mcp_kb.knowledge.events import (
    FileDeleteEvent,
    FileUpsertEvent,
    KnowledgeBaseListener,
    KnowledgeBaseReindexListener,
)
from mcp_kb.knowledge.search import SearchMatch

if TYPE_CHECKING:  # pragma: no cover - type checking only imports
    from chromadb.api import ClientAPI, GetResult
    from chromadb.api.models.Collection import Collection
    from mcp_kb.knowledge.store import KnowledgeBase

SUPPORTED_CLIENTS: Tuple[str, ...] = ("off", "ephemeral", "persistent", "http", "cloud")
"""Recognised client types exposed to operators enabling Chroma ingestion."""

@dataclass(frozen=True)
class ChromaConfiguration:
    """Runtime configuration controlling how Chroma ingestion behaves.

    Each attribute corresponds to either a CLI flag or an environment variable
    so that deployments can toggle Chroma synchronisation without changing the
    application code. The configuration intentionally stores already-normalised
    values (e.g., resolved paths and lowercase enums) so downstream components
    can rely on consistent semantics regardless of where the data originated.
    """

    client_type: str
    collection_name: str
    embedding: str
    data_directory: Optional[Path]
    host: Optional[str]
    port: Optional[int]
    ssl: bool
    tenant: Optional[str]
    database: Optional[str]
    api_key: Optional[str]
    custom_auth_credentials: Optional[str]
    id_prefix: str

    @property
    def enabled(self) -> bool:
        """Return ``True`` when ingestion should be activated."""

        return self.client_type != "off"

    @classmethod
    def from_options(
        cls,
        *,
        root: Path,
        client_type: str,
        collection_name: str,
        embedding: str,
        data_directory: Optional[str],
        host: Optional[str],
        port: Optional[int],
        ssl: bool,
        tenant: Optional[str],
        database: Optional[str],
        api_key: Optional[str],
        custom_auth_credentials: Optional[str],
        id_prefix: Optional[str],
    ) -> "ChromaConfiguration":
        """Normalise CLI and environment inputs into a configuration object.

        Parameters
        ----------
        root:
            Absolute knowledge base root used to derive default directories.
        client_type:
            One of :data:`SUPPORTED_CLIENTS`. ``"off"`` disables ingestion.
        collection_name:
            Target Chroma collection that will store knowledge base documents.
        embedding:
            Name of the embedding function to instantiate. Values are matched
            case-insensitively to the functions exported by Chroma.
        data_directory:
            Optional directory for the persistent client. When omitted and the
            client type is ``"persistent"`` the function creates a ``chroma``
            sub-directory next to the knowledge base.
        host / port / ssl / tenant / database / api_key / custom_auth_credentials:
            Transport-specific settings passed directly to the Chroma client
            constructors.
        id_prefix:
            Optional prefix prepended to every document ID stored in Chroma.
            Defaults to ``"kb::"`` for readability.
        """

        normalized_type = (client_type or "off").lower()
        if normalized_type not in SUPPORTED_CLIENTS:
            raise ValueError(f"Unsupported Chroma client type: {client_type}")

        resolved_directory: Optional[Path]
        if data_directory:
            resolved_directory = Path(data_directory).expanduser().resolve()
        elif normalized_type == "persistent":
            resolved_directory = (root / "chroma").resolve()
        else:
            resolved_directory = None

        if resolved_directory is not None:
            resolved_directory.mkdir(parents=True, exist_ok=True)

        prefix = id_prefix or "kb::"

        normalized_embedding = (embedding or "default").lower()

        config = cls(
            client_type=normalized_type,
            collection_name=collection_name,
            embedding=normalized_embedding,
            data_directory=resolved_directory,
            host=host,
            port=port,
            ssl=ssl,
            tenant=tenant,
            database=database,
            api_key=api_key,
            custom_auth_credentials=custom_auth_credentials,
            id_prefix=prefix,
        )
        config._validate()
        return config

    def _validate(self) -> None:
        """Validate the configuration and raise descriptive errors when invalid."""

        if not self.enabled:
            return

        if self.client_type == "persistent" and self.data_directory is None:
            raise ValueError("Persistent Chroma client requires a data directory")

        if self.client_type == "http" and not self.host:
            raise ValueError("HTTP Chroma client requires --chroma-host or MCP_KB_CHROMA_HOST")

        if self.client_type == "cloud":
            missing = [
                name
                for name, value in (
                    ("tenant", self.tenant),
                    ("database", self.database),
                    ("api_key", self.api_key),
                )
                if not value
            ]
            if missing:
                pretty = ", ".join(missing)
                raise ValueError(f"Cloud Chroma client requires values for: {pretty}")

        if not self.collection_name:
            raise ValueError("Collection name must be provided")

        if not self.embedding:
            raise ValueError("Embedding function name must be provided")


@dataclass(frozen=True)
class _ChromaDependencies:
    """Lazy import bundle containing the pieces needed to talk to ChromaDB."""

    chroma_module: Any
    settings_cls: Type[Any]
    embedding_factories: Mapping[str, Type[Any]]


def _load_dependencies() -> _ChromaDependencies:
    """Import ChromaDB lazily so the base server works without the dependency."""

    try:
        chroma_module = importlib.import_module("chromadb")
    except ModuleNotFoundError as exc:  # pragma: no cover - dependent on environment
        raise RuntimeError(
            "Chroma integration requested but the 'chromadb' package is not installed. "
            "Install chromadb via 'uv add chromadb' or disable ingestion."
        ) from exc

    config_module = importlib.import_module("chromadb.config")
    embedding_module = importlib.import_module("chromadb.utils.embedding_functions")

    factories: Dict[str, Type[Any]] = {}
    fallback_map = {
        "default": "DefaultEmbeddingFunction",
        "cohere": "CohereEmbeddingFunction",
        "openai": "OpenAIEmbeddingFunction",
        "jina": "JinaEmbeddingFunction",
        "voyageai": "VoyageAIEmbeddingFunction",
        "roboflow": "RoboflowEmbeddingFunction",
    }
    for alias, attr in fallback_map.items():
        if hasattr(embedding_module, attr):
            factories[alias] = getattr(embedding_module, attr)
    if not factories:
        raise RuntimeError("No embedding functions were found in chromadb.utils.embedding_functions")

    return _ChromaDependencies(
        chroma_module=chroma_module,
        settings_cls=getattr(config_module, "Settings"),
        embedding_factories=factories,
    )


class ChromaIngestor(KnowledgeBaseListener, KnowledgeBaseReindexListener):
    """Listener that mirrors knowledge base writes into a Chroma collection.

    The listener adheres to the :class:`KnowledgeBaseListener` protocol so it
    can be registered alongside other observers without coupling. Events are
    written synchronously to guarantee that indexing stays consistent with the
    underlying filesystem operations.
    """

    def __init__(self, configuration: ChromaConfiguration) -> None:
        """Create an ingestor bound to ``configuration``.

        Parameters
        ----------
        configuration:
            Sanitised :class:`ChromaConfiguration` describing how to connect to
            Chroma and which collection to mirror.
        """

        self.configuration = configuration
        self._deps = _load_dependencies()
        self._client = self._create_client()
        self._collection = self._ensure_collection()
        self.textsplitter = TokenTextSplitter(
            chunk_size=200,
            chunk_overlap=20,
            add_start_index=True
        )

    def get_document_chunks(self, document_id: str, include: List[str] = ["metadatas", "documents"]) -> GetResult:
        """Get a document from the Chroma index."""
        return self._collection.get(where={"document_id": document_id},include=include)

    def handle_upsert(self, event: FileUpsertEvent) -> None:
        """Upsert ``event`` into the configured Chroma collection.

        Every invocation removes any existing Chroma entry before inserting the
        fresh payload so that the embedding engine recomputes vectors using the
        latest markdown. The stored metadata keeps both absolute and relative
        paths, enabling downstream semantic search tools to surface references
        that point straight back into the knowledge base.
        """

        document_id = f"{self.configuration.id_prefix}{event.relative_path}"
        metadata = {
            "relative_path": event.relative_path,
        }
        self._reindex_document(document_id, event.content, metadata)

    def delete_document(self, document_id: str) -> None:
        """Delete a document from the Chroma index."""
        self._collection.delete(ids=self.get_document_chunks(document_id,include=[])["ids"])

    def handle_delete(self, event: FileDeleteEvent) -> None:
        """Remove documents associated with ``event`` from the Chroma index.

        Soft deletions translate to a straight removal because the PRD treats
        files carrying the delete sentinel as hidden from client tooling.
        """

        document_id = f"{self.configuration.id_prefix}{event.relative_path}"
        try:
            self.delete_document(document_id)
        except Exception:  # pragma: no cover - depends on Chroma exceptions
            # Chroma raises a custom error when the ID is missing. Deletion should
            # be idempotent so we swallow those errors silently.
            pass

    @property
    def collection(self) -> "Collection":
        """Return the underlying Chroma collection for diagnostics and tests."""

        return self._collection

    def query(self, query: str, *, n_results: int = 5) -> List[Dict[str, Any]]:
        """Return structured query results from the configured collection.

        Parameters
        ----------
        query:
            Natural language string used to compute the semantic embedding.
        n_results:
            Maximum number of results to return. Defaults to five to mirror the
            behaviour surfaced through the MCP search tool.

        Returns
        -------
        list[dict[str, Any]]
            Each dictionary contains the ``document`` text, associated
            ``metadata`` payload, and a floating-point ``distance`` score if
            provided by Chroma.
        """

        payload = self._collection.query(
            query_texts=[query],
            n_results=n_results,
            include=["metadatas", "documents", "distances"],
        )

        documents = payload.get("documents", [[]])
        metadatas = payload.get("metadatas", [[]])
        distances = payload.get("distances", [[]])

        if not documents or not documents[0]:
            return []

        results: List[Dict[str, Any]] = []
        for index, metadata in enumerate(metadatas[0]):
            document = documents[0][index] if index < len(documents[0]) else ""
            distance = distances[0][index] if distances and distances[0] else None
            results.append(
                {
                    "metadata": metadata or {},
                    "document": document,
                    "distance": distance,
                }
            )

        return results

    # Optional search extension -------------------------------------------------

    def search(
        self,
        kb: "KnowledgeBase",
        query: str,
        *,
        context_lines: int = 2,
        limit: Optional[int] = None,
    ) -> List[SearchMatch]:
        """Translate semantic query results into :class:`SearchMatch` objects."""

        max_results = limit or 5
        records = self.query(query, n_results=max_results)
        matches: List[SearchMatch] = []
        seen_paths: Set[Path] = set()

        for record in records:
            metadata = record.get("metadata") or {}
            candidate = self._resolve_candidate_path(
                kb,
                metadata.get("relative_path"),
            )
            if candidate is None or candidate in seen_paths:
                continue

            seen_paths.add(candidate)
            try:
                text = candidate.read_text(encoding="utf-8")
            except FileNotFoundError:
                continue

            lines = text.splitlines()
            file_matches = self._extract_matches_from_lines(candidate, lines, query, context_lines)
            if file_matches:
                matches.append(file_matches[0])
            elif lines:
                preview_limit = min(len(lines), context_lines * 2 + 1)
                matches.append(
                    SearchMatch(
                        path=candidate,
                        line_number=1,
                        context=lines[:preview_limit],
                    )
                )

            if limit is not None and len(matches) >= limit:
                break

        return matches

    # Internal helpers ----------------------------------------------------------

    def _reindex_document(
        self,
        document_id: str,
        content: str,
        metadata: Mapping[str, Any],
    ) -> None:
        """Replace the stored document so embeddings are recomputed.

        Reindexing involves removing any stale record before inserting the new
        payload. Some Chroma backends keep historical data around when ``add``
        is invoked with an existing ID, so the deletion step ensures the stored
        embedding always reflects the latest markdown contents. ``metadata`` is
        copied to break accidental references held by callers.
        """

        try:
            # filter by document_id in metadata
            self.delete_document(document_id)
        except Exception:  # pragma: no cover - depends on Chroma exception types
            # Missing IDs are not an error; most clients raise when attempting to
            # delete a non-existent record. We swallow those errors to keep the
            # reindexing path idempotent.
            pass

        payload_metadata = dict(metadata)
        payload_metadata['document_id'] = document_id

        # splitting

        split_docs = self.textsplitter.create_documents([content])
        
        for i, d in enumerate(split_docs):
            d.metadata.update(payload_metadata)
            d.metadata['chunk_number'] = i
            d.metadata['startline'] = len(content[:d.metadata['start_index']].splitlines())
            d.metadata['endline'] =  d.metadata['startline']  + len(d.page_content.splitlines())-1

        self._collection.add(
            documents=[d.page_content for d in split_docs],
            metadatas=[d.metadata for d in split_docs],
            ids=[f"{d.metadata['document_id']}-{d.metadata['chunk_number']}" for d in split_docs],
        )

    # Optional full reindex -----------------------------------------------------

    def reindex(self, kb: "KnowledgeBase") -> int:
        """Rebuild the Chroma index from the current knowledge base state.

        The method iterates over all active markdown files visible to the
        provided knowledge base instance, computing a deterministic document ID
        for each path using the configured ``id_prefix``. Each file is read from
        disk and upserted into the underlying Chroma collection by delegating to
        :meth:`_reindex_document`, ensuring embeddings are recomputed.

        Parameters
        ----------
        kb:
            The :class:`~mcp_kb.knowledge.store.KnowledgeBase` providing access
            to the validated filesystem and utility methods.

        Returns
        -------
        int
            The number of documents processed during the reindex run.
        """

        count = 0
        root = kb.rules.root
        for path in kb.iter_active_files(include_docs=False):
            try:
                content = path.read_text(encoding="utf-8")
            except FileNotFoundError:  # pragma: no cover - race with external edits
                continue

            relative = str(path.relative_to(root))
            document_id = f"{self.configuration.id_prefix}{relative}"
            metadata = {
                "relative_path": relative,
            }
            self._reindex_document(document_id, content, metadata)
            count += 1

        return count

    def _extract_matches_from_lines(
        self,
        path: Path,
        lines: List[str],
        query: str,
        context_lines: int,
    ) -> List[SearchMatch]:
        """Return line-based matches for ``query`` within ``lines``."""

        matches: List[SearchMatch] = []
        for index, line in enumerate(lines, start=1):
            if query in line:
                start = max(0, index - context_lines - 1)
                end = min(len(lines), index + context_lines)
                matches.append(
                    SearchMatch(
                        path=path,
                        line_number=index,
                        context=lines[start:end],
                    )
                )
        return matches

    def _resolve_candidate_path(
        self,
        kb: "KnowledgeBase",
        relative: Optional[str],
    ) -> Optional[Path]:
        """Translate metadata hints into a validated path inside ``kb``."""

        path: Optional[Path] = None
        if relative:
            candidate = (kb.rules.root / relative).resolve()
            try:
                candidate.relative_to(kb.rules.root)
            except ValueError:
                path = None
            else:
                if candidate.exists():
                    path = candidate

        return path

    def _create_client(self) -> "ClientAPI":
        """Instantiate the proper Chroma client based on configuration.

        The method supports all transport modes referenced in the user
        requirements. It constructs the minimal set of keyword arguments for the
        chosen backend and lets Chroma's client validate the final configuration.
        """

        chroma = self._deps.chroma_module
        config = self.configuration

        if not config.enabled:
            raise RuntimeError("ChromaIngestor cannot be constructed when ingestion is disabled")

        if config.client_type == "ephemeral":
            return chroma.EphemeralClient()

        if config.client_type == "persistent":
            return chroma.PersistentClient(path=str(config.data_directory))

        if config.client_type in {"http", "cloud"}:
            kwargs: Dict[str, Any] = {
                "ssl": config.ssl if config.client_type == "http" else True,
            }
            if config.client_type == "http":
                kwargs["host"] = config.host
                if config.port is not None:
                    kwargs["port"] = config.port
                if config.custom_auth_credentials:
                    kwargs["settings"] = self._deps.settings_cls(
                        chroma_client_auth_provider="chromadb.auth.basic_authn.BasicAuthClientProvider",
                        chroma_client_auth_credentials=config.custom_auth_credentials,
                    )
            else:  # cloud
                kwargs["host"] = config.host or "api.trychroma.com"
                kwargs["tenant"] = config.tenant
                kwargs["database"] = config.database
                kwargs.setdefault("headers", {})
                kwargs["headers"]["x-chroma-token"] = config.api_key

            return chroma.HttpClient(**kwargs)

        raise ValueError(f"Unsupported client type: {config.client_type}")

    def _ensure_collection(self) -> "Collection":
        """Create or return the configured Chroma collection."""

        factory = self._deps.embedding_factories.get(self.configuration.embedding)
        if factory is None:
            available = ", ".join(sorted(self._deps.embedding_factories))
            raise ValueError(
                f"Unknown embedding function '{self.configuration.embedding}'. "
                f"Available options: {available}"
            )
        embedding_function = factory()

        metadata = {"source": "mcp-knowledge-base"}
        client = self._client
        try:
            return client.get_or_create_collection(
                name=self.configuration.collection_name,
                metadata=metadata,
                embedding_function=embedding_function,
            )
        except TypeError:
            # Older Chroma versions expect CreateCollectionConfiguration. Fall back
            # to create_collection for compatibility.
            return client.get_or_create_collection(
                name=self.configuration.collection_name,
                embedding_function=embedding_function,
            )
