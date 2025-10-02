import argparse
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi

app = FastAPI(title="Kalibr Demo", version="0.1.0")

# === DEMO ACTION ===
@app.post("/proxy/add_contact")
async def add_contact(request: Request):
    """Demo endpoint: add a contact (name + email)"""
    body = await request.json()
    name = body.get("name")
    email = body.get("email")
    # Just echo for demo – in real version this would call Airtable
    return {"status": "ok", "contact": {"name": name, "email": email}}

# === CUSTOM OPENAPI (for GPT) ===
@app.get("/openapi.json")
async def custom_openapi():
    return get_openapi(
        title="Kalibr Demo",
        version="0.1.0",
        description="Demo API made agent-ready by Kalibr",
        routes=app.routes,
        servers=[{"url": "https://YOUR_NGROK_URL"}]  # 🔑 GPT requires this
    )

# === CHATGPT MANIFEST (legacy ai-plugin.json) ===
@app.get("/.well-known/ai-plugin.json")
async def serve_manifest():
    manifest = {
        "schema_version": "v1",
        "name_for_human": "Kalibr Demo",
        "name_for_model": "kalibr_demo",
        "description_for_human": "Demo API made agent-ready by Kalibr",
        "description_for_model": "Demo API made agent-ready by Kalibr",
        "auth": {"type": "none"},
        "api": {
            "type": "openapi",
            "url": "https://YOUR_NGROK_URL/openapi.json"
        },
        "logo_url": "https://kalibr.systems/logo.png",
        "contact_email": "hello@kalibr.systems",
        "legal_info_url": "https://kalibr.systems/legal"
    }
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=manifest, headers=headers)

# === CLAUDE MCP MANIFEST ===
@app.get("/mcp.json")
async def serve_mcp():
    mcp_manifest = {
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
                "server": {"url": "https://YOUR_NGROK_URL/proxy/add_contact"}
            }
        ]
    }
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=mcp_manifest, headers=headers)

# === ENTRYPOINT ===
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    print("🚀 Starting Kalibr Demo server…")
    print("⚠️ Replace YOUR_NGROK_URL with the real one shown by ngrok")
    print(f"📋 ChatGPT OpenAPI:  https://<YOUR_NGROK_URL>/openapi.json")
    print(f"📋 Claude MCP:       https://<YOUR_NGROK_URL>/mcp.json")

    uvicorn.run("kalibr.__main__:app", host="0.0.0.0", port=args.port, reload=False)

if __name__ == "__main__":
    main()
