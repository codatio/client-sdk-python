# Reports

## Overview

Reports

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
import codataccounting
import dateutil.parser
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAgedCreditorsReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    number_of_periods=12,
    period_length_days=30,
    report_date=dateutil.parser.parse('2022-12-31').date(),
)

res = s.reports.get_aged_creditors_report(req)

if res.aged_creditor_report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetAgedCreditorsReportRequest](../../models/operations/getagedcreditorsreportrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |


### Response

**[operations.GetAgedCreditorsReportResponse](../../models/operations/getagedcreditorsreportresponse.md)**


## get_aged_debtors_report

Returns aged debtors report for company that shows the total outstanding balance due from customers to the business over time.

### Example Usage

```python
import codataccounting
import dateutil.parser
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAgedDebtorsReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    number_of_periods=12,
    period_length_days=30,
    report_date=dateutil.parser.parse('2022-12-31').date(),
)

res = s.reports.get_aged_debtors_report(req)

if res.aged_debtor_report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAgedDebtorsReportRequest](../../models/operations/getageddebtorsreportrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.GetAgedDebtorsReportResponse](../../models/operations/getageddebtorsreportresponse.md)**


## get_balance_sheet

Gets the latest balance sheet for a company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetBalanceSheetRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    period_length=4,
    periods_to_compare=20,
    start_month='2022-10-23T00:00:00.000Z',
)

res = s.reports.get_balance_sheet(req)

if res.balance_sheet is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetBalanceSheetRequest](../../models/operations/getbalancesheetrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |


### Response

**[operations.GetBalanceSheetResponse](../../models/operations/getbalancesheetresponse.md)**


## get_cash_flow_statement

Gets the latest cash flow statement for a company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCashFlowStatementRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    period_length=4,
    periods_to_compare=20,
    start_month='2022-10-23T00:00:00.000Z',
)

res = s.reports.get_cash_flow_statement(req)

if res.cash_flow_statement is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetCashFlowStatementRequest](../../models/operations/getcashflowstatementrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.GetCashFlowStatementResponse](../../models/operations/getcashflowstatementresponse.md)**


## get_profit_and_loss

Gets the latest profit and loss for a company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetProfitAndLossRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    period_length=4,
    periods_to_compare=20,
    start_month='2022-10-23T00:00:00.000Z',
)

res = s.reports.get_profit_and_loss(req)

if res.profit_and_loss_report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetProfitAndLossRequest](../../models/operations/getprofitandlossrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.GetProfitAndLossResponse](../../models/operations/getprofitandlossresponse.md)**


## is_aged_creditors_report_available

Indicates whether the aged creditor report is available for the company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.IsAgedCreditorsReportAvailableRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.reports.is_aged_creditors_report_available(req)

if res.is_aged_creditors_report_available_200_application_json_boolean is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.IsAgedCreditorsReportAvailableRequest](../../models/operations/isagedcreditorsreportavailablerequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |


### Response

**[operations.IsAgedCreditorsReportAvailableResponse](../../models/operations/isagedcreditorsreportavailableresponse.md)**


## is_aged_debtor_report_available

Indicates whether the aged debtor report is available for the company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.IsAgedDebtorReportAvailableRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.reports.is_aged_debtor_report_available(req)

if res.is_aged_debtor_report_available_200_application_json_boolean is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.IsAgedDebtorReportAvailableRequest](../../models/operations/isageddebtorreportavailablerequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |


### Response

**[operations.IsAgedDebtorReportAvailableResponse](../../models/operations/isageddebtorreportavailableresponse.md)**

