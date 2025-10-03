import time
from typing import Optional, Dict, Any
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .errors import NeoSpeechError
from .audio import Audio
from .voices import Voices
from .models import Models
from .balance import Balance


class NeoSpeech:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.neospeech.io/v1",
        timeout: int = 120,
        max_retries: int = 3,
    ):
        if not api_key:
            raise NeoSpeechError("API key is required", "MISSING_API_KEY", 401)

        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries

        self.audio = Audio(self)
        self.voices = Voices(self)
        self.models = Models(self)
        self.balance = Balance(self)

        self._session = self._create_session()

    def _create_session(self) -> requests.Session:
        session = requests.Session()

        retry_strategy = Retry(
            total=self.max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"],
            backoff_factor=1,
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        return session

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        stream: bool = False,
    ) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "neospeech-python/1.0.0",
        }

        try:
            response = self._session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json,
                timeout=self.timeout,
                stream=stream,
            )

            if not response.ok:
                self._handle_error(response)

            return response

        except requests.exceptions.Timeout:
            raise NeoSpeechError("Request timeout", "TIMEOUT", 408, True)
        except requests.exceptions.RequestException as e:
            raise NeoSpeechError(str(e), "REQUEST_FAILED", 500, False)

    def _handle_error(self, response: requests.Response):
        try:
            error_data = response.json()
            message = error_data.get("message", f"HTTP {response.status_code}")
            code = error_data.get("error_code", "UNKNOWN_ERROR")
            retryable = error_data.get("retryable", response.status_code >= 500)
        except ValueError:
            message = f"HTTP {response.status_code}"
            code = "UNKNOWN_ERROR"
            retryable = response.status_code >= 500

        raise NeoSpeechError(message, code, response.status_code, retryable)

    def close(self):
        self._session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
