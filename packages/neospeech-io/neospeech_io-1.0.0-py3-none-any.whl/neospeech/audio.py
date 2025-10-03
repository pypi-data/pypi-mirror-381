from typing import Iterator, Optional
from .errors import NeoSpeechError


class Audio:
    def __init__(self, client):
        self._client = client

    def speech(
        self,
        input: str,
        voice: str,
        model: str = "aurora-4",
        pitch: Optional[str] = None,
        style: Optional[str] = None,
        style_degree: Optional[str] = None,
        lang: Optional[str] = None,
    ) -> bytes:
        if not input:
            raise NeoSpeechError("Input text is required", "MISSING_INPUT", 400)

        if not voice:
            raise NeoSpeechError("Voice is required", "MISSING_VOICE", 400)

        if len(input) > 5000:
            raise NeoSpeechError(
                "Input exceeds 5000 character limit", "TEXT_TOO_LONG", 400
            )

        payload = {"input": input, "voice": voice, "model": model}

        if pitch:
            payload["pitch"] = pitch
        if style:
            payload["style"] = style
        if style_degree:
            payload["styleDegree"] = style_degree
        if lang:
            payload["lang"] = lang

        response = self._client._request("POST", "/audio/speech", json=payload)
        return response.content

    def stream(
        self,
        input: str,
        voice: str,
        model: str = "aurora-4",
        pitch: Optional[str] = None,
        style: Optional[str] = None,
        style_degree: Optional[str] = None,
        lang: Optional[str] = None,
        chunk_size: int = 8192,
    ) -> Iterator[bytes]:
        if not input:
            raise NeoSpeechError("Input text is required", "MISSING_INPUT", 400)

        if not voice:
            raise NeoSpeechError("Voice is required", "MISSING_VOICE", 400)

        if len(input) > 5000:
            raise NeoSpeechError(
                "Input exceeds 5000 character limit", "TEXT_TOO_LONG", 400
            )

        payload = {"input": input, "voice": voice, "model": model}

        if pitch:
            payload["pitch"] = pitch
        if style:
            payload["style"] = style
        if style_degree:
            payload["styleDegree"] = style_degree
        if lang:
            payload["lang"] = lang

        response = self._client._request(
            "POST", "/audio/stream", json=payload, stream=True
        )

        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                yield chunk
