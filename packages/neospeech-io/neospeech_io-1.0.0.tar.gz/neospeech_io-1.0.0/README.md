# NeoSpeech Python SDK

Official Python SDK for the NeoSpeech Text-to-Speech API. Convert text into natural-sounding speech with 50+ voices in 90+ languages.

## Installation

```bash
pip install neospeech-io
```

## Quick Start

```python
from neospeech import NeoSpeech

neospeech = NeoSpeech('your-api-key')

# Generate speech
audio = neospeech.audio.speech(
    input="Hello, world!",
    voice="lyra",
    model="aurora-4"
)

# Save to file
with open('output.mp3', 'wb') as f:
    f.write(audio)
```

## Authentication

Get your API key from the [NeoSpeech dashboard](https://neospeech.io). Pro or Business plan required.

```python
import os
from neospeech import NeoSpeech

neospeech = NeoSpeech(os.getenv('NEOSPEECH_API_KEY'))
```

## Usage

### Generate Speech

Convert text to audio with high-quality voices:

```python
audio = neospeech.audio.speech(
    input="Welcome to NeoSpeech!",
    voice="lyra",
    model="aurora-4"
)

with open('speech.mp3', 'wb') as f:
    f.write(audio)
```

### Advanced Options

Customize voice characteristics:

```python
audio = neospeech.audio.speech(
    input="Professional narration",
    voice="emma",
    model="aurora-3.5",
    pitch="+10%",
    style="cheerful",
    style_degree="1.5",
    lang="en-US"
)
```

### Stream Speech

Stream audio in real-time for lower latency:

```python
stream = neospeech.audio.stream(
    input="This is streaming audio",
    voice="kai",
    model="turbo-3"
)

with open('stream.mp3', 'wb') as f:
    for chunk in stream:
        f.write(chunk)
        print(f"Received {len(chunk)} bytes")
```

### List Voices

Explore available voices:

```python
voices_data = neospeech.voices.list(
    gender="female",
    locale="en-US",
    limit=10
)

for voice in voices_data['voices']:
    print(f"{voice['name']} ({voice['id']}): {voice['language']}")
```

Filter and search:

```python
# Search by name
results = neospeech.voices.list(search="lyra")

# Filter by gender and locale
female_voices = neospeech.voices.list(
    gender="female",
    locale="en-GB"
)

# Paginate results
page1 = neospeech.voices.list(limit=20, offset=0)
page2 = neospeech.voices.list(limit=20, offset=20)
```

### List Models

Get available audio models:

```python
models_data = neospeech.models.list()

for model in models_data['models']:
    print(f"{model['name']}: {model['quality']} quality")
```

### Check Balance

Monitor your credit usage:

```python
balance_data = neospeech.balance.get()

print(f"Remaining credits: {balance_data['balance']['remaining_credits']}")
print(f"Plan: {balance_data['plan']['type']}")
print(f"Usage: {balance_data['usage_summary']['current_period_usage']}")
```

## API Reference

### NeoSpeech

Constructor options:

```python
neospeech = NeoSpeech(
    api_key='your-api-key',
    base_url='https://api.neospeech.io/v1',  # Default
    timeout=120,                              # Seconds
    max_retries=3                             # Retry failed requests
)
```

### audio.speech()

Generate complete audio file.

**Parameters:**
- `input` (str, required) - Text to convert (max 5000 characters)
- `voice` (str, required) - Voice ID
- `model` (str, optional) - Model: `aurora-4`, `aurora-3.5`, `aurora-3`, `turbo-3`, `mini-2`
- `pitch` (str, optional) - Pitch adjustment (e.g., `+10%`, `-5%`)
- `style` (str, optional) - Voice style
- `style_degree` (str, optional) - Style intensity
- `lang` (str, optional) - Language code

**Returns:** `bytes` - Audio data

### audio.stream()

Stream audio in real-time.

**Parameters:** Same as `audio.speech()` plus:
- `chunk_size` (int, optional) - Chunk size in bytes (default: 8192)

**Returns:** `Iterator[bytes]` - Audio chunks

### voices.list()

List available voices.

**Parameters:**
- `gender` (str, optional) - Filter by `male` or `female`
- `locale` (str, optional) - Filter by locale (e.g., `en-US`)
- `search` (str, optional) - Search by name or tags
- `limit` (int, optional) - Results per page
- `offset` (int, optional) - Pagination offset

**Returns:** `dict` - Voice data with pagination info

### models.list()

List available models.

**Returns:** `dict` - Model data

### balance.get()

Get account balance and usage.

**Returns:** `dict` - Balance, plan, and usage data

## Error Handling

The SDK raises `NeoSpeechError` for API errors:

```python
from neospeech import NeoSpeech, NeoSpeechError

neospeech = NeoSpeech('your-api-key')

try:
    audio = neospeech.audio.speech(
        input="Test",
        voice="lyra",
        model="aurora-4"
    )
except NeoSpeechError as error:
    print(f"Error [{error.code}]: {error.message}")
    print(f"Status: {error.status}")
    print(f"Retryable: {error.retryable}")

    if error.is_auth_error():
        print("Check your API key")
    elif error.is_rate_limit_error():
        print("Rate limit exceeded")
```

### Error Methods

- `is_client_error()` - 4xx errors (your request)
- `is_server_error()` - 5xx errors (server issue)
- `is_rate_limit_error()` - 429 rate limit
- `is_auth_error()` - 401/403 authentication

## Examples

### Save Audio to File

```python
def generate_and_save(text: str, filename: str):
    audio = neospeech.audio.speech(
        input=text,
        voice="lyra",
        model="aurora-4"
    )

    with open(filename, 'wb') as f:
        f.write(audio)

    print(f"Saved to {filename}")

generate_and_save("Hello, world!", "hello.mp3")
```

### Batch Processing

```python
def batch_generate(texts: list, voice: str, model: str):
    results = []
    for text in texts:
        audio = neospeech.audio.speech(
            input=text,
            voice=voice,
            model=model
        )
        results.append(audio)
    return results

texts = ["First message", "Second message", "Third message"]
audios = batch_generate(texts, "kai", "turbo-3")

for i, audio in enumerate(audios):
    with open(f"output-{i+1}.mp3", 'wb') as f:
        f.write(audio)
```

### Stream with Progress

```python
def stream_with_progress(text: str, voice: str, model: str):
    stream = neospeech.audio.stream(
        input=text,
        voice=voice,
        model=model
    )

    total_bytes = 0
    chunks = []

    for chunk in stream:
        chunks.append(chunk)
        total_bytes += len(chunk)
        print(f"Progress: {total_bytes} bytes")

    return b''.join(chunks)

audio = stream_with_progress("Long text here...", "lyra", "aurora-3.5")
```

### Context Manager

Use context manager for automatic cleanup:

```python
with NeoSpeech('your-api-key') as neospeech:
    audio = neospeech.audio.speech(
        input="Hello, world!",
        voice="lyra",
        model="aurora-4"
    )

    with open('output.mp3', 'wb') as f:
        f.write(audio)
```

### Retry Logic

```python
import time

def generate_with_retry(text: str, max_retries: int = 3):
    for attempt in range(max_retries):
        try:
            return neospeech.audio.speech(
                input=text,
                voice="lyra",
                model="aurora-4"
            )
        except NeoSpeechError as error:
            if not error.retryable or attempt == max_retries - 1:
                raise

            delay = 2 ** attempt
            print(f"Retry {attempt + 1} in {delay}s...")
            time.sleep(delay)
```

## Type Hints

Full type hints support included:

```python
from neospeech import NeoSpeech
from typing import Dict, Any

neospeech: NeoSpeech = NeoSpeech('your-api-key')

audio: bytes = neospeech.audio.speech(
    input="Hello, world!",
    voice="lyra",
    model="aurora-4"
)

voices: Dict[str, Any] = neospeech.voices.list()
```

## Requirements

- Python 3.8 or higher
- NeoSpeech API key (Pro or Business plan)

## Documentation

- [Full API Documentation](https://docs.neospeech.io)
- [Voice Gallery](https://neospeech.io/voices)
- [Pricing](https://neospeech.io/pricing)

## Support

- Email: support@neospeech.io
- Issues: [GitHub Issues](https://github.com/neospeech/neospeech-python/issues)
- Documentation: [docs.neospeech.io](https://docs.neospeech.io)

## License

MIT
