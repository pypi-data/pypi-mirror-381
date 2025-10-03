"""Change event types and listener contracts for knowledge base updates.

The knowledge base emits high-level events whenever a markdown document is
created, updated, or soft deleted. Downstream components can subscribe to these
notifications to implement side effects such as vector database ingestion without
coupling the core filesystem logic to specific backends. Each event captures both
absolute and knowledge-base-relative paths so that listeners can decide which
identifier best fits their storage requirements.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Protocol, runtime_checkable, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - type hints only
    from typing import List

    from mcp_kb.knowledge.search import SearchMatch
    from mcp_kb.knowledge.store import KnowledgeBase


@dataclass(frozen=True)
class FileUpsertEvent:
    """Describes a document that was created or updated inside the knowledge base.

    Attributes
    ----------
    absolute_path:
        Fully resolved path to the document on disk. Listeners that need direct
        filesystem access can rely on this value to open the file again.
    relative_path:
        Path relative to the configured knowledge base root. This identifier is
        stable across restarts and makes for concise IDs in downstream systems.
    content:
        Full markdown content of the updated document at the time the event was
        emitted. Listeners can avoid re-reading the file when they only need the
        text payload.
    """

    absolute_path: Path
    relative_path: str
    content: str


@dataclass(frozen=True)
class FileDeleteEvent:
    """Signals that a document has been soft deleted according to PRD semantics.

    Attributes
    ----------
    absolute_path:
        Fully resolved path that now contains the soft-deleted file. The path
        may include the configured delete sentinel in its name.
    relative_path:
        Original knowledge-base-relative path before soft deletion. Downstream
        systems should remove entries keyed by this relative path to stay in
        sync with the knowledge base state.
    """

    absolute_path: Path
    relative_path: str


class KnowledgeBaseListener(Protocol):
    """Interface for components that react to knowledge base change events."""

    def handle_upsert(self, event: FileUpsertEvent) -> None:
        """Persist changes triggered by a document creation or update event."""

    def handle_delete(self, event: FileDeleteEvent) -> None:
        """Process the removal of a previously ingested document."""


@runtime_checkable
class KnowledgeBaseSearchListener(Protocol):
    """Optional extension that allows listeners to service search requests."""

    def search(
        self,
        kb: "KnowledgeBase",
        query: str,
        *,
        context_lines: int = 2,
        limit: Optional[int] = None,
    ) -> "List[SearchMatch]":
        """Return semantic search matches for ``query`` or an empty list."""


@runtime_checkable
class KnowledgeBaseReindexListener(Protocol):
    """Optional extension that allows listeners to perform full reindexing.

    Implementations can expose a ``reindex`` method to rebuild any external
    indexes from the current state of the knowledge base. The method should be
    idempotent and safe to run multiple times.
    """

    def reindex(self, kb: "KnowledgeBase") -> int:
        """Rebuild indexes, returning the number of documents processed."""
