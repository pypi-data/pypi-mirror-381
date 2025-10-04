import uvicorn
from .kalibr_sdk import app

def main():
    """Run Kalibr demo server via CLI."""
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
