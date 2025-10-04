from fastapi import FastAPI
from pydantic import BaseModel, create_model
from typing import Callable, Dict, Any
import inspect

class Kalibr:
    def __init__(self, title="Kalibr API", version="1.0.0", base_url="http://localhost:8000"):
        self.app = FastAPI(title=title, version=version)
        self.base_url = base_url
        self.actions: Dict[str, Dict[str, Any]] = {}
        self._setup_routes()

    def action(self, name: str, description: str = ""):
        """Decorator to register an action that works across all AI models"""
        def decorator(func: Callable):
            sig = inspect.signature(func)
            fields = {}
            for param_name, param in sig.parameters.items():
                anno = param.annotation if param.annotation != inspect.Parameter.empty else str
                default = ... if param.default == inspect.Parameter.empty else param.default
                fields[param_name] = (anno, default)

            # Build a Pydantic model dynamically
            InputModel = create_model(f"{name.title()}Input", **fields)

            async def endpoint_handler(body: InputModel):
                data = body.dict()
                result = func(**data)
                return result

            path = f"/proxy/{name}"
            self.app.post(path)(endpoint_handler)

            self.actions[name] = {
                "func": func,
                "description": description,
                "model": InputModel,
            }
            return func
        return decorator

    def _setup_routes(self):
        @self.app.get("/")
        def root():
            return {"message": "Kalibr API running", "actions": list(self.actions.keys())}

        @self.app.get("/mcp.json")
        def mcp_manifest():
            tools = []
            for name, meta in self.actions.items():
                props, required = {}, []
                for field_name, field in meta["model"].model_fields.items():
                    ftype = "string"
                    if field.annotation is int:
                        ftype = "integer"
                    elif field.annotation is float:
                        ftype = "number"
                    elif field.annotation is bool:
                        ftype = "boolean"
                    props[field_name] = {"type": ftype}
                    if field.default is Ellipsis:
                        required.append(field_name)
                tools.append({
                    "name": name,
                    "description": meta["description"],
                    "input_schema": {"type": "object", "properties": props, "required": required},
                    "server": {"url": f"{self.base_url}/proxy/{name}"}
                })
            return {"mcp": "1.0", "name": "kalibr", "tools": tools}

        from fastapi.openapi.utils import get_openapi
        def custom_openapi():
            if self.app.openapi_schema:
                return self.app.openapi_schema
            schema = get_openapi(
                title=self.app.title,
                version=self.app.version,
                routes=self.app.routes,
            )
            schema["servers"] = [{"url": self.base_url}]
            self.app.openapi_schema = schema
            return schema
        self.app.openapi = custom_openapi

    def get_app(self):
        return self.app
