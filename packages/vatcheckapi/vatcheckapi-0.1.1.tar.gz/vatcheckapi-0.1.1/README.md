### vatcheckapi-python

Python client for the `vatcheckapi.com` API.

- Website: [`https://vatcheckapi.com/`](https://vatcheckapi.com/)
 

This SDK supports authentication via `apikey` header (default) or `apikey` query parameter.

### Installation

```bash
pip install vatcheckapi
```

### Quickstart

```python
from vatcheckapi import Client

client = Client(api_key="YOUR_API_KEY")

# Check a VAT number
res = client.check(vat_number="DE123456789")
print(res)

# Get API status/quota
status = client.status()
print(status)
```

### Authentication

```python
# Header-based (default)
client = Client(api_key="YOUR_API_KEY")

# Query parameter based
client_query = Client(api_key="YOUR_API_KEY", auth_in_query=True)
```

### API

- `check(vat_number: str, **params) -> dict`
- `status() -> dict`

### License

MIT


