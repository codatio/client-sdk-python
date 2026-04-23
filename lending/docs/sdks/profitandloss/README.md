# FinancialStatements.ProfitAndLoss

## Overview

### Available Operations

* [get](#get) - Get profit and loss
* [get_categorized_accounts](#get_categorized_accounts) - Get categorized profit and loss statement

## get

Gets the latest profit and loss for a company.

### Example Usage: Clear Books

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="Clear Books" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="Dynamics 365 Business Central" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="Exact (Netherlands)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="Exact (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: FreshBooks

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="FreshBooks" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: KashFlow

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="KashFlow" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: MYOB AccountRight and Essentials

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="MYOB AccountRight and Essentials" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="Oracle NetSuite" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="QuickBooks Desktop" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="QuickBooks Online" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="QuickBooks Online Sandbox" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 200cloud

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="Sage 200cloud" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="Sage 50 (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="Sage Business Cloud Accounting" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: Wave

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="Wave" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="Xero" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```
### Example Usage: Zoho Books

<!-- UsageSnippet language="python" operationID="get-accounting-profit-and-loss" method="get" path="/companies/{companyId}/data/financials/profitAndLoss" example="Zoho Books" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAccountingProfitAndLossRequest](../../models/operations/getaccountingprofitandlossrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[shared.AccountingProfitAndLossReport](../../models/shared/accountingprofitandlossreport.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 401, 402, 403, 404, 409, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_categorized_accounts

The *Get categorized profit and loss statement* endpoint returns a list of categorized accounts that appear on a company’s Profit and Loss statement. It also includes a balance as of the financial statement date.

Codat suggests a category for each account automatically, but you can [change it](https://docs.codat.io/lending/features/financial-statements-overview#recategorizing-accounts) to a more suitable one.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-categorized-profit-and-loss-statement" method="get" path="/companies/{companyId}/reports/enhancedProfitAndLoss/accounts" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.profit_and_loss.get_categorized_accounts(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "report_date": "29-09-2020",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.GetCategorizedProfitAndLossStatementRequest](../../models/operations/getcategorizedprofitandlossstatementrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[shared.EnhancedFinancialReport](../../models/shared/enhancedfinancialreport.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |