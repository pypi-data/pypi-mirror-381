### screenshotbase-python

Python client for the `screenshotbase.com` API.

- Website: [`https://screenshotbase.com/`](https://screenshotbase.com/)
- Docs: [`https://screenshotbase.com/docs/`](https://screenshotbase.com/docs/)

This SDK wraps the public endpoints and supports authentication via `apikey` header (default) or `apikey` query parameter.

### Installation

```bash
pip install screenshotbase
```

### Quickstart

```python
from screenshotbase.client import Client
import os

client = Client(api_key=os.environ.get("SCREENSHOTBASE_API_KEY"))

# Status
print(client.status())

# Render screenshot
print(client.render({
    "url": "https://example.com",
    "full_page": True,
    "viewport": "1366x768",
    "format": "png",
}))
```

### Authentication

Header (default) vs query parameter auth:

```python
client = Client(api_key="your_api_key")
client_qs = Client(api_key="your_api_key", auth_in_query=True)
```

### API

- `status()` → API availability and quota
- `render(params)` → website screenshot render. Example params: `{ "url": "https://example.com", "viewport": "1366x768", "full_page": True, "format": "png" }`

For full parameters, see docs: [`https://screenshotbase.com/docs/`](https://screenshotbase.com/docs/)

### License

MIT


