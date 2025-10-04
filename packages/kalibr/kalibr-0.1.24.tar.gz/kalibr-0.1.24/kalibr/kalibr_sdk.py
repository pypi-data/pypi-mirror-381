from fastapi import FastAPI
from pydantic import BaseModel

class Contact(BaseModel):
    name: str
    email: str

app = FastAPI(title="Kalibr Demo", version="0.1.19")

@app.get("/")
def root():
    return {"message": "Welcome to Kalibr Demo"}

@app.get("/proxy/list_contacts")
def list_contacts():
    return {"contacts": [{"name": "Alice", "email": "alice@example.com"}]}

@app.post("/proxy/add_contact")
def add_contact(contact: Contact):
    return {"status": "added", "contact": contact}
