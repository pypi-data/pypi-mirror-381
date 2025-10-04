# kalibr/__main__.py

import typer
import uvicorn

from .kalibr_sdk import app

cli = typer.Typer(help="Kalibr CLI")

@cli.command()
def serve(host: str = "0.0.0.0", port: int = 8000, reload: bool = False):
    """Run the Kalibr FastAPI server."""
    uvicorn.run(app, host=host, port=port, reload=reload)

def main():
    cli()

if __name__ == "__main__":
    main()
