# kalibr/__main__.py

import typer
import uvicorn

def main():
    app = typer.Typer()
    
    @app.command()
    def serve(
        host: str = typer.Option("0.0.0.0", "--host", "-h"),
        port: int = typer.Option(8000, "--port", "-p")
    ):
        """Run the Kalibr demo FastAPI server."""
        print(f"Starting server on {host}:{port}")
        from .kalibr_sdk import app as fastapi_app
        uvicorn.run(fastapi_app, host=host, port=port)
    
    @app.command()
    def version():
        """Show version"""
        print("kalibr version 0.1.24")
    
    # This is the key - actually run the app
    app()

if __name__ == "__main__":
    main()
