# Files

<!-- Start Codat Library Description -->
﻿Use Codat's Files API to upload your SMB customers' files.
<!-- End Codat Library Description -->
Use Codat's Files API to upload your SMB customers' files.

<!-- Start Summary [summary] -->
## Summary

Files API: > ### New to Codat?
>
> Our Files API reference is relevant only to our existing clients.
> Please reach out to your Codat contact so that we can find the right product for you.

An API for uploading and downloading files from 'File Upload' Integrations.

The Accounting file upload, Banking file upload, and Business documents file upload integrations provide simple file upload functionality.

<!-- Start Codat Tags Table -->
## Endpoints

| Endpoints | Description |
| :- |:- |
| Files | Endpoints to manage uploaded files. |
<!-- End Codat Tags Table -->
[Read more...](https://docs.codat.io/other/file-upload)

[See our OpenAPI spec](https://github.com/codatio/oas)
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](#sdk-installation)
* [IDE Support](#ide-support)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [File uploads](#file-uploads)
* [Retries](#retries)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
* [Debugging](#debugging)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install codat-files
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add codat-files
```
<!-- End SDK Installation [installation] -->

## Example Usage
<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from codat_files import CodatFiles

s = CodatFiles(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.files.download_files(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "date_": "2022-10-23T00:00:00Z",
})

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from codat_files import CodatFiles

async def main():
    s = CodatFiles(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    )
    res = await s.files.download_files_async(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "date_": "2022-10-23T00:00:00Z",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>


### [files](docs/sdks/files/README.md)

* [download_files](docs/sdks/files/README.md#download_files) - Download all files for a company
* [list_files](docs/sdks/files/README.md#list_files) - List all files uploaded by a company
* [upload_files](docs/sdks/files/README.md#upload_files) - Upload files for a company

</details>
<!-- End Available Resources and Operations [operations] -->



<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from codat_files import CodatFiles

s = CodatFiles(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

s.files.upload_files(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
})

# Use the SDK ...

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from codat_files import CodatFiles
from codatfiles.utils import BackoffStrategy, RetryConfig

s = CodatFiles(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.files.download_files(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "date_": "2022-10-23T00:00:00Z",
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from codat_files import CodatFiles
from codatfiles.utils import BackoffStrategy, RetryConfig

s = CodatFiles(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.files.download_files(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "date_": "2022-10-23T00:00:00Z",
})

if res is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.Schema                    | 400,401,402,404,429,500,503      | application/json                 |
| errors.DownloadFilesErrorMessage | 403                              | application/json                 |
| errors.SDKError                  | 4xx-5xx                          | */*                              |

### Example

```python
from codat_files import CodatFiles
from codat_files.models import errors

s = CodatFiles(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = None
try:
    res = s.files.download_files(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "date_": "2022-10-23T00:00:00Z",
    })

    if res is not None:
        # handle response
        pass

except errors.Schema as e:
    # handle e.data: errors.SchemaData
    raise(e)
except errors.DownloadFilesErrorMessage as e:
    # handle e.data: errors.DownloadFilesErrorMessageData
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.codat.io` | None |

#### Example

```python
from codat_files import CodatFiles

s = CodatFiles(
    server_idx=0,
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.files.download_files(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "date_": "2022-10-23T00:00:00Z",
})

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_files import CodatFiles

s = CodatFiles(
    server_url="https://api.codat.io",
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.files.download_files(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "date_": "2022-10-23T00:00:00Z",
})

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from codat_files import CodatFiles
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatFiles(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from codat_files import CodatFiles
from codat_files.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = CodatFiles(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `auth_header` | apiKey        | API key       |

To authenticate with the API the `auth_header` parameter must be set when initializing the SDK client instance. For example:
```python
from codat_files import CodatFiles

s = CodatFiles(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.files.download_files(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "date_": "2022-10-23T00:00:00Z",
})

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from codat_files import CodatFiles
import logging

logging.basicConfig(level=logging.DEBUG)
s = CodatFiles(debug_logger=logging.getLogger("codat_files"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

<!-- Start Codat Support Notes -->
### Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance. 
You can raise any issues by contacting your dedicated Codat representative or reaching out to our [support team](mailto:support@codat.io).
We're here to help ensure a smooth experience for you.
<!-- End Codat Support Notes -->

<!-- Start Codat Generated By -->
### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
<!-- End Codat Generated By -->