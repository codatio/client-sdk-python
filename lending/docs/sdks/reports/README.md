# AccountsReceivable.Reports

## Overview

### Available Operations

* [get_aged_creditors](#get_aged_creditors) - Aged creditors report
* [get_aged_debtors](#get_aged_debtors) - Aged debtors report
* [is_aged_creditors_available](#is_aged_creditors_available) - Aged creditors report available
* [is_aged_debtors_available](#is_aged_debtors_available) - Aged debtors report available

## get_aged_creditors

Returns aged creditors report for company that shows the total balance owed by a business to its suppliers over time.

### Example Usage: Clear Books

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="Clear Books" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="Dynamics 365 Business Central" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="Exact (Netherlands)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="Exact (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: FreeAgent

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="FreeAgent" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: MYOB AccountRight and Essentials

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="MYOB AccountRight and Essentials" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="Oracle NetSuite" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="QuickBooks Desktop" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="QuickBooks Online" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 200cloud

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="Sage 200cloud" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="Sage 50 (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="Sage Business Cloud Accounting" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="Sage Intacct" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="get-accounting-aged-creditors-report" method="get" path="/companies/{companyId}/reports/agedCreditor" example="Xero" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_creditors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetAccountingAgedCreditorsReportRequest](../../models/operations/getaccountingagedcreditorsreportrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[shared.AccountingAgedCreditorReport](../../models/shared/accountingagedcreditorreport.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_aged_debtors

Returns aged debtors report for company that shows the total outstanding balance due from customers to the business over time.

### Example Usage: Clear Books

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="Clear Books" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="Dynamics 365 Business Central" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: FreshBooks

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="FreshBooks" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: KashFlow

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="KashFlow" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: MYOB AccountRight and Essentials

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="MYOB AccountRight and Essentials" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="Oracle NetSuite" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="QuickBooks Desktop" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="QuickBooks Online" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 200cloud

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="Sage 200cloud" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="Sage 50 (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="Sage Business Cloud Accounting" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="Sage Intacct" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="Xero" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```
### Example Usage: Zoho Books

<!-- UsageSnippet language="python" operationID="get-accounting-aged-debtors-report" method="get" path="/companies/{companyId}/reports/agedDebtor" example="Zoho Books" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.get_aged_debtors(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "number_of_periods": 12,
        "period_length_days": 30,
        "report_date": "2022-12-31",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAccountingAgedDebtorsReportRequest](../../models/operations/getaccountingageddebtorsreportrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[shared.AccountingAgedDebtorReport](../../models/shared/accountingageddebtorreport.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## is_aged_creditors_available

Indicates whether the aged creditor report is available for the company.

### Example Usage

<!-- UsageSnippet language="python" operationID="is-aged-creditors-report-available" method="get" path="/companies/{companyId}/reports/agedCreditor/available" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.is_aged_creditors_available(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.IsAgedCreditorsReportAvailableRequest](../../models/operations/isagedcreditorsreportavailablerequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## is_aged_debtors_available

Indicates whether the aged debtors report is available for the company.

### Example Usage

<!-- UsageSnippet language="python" operationID="is-aged-debtors-report-available" method="get" path="/companies/{companyId}/reports/agedDebtor/available" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.reports.is_aged_debtors_available(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.IsAgedDebtorsReportAvailableRequest](../../models/operations/isageddebtorsreportavailablerequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[bool](../../models/.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |