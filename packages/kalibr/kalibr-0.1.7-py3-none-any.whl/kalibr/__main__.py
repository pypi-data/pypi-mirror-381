import json
import subprocess
import sys
import threading
import time

import requests
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# === Globals ===
PUBLIC_URL = None
app = FastAPI(title="Kalibr Demo API")


# ---------------------------
# DEMO ACTION
# ---------------------------
@app.post("/proxy/add_contact")
async def add_contact(request: Request):
    """Mock add_contact action (would connect to Airtable in real SaaS)."""
    data = await request.json()
    return {"status": "success", "contact": data}


# ---------------------------
# CHATGPT PLUGIN MANIFEST
# ---------------------------
@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    return JSONResponse({
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
    })


# ---------------------------
# CLAUDE MCP MANIFEST
# ---------------------------
@app.get("/mcp.json")
async def mcp_manifest():
    return JSONResponse({
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
                "server": {
                    "url": f"{PUBLIC_URL}/proxy/add_contact" if PUBLIC_URL else "http://localhost:8000/proxy/add_contact"
                }
            }
        ]
    })


# ---------------------------
# INTERNAL HELPERS
# ---------------------------
def start_server():
    """Run FastAPI app on port 8000."""
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except OSError as e:
        if e.errno == 48:  # Port in use
            print("⚠️  Port 8000 already in use. Kill the other process or free the port.")
            sys.exit(1)
        raise


def main():
    global PUBLIC_URL

    print("🚀 Starting Kalibr Demo...")

    # Start FastAPI in background
    threading.Thread(target=start_server, daemon=True).start()
    time.sleep(2)

    # Start ngrok
    print("⏳ Starting ngrok...")
    ngrok = subprocess.Popen(["ngrok", "http", "8000"],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    time.sleep(3)

    # Fetch ngrok public URL
    try:
        resp = requests.get("http://localhost:4040/api/tunnels")
        PUBLIC_URL = resp.json()["tunnels"][0]["public_url"]
    except Exception as e:
        print("❌ Could not fetch ngrok URL:", e)
        sys.exit(1)

    print(f"✅ Proxy running at {PUBLIC_URL}\n")

    # Print where manifests live
    print("📋 ChatGPT manifest:")
    print(f"{PUBLIC_URL}/.well-known/ai-plugin.json\n")

    print("📋 Claude MCP manifest:")
    print(f"{PUBLIC_URL}/mcp.json\n")

    print("✨ Your API is now AI-ready! Press Ctrl+C to stop.\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        ngrok.terminate()
        print("👋 Shutting down.")


if __name__ == "__main__":
    main()
