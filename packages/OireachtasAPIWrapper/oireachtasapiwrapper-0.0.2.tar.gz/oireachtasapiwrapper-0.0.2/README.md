# Oireachtas API Wrapper

Python client maintained by **Aaron Bowman** for the public [Oireachtas API](https://api.oireachtas.ie/). The package exposes thin helper classes that make it easy to call official endpoints for legislation, debates, members, questions, and other parliamentary data.

## Features

- Lightweight wrappers around the official Oireachtas REST endpoints
- Optional convenience wrapper for resolving endpoint names to URLs
- Basic error mapping for common HTTP status codes
- Opt-in helper for file-based logging during local development

## Installation

Install from PyPI (or your preferred index):

```bash
pip install OireachtasAPIWrapper
```

Using uv:

```bash
uv add OireachtasAPIWrapper
```

## Quick Start

```python
from OireachtasAPI import API

client = API()
response = client.make_request(
    endpoint="https://api.oireachtas.ie/v1/legislation",
    params={"limit": 5},
)

print(response.json())
```

Enable basic file logging when you need to trace requests:

```python
from OireachtasAPI import configure_logging

configure_logging()
```

## Local Development

Create an isolated environment and install dev dependencies with uv:

```bash
uv sync
uv run pytest
```

If you prefer standard tooling, `pip install -e .[test]` provides the same dependencies defined in `pyproject.toml`.

## Contributing

Issues and pull requests are welcome on [GitHub](https://github.com/aaronbowman/OireachtasAPIWrapper). Please open an issue before submitting large changes so we can coordinate work.

## License

Released under the MIT License. See [`LICENSE.txt`](LICENSE.txt) for details.
