import typer
import uvicorn
import sys
import importlib.util
from pathlib import Path

app = typer.Typer()

@app.command()
def serve(
    file: str = typer.Argument("kalibr_app.py", help="Python file with Kalibr app"),
    host: str = typer.Option("0.0.0.0", "--host", "-h"),
    port: int = typer.Option(8000, "--port", "-p"),
    base_url: str = typer.Option("http://localhost:8000", "--base-url", "-b")
):
    """Serve a Kalibr-powered API."""

    file_path = Path(file).resolve()
    if not file_path.exists():
        print(f"❌ Error: {file} not found")
        raise typer.Exit(1)

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

    from kalibr import Kalibr
    kalibr_instance = None

    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if isinstance(attr, Kalibr):
            kalibr_instance = attr
            # override base_url if flag is passed
            kalibr_instance.base_url = base_url
            break

    if not kalibr_instance:
        print(f"❌ Error: No Kalibr instance found in {file}")
        raise typer.Exit(1)

    fastapi_app = kalibr_instance.get_app()

    print(f"🚀 Starting Kalibr server from {file}")
    print(f"📍 GPT (OpenAPI): {base_url}/openapi.json")
    print(f"📍 Claude (MCP): {base_url}/mcp.json")
    print(f"📍 Swagger UI:   {base_url}/docs")
    print(f"🔌 Actions registered: {list(kalibr_instance.actions.keys())}")

    uvicorn.run(fastapi_app, host=host, port=port)


@app.command()
def init():
    """Generate a starter Kalibr app file."""
    sample = '''from kalibr import Kalibr

sdk = Kalibr(title="My API", base_url="http://localhost:8000")

@sdk.action("hello", "Say hello to someone")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}"}

@sdk.action("add_contact", "Add a CRM contact")
def add_contact(name: str, email: str):
    return {"status": "success", "contact": {"name": name, "email": email}}
'''
    with open("kalibr_app.py", "w") as f:
        f.write(sample)
    print("✅ Created kalibr_app.py")
    print("Run it with: kalibr serve kalibr_app.py")
    

def main():
    app()

if __name__ == "__main__":
    main()
