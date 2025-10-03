"""Core knowledge base operations for file lifecycle management.

This module exposes the ``KnowledgeBase`` class, which orchestrates validated
filesystem operations for the MCP server. The class encapsulates logic for
creating, reading, appending, and modifying markdown files while respecting the
security constraints defined in the PRD. Each method returns plain Python data
structures so that higher-level layers (e.g., JSON-RPC handlers) can focus on
protocol serialization rather than filesystem minutiae.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

from mcp_kb.config import DELETE_SENTINEL, DOCS_FOLDER_NAME
from mcp_kb.knowledge.events import FileDeleteEvent, FileUpsertEvent, KnowledgeBaseListener
from mcp_kb.security.path_validation import (
    PathRules,
    ensure_write_allowed,
    normalize_path,
)
from mcp_kb.utils.filesystem import (
    FileLockRegistry,
    append_text,
    ensure_parent_directory,
    read_text,
    rename,
    write_text,
)


@dataclass
class FileSegment:
    """Represents a snippet of file content returned to MCP clients."""

    path: Path
    start_line: int
    end_line: int
    content: str


class KnowledgeBase:
    """High-level API that executes validated knowledge base operations.

    The class is intentionally stateless aside from the path rules and lock
    registry. Stateless methods make this component easy to reuse across tests
    and potential future transports. Locking responsibilities are scoped to the
    knowledge base to keep write safety consistent across entry points.
    """

    def __init__(
        self,
        rules: PathRules,
        lock_registry: FileLockRegistry | None = None,
        listeners: Iterable[KnowledgeBaseListener] | None = None,
    ) -> None:
        """Initialize the knowledge base with path rules and optional locks.

        Parameters
        ----------
        rules:
            Active path rules that govern which paths are safe to touch.
        lock_registry:
            Optional ``FileLockRegistry`` allowing tests to inject deterministic
            locking behavior. A new registry is created when omitted.
        listeners:
            Optional iterable of callback objects that subscribe to change
            events. Each listener must implement the
            :class:`~mcp_kb.knowledge.events.KnowledgeBaseListener` protocol.
            Events are dispatched synchronously after filesystem operations
            succeed, which allows callers to maintain eventual consistency with
            external systems such as vector databases.
        """

        self.rules = rules
        self.locks = lock_registry or FileLockRegistry()
        self.listeners = tuple(listeners or ())

    def create_file(self, relative_path: str, content: str) -> Path:
        """Create or overwrite a markdown file at ``relative_path``.

        The method validates the path, ensures that the parent directory exists,
        and writes the provided content as UTF-8 text. Existing files are
        overwritten to match the PRD, which views creation as setting the file
        contents.
        """

        normalized = normalize_path(relative_path, self.rules)
        ensure_write_allowed(normalized, self.rules)
        ensure_parent_directory(normalized)
        with self.locks.acquire(normalized):
            write_text(normalized, content)
        self._notify_upsert(normalized, content)
        return normalized

    def read_file(
        self,
        relative_path: str,
        start_line: Optional[int] = None,
        end_line: Optional[int] = None,
    ) -> FileSegment:
        """Read content from ``relative_path`` optionally constraining lines.

        Parameters
        ----------
        relative_path:
            Target file path relative to the knowledge base root.
        start_line:
            One-based index for the first line to include. ``None`` means start
            from the beginning of the file.
        end_line:
            One-based index signaling the last line to include. ``None`` means
            include content through the end of the file.
        """

        normalized = normalize_path(relative_path, self.rules)
        full_content = read_text(normalized)
        lines = full_content.splitlines()

        if start_line is None and end_line is None:
            segment_content = full_content
            actual_start = 1
            actual_end = len(lines)
        else:
            actual_start = start_line or 1
            actual_end = end_line or len(lines)
            if actual_start < 1 or actual_end < actual_start:
                raise ValueError("Invalid line interval requested")
            selected = lines[actual_start - 1 : actual_end]
            segment_content = "\n".join(selected)

        return FileSegment(
            path=normalized,
            start_line=actual_start,
            end_line=actual_end,
            content=segment_content,
        )

    def append_file(self, relative_path: str, content: str) -> Path:
        """Append ``content`` to the file located at ``relative_path``.

        Missing files are created automatically so that append operations remain
        idempotent for clients.
        """

        normalized = normalize_path(relative_path, self.rules)
        ensure_write_allowed(normalized, self.rules)
        ensure_parent_directory(normalized)
        with self.locks.acquire(normalized):
            if not normalized.exists():
                write_text(normalized, content)
            else:
                append_text(normalized, content)
        updated_text = read_text(normalized)
        self._notify_upsert(normalized, updated_text)
        return normalized

    def regex_replace(self, relative_path: str, pattern: str, replacement: str) -> int:
        """Perform regex replacement and return the number of substitutions."""

        normalized = normalize_path(relative_path, self.rules)
        ensure_write_allowed(normalized, self.rules)
        with self.locks.acquire(normalized):
            text = read_text(normalized)
            new_text, count = re.subn(pattern, replacement, text, flags=re.MULTILINE)
            write_text(normalized, new_text)
        self._notify_upsert(normalized, new_text)
        return count

    def soft_delete(self, relative_path: str) -> Path:
        """Apply soft deletion semantics by appending the deletion sentinel."""

        normalized = normalize_path(relative_path, self.rules)
        ensure_write_allowed(normalized, self.rules)
        if not normalized.exists():
            raise FileNotFoundError(f"File '{relative_path}' does not exist")

        target_name = f"{normalized.stem}{DELETE_SENTINEL}{normalized.suffix}"
        target = normalized.with_name(target_name)
        ensure_write_allowed(target, self.rules)
        with self.locks.acquire(normalized):
            rename(normalized, target)
        original_relative = self._relative_path(normalized)
        self._notify_delete(target, original_relative)
        return target

    def iter_active_files(self, include_docs: bool = False) -> Iterable[Path]:
        """Yield non-deleted markdown files under the root directory.

        Parameters
        ----------
        include_docs:
            When ``True`` the generator includes files located in the protected
            documentation folder. By default those files are skipped to match
            the search and overview requirements from the PRD.
        """

        for path in self.rules.root.rglob("*.md"):
            if DELETE_SENTINEL in path.name:
                continue
            parts = path.relative_to(self.rules.root).parts
            if parts and parts[0] == DOCS_FOLDER_NAME and not include_docs:
                continue
            yield path

    def _relative_path(self, absolute: Path) -> str:
        """Return ``absolute`` rewritten relative to the knowledge base root."""

        return str(absolute.relative_to(self.rules.root))

    def _notify_upsert(self, absolute: Path, content: str) -> None:
        """Dispatch an upsert event to registered listeners.

        Parameters
        ----------
        absolute:
            Fully resolved path that was modified on disk.
        content:
            Markdown payload that should be provided to subscribers.
        """

        if not self.listeners:
            return

        event = FileUpsertEvent(
            absolute_path=absolute,
            relative_path=self._relative_path(absolute),
            content=content,
        )
        self._dispatch("handle_upsert", event)

    def _notify_delete(self, absolute: Path, relative: str) -> None:
        """Dispatch a delete event to registered listeners."""

        if not self.listeners:
            return

        event = FileDeleteEvent(absolute_path=absolute, relative_path=relative)
        self._dispatch("handle_delete", event)

    def _dispatch(self, method_name: str, event: FileUpsertEvent | FileDeleteEvent) -> None:
        """Call ``method_name`` on every listener and wrap failures for clarity."""

        for listener in self.listeners:
            handler = getattr(listener, method_name)
            try:
                handler(event)  # type: ignore[misc]
            except Exception as exc:  # pragma: no cover - defensive logging path
                raise RuntimeError(
                    f"Knowledge base listener {listener!r} failed during {method_name}: {exc}"
                ) from exc
