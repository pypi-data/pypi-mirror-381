from fastapi import FastAPI, Request
from typing import Callable, Dict, Any
import inspect
import json

class Kalibr:
    def __init__(
        self,
        title: str = "Kalibr API",
        version: str = "1.0.0",
        base_url: str = "https://kalibr-demo.fly.dev"  # hosted default
    ):
        self.app = FastAPI(title=title, version=version)
        self.base_url = base_url
        self.actions: Dict[str, Dict[str, Any]] = {}
        self._setup_routes()

    def action(self, name: str, description: str = ""):
        """Decorator to register an action across all AI models."""
        def decorator(func: Callable):
            self.actions[name] = {
                "func": func,
                "description": description,
                "params": self._extract_params(func),
            }

            endpoint_path = f"/proxy/{name}"

            async def endpoint_handler(request: Request):
                body = await request.json() if request.method == "POST" else {}
                params = {**request.query_params, **body}
                result = func(**params)
                return result

            self.app.post(endpoint_path)(endpoint_handler)
            self.app.get(endpoint_path)(endpoint_handler)

            return func
        return decorator

    def _extract_params(self, func: Callable) -> Dict:
        sig = inspect.signature(func)
        params = {}
        for name, param in sig.parameters.items():
            param_type = "string"
            if param.annotation != inspect.Parameter.empty:
                if param.annotation == int:
                    param_type = "integer"
                elif param.annotation == bool:
                    param_type = "boolean"
                elif param.annotation == float:
                    param_type = "number"
            params[name] = {
                "type": param_type,
                "required": param.default == inspect.Parameter.empty,
            }
        return params

    def _setup_routes(self):
        @self.app.get("/")
        def root():
            return {"message": "Kalibr API is running", "actions": list(self.actions.keys())}

        @self.app.get("/mcp.json")
        def mcp_manifest():
            tools = []
            for action_name, action_data in self.actions.items():
                properties = {}
                required = []
                for param_name, param_info in action_data["params"].items():
                    properties[param_name] = {"type": param_info["type"]}
                    if param_info["required"]:
                        required.append(param_name)

                tools.append({
                    "name": action_name,
                    "description": action_data["description"],
                    "input_schema": {
                        "type": "object",
                        "properties": properties,
                        "required": required,
                    },
                    "server": {"url": f"{self.base_url}/proxy/{action_name}"},
                })

            return {"mcp": "1.0", "name": "kalibr", "tools": tools}

        def custom_openapi():
            if self.app.openapi_schema:
                return self.app.openapi_schema

            from fastapi.openapi.utils import get_openapi
            openapi_schema = get_openapi(
                title=self.app.title,
                version=self.app.version,
                routes=self.app.routes,
            )
            openapi_schema["servers"] = [{"url": self.base_url}]

            for path in openapi_schema.get("paths", {}).values():
                for operation in path.values():
                    if "operationId" in operation:
                        operation["operationId"] = operation["operationId"].replace("_proxy_", "")

            self.app.openapi_schema = openapi_schema
            return self.app.openapi_schema

        self.app.openapi = custom_openapi

    def get_app(self):
        return self.app
