import typer
import uvicorn
from kalibr.kalibr_sdk import app

cli = typer.Typer(help="Kalibr SDK CLI")

@cli.command()
def serve(host: str = "0.0.0.0", port: int = 8000):
    """
    Start the Kalibr API server.
    """
    uvicorn.run(app, host=host, port=port, reload=False)

def main():
    cli()

if __name__ == "__main__":
    main()
