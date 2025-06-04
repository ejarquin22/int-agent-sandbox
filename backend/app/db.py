import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "players.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    goals INTEGER,
    assists INTEGER
);
"""

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(SCHEMA)
    conn.commit()
    return conn

def get_player(conn, player_id):
    cur = conn.execute("SELECT id, name, age, goals, assists FROM players WHERE id=?", (player_id,))
    row = cur.fetchone()
    if row:
        return {
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "goals": row[3],
            "assists": row[4]
        }
    return None


def list_players(conn):
    cur = conn.execute("SELECT id, name, age, goals, assists FROM players")
    return [
        {"id": row[0], "name": row[1], "age": row[2], "goals": row[3], "assists": row[4]}
        for row in cur.fetchall()
    ]
