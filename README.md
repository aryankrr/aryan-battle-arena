<div align="center">

# ⚔️ ARYAN BATTLE ARENA
### *High-Concurrency 2D Real-Time Multiplayer Combat Engine*

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![WebSockets](https://img.shields.io/badge/WebSockets-Real--Time-010101?style=for-the-badge&logo=socketdotio&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
[![HTML5 Canvas](https://img.shields.io/badge/HTML5-Canvas%202D-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

<p align="center">
  A low-latency, browser-based 2D multiplayer combat arena featuring authoritative server physics, dynamic level-ups, vector aiming, power-up pickups, and a neon sci-fi HUD.
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
| **Backend** | Python 3.x, FastAPI, Uvicorn | ASGI server, event loop, and state management |
| **Networking** | WebSockets (`ws://`) | Full-duplex real-time client-server communication |
| **Frontend Engine** | JavaScript (ES6+), HTML5 Canvas API | 60 FPS graphics pipeline and user input handling |
| **Styling & UI** | CSS3 (Cyberpunk Neon Theme) | Glassmorphism leaderboard HUD and responsive layout |

---

## 🕹️ Controls
