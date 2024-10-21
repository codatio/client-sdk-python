# Assess

<!-- Start Codat Library Description -->
﻿Assess helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from the operating systems they are already using.
You can use that data for automating decisioning and surfacing new insights on the customer, all via one API.
<!-- End Codat Library Description -->
Assess helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from the operating systems they are already using.
You can use that data for automating decisioning and surfacing new insights on the customer, all via one API.

<!-- Start Summary [summary] -->
## Summary

Assess API: Codat's financial insights API

> ### New to Codat?
>
> Our Assess API reference is relevant only to our existing clients.
> Please reach out to your Codat contact so that we can find the right product for you.

Check that you have enabled the [data types required by Assess](https://docs.codat.io/assess/get-started#prerequisites) for all of its features to work.  

<!-- Start Codat Tags Table -->
## Endpoints

| Endpoints | Description |
| :- |:- |
| Reports | Enriched reports and analyses of financial data. |
| Excel reports | Downloadable reports. |
| Data integrity | Match mutable accounting data with immutable banking data to increase confidence in financial data. |
<!-- End Codat Tags Table -->

[Read more...](https://www.docs.codat.io/assess/)

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

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install codat-assess
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add codat-assess
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
from codat_assess import CodatAssess
from codat_assess.models import operations

s = CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

s.reports.generate_loan_summary(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "source_type": operations.SourceType.ACCOUNTING,
})

# Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from codat_assess import CodatAssess
from codat_assess.models import operations

async def main():
    s = CodatAssess(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    )
    await s.reports.generate_loan_summary_async(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "source_type": operations.SourceType.ACCOUNTING,
    })
    # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>


### [data_integrity](docs/sdks/dataintegrity/README.md)

* [details](docs/sdks/dataintegrity/README.md#details) - List data type data integrity
* [status](docs/sdks/dataintegrity/README.md#status) - Get data integrity status
* [summary](docs/sdks/dataintegrity/README.md#summary) - Get data integrity summary

### [excel_reports](docs/sdks/excelreports/README.md)

* [generate_excel_report](docs/sdks/excelreports/README.md#generate_excel_report) - Generate Excel report
* [get_accounting_marketing_metrics](docs/sdks/excelreports/README.md#get_accounting_marketing_metrics) - Get marketing metrics report
* [get_excel_report](docs/sdks/excelreports/README.md#get_excel_report) - Download Excel report
* [get_excel_report_generation_status](docs/sdks/excelreports/README.md#get_excel_report_generation_status) - Get Excel report status

### [reports](docs/sdks/reports/README.md)

* [generate_loan_summary](docs/sdks/reports/README.md#generate_loan_summary) - Generate loan summaries report
* [generate_loan_transactions](docs/sdks/reports/README.md#generate_loan_transactions) - Generate loan transactions report
* [get_accounts_for_enhanced_balance_sheet](docs/sdks/reports/README.md#get_accounts_for_enhanced_balance_sheet) - Get enhanced balance sheet accounts
* [get_accounts_for_enhanced_profit_and_loss](docs/sdks/reports/README.md#get_accounts_for_enhanced_profit_and_loss) - Get enhanced profit and loss accounts
* [get_commerce_customer_retention_metrics](docs/sdks/reports/README.md#get_commerce_customer_retention_metrics) - Get customer retention metrics
* [get_commerce_lifetime_value_metrics](docs/sdks/reports/README.md#get_commerce_lifetime_value_metrics) - Get lifetime value metric
* [get_commerce_orders_metrics](docs/sdks/reports/README.md#get_commerce_orders_metrics) - Get orders report
* [get_commerce_refunds_metrics](docs/sdks/reports/README.md#get_commerce_refunds_metrics) - Get refunds report
* [get_commerce_revenue_metrics](docs/sdks/reports/README.md#get_commerce_revenue_metrics) - Get commerce revenue metrics
* [get_enhanced_cash_flow_transactions](docs/sdks/reports/README.md#get_enhanced_cash_flow_transactions) - Get enhanced cash flow report
* [get_enhanced_invoices_report](docs/sdks/reports/README.md#get_enhanced_invoices_report) - Get enhanced invoices report
* [get_loan_summary](docs/sdks/reports/README.md#get_loan_summary) - Get loan summaries
* [get_recurring_revenue_metrics](docs/sdks/reports/README.md#get_recurring_revenue_metrics) - Get key subscription revenue metrics
* [list_loan_transactions](docs/sdks/reports/README.md#list_loan_transactions) - List loan transactions
* [request_recurring_revenue_metrics](docs/sdks/reports/README.md#request_recurring_revenue_metrics) - Generate key subscription revenue metrics

</details>
<!-- End Available Resources and Operations [operations] -->



<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from codat_assess import CodatAssess
from codat_assess.models import operations
from codatassess.utils import BackoffStrategy, RetryConfig

s = CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

s.reports.generate_loan_summary(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "source_type": operations.SourceType.ACCOUNTING,
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

# Use the SDK ...

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from codat_assess import CodatAssess
from codat_assess.models import operations
from codatassess.utils import BackoffStrategy, RetryConfig

s = CodatAssess(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

s.reports.generate_loan_summary(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "source_type": operations.SourceType.ACCOUNTING,
})

# Use the SDK ...

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

### Example

```python
from codat_assess import CodatAssess
from codat_assess.models import errors, operations

s = CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)


try:
    s.reports.generate_loan_summary(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "source_type": operations.SourceType.ACCOUNTING,
    })

    # Use the SDK ...

except errors.ErrorMessage as e:
    # handle e.data: errors.ErrorMessageData
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
from codat_assess import CodatAssess
from codat_assess.models import operations

s = CodatAssess(
    server_idx=0,
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

s.reports.generate_loan_summary(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "source_type": operations.SourceType.ACCOUNTING,
})

# Use the SDK ...

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_assess import CodatAssess
from codat_assess.models import operations

s = CodatAssess(
    server_url="https://api.codat.io",
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

s.reports.generate_loan_summary(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "source_type": operations.SourceType.ACCOUNTING,
})

# Use the SDK ...

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from codat_assess import CodatAssess
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatAssess(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from codat_assess import CodatAssess
from codat_assess.httpclient import AsyncHttpClient
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

s = CodatAssess(async_client=CustomClient(httpx.AsyncClient()))
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
from codat_assess import CodatAssess
from codat_assess.models import operations

s = CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

s.reports.generate_loan_summary(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "source_type": operations.SourceType.ACCOUNTING,
})

# Use the SDK ...

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from codat_assess import CodatAssess
import logging

logging.basicConfig(level=logging.DEBUG)
s = CodatAssess(debug_logger=logging.getLogger("codat_assess"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

<!-- Start Codat Support Notes -->
## Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance. 
You can raise any issues by contacting your dedicated Codat representative or reaching out to our [support team](mailto:support@codat.io).
We're here to help ensure a smooth experience for you.
<!-- End Codat Support Notes -->

<!-- Start Codat Generated By -->
### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
<!-- End Codat Generated By -->