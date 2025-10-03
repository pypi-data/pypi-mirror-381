# Knowledge Base Usage Guide

Welcome to the MCP-managed knowledge base. This document is automatically
installed the first time the server starts to ensure every deployment ships with
baseline documentation. Customize it to describe project-specific conventions or
operational practices.

## Structure

- All knowledge content lives beneath the `.knowledgebase/` root.
- Documentation resides under `.docs/` and is read-only from the MCP tools.
- Soft-deleted files are suffixed with `_DELETE_` and ignored by search/overview.

## Recommended Practices

1. Organize content into topic-based folders (e.g., `architecture/`, `ops/`).
2. Keep document titles within the first heading so search results show context.
3. Use relative markdown links to connect related documents inside the knowledge
   base.
4. Periodically review `_DELETE_` files and clean up as necessary via direct
   filesystem operations.

## Default Tools

| Tool            | Purpose                                   |
| --------------- | ----------------------------------------- |
| `create_file`   | Create or overwrite markdown documents    |
| `read_file`     | Read entire files or specific line ranges |
| `append_file`   | Append additional content to a file       |
| `regex_replace` | Run regex-based replacements              |
| `search`        | Search text across active documents       |
| `overview`      | Display a tree overview of the knowledge  |
| `documentation` | Read this documentation file              |
| `delete`        | Soft-delete files safely                  |

Update this document to reflect your team's workflows after deployment.
