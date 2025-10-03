#!/usr/bin/env python3
import argparse
import subprocess
import time
import requests
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi

app = FastAPI(title="Kalibr Demo", version="0.1.0")

# In-memory contacts DB for demo
CONTACTS = []

def get_ngrok_url():
    """
    Query ngrok's local API to get the public HTTPS tunnel.
    """
    try:
        res = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = res.json().get("tunnels", [])
        for t in tunnels:
            if t["public_url"].startswith("https://"):
                return t["public_url"]
    except Exception:
        return None
    return None

@app.get("/")
async def root():
    return {"message": "Kalibr Demo API is running"}

@app.post("/proxy/add_contact")
async def add_contact(request: Request):
    data = await request.json()
    CONTACTS.append(data)
    return {"status": "ok", "added": data}

@app.get("/proxy/list_contacts")
async def list_contacts():
    return {"contacts": CONTACTS}

@app.get("/openapi.json")
async def custom_openapi():
    """
    Generate OpenAPI schema with the *current* ngrok URL injected.
    """
    openapi_schema = get_openapi(
        title="Kalibr Demo API",
        version="0.1.0",
        description="Demo API made agent-ready by Kalibr",
        routes=app.routes,
    )
    ngrok_url = get_ngrok_url()
    if ngrok_url:
        openapi_schema["servers"] = [{"url": ngrok_url}]
    return JSONResponse(openapi_schema)

@app.get("/mcp.json")
async def mcp_manifest():
    """
    Claude MCP manifest. (Claude still needs manual config for now.)
    """
    ngrok_url = get_ngrok_url() or "http://localhost:8000"
    return {
        "mcp": "1.0",
        "name": "kalibr_demo",
        "tools": [
            {
                "name": "add_contact",
                "description": "Add a contact to CRM",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "email": {"type": "string"},
                    },
                    "required": ["name", "email"],
                },
                "server": {"url": f"{ngrok_url}/proxy/add_contact"},
            },
            {
                "name": "list_contacts",
                "description": "List contacts in CRM",
                "input_schema": {"type": "object", "properties": {}},
                "server": {"url": f"{ngrok_url}/proxy/list_contacts"},
            },
        ],
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ngrok", action="store_true", help="Start with ngrok tunnel")
    args = parser.parse_args()

    if args.ngrok:
        print("⏳ Starting ngrok...")
        subprocess.Popen(["ngrok", "http", "8000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)
        url = get_ngrok_url()
        if url:
            print(f"✅ Proxy running at {url}\n")
            print("📋 ChatGPT manifest:")
            print(f"{url}/openapi.json\n")
            print("📋 Claude MCP manifest:")
            print(f"{url}/mcp.json\n")
            print("✨ Your API is now AI-ready!\n")
        else:
            print("⚠️ Could not detect ngrok tunnel. Is ngrok running?")

    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
