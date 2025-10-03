# kalibr/kalibr_sdk.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Kalibr Demo", version="0.1.15")

# In-memory demo store
CONTACTS = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
]

class Contact(BaseModel):
    name: str
    email: str

@app.get("/")
def root():
    return {"message": "Kalibr Demo API is running"}

@app.get("/proxy/list_contacts")
def list_contacts():
    return CONTACTS

@app.post("/proxy/add_contact")
def add_contact(contact: Contact):
    CONTACTS.append(contact.dict())
    return {"status": "success", "contact": contact.dict()}

# ChatGPT manifest
@app.get("/.well-known/ai-plugin.json")
def plugin_manifest():
    return {
        "schema_version": "v1",
        "name_for_human": "Kalibr Demo",
        "name_for_model": "kalibr_demo",
        "description_for_human": "Demo Kalibr connector API",
        "description_for_model": "Exposes a simple contacts API via Kalibr",
        "auth": {"type": "none"},
        "api": {"type": "openapi", "url": "http://localhost:8000/openapi.json"},
        "logo_url": "https://kalibr.systems/logo.png",
        "contact_email": "dev@kalibr.systems",
        "legal_info_url": "https://kalibr.systems/legal"
    }

# Claude MCP manifest
@app.get("/mcp.json")
def mcp_manifest():
    return {
        "mcp": "1.0",
        "name": "kalibr_demo",
        "tools": [
            {
                "name": "list_contacts",
                "description": "List CRM contacts",
                "input_schema": {"type": "object", "properties": {}},
                "server": {"url": "http://localhost:8000/proxy/list_contacts"},
            },
            {
                "name": "add_contact",
                "description": "Add CRM contact",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "email": {"type": "string"}
                    },
                    "required": ["name", "email"]
                },
                "server": {"url": "http://localhost:8000/proxy/add_contact"},
            },
        ],
    }
