# kalibr/__main__.py
import uvicorn
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "serve":
        # run the FastAPI server
        uvicorn.run("kalibr.kalibr_sdk:app", host="0.0.0.0", port=8000, reload=False)
    else:
        print("Usage: kalibr serve")

if __name__ == "__main__":
    main()
