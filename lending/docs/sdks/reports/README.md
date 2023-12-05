# Reports
(*accounts_receivable.reports*)

### Available Operations

* [get_aged_creditors](#get_aged_creditors) - Aged creditors report
* [get_aged_debtors](#get_aged_debtors) - Aged debtors report
* [is_aged_creditors_available](#is_aged_creditors_available) - Aged creditors report available
* [is_aged_debtors_available](#is_aged_debtors_available) - Aged debtors report available

## get_aged_creditors

Returns aged creditors report for company that shows the total balance owed by a business to its suppliers over time.

### Example Usage

```python
import codatlending
import dateutil.parser
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingAgedCreditorsReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    number_of_periods=12,
    period_length_days=30,
    report_date=dateutil.parser.parse('2022-12-31').date(),
)

res = s.accounts_receivable.reports.get_aged_creditors(req)

if res.accounting_aged_creditor_report is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetAccountingAgedCreditorsReportRequest](../../models/operations/getaccountingagedcreditorsreportrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |


### Response

**[operations.GetAccountingAgedCreditorsReportResponse](../../models/operations/getaccountingagedcreditorsreportresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 400-600                     | */*                         |

## get_aged_debtors

Returns aged debtors report for company that shows the total outstanding balance due from customers to the business over time.

### Example Usage

```python
import codatlending
import dateutil.parser
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingAgedDebtorsReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    number_of_periods=12,
    period_length_days=30,
    report_date=dateutil.parser.parse('2022-12-31').date(),
)

res = s.accounts_receivable.reports.get_aged_debtors(req)

if res.accounting_aged_debtor_report is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAccountingAgedDebtorsReportRequest](../../models/operations/getaccountingageddebtorsreportrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |


### Response

**[operations.GetAccountingAgedDebtorsReportResponse](../../models/operations/getaccountingageddebtorsreportresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 400-600                     | */*                         |

## is_aged_creditors_available

Indicates whether the aged creditor report is available for the company.

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.IsAgedCreditorsReportAvailableRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.accounts_receivable.reports.is_aged_creditors_available(req)

if res.boolean is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.IsAgedCreditorsReportAvailableRequest](../../models/operations/isagedcreditorsreportavailablerequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |


### Response

**[operations.IsAgedCreditorsReportAvailableResponse](../../models/operations/isagedcreditorsreportavailableresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 400-600                     | */*                         |

## is_aged_debtors_available

Indicates whether the aged debtors report is available for the company.

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.IsAgedDebtorsReportAvailableRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.accounts_receivable.reports.is_aged_debtors_available(req)

if res.boolean is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.IsAgedDebtorsReportAvailableRequest](../../models/operations/isageddebtorsreportavailablerequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |


### Response

**[operations.IsAgedDebtorsReportAvailableResponse](../../models/operations/isageddebtorsreportavailableresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 400-600                     | */*                         |
