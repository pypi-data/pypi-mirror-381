from typing import Dict, Any


class Models:
    def __init__(self, client):
        self._client = client

    def list(self) -> Dict[str, Any]:
        response = self._client._request("GET", "/models/list")
        return response.json()["data"]
