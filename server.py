from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import json
import math
import random
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

players = {}
bullets = []
powerups = [
    {"id": "p1", "x": 250, "y": 260, "type": "heal"},
    {"id": "p2", "x": 650, "y": 260, "type": "boost"}
]
barriers = [
    {"x": 420, "y": 140, "w": 60, "h": 60},
    {"x": 420, "y": 340, "w": 60, "h": 60}
]

def reset_player(player_id):
    return {
        "x": random.randint(80, 820),
        "y": random.randint(80, 460),
        "angle": 0,
        "health": 100,
        "maxHealth": 100,
        "score": 0,
        "xp": 0,
        "level": 1,
        "name": f"Cadet_{player_id[-4:]}"
    }

@app.websocket("/ws/{player_id}")
async def websocket_endpoint(websocket: WebSocket, player_id: str):
    await websocket.accept()
    players[player_id] = reset_player(player_id)
    
    try:
        while True:
            data = await websocket.receive_text()
            payload = json.loads(data)
            action = payload.get("type")

            if action == "move" and player_id in players:
                players[player_id]["x"] = payload.get("x", players[player_id]["x"])
                players[player_id]["y"] = payload.get("y", players[player_id]["y"])
                players[player_id]["angle"] = payload.get("angle", players[player_id]["angle"])

            elif action == "shoot" and player_id in players:
                lvl = players[player_id]["level"]
                bullets.append({
                    "id": f"b_{random.randint(1000, 9999)}",
                    "owner": player_id,
                    "x": payload.get("x"),
                    "y": payload.get("y"),
                    "vx": math.cos(payload.get("angle")) * (14 + lvl),
                    "vy": math.sin(payload.get("angle")) * (14 + lvl),
                    "damage": 18 + (lvl * 4),
                    "life": 45
                })

            # Check powerup pickups
            p_obj = players.get(player_id)
            if p_obj:
                for pw in powerups:
                    if math.hypot(p_obj["x"] - pw["x"], p_obj["y"] - pw["y"]) < 30:
                        if pw["type"] == "heal":
                            p_obj["health"] = min(100, p_obj["health"] + 35)
                        elif pw["type"] == "boost":
                            p_obj["xp"] += 60
                            if p_obj["xp"] >= p_obj["level"] * 100 and p_obj["level"] < 5:
                                p_obj["level"] += 1
                        pw["x"] = random.randint(100, 800)
                        pw["y"] = random.randint(100, 440)

            # Bullet Physics & Collisions
            active_bullets = []
            for b in bullets:
                b["x"] += b["vx"]
                b["y"] += b["vy"]
                b["life"] -= 1

                # Barrier hit
                hit_barrier = False
                for br in barriers:
                    if br["x"] <= b["x"] <= br["x"] + br["w"] and br["y"] <= b["y"] <= br["y"] + br["h"]:
                        hit_barrier = True
                        break
                if hit_barrier:
                    continue

                # Player hit
                hit_player = False
                for pid, p in players.items():
                    if pid != b["owner"] and math.hypot(p["x"] - b["x"], p["y"] - b["y"]) < 24:
                        p["health"] -= b["damage"]
                        hit_player = True
                        if p["health"] <= 0:
                            if b["owner"] in players:
                                players[b["owner"]]["score"] += 150
                                players[b["owner"]]["xp"] += 100
                                if players[b["owner"]]["xp"] >= players[b["owner"]]["level"] * 100 and players[b["owner"]]["level"] < 5:
                                    players[b["owner"]]["level"] += 1
                            players[pid] = reset_player(pid)
                        break
                
                if not hit_player and b["life"] > 0:
                    active_bullets.append(b)
            
            bullets.clear()
            bullets.extend(active_bullets)

            await websocket.send_text(json.dumps({
                "players": players,
                "bullets": bullets,
                "powerups": powerups,
                "barriers": barriers
            }))

    except WebSocketDisconnect:
        if player_id in players:
            del players[player_id]