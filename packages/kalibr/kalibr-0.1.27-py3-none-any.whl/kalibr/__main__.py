# kalibr/__main__.py

import typer
import uvicorn
import sys
import importlib.util
from pathlib import Path

def main():
    app = typer.Typer()
    
    @app.command()
    def serve(
        file: str = typer.Argument(..., help="Python file with Kalibr app"),
        host: str = typer.Option("0.0.0.0", "--host", "-h"),
        port: int = typer.Option(8000, "--port", "-p")
    ):
        """Serve a Kalibr-powered API"""
        
        # Load the user's file
        file_path = Path(file).resolve()
        if not file_path.exists():
            print(f"❌ Error: {file} not found")
            raise typer.Exit(1)
        
        # Import the module dynamically
        spec = importlib.util.spec_from_file_location("user_app", file_path)
        if not spec or not spec.loader:
            print(f"❌ Error: Could not load {file}")
            raise typer.Exit(1)
            
        module = importlib.util.module_from_spec(spec)
        sys.modules["user_app"] = module
        
        try:
            spec.loader.exec_module(module)
        except Exception as e:
            print(f"❌ Error loading {file}: {e}")
            raise typer.Exit(1)
        
        # Find the Kalibr instance (look for any Kalibr object)
        from kalibr import Kalibr
        kalibr_instance = None
        
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, Kalibr):
                kalibr_instance = attr
                break
        
        if not kalibr_instance:
            print(f"❌ No Kalibr instance found in {file}")
            print("👉 Make sure your file has something like:\n\n  sdk = Kalibr()")
            raise typer.Exit(1)
        
        # Get the FastAPI app from the Kalibr instance
        fastapi_app = kalibr_instance.get_app()
        
        print(f"🚀 Starting Kalibr server from {file}")
        print(f"📍 GPT (OpenAPI schema): http://{host}:{port}/openapi.json")
        print(f"📍 Claude (MCP manifest): http://{host}:{port}/mcp.json")
        print(f"📍 Swagger UI (human docs): http://{host}:{port}/docs")
        print(f"🔌 Actions registered: {list(kalibr_instance.actions.keys())}")
        
        # Run the FastAPI app
        uvicorn.run(fastapi_app, host=host, port=port)
    
    @app.command()
    def init():
        """Create a sample Kalibr app file"""
        sample = '''from kalibr import Kalibr

# Create your SDK instance
sdk = Kalibr(title="My API", base_url="http://localhost:8000")

# Define your actions - they work with both Claude and GPT!
@sdk.action("hello", "Say hello to someone")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}

@sdk.action("add_contact", "Add a contact to CRM")
def add_contact(name: str, email: str, company: str = ""):
    # Your actual business logic here
    return {
        "status": "success",
        "contact": {
            "name": name,
            "email": email,
            "company": company
        }
    }

# Run with: kalibr serve this_file.py
'''
        with open("kalibr_app.py", "w") as f:
            f.write(sample)
        print("✅ Created kalibr_app.py")
        print("👉 Run it with: kalibr serve kalibr_app.py")
    
    app()

if __name__ == "__main__":
    main()
