import sqlite3
import json
import asyncio
import argparse
from pydantic import BaseModel
from typing import Dict, Any
from pathlib import Path
import appdirs
from fastmcp import FastMCP

# Se define globalmente pero se inicializa dentro de run()
DB_FILE = None

def get_db_path() -> Path:
    """
    Gets the database file path.
    Priority: 1. --db command-line argument. 2. Default user data directory.
    """
    parser = argparse.ArgumentParser(description="MCP Context Server")
    parser.add_argument(
        "--db",
        type=str,
        default=None,
        help="Optional: Absolute path to the SQLite database file."
    )
    args, _ = parser.parse_known_args()

    if args.db:
        # If a path was provided via command line, use it.
        return Path(args.db)
    else:
        # Otherwise, fall back to the standard user data directory.
        data_dir = Path(appdirs.user_data_dir("ContextServer", "dmarcas"))
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir / "memoria_tests.db"

def initialize_db(db_path: Path):
    """Creates the database and the table if they don't exist."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contexts (
            id TEXT PRIMARY KEY,
            context_json TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

class SaveContextInput(BaseModel):
    id: str
    context: Dict[str, Any]

class LoadContextInput(BaseModel):
    id: str

class SearchContextsInput(BaseModel):
    query: str

mcp = FastMCP(name="ContextServer")

def unpack_and_validate(received_data: dict, expected_model: BaseModel):
    params = received_data.get("input", received_data)
    if isinstance(params, str):
        params = json.loads(params)
    return expected_model(**params)

@mcp.tool(name="save_context", description="Saves the context of a test run.")
async def save_context(input: dict) -> dict:
    try:
        validated_input = unpack_and_validate(input, SaveContextInput)
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "REPLACE INTO contexts (id, context_json) VALUES (?, ?)",
            (validated_input.id, json.dumps(validated_input.context))
        )
        conn.commit()
        conn.close()
        return {"message": f"Context '{validated_input.id}' saved successfully."}
    except Exception as e:
        return {"error": f"Error in save_context: {type(e).__name__}: {str(e)}"}

@mcp.tool(name="load_context", description="Loads a previously saved context.")
async def load_context(input: dict) -> dict:
    try:
        validated_input = unpack_and_validate(input, LoadContextInput)
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT context_json FROM contexts WHERE id = ?", (validated_input.id,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return {"context": json.loads(result[0])}
        else:
            return {"message": "No context found with that identifier."}
    except Exception as e:
        return {"error": f"Error in load_context: {type(e).__name__}: {str(e)}"}

@mcp.tool(name="list_contexts", description="Returns a list of all saved context IDs.")
async def list_contexts() -> dict:
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

@mcp.tool(name="search_contexts", description="Searches for context IDs that match a search term.")
async def search_contexts(input: dict) -> dict:
    try:
        validated_input = unpack_and_validate(input, SearchContextsInput)
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        term = f"%{validated_input.query}%"
        cursor.execute("SELECT id FROM contexts WHERE id LIKE ? ORDER BY id", (term,))
        results = cursor.fetchall()
        conn.close()
        id_list = [result[0] for result in results]
        return {"contexts": id_list}
    except Exception as e:
        return {"error": f"Error in search_contexts: {type(e).__name__}: {str(e)}"}

def run():
    """This is the main function that the package will execute."""
    global DB_FILE
    DB_FILE = get_db_path()
    initialize_db(DB_FILE)
    print(f"Context Server DB location: {DB_FILE}")
    print("Starting MCP Context Server via stdio...")
    asyncio.run(mcp.run_stdio_async())

if __name__ == "__main__":
    run()
