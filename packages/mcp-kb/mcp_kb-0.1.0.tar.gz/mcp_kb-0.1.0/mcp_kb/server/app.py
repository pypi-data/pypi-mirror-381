"""FastMCP application that exposes knowledge base management tools.

The module builds a :class:`FastMCP` server configured with the knowledge base
operations defined elsewhere in the package. Using FastMCP drastically reduces
protocol boilerplate because the framework introspects type hints and
Docstrings to generate MCP-compatible tool schemas automatically.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

from mcp.server.fastmcp import FastMCP

from mcp_kb.config import DOC_FILENAME
from mcp_kb.knowledge.events import (
    KnowledgeBaseListener,
    KnowledgeBaseSearchListener,
)
from mcp_kb.knowledge.search import build_tree_overview, read_documentation, search_text
from mcp_kb.knowledge.store import FileSegment, KnowledgeBase
from mcp_kb.security.path_validation import PathRules, PathValidationError


@dataclass
class ReadFileResult:
    """Structured output for the ``kb.read_file`` tool."""

    path: str
    start_line: int
    end_line: int
    content: str


@dataclass
class RegexReplaceResult:
    """Structured output describing the number of replacements performed."""

    replacements: int


@dataclass
class SearchMatchResult:
    """Structured representation of a search result with contextual lines."""

    path: str
    line: int
    context: List[str]


def create_fastmcp_app(
    rules: PathRules,
    *,
    host: str | None = None,
    port: int | None = None,
    listeners: Iterable[KnowledgeBaseListener] | None = None,
) -> FastMCP:
    """Build and return a configured :class:`FastMCP` server instance.

    Parameters
    ----------
    rules:
        Sanitised filesystem rules that restrict all knowledge base operations to
        a designated root.
    host:
        Optional host interface for HTTP/SSE transports. ``None`` uses FastMCP's
        defaults.
    port:
        Optional TCP port for HTTP/SSE transports. ``None`` uses FastMCP's defaults.
    listeners:
        Optional iterable of :class:`KnowledgeBaseListener` implementations that
        should receive change notifications. The iterable is passed directly to
        :class:`~mcp_kb.knowledge.store.KnowledgeBase` so that integrations such
        as Chroma ingestion can react to file lifecycle events.
    """

    kb = KnowledgeBase(rules, listeners=listeners)
    search_providers: List[KnowledgeBaseSearchListener] = []
    if listeners is not None:
        for listener in listeners:
            if isinstance(listener, KnowledgeBaseSearchListener):
                search_providers.append(listener)
    fastmcp_kwargs: dict[str, object] = {}
    if host is not None:
        fastmcp_kwargs["host"] = host
    if port is not None:
        fastmcp_kwargs["port"] = port

    mcp = FastMCP(
        "mcp-knowledge-base",
        instructions=(
            "You are connected to a local markdown knowledge base. Use the provided "
            "tools to create, inspect, and organize content while respecting the "
            "soft deletion semantics and the protected documentation folder."
        ),
        **fastmcp_kwargs,
    )

    @mcp.tool(name="create_file", title="Create File")
    def create_file(path: str, content: str) -> str:
        """Create or overwrite a markdown file at ``path`` with ``content``."""

        try:
            created = kb.create_file(path, content)
        except PathValidationError as exc:
            raise ValueError(str(exc)) from exc
        return f"Created {created}"

    @mcp.tool(name="read_file", title="Read File", structured_output=True)
    def read_file(path: str, start_line: int | None = None, end_line: int | None = None) -> ReadFileResult:
        """Read a markdown file returning metadata about the extracted segment."""

        try:
            segment: FileSegment = kb.read_file(path, start_line=start_line, end_line=end_line)
        except PathValidationError as exc:
            raise ValueError(str(exc)) from exc
        except FileNotFoundError as exc:
            raise ValueError(str(exc)) from exc
        return ReadFileResult(
            path=str(segment.path),
            start_line=segment.start_line,
            end_line=segment.end_line,
            content=segment.content,
        )

    @mcp.tool(name="append_file", title="Append File")
    def append_file(path: str, content: str) -> str:
        """Append ``content`` to the file specified by ``path``."""

        try:
            target = kb.append_file(path, content)
        except PathValidationError as exc:
            raise ValueError(str(exc)) from exc
        return f"Appended to {target}"

    @mcp.tool(name="regex_replace", title="Regex Replace", structured_output=True)
    def regex_replace(path: str, pattern: str, replacement: str) -> RegexReplaceResult:
        """Perform a regex-based replacement across the full file."""

        try:
            replacements = kb.regex_replace(path, pattern, replacement)
        except PathValidationError as exc:
            raise ValueError(str(exc)) from exc
        return RegexReplaceResult(replacements=replacements)

    @mcp.tool(name="delete", title="Soft Delete")
    def delete(path: str) -> str:
        """Soft delete the file at ``path`` by appending the configured sentinel."""

        try:
            deleted = kb.soft_delete(path)
        except PathValidationError as exc:
            raise ValueError(str(exc)) from exc
        except FileNotFoundError as exc:
            raise ValueError(str(exc)) from exc
        return f"Marked {deleted.name} as deleted"

    @mcp.tool(name="search", title="Search", structured_output=True)
    def search(query: str, limit: int = 5) -> List[SearchMatchResult]:
        """Search for ``query`` across the knowledge base with semantic ranking.

        Registered listeners that implement the optional search interface are
        queried first (e.g., the Chroma ingestor). When no listener returns a
        result the tool falls back to streaming the markdown files directly so
        callers always receive deterministic text snippets.
        """

        if limit <= 0:
            raise ValueError("limit must be greater than zero")

        matches = search_text(
            kb,
            query,
            providers=search_providers,
            n_results=limit,
        )
        return [
            SearchMatchResult(
                path=str(match.path),
                line=match.line_number,
                context=match.context,
            )
            for match in matches
        ]

    @mcp.tool(name="overview", title="Overview")
    def overview() -> str:
        """Return a textual tree describing the knowledge base structure."""

        return build_tree_overview(kb)

    @mcp.tool(name="documentation", title="Documentation")
    def documentation() -> str:
        """Read the knowledge base documentation if ``%s`` exists.""" % DOC_FILENAME

        text = read_documentation(kb)
        if not text:
            return "Documentation is not available."
        return text

    return mcp
