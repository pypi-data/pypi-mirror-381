# kalibr/kalibr_sdk.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# ----------------------------
# Pydantic models
# ----------------------------
class Contact(BaseModel):
    name: str
    email: str

# ----------------------------
# Kalibr wrapper
# ----------------------------
class Kalibr:
    """Wrapper to manage Kalibr FastAPI app."""

    def __init__(self):
        self.app = FastAPI(title="Kalibr Demo", version="0.1.18")
        self.contacts = []
        self._register_routes()

    def _register_routes(self):
        app = self.app

        @app.get("/")
        def root():
            return {"message": "Welcome to Kalibr Demo SDK"}

        @app.get("/proxy/list_contacts")
        def list_contacts():
            return {"contacts": self.contacts}

        @app.post("/proxy/add_contact")
        def add_contact(contact: Contact):
            self.contacts.append(contact.dict())
            return {"message": "Contact added", "contact": contact.dict()}

        # ----------------------------
        # MCP manifest endpoint
        # ----------------------------
        @app.get("/mcp.json")
        def mcp_manifest():
            manifest = {
                "mcp": "1.0",
                "name": "kalibr_demo",
                "description": "Demo MCP server powered by Kalibr",
                "tools": [
                    {
                        "name": "add_contact",
                        "description": "Add a contact to CRM",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "email": {"type": "string"}
                            },
                            "required": ["name", "email"]
                        }
                    },
                    {
                        "name": "list_contacts",
                        "description": "List contacts from CRM",
                        "input_schema": {
                            "type": "object",
                            "properties": {}
                        }
                    }
                ]
            }
            return JSONResponse(content=manifest)


# ----------------------------
# Module-level app for Uvicorn
# ----------------------------
kalibr_instance = Kalibr()
app = kalibr_instance.app
