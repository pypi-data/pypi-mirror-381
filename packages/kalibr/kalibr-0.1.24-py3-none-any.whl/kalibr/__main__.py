# kalibr/__main__.py

import typer
import uvicorn

app = typer.Typer(help="Kalibr SDK CLI")

@app.command()
def serve(
    host: str = typer.Option("0.0.0.0", "--host", "-h", help="Host to bind to"),
    port: int = typer.Option(8000, "--port", "-p", help="Port to bind to")
):
    """
    Run the Kalibr demo FastAPI server.
    """
    from .kalibr_sdk import app as fastapi_app
    uvicorn.run(fastapi_app, host=host, port=port)

def main():
    app()

if __name__ == "__main__":
    main()
