# Commerce

<!-- Start Codat Library Description -->
﻿Codat's Commerce API enables you to pull up-date-date commerce data from several leading payments, point-of-sale, and eCommerce systems.
You can view your SMB customers' products, orders, payments, payouts, disputes, and more - all standardized to our Commerce data model.

<!-- End Codat Library Description -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install codat-commerce
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add codat-commerce
```
<!-- End SDK Installation [installation] -->

## Example Usage
<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from codat_commerce import CodatCommerce

s = CodatCommerce(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.customers.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "customer_id": "<value>",
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
from codat_commerce import CodatCommerce

async def main():
    s = CodatCommerce(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    )
    res = await s.customers.get_async(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "customer_id": "<value>",
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


### [company_info](docs/sdks/companyinfosdk/README.md)

* [get](docs/sdks/companyinfosdk/README.md#get) - Get company info

### [customers](docs/sdks/customerssdk/README.md)

* [get](docs/sdks/customerssdk/README.md#get) - Get customer
* [list](docs/sdks/customerssdk/README.md#list) - List customers

### [disputes](docs/sdks/disputessdk/README.md)

* [get](docs/sdks/disputessdk/README.md#get) - Get dispute
* [list](docs/sdks/disputessdk/README.md#list) - List disputes

### [locations](docs/sdks/locationssdk/README.md)

* [get](docs/sdks/locationssdk/README.md#get) - Get location
* [list](docs/sdks/locationssdk/README.md#list) - List locations

### [orders](docs/sdks/orderssdk/README.md)

* [get](docs/sdks/orderssdk/README.md#get) - Get order
* [list](docs/sdks/orderssdk/README.md#list) - List orders

### [payments](docs/sdks/paymentssdk/README.md)

* [get](docs/sdks/paymentssdk/README.md#get) - Get payment
* [get_method](docs/sdks/paymentssdk/README.md#get_method) - Get payment method
* [list](docs/sdks/paymentssdk/README.md#list) - List payments
* [list_methods](docs/sdks/paymentssdk/README.md#list_methods) - List payment methods

### [products](docs/sdks/productssdk/README.md)

* [get](docs/sdks/productssdk/README.md#get) - Get product
* [get_category](docs/sdks/productssdk/README.md#get_category) - Get product category
* [list](docs/sdks/productssdk/README.md#list) - List products
* [list_categories](docs/sdks/productssdk/README.md#list_categories) - List product categories

### [tax_components](docs/sdks/taxcomponentssdk/README.md)

* [get](docs/sdks/taxcomponentssdk/README.md#get) - Get tax component
* [list](docs/sdks/taxcomponentssdk/README.md#list) - List tax components

### [transactions](docs/sdks/transactionssdk/README.md)

* [get](docs/sdks/transactionssdk/README.md#get) - Get transaction
* [list](docs/sdks/transactionssdk/README.md#list) - List transactions

</details>
<!-- End Available Resources and Operations [operations] -->



<!-- Start Summary [summary] -->
## Summary

Commerce API: Codat's standardized API for accessing commerce data 

> ### New to Codat?
>
> Our Commerce API reference is relevant only to our existing clients.
> Please reach out to your Codat contact so that we can find the right product for you.

Codat's Commerce API allows you to access standardised data from over 11 commerce and POS systems.

Standardize how you connect to your customers’ payment, PoS, and eCommerce systems. Retrieve orders, payouts, payments, and product data in the same way for all the leading commerce software.

<!-- Start Codat Tags Table -->
## Endpoints

| Endpoints | Description |
| :- |:- |
| Customers | Retrieve standardized data from linked commerce software. |
| Disputes | Retrieve standardized data from linked commerce software. |
| Company info | Retrieve standardized data from linked commerce software. |
| Locations | Retrieve standardized data from linked commerce software. |
| Orders | Retrieve standardized data from linked commerce software. |
| Payments | Retrieve standardized data from linked commerce software. |
| Products | Retrieve standardized data from linked commerce software. |
| Tax components | Retrieve standardized data from linked commerce software. |
| Transactions | Retrieve standardized data from linked commerce software. |
<!-- End Codat Tags Table -->

[Read more...](https://docs.codat.io/commerce-api/overview)

[See our OpenAPI spec](https://github.com/codatio/oas)
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](#sdk-installation)
* [IDE Support](#ide-support)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [Retries](#retries)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
* [Debugging](#debugging)
<!-- End Table of Contents [toc] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from codat_commerce import CodatCommerce
from codatcommerce.utils import BackoffStrategy, RetryConfig

s = CodatCommerce(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.customers.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "customer_id": "<value>",
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from codat_commerce import CodatCommerce
from codatcommerce.utils import BackoffStrategy, RetryConfig

s = CodatCommerce(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.customers.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "customer_id": "<value>",
})

if res is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| models.SDKError                 | 4xx-5xx                         | */*                             |

### Example

```python
from codat_commerce import CodatCommerce, models

s = CodatCommerce(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = None
try:
    res = s.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "customer_id": "<value>",
    })

    if res is not None:
        # handle response
        pass

except models.ErrorMessage as e:
    # handle e.data: models.ErrorMessageData
    raise(e)
except models.SDKError as e:
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
from codat_commerce import CodatCommerce

s = CodatCommerce(
    server_idx=0,
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.customers.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "customer_id": "<value>",
})

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_commerce import CodatCommerce

s = CodatCommerce(
    server_url="https://api.codat.io",
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.customers.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "customer_id": "<value>",
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
from codat_commerce import CodatCommerce
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatCommerce(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from codat_commerce import CodatCommerce
from codat_commerce.httpclient import AsyncHttpClient
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

s = CodatCommerce(async_client=CustomClient(httpx.AsyncClient()))
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
from codat_commerce import CodatCommerce

s = CodatCommerce(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.customers.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "customer_id": "<value>",
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
from codat_commerce import CodatCommerce
import logging

logging.basicConfig(level=logging.DEBUG)
s = CodatCommerce(debug_logger=logging.getLogger("codat_commerce"))
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