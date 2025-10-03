import uvicorn
from kalibr_demo_sdk import app

def main():
    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()
