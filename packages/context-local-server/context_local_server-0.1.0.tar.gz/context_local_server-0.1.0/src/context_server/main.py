import sqlite3
import json
import asyncio
from pydantic import BaseModel, Field
from typing import Dict, Any, List
from pathlib import Path # <-- 1. Import the Path library

from fastmcp import FastMCP

# --- 2. DYNAMIC AND ROBUST DATABASE PATH ---
# Get the user's home directory
home_dir = Path.home()
# Define the path for the database inside a specific folder
db_dir = home_dir / "context-database"
# Create the directory if it doesn't already exist
db_dir.mkdir(parents=True, exist_ok=True)
# Define the final path to the database file
DB_FILE = db_dir / "memory_tests.db"

def initialize_db():
    """Creates the database and the 'contexts' table if they don't already exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contexts (
            id TEXT PRIMARY KEY,
            context_json TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# The SaveContextInput and LoadContextInput classes are no longer needed.

# --- Server Setup ---

mcp = FastMCP(name="ContextServer")

# --- Tool Definitions ---

@mcp.tool(name="save_context", description="Saves or updates the context for a specific test execution.")
async def save_context(
    test_identifier: str = Field(..., description="A unique ID for the test context, e.g., 'onboarding_v2_user_signup'."),
    context: Dict[str, Any] = Field(..., description="A JSON object containing the data to be saved.")
) -> dict:
    """Saves a given context object to the database, associated with a unique identifier."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "REPLACE INTO contexts (id, context_json) VALUES (?, ?)",
            (test_identifier, json.dumps(context))
        )
        conn.commit()
        conn.close()
        return {"message": f"Context '{test_identifier}' saved successfully."}
    except Exception as e:
        return {"error": f"Error saving context: {e}"}

@mcp.tool(name="load_context", description="Loads or retrieves a previously saved context using its unique ID.")
async def load_context(
    test_identifier: str = Field(..., description="The unique ID of the test context to retrieve.")
) -> dict:
    """Retrieves a context object from the database based on its test identifier."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT context_json FROM contexts WHERE id = ?", (test_identifier,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return {"context": json.loads(result[0])}
        else:
            return {"message": f"No context found with the identifier '{test_identifier}'."}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool(name="list_contexts", description="Returns a list of all saved context IDs.")
async def list_contexts() -> dict:
    """Provides a complete list of all unique IDs for the contexts stored in the database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM contexts ORDER BY id")
        results = cursor.fetchall()
        conn.close()
        id_list = [result[0] for result in results]
        return {"contexts": id_list}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool(
    name="search_contexts",
    description="Searches for context IDs that match a specific keyword. It takes a single, direct string argument."
)
async def search_contexts(
    search_term: str = Field(
        ...,
        description="The keyword or phrase to search for within the context IDs.",
        examples=["onboarding", "user_flow_test"]
    )
) -> dict:
    """
    Searches for and returns context IDs that contain a matching keyword in the ID.
    This search is case-insensitive.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        term = f"%{search_term.lower()}%"
        cursor.execute(
            "SELECT id FROM contexts WHERE LOWER(id) LIKE ?",
            (term,)
        )
        results = cursor.fetchall()
        conn.close()
        id_list = [result[0] for result in results]
        if not id_list:
            return {"message": f"No contexts found matching '{search_term}'."}
        return {"contexts": id_list}
    except Exception as e:
        return {"error": str(e)}

# --- Main executable function ---

def run():
    """This is the main function that the package will execute."""
    print(f"Attempting to connect to database at: {DB_FILE}")
    print("Initializing the context database...")
    initialize_db()
    print("Starting the MCP Context Server. Waiting for requests...")
    asyncio.run(mcp.run_stdio_async())

if __name__ == "__main__":
    run()
