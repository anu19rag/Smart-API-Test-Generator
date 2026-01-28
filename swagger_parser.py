import json


class SwaggerParser:
    def __init__(self, file_path):
        with open(file_path) as f:
            self.spec = json.load(f)

    def get_endpoints(self):
        endpoints = []

        paths = self.spec.get("paths", {})

        for path, methods in paths.items():
            for method, details in methods.items():
                endpoints.append({
                    "path": path,
                    "method": method.upper(),
                    "params": details.get("parameters", []),
                    "requestBody": details.get("requestBody", {})
                })

        return endpoints
