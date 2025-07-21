from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import random
import asyncio

from fastapi import HTTPException, status

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path setup
import os
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))
index_file = os.path.join(frontend_path, 'index.html')

# Serve static files (CSS, JS, etc.) at /static
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Serve index.html at root
@app.get("/", response_class=HTMLResponse)
async def get_index():
    return open(index_file, encoding="utf-8").read()

latest_sensor_data = {}
AUTH_TOKEN = "mysecrettoken123"

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    token = websocket.query_params.get("token")
    if token != AUTH_TOKEN:
        await websocket.close(code=1008)
        print(f"WebSocket unauthorized connection attempt from {websocket.client.host}:{websocket.client.port}")
        return
    client = websocket.client
    print(f"WebSocket connect: {client.host}:{client.port}")
    await websocket.accept()
    try:
        while True:
            data = {
                "temperature": round(random.uniform(60, 90), 2),
                "pressure": round(random.uniform(1.0, 2.0), 2),
                "vibration": round(random.uniform(0.1, 0.5), 2),
                "humidity": round(random.uniform(30, 70), 2),
                "voltage": round(random.uniform(220, 240), 2),
                "current": round(random.uniform(0.5, 2.0), 2),
                "status": random.choice(["OK", "WARN", "FAIL"])
            }
            global latest_sensor_data
            latest_sensor_data = data
            await websocket.send_json(data)
            await asyncio.sleep(1)
    except Exception as e:
        print(f"WebSocket error for {client.host}:{client.port}: {e}")
    finally:
        print(f"WebSocket disconnect: {client.host}:{client.port}")
        await websocket.close()

@app.get("/api/latest")
async def get_latest_sensor_data(request: Request):
    auth_header = request.headers.get("authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid Authorization header.")
    token = auth_header.split(" ", 1)[1]
    if token != AUTH_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token.")
    if latest_sensor_data:
        return latest_sensor_data
    return {"error": "No data available yet."}
