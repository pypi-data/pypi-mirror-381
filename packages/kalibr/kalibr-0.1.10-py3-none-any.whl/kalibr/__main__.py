import argparse
import uvicorn
import requests
import subprocess
import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi

app = FastAPI(title="Kalibr Demo", version="0.1.0")

# Store the ngrok URL globally
NGROK_URL = None

def get_ngrok_url():
    """Get the current ngrok tunnel URL"""
    try:
        response = requests.get("http://localhost:4040/api/tunnels")
        tunnels = response.json()
        if tunnels["tunnels"]:
            return tunnels["tunnels"][0]["public_url"]
    except:
        pass
    return "https://YOUR_NGROK_URL"  # Fallback

# === DEMO ACTION ===
@app.post("/proxy/add_contact")
async def add_contact(request: Request):
    """Demo endpoint: add a contact to Airtable CRM"""
    body = await request.json()
    name = body.get("name", "Unknown")
    email = body.get("email", "")
    company = body.get("company", "")
    
    # In production, this would actually call Airtable API
    # For demo, we just echo back
    return {
        "status": "success",
        "message": f"Added contact: {name}",
        "contact": {
            "name": name,
            "email": email,
            "company": company,
            "added_at": "2025-01-20T12:00:00Z"
        }
    }

@app.get("/proxy/list_contacts")
async def list_contacts():
    """Demo endpoint: list CRM contacts"""
    # Mock data for demo
    return {
        "contacts": [
            {"name": "John Doe", "email": "john@example.com", "company": "Acme Corp"},
            {"name": "Jane Smith", "email": "jane@example.com", "company": "Tech Inc"}
        ],
        "total": 2
    }

# === DYNAMIC OPENAPI (for GPT) ===
@app.get("/openapi.json")
async def custom_openapi():
    # Get the current ngrok URL dynamically
    current_url = get_ngrok_url()
    
    openapi_schema = get_openapi(
        title="Kalibr Demo API",
        version="0.1.0",
        description="Demo API made agent-ready by Kalibr SDK",
        routes=app.routes
    )
    
    # CRITICAL: Add servers block with actual ngrok URL
    openapi_schema["servers"] = [{"url": current_url}]
    
    # Add proper path definitions
    if "paths" not in openapi_schema:
        openapi_schema["paths"] = {}
    
    # Ensure our endpoints are properly documented
    openapi_schema["paths"]["/proxy/add_contact"] = {
        "post": {
            "summary": "Add a contact to CRM",
            "operationId": "add_contact",
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string", "description": "Contact name"},
                                "email": {"type": "string", "description": "Contact email"},
                                "company": {"type": "string", "description": "Company name"}
                            },
                            "required": ["name"]
                        }
                    }
                }
            },
            "responses": {
                "200": {
                    "description": "Contact added successfully",
                    "content": {
                        "application/json": {
                            "schema": {"type": "object"}
                        }
                    }
                }
            }
        }
    }
    
    openapi_schema["paths"]["/proxy/list_contacts"] = {
        "get": {
            "summary": "List all CRM contacts",
            "operationId": "list_contacts",
            "responses": {
                "200": {
                    "description": "List of contacts",
                    "content": {
                        "application/json": {
                            "schema": {"type": "object"}
                        }
                    }
                }
            }
        }
    }
    
    return JSONResponse(content=openapi_schema)

# === CHATGPT MANIFEST (legacy) ===
@app.get("/.well-known/ai-plugin.json")
async def serve_manifest():
    current_url = get_ngrok_url()
    
    manifest = {
        "schema_version": "v1",
        "name_for_human": "Kalibr Demo",
        "name_for_model": "kalibr_demo",
        "description_for_human": "Demo API made agent-ready by Kalibr",
        "description_for_model": "Use this to add contacts to CRM and list existing contacts",
        "auth": {"type": "none"},
        "api": {
            "type": "openapi",
            "url": f"{current_url}/openapi.json"  # Dynamic URL
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
    current_url = get_ngrok_url()
    
    mcp_manifest = {
        "mcp": "1.0",
        "name": "kalibr_demo",
        "version": "0.1.0",
        "description": "Kalibr Demo - Airtable CRM connector",
        "tools": [
            {
                "name": "add_to_crm",
                "description": "Add a contact to Airtable CRM",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Contact name"},
                        "email": {"type": "string", "description": "Contact email"},
                        "company": {"type": "string", "description": "Company name"}
                    },
                    "required": ["name"]
                },
                "server": {"url": f"{current_url}/proxy/add_contact"}
            },
            {
                "name": "list_crm_contacts",
                "description": "List all contacts in CRM",
                "input_schema": {
                    "type": "object",
                    "properties": {}
                },
                "server": {"url": f"{current_url}/proxy/list_contacts"}
            }
        ]
    }
    
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=mcp_manifest, headers=headers)

# === ROOT ENDPOINT ===
@app.get("/")
async def root():
    current_url = get_ngrok_url()
    return {
        "message": "Kalibr Demo Server Running",
        "endpoints": {
            "openapi": f"{current_url}/openapi.json",
            "chatgpt_manifest": f"{current_url}/.well-known/ai-plugin.json",
            "claude_mcp": f"{current_url}/mcp.json"
        },
        "actions": [
            "POST /proxy/add_contact - Add a contact to CRM",
            "GET /proxy/list_contacts - List all contacts"
        ]
    }

# === ENTRYPOINT ===
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--ngrok", action="store_true", help="Start ngrok tunnel")
    args = parser.parse_args()
    
    print("🚀 Starting Kalibr Demo Server...")
    
    if args.ngrok:
        print("🌐 Starting ngrok tunnel...")
        ngrok_process = subprocess.Popen(
            ["ngrok", "http", str(args.port)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(3)  # Give ngrok time to start
        
        ngrok_url = get_ngrok_url()
        if ngrok_url != "https://YOUR_NGROK_URL":
            print(f"✅ ngrok tunnel: {ngrok_url}")
            print("\n📋 FOR CHATGPT:")
            print(f"   Add this URL in Custom GPT Actions: {ngrok_url}/openapi.json")
            print("\n📋 FOR CLAUDE:")
            print(f"   MCP manifest available at: {ngrok_url}/mcp.json")
            print("   (Note: Claude requires manual config in servers.json)")
        else:
            print("⚠️  Could not get ngrok URL. Make sure ngrok is running.")
    
    print(f"\n🎯 Server running on http://localhost:{args.port}")
    print("   Press Ctrl+C to stop\n")
    
    uvicorn.run("kalibr.__main__:app", host="0.0.0.0", port=args.port, reload=False)

if __name__ == "__main__":
    main()
