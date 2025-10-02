# Serpnode Python SDK (Unofficial)

Python client for the Serpnode API. Supports authentication via `apikey` header (default) or `apikey` query parameter. Implements `status`, `search`, `options`, and `locations` endpoints.

 

## Install

```bash
pip install serpnode
```

## Usage

```python
from serpnode import Client
import os

client = Client(api_key=os.environ["SERPNODE_API_KEY"])  # or auth_in_query=True

print(client.status())
print(client.search({"q": "site:example.com", "engine": "google"}))
print(client.options())
print(client.locations({"q": "United States"}))
```

## Authentication

- Default: `Authorization: Bearer <API_KEY>`
- Alternative: `auth_in_query=True` adds `apikey=<API_KEY>` to the query string

## License

MIT
