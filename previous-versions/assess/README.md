# Assess

<!-- Start Codat Library Description -->
﻿Assess helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from the operating systems they are already using.
You can use that data for automating decisioning and surfacing new insights on the customer, all via one API.
<!-- End Codat Library Description -->
Assess helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from the operating systems they are already using.
You can use that data for automating decisioning and surfacing new insights on the customer, all via one API.

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install codat-assess
```
<!-- End SDK Installation -->

## Example Usage
<!-- Start SDK Example Usage -->
### Example

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.GenerateLoanSummaryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    source_type=operations.SourceType.ACCOUNTING,
)

res = s.reports.generate_loan_summary(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


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

### [data_integrity](docs/sdks/dataintegrity/README.md)

* [details](docs/sdks/dataintegrity/README.md#details) - List data type data integrity
* [status](docs/sdks/dataintegrity/README.md#status) - Get data integrity status
* [summary](docs/sdks/dataintegrity/README.md#summary) - Get data integrity summary

### [excel_reports](docs/sdks/excelreports/README.md)

* [generate_excel_report](docs/sdks/excelreports/README.md#generate_excel_report) - Generate Excel report
* [get_accounting_marketing_metrics](docs/sdks/excelreports/README.md#get_accounting_marketing_metrics) - Get marketing metrics report
* [get_excel_report](docs/sdks/excelreports/README.md#get_excel_report) - Download Excel report
* [get_excel_report_generation_status](docs/sdks/excelreports/README.md#get_excel_report_generation_status) - Get Excel report status
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Error Handling -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 400-600                     | */*                         |

### Example

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.GenerateLoanSummaryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    source_type=operations.SourceType.ACCOUNTING,
)

res = None
try:
    res = s.reports.generate_loan_summary(req)
except (errors.ErrorMessage) as e:
    print(e) # handle exception

except (errors.SDKError) as e:
    print(e) # handle exception


if res.status_code == 200:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.codat.io` | None |

#### Example

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    server_idx=0,
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.GenerateLoanSummaryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    source_type=operations.SourceType.ACCOUNTING,
)

res = s.reports.generate_loan_summary(req)

if res.status_code == 200:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    server_url="https://api.codat.io",
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.GenerateLoanSummaryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    source_type=operations.SourceType.ACCOUNTING,
)

res = s.reports.generate_loan_summary(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import codatassess
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = codatassess.CodatAssess(client: http_client)
```
<!-- End Custom HTTP Client -->



<!-- Start Retries -->
## Retries

Some of the endpoints in this SDK support retries.  If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API.  However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a retryConfig object to the call:
```python
import codatassess
from codatassess.models import operations
from codatassess.utils import BackoffStrategy, RetryConfig

s = codatassess.CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.GenerateLoanSummaryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    source_type=operations.SourceType.ACCOUNTING,
)

res = s.reports.generate_loan_summary(req,
    RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False))

if res.status_code == 200:
    # handle response
    pass
```

If you'd like to override the default retry strategy for all operations that support retries, you can provide a retryConfig at SDK initialization:
```python
import codatassess
from codatassess.models import operations
from codatassess.utils import BackoffStrategy, RetryConfig

s = codatassess.CodatAssess(
    retry_config=RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False)
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.GenerateLoanSummaryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    source_type=operations.SourceType.ACCOUNTING,
)

res = s.reports.generate_loan_summary(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Retries -->



<!-- Start Authentication -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `auth_header` | apiKey        | API key       |

To authenticate with the API the `auth_header` parameter must be set when initializing the SDK client instance. For example:
```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.GenerateLoanSummaryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    source_type=operations.SourceType.ACCOUNTING,
)

res = s.reports.generate_loan_summary(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->


### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)