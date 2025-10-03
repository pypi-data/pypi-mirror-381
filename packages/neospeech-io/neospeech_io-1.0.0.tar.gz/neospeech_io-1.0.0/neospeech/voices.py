from typing import Optional, Dict, Any


class Voices:
    def __init__(self, client):
        self._client = client

    def list(
        self,
        gender: Optional[str] = None,
        locale: Optional[str] = None,
        search: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        params = {}

        if gender:
            params["gender"] = gender
        if locale:
            params["locale"] = locale
        if search:
            params["search"] = search
        if limit:
            params["limit"] = str(limit)
        if offset:
            params["offset"] = str(offset)

        response = self._client._request("GET", "/voices/list", params=params)
        return response.json()["data"]
