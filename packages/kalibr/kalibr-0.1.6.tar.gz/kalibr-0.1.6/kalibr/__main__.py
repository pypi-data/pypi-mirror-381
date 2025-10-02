import json
import threading
import time
import subprocess
import sys
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
import requests

PUBLIC_URL = None
app = FastAPI(title="Kalibr Demo API")

# === Example action: add_contact ===
@app.post("/proxy/add_contact")
async def add_contact(request: Request):
    data = await request.json()
    return {"status": "success", "contact": data}

# === GPT Manifest ===
@app.get("/.well-known/ai-plugin.json")
def plugin_manifest():
    return {
        "schema_version": "v1",
        "name_for_model": "kalibr_demo",
        "name_for_human": "Kalibr Demo",
        "description_for_model": "Demo API made agent-ready by Kalibr",
        "description_for_human": "Use this to test a demo API",
        "auth": {"type": "none"},
        "api": {
            "type": "openapi",
            "url": f"{PUBLIC_URL}/openapi.json" if PUBLIC_URL else "http://localhost:8000/openapi.json"
        }
    }

# === Claude MCP Manifest ===
@app.get("/mcp.json")
def mcp_manifest():
    return {
        "mcp": "1.0",
        "name": "kalibr_demo",
        "tools": [
            {
                "name": "add_contact",
                "description": "Add a contact to Airtable CRM",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "email": {"type": "string"}
                    },
                    "required": ["name", "email"]
                },
                "server": {"url": f"{PUBLIC_URL}/proxy/add_contact" if PUBLIC_URL else "http://localhost:8000/proxy/add_contact"}
            }
        ]
    }

def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)

def main():
    global PUBLIC_URL

    print("🚀 Starting Kalibr Demo...")

    # Start FastAPI in background
    threading.Thread(target=start_server, daemon=True).start()
    time.sleep(2)

    # Start ngrok
    print("⏳ Starting ngrok...")
    ngrok = subprocess.Popen(["ngrok", "http", "8000"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(3)

    try:
        resp = requests.get("http://localhost:4040/api/tunnels")
        PUBLIC_URL = resp.json()["tunnels"][0]["public_url"]
    except Exception as e:
        print("❌ Could not fetch ngrok URL:", e)
        sys.exit(1)

    print(f"✅ Proxy running at {PUBLIC_URL}")

    # Print where manifests live
    print("\n📋 ChatGPT manifest:")
    print(f"{PUBLIC_URL}/.well-known/ai-plugin.json")

    print("\n📋 Claude MCP manifest:")
    print(f"{PUBLIC_URL}/mcp.json")

    print("\n✨ Your API is now AI-ready!")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        ngrok.terminate()
        print("👋 Shutting down.")
