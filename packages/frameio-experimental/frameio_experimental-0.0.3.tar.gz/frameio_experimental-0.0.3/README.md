# Frameio Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2FFrameio%2Fpython-sdk-experimental)
[![pypi](https://img.shields.io/pypi/v/frameio-experimental)](https://pypi.python.org/pypi/frameio-experimental)

The Frameio Python library provides convenient access to the Frameio APIs from Python.

## Installation

```sh
pip install frameio-experimental
```

## Reference

A full reference for this library is available [here](https://github.com/Frameio/python-sdk-experimental/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from frameio_experimental import FrameioExperimental
from frameio_experimental.custom_actions import ActionCreateParamsData

client = FrameioExperimental(
    api_version="YOUR_API_VERSION",
    token="YOUR_TOKEN",
)
client.custom_actions.actions_create(
    account_id="b2702c44-c6da-4bb6-8bbd-be6e547ccf1b",
    workspace_id="b2702c44-c6da-4bb6-8bbd-be6e547ccf1b",
    data=ActionCreateParamsData(
        description="customizing our workflow",
        event="my.event",
        name="First Custom Action",
        url="https://example.com/custom-action",
    ),
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from frameio_experimental import AsyncFrameioExperimental
from frameio_experimental.custom_actions import ActionCreateParamsData

client = AsyncFrameioExperimental(
    api_version="YOUR_API_VERSION",
    token="YOUR_TOKEN",
)


async def main() -> None:
    await client.custom_actions.actions_create(
        account_id="b2702c44-c6da-4bb6-8bbd-be6e547ccf1b",
        workspace_id="b2702c44-c6da-4bb6-8bbd-be6e547ccf1b",
        data=ActionCreateParamsData(
            description="customizing our workflow",
            event="my.event",
            name="First Custom Action",
            url="https://example.com/custom-action",
        ),
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from frameio_experimental.core.api_error import ApiError

try:
    client.custom_actions.actions_create(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from frameio_experimental import FrameioExperimental

client = FrameioExperimental(
    ...,
)
response = client.custom_actions.with_raw_response.actions_create(...)
print(response.headers)  # access the response headers
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.custom_actions.actions_create(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from frameio_experimental import FrameioExperimental

client = FrameioExperimental(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.custom_actions.actions_create(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from frameio_experimental import FrameioExperimental

client = FrameioExperimental(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
