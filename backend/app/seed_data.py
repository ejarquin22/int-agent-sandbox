from .db import init_db

SAMPLE_PLAYERS = [
    ("Lionel Messi", 36, 30, 12),
    ("Cristiano Ronaldo", 39, 28, 10),
    ("Erling Haaland", 24, 25, 5)
]

def seed():
    conn = init_db()
    for name, age, goals, assists in SAMPLE_PLAYERS:
        conn.execute(
            "INSERT INTO players (name, age, goals, assists) VALUES (?, ?, ?, ?)",
            (name, age, goals, assists)
        )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()
