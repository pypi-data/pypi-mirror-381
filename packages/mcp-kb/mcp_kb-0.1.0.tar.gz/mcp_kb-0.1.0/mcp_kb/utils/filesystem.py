"""Filesystem helpers wrapping Python's standard library primitives.

The knowledge base server performs numerous file operations. Consolidating the
logic in this module keeps the rest of the code focused on business semantics
such as validating incoming requests and shaping responses. Each helper function
is intentionally small so that callers can compose them for different workflows
without duplicating the low-level boilerplate.
"""
from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from threading import Lock
from typing import Dict, Iterator


class FileLockRegistry:
    """In-memory lock registry to serialize write operations per file.

    Using per-path locks prevents concurrent writes from interleaving content
    and potentially corrupting files. The registry lazily creates locks when a
    path is first encountered. We reuse locks for subsequent operations to avoid
    unbounded memory usage.
    """

    def __init__(self) -> None:
        """Initialize the registry with an empty dictionary."""

        self._locks: Dict[Path, Lock] = {}
        self._global_lock = Lock()

    @contextmanager
    def acquire(self, path: Path) -> Iterator[None]:
        """Context manager that acquires a lock for the supplied path.

        The helper nests two locks: a global mutex to retrieve or create the
        per-path lock, and the per-path lock itself for the duration of the
        caller's critical section.

        Parameters
        ----------
        path:
            Absolute path indicating which file should be protected.
        """

        with self._global_lock:
            lock = self._locks.setdefault(path, Lock())
        lock.acquire()
        try:
            yield
        finally:
            lock.release()


def write_text(path: Path, content: str) -> None:
    """Write text content to ``path`` using UTF-8 encoding."""

    path.write_text(content, encoding="utf-8")


def append_text(path: Path, content: str) -> None:
    """Append text content to ``path`` using UTF-8 encoding."""

    with path.open("a", encoding="utf-8") as handle:
        handle.write(content)


def read_text(path: Path) -> str:
    """Read UTF-8 text content from ``path`` and return it."""

    return path.read_text(encoding="utf-8")


def ensure_parent_directory(path: Path) -> None:
    """Ensure the parent directory of ``path`` exists by creating it."""

    path.parent.mkdir(parents=True, exist_ok=True)


def rename(path: Path, target: Path) -> None:
    """Rename ``path`` to ``target`` using ``Path.rename`` semantics."""

    path.rename(target)
