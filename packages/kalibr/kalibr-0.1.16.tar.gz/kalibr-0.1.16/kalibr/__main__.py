# kalibr/__main__.py
import uvicorn
from .kalibr_sdk import kalibr_instance

def main():
    uvicorn.run(kalibr_instance.app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
