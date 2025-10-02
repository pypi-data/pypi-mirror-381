# Behind API Client - Python

Auto-generated API client for Behind API.

## Installation

```bash
pip install -r requirements.txt
```

Or install the package:

```bash
pip install -e .
```

## Usage

```python
from behind_api_client import BehindApiClient

# Initialize the client
api_client = BehindApiClient("https://api.behind.ai:6002", "your-access-token")

# Use the API
result = api_client.zecamp10.v10.message.send(
    email="user@example.com",
    recipient_name="John Doe",
    account_name="my_account",
    template_name="welcome",
    data={},
    time=""
)
```

## Structure

The API client follows this structure:
- `api_client.{app}.{version}.{endpoint}.{method}(params)`

For example:
- `api_client.zecamp10.v10.companies.get(...)`
- `api_client.raet.v10.cv.create(...)`

Note: Hyphenated app names are converted to snake_case (e.g., `web-harvester` becomes `web_harvester`).

## Event Handlers

```python
api_client.on_expired(lambda data: print("Token expired"))
api_client.on_reject(lambda data: print(f"Rejected: {data}"))
api_client.on_too_many_requests(lambda data: print(f"Rate limited: {data}"))
```
