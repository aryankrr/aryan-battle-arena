<<<<<<< Updated upstream
<div align="center">

# ⚔️ ARYAN BATTLE ARENA
### *High-Concurrency 2D Real-Time Multiplayer Combat Engine*

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![WebSockets](https://img.shields.io/badge/WebSockets-Real--Time-010101?style=for-the-badge&logo=socketdotio&logoColor=white)](https://websockets.readthedocs.io)
[![HTML5 Canvas](https://img.shields.io/badge/HTML5-Canvas%202D-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)

<p align="center">
  A high-performance, low-latency 2D browser-based multiplayer combat arena featuring authoritative server physics, dynamic level-ups, vector aiming, power-up pickups, and a cyberpunk HUD.
</p>

</div>

---

## ⚡ Key Architectural Highlights

* 🛰️ **Sub-30ms Real-Time State Synchronization:** Authoritative server-side loop built on FastAPI and AsyncIO handling bi-directional state broadcast across active combatants.
* 🎯 **360° Vector Aiming & Trajectory:** Trigonometric mouse-guided angle calculation (`Math.atan2`) driving directional lasers and muzzle recoil flashes.
* 🛡️ **Tactical Arenas & Power-ups:** Destructible tactical barriers, dynamic health repair packs, and XP overcharge nodes.
* 📈 **Dynamic Combat Progression:** Real-time XP tracking system unlocking multi-barrel plasma upgrades (Level 1–5).
* 💥 **Cyberpunk Canvas Rendering:** 60 FPS client engine with dynamic screen shake, glowing vector trails, and damage particle explosions.

---

## 🛠️ Tech Stack & Protocols

| Layer | Technology / Protocol | Purpose |
| :--- | :--- | :--- |
| **Backend Engine** | Python 3.x, FastAPI, Uvicorn | High-concurrency ASGI server, event loop, and state broadcast |
| **Networking** | WebSockets (`ws://`) | Full-duplex bidirectional real-time client-server communication |
| **Graphics Engine** | JavaScript (ES6+), HTML5 Canvas API | 60 FPS hardware-accelerated 2D rendering pipeline |
| **Interface / UI** | CSS3 (Cyberpunk Glassmorphism) | Dynamic HUD, responsive layout, and tactical scoreboard |

---

## 🕹️ Controls & Mechanics

| Action | Control Key / Input | Details |
| :--- | :--- | :--- |
| **Movement** | `W`, `A`, `S`, `D` / Arrow Keys | 8-directional tactical tank navigation |
| **Aiming** | `Mouse Cursor` | 360-degree turret orientation tracking |
| **Primary Cannon**| `Left Mouse Click` / `Spacebar` | Fires high-velocity plasma projectiles |
| **Power-ups** | `Collision Pickup` | Green: +35 Health / Yellow: +60 XP Boost |

---

## 🏗️ System Architecture
┌────────────────────────┐         ┌────────────────────────┐
│   Player 1 (Browser)   │         │   Player 2 (Browser)   │
└───────────┬────────────┘         └───────────┬────────────┘
│ WebSocket Inputs                 │ WebSocket Inputs
▼                                  ▼
┌───────────────────────────────────────────────────────────┐
│               FastAPI WebSocket Server Engine             │
│  • Concurrency Management   • Laser Trajectory & Hitboxes │
│  • Tactical Barrier Checks  • Dynamic Level & XP State    │
└───────────────────────────┬───────────────────────────────┘
│
▼ State Broadcast (60 Ticks/sec)
┌───────────────────────────────┐
│ Client HTML5 Canvas Rendering │
└───────────────────────────────┘


---
=======
# ⚔️ Aryan Battle Arena - 2D Real-Time Combat Game

A high-concurrency, low-latency 2D multiplayer combat arena running directly in the browser. Built with **Python (FastAPI)** and **WebSockets** for real-time bidirectional state synchronization, paired with a custom **HTML5 Canvas** rendering engine.

---

## 🚀 Key Features
* **Sub-30ms Real-Time State Sync:** Authoritative server-side loop in Python managing player positions, weapon trajectories, obstacle collisions, and health states over WebSockets.
* **Combat & Level Progression System:** Real-time XP tracking, dynamic multi-barrel upgrades (Level 1 to Level 5), and floating health indicators.
* **Tactical Arenas & Power-ups:** Destructible barriers and real-time spawning power-ups (Health Kits & XP Overcharges).
* **Cyberpunk Visual Engine:** 60 FPS rendering pipeline with mouse-guided 360° turret rotation, dynamic screen recoil/shake, and particle explosion physics.

---

## 🛠️ Tech Stack
* **Backend:** Python 3.x, FastAPI, Uvicorn, WebSockets (AsyncIO)
* **Frontend:** JavaScript (ES6+), HTML5 Canvas API, CSS3
* **Protocol:** Full-Duplex WebSockets (`ws://`)

---

## 🕹️ Controls
* **Move:** `W`, `A`, `S`, `D` or `Arrow Keys`
* **Aim:** `Mouse Cursor` (360° Rotation)
* **Fire:** `Left Click` or `Spacebar`

---

## ⚙️ Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/aryankrr/aryan-battle-arena.git](https://github.com/aryankrr/aryan-battle-arena.git)
   cd realtime-multiplayer-arena
>>>>>>> Stashed changes
