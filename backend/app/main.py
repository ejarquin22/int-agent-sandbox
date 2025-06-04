from fastapi import FastAPI, HTTPException
from .db import init_db, get_player, list_players

app = FastAPI()

@app.on_event("startup")
def startup():
    global conn
    conn = init_db()

@app.on_event("shutdown")
def shutdown():
    conn.close()

@app.get("/players")
def get_players():
    return list_players(conn)

@app.get("/players/{player_id}")
def api_get_player(player_id: int):
    player = get_player(conn, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@app.get("/compare/{id1}/{id2}")
def compare_players(id1: int, id2: int):
    p1 = get_player(conn, id1)
    p2 = get_player(conn, id2)
    if not p1 or not p2:
        raise HTTPException(status_code=404, detail="One or both players not found")
    return {
        "player1": p1,
        "player2": p2
    }
