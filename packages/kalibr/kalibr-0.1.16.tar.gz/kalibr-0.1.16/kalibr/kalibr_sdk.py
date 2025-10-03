# kalibr/kalibr_sdk.py
from fastapi import FastAPI
from pydantic import BaseModel

class Contact(BaseModel):
    name: str
    email: str

class Kalibr:
    """Simple wrapper class to manage Kalibr integrations."""
    def __init__(self):
        self.app = FastAPI(title="Kalibr Demo", version="0.1.15")
        self.contacts = []

        @self.app.get("/")
        def root():
            return {"status": "ok", "message": "Kalibr SDK is running"}

        @self.app.get("/proxy/list_contacts")
        def list_contacts():
            return {"contacts": self.contacts}

        @self.app.post("/proxy/add_contact")
        def add_contact(contact: Contact):
            self.contacts.append(contact.dict())
            return {"status": "success", "contact": contact.dict()}

# Global instance for FastAPI runner
kalibr_instance = Kalibr()
app = kalibr_instance.app
