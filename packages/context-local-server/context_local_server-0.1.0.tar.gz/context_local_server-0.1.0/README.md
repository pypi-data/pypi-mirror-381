# AI Agent Context Server

**local-context-server** is a lightweight, local MCP (Model Context Protocol) server designed to provide long-term memory for AI agents like Gemini, Claude, and others within environments like Cursor.

It allows an AI agent to save, load, list, and search for *"contexts"*—pieces of knowledge such as application maps, test data, or business requirements—making it possible to create adaptive and intelligent QA automation.

## Features

- **Persistent Memory:** Store any JSON-serializable data in a local SQLite database.

- **Simple Tool API:** Provides four core tools for the AI to manage its knowledge:
  - `save_context`: Save or update a piece of knowledge.
  - `load_context`: Retrieve knowledge by its unique ID.
  - `list_contexts`: Browse all available knowledge.
  - `search_contexts`: Search for knowledge by keyword.

- **Automatic Database Location:** The server automatically creates and manages its database file (`memory_tests.db`) in a folder named `context-database` inside your user's home directory. This requires no configuration.