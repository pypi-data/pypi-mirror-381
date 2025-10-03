class NeoSpeechError(Exception):
    def __init__(self, message: str, code: str = None, status: int = None, retryable: bool = False):
        super().__init__(message)
        self.message = message
        self.code = code
        self.status = status
        self.retryable = retryable

    def is_client_error(self) -> bool:
        return self.status is not None and 400 <= self.status < 500

    def is_server_error(self) -> bool:
        return self.status is not None and self.status >= 500

    def is_rate_limit_error(self) -> bool:
        return self.status == 429

    def is_auth_error(self) -> bool:
        return self.status in (401, 403)

    def __str__(self) -> str:
        return f"NeoSpeechError(code={self.code}, status={self.status}): {self.message}"
