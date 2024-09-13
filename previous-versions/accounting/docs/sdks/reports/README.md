# Reports
(*reports*)

## Overview

Access standardized Reports from linked accounting software.

### Available Operations

* [get_aged_creditors_report](#get_aged_creditors_report) - Aged creditors report
* [get_aged_debtors_report](#get_aged_debtors_report) - Aged debtors report
* [get_balance_sheet](#get_balance_sheet) - Get balance sheet
* [get_cash_flow_statement](#get_cash_flow_statement) - Get cash flow statement
* [get_profit_and_loss](#get_profit_and_loss) - Get profit and loss
* [is_aged_creditors_report_available](#is_aged_creditors_report_available) - Aged creditors report available
* [is_aged_debtor_report_available](#is_aged_debtor_report_available) - Aged debtors report available

## get_aged_creditors_report

Returns aged creditors report for company that shows the total balance owed by a business to its suppliers over time.

### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared
import dateutil.parser

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.reports.get_aged_creditors_report(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "number_of_periods": 12,
    "period_length_days": 30,
    "report_date": dateutil.parser.parse("2022-12-31").date(),
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetAgedCreditorsReportRequest](../../models/operations/getagedcreditorsreportrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[shared.AgedCreditorReport](../../models/shared/agedcreditorreport.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## get_aged_debtors_report

Returns aged debtors report for company that shows the total outstanding balance due from customers to the business over time.

### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared
import dateutil.parser

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.reports.get_aged_debtors_report(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "number_of_periods": 12,
    "period_length_days": 30,
    "report_date": dateutil.parser.parse("2022-12-31").date(),
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAgedDebtorsReportRequest](../../models/operations/getageddebtorsreportrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[shared.AgedDebtorReport](../../models/shared/ageddebtorreport.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## get_balance_sheet

Gets the latest balance sheet for a company.

### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.reports.get_balance_sheet(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "period_length": 4,
    "periods_to_compare": 20,
    "start_month": "2022-10-23T00:00:00Z",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetBalanceSheetRequest](../../models/operations/getbalancesheetrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[shared.BalanceSheetInput](../../models/shared/balancesheetinput.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |


## get_cash_flow_statement

Gets the latest cash flow statement for a company.

### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.reports.get_cash_flow_statement(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "period_length": 4,
    "periods_to_compare": 20,
    "start_month": "2022-10-23T00:00:00Z",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetCashFlowStatementRequest](../../models/operations/getcashflowstatementrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[shared.CashFlowStatementInput](../../models/shared/cashflowstatementinput.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |


## get_profit_and_loss

Gets the latest profit and loss for a company.

### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.reports.get_profit_and_loss(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "period_length": 4,
    "periods_to_compare": 20,
    "start_month": "2022-10-23T00:00:00Z",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetProfitAndLossRequest](../../models/operations/getprofitandlossrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[shared.ProfitAndLossReportInput](../../models/shared/profitandlossreportinput.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |


## is_aged_creditors_report_available

Indicates whether the aged creditor report is available for the company.

### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.reports.is_aged_creditors_report_available(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.IsAgedCreditorsReportAvailableRequest](../../models/operations/isagedcreditorsreportavailablerequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[bool](../../models/.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## is_aged_debtor_report_available

Indicates whether the aged debtor report is available for the company.

### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.reports.is_aged_debtor_report_available(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.IsAgedDebtorReportAvailableRequest](../../models/operations/isageddebtorreportavailablerequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[bool](../../models/.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |
