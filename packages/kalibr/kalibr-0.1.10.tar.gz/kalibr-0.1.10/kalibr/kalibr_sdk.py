# kalibr/kalibr_sdk.py
import subprocess
import json
import time
import threading
import requests
import uvicorn
from fastapi import FastAPI, Request

class Kalibr:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.actions = {}
        self.app = FastAPI()
        self._register_routes()

    def add_action(self, name, path, method, params=None):
        self.actions[name] = {
            "path": path,
            "method": method.upper(),
            "params": params or {}
        }

    def _register_routes(self):
        @self.app.post("/proxy/{action_name}")
        async def proxy(action_name: str, request: Request):
            if action_name not in self.actions:
                return {"error": "Unknown action"}

            action = self.actions[action_name]
            url = f"{self.base_url}{action['path']}"
            headers = {}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            if action["method"] == "GET":
                resp = requests.get(url, headers=headers)
            elif action["method"] == "POST":
                data = await request.json()
                resp = requests.post(url, json=data, headers=headers)
            else:
                return {"error": f"Unsupported method {action['method']}"}
            return resp.json()

    def _start_proxy(self):
        uvicorn.run(self.app, host="0.0.0.0", port=8000)

    def _start_ngrok(self):
        ngrok = subprocess.Popen(
            ["ngrok", "http", "8000"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(3)
        tunnels = requests.get("http://localhost:4040/api/tunnels").json()
        url = tunnels["tunnels"][0]["public_url"]
        return ngrok, url

    def _generate_gpt_config(self, public_url):
        cfg = {
            "schema_version": "v1",
            "name_for_model": "kalibr_demo",
            "name_for_human": "Kalibr Demo",
            "description_for_model": "Demo API made agent-ready by Kalibr",
            "description_for_human": "Use this to test a demo API",
            "auth": {"type": "none"},
            "api": {
                "type": "openapi",
                "url": f"{public_url}/openapi.json"
            }
        }
        with open("gpt_config.json", "w") as f:
            json.dump(cfg, f, indent=2)
        return cfg

    def _generate_claude_config(self, public_url):
        cfg = {
            "mcp": "1.0",
            "name": "kalibr_demo",
            "tools": [
                {
                    "name": "add_contact",
                    "description": "Add a contact to Airtable CRM",
                    "input_schema": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "email": {"type": "string"}
                        },
                        "required": ["name", "email"]
                    },
                    "server": {"url": f"{public_url}/proxy/add_contact"}
                }
            ]
        }
        with open("claude_config.json", "w") as f:
            json.dump(cfg, f, indent=2)
        return cfg

    def deploy(self):
        proxy_thread = threading.Thread(target=self._start_proxy, daemon=True)
        proxy_thread.start()

        print("⏳ Starting ngrok...")
        ngrok, url = self._start_ngrok()
        print(f"✅ Proxy running at {url}")

        gpt_cfg = self._generate_gpt_config(url)
        claude_cfg = self._generate_claude_config(url)

        print("\n📋 COPY THIS TO CHATGPT:")
        print(json.dumps(gpt_cfg, indent=2))
        print("\n📋 COPY THIS TO CLAUDE:")
        print(json.dumps(claude_cfg, indent=2))

        print("\n✨ Your API is now AI-ready!")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping...")
            ngrok.terminate()
