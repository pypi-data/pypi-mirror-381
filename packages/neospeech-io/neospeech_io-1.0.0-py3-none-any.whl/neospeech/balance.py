from typing import Dict, Any


class Balance:
    def __init__(self, client):
        self._client = client

    def get(self) -> Dict[str, Any]:
        response = self._client._request("GET", "/balance")
        return response.json()["data"]
