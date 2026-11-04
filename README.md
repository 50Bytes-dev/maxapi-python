# maxapi-python
A client library for [maxapi](https://github.com/50Bytes-dev/maxapi), the MAX Messenger REST gateway.
Generated from maxapi's OpenAPI schema (`static/api/spec.yml`); version 4.0.0 matches the schema of maxapi 1.5.0.

Requires Python 3.9 or newer.

## Install

```shell
uv add "maxapi-python @ git+https://github.com/50Bytes-dev/maxapi-python.git@<commit>"
```

## Clients
maxapi has two kinds of tokens, both sent raw (no `Bearer` prefix):

- the admin token, in the `Authorization` header, for `/admin/*`;
- an account token (from `add_user`), in the `token` header, for every other call.

```python
from maxapi_python import AuthenticatedClient, Client

admin = AuthenticatedClient(
    base_url="http://maxapi:5555",
    token="ADMIN_TOKEN",
    auth_header_name="Authorization",
    prefix="",
)
account = AuthenticatedClient(
    base_url="http://maxapi:5555",
    token="ACCOUNT_TOKEN",
    auth_header_name="token",
    prefix="",
)
public = Client(base_url="http://maxapi:5555")  # GET /health only
```

## Calls
Every operation is a module named after its `operationId`, under the package of its tag
(`admin`, `session`, `chat`, `user`, `group`, `webhook`, `health`), with four functions:

1. `sync`: blocking; returns the parsed body, or `None` for a status the schema does not list;
1. `sync_detailed`: blocking; returns a `Response` with `status_code`, `content`, `headers` and `parsed`;
1. `asyncio` and `asyncio_detailed`: the same, async.

Errors are not raised: a documented error status returns `ErrorResponse` (`success`, `error`, and where
maxapi sends them `code`, `upstream_code`, `paused`, `pause_reason`). Use `sync_detailed` when the HTTP
status matters, since most maxapi errors carry no `code`.

```python
from maxapi_python.api.admin import add_user
from maxapi_python.api.chat import send_text
from maxapi_python.api.session import get_status
from maxapi_python.models import AddUserBody, ErrorResponse, SendTextBody, SendTextResponse

created = add_user.sync(client=admin, body=AddUserBody(name="Shop bot", webhook="https://example.com/webhook"))

status = get_status.sync(client=account)
if status is not None and status.connected and not status.paused:
    response = send_text.sync_detailed(client=account, body=SendTextBody(phone="79001234567", text="Hello"))
    if isinstance(response.parsed, SendTextResponse):
        print(response.parsed.message_id)
    elif isinstance(response.parsed, ErrorResponse):
        print(response.status_code, response.parsed.code, response.parsed.upstream_code)
```

## Webhook events
maxapi posts events to the account's webhook. Each event has a model (`SyncEvent`, `QRAuthorizedEvent`,
`AuthExpiredEvent`, `MessageEvent`, ...): pick it by the body's `type` and call `from_dict`. Fields the
model does not name stay in `additional_properties`.

```python
from maxapi_python.models import AuthExpiredEvent, SyncEvent

EVENTS = {"Sync": SyncEvent, "AuthExpired": AuthExpiredEvent}
event = EVENTS[body["type"]].from_dict(body)
```

## Customizing the HTTP client
`timeout`, `verify_ssl`, `headers`, `cookies`, `follow_redirects` and `raise_on_unexpected_status` are
arguments of both clients; `httpx_args` passes anything else to the underlying `httpx` client
(for example `{"event_hooks": {...}}`), and `set_httpx_client` / `set_async_httpx_client` replace it.

## Regenerate
`generate.sh` regenerates the package from `../maxapi/static/api/spec.yml` with the
openapi-python-client locked in `uv.lock` (0.26.1; versions 0.29 and newer emit `typing.Self`, which needs
Python 3.11). Bump `version` in `pyproject.toml` with the schema's `info.version`.

```shell
uv sync && ./generate.sh && uv run ruff check maxapi_python && uv run ruff format --check maxapi_python
```
