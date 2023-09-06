# financial_statements

## Overview

Financial data and reports from a linked accounting platform.

### Available Operations

* [get_account](#get_account) - Get account
* [get_balance_sheet](#get_balance_sheet) - Get balance sheet
* [get_cash_flow_statement](#get_cash_flow_statement) - Get cash flow statement
* [get_categorized_balance_sheet](#get_categorized_balance_sheet) - Get categorized balance sheet statement
* [get_categorized_profit_and_loss](#get_categorized_profit_and_loss) - Get categorized profit and loss statement
* [get_profit_and_loss](#get_profit_and_loss) - Get profit and loss
* [list_accounts](#list_accounts) - List accounts

## get_account

The *Get account* endpoint returns a single account for a given accountId.

[Accounts](https://docs.codat.io/accounting-api#/schemas/Account) are the categories a business uses to record accounting transactions.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support getting a specific account.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).


### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingAccountRequest(
    account_id='impedit',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.financial_statements.get_account(req)

if res.accounting_account is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingAccountRequest](../../models/operations/getaccountingaccountrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.GetAccountingAccountResponse](../../models/operations/getaccountingaccountresponse.md)**


## get_balance_sheet

Gets the latest balance sheet for a company.

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingBalanceSheetRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    period_length=4,
    periods_to_compare=20,
    start_month='2022-10-23T00:00:00.000Z',
)

res = s.financial_statements.get_balance_sheet(req)

if res.accounting_balance_sheet is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingBalanceSheetRequest](../../models/operations/getaccountingbalancesheetrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.GetAccountingBalanceSheetResponse](../../models/operations/getaccountingbalancesheetresponse.md)**


## get_cash_flow_statement

Gets the latest cash flow statement for a company.

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingCashFlowStatementRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    period_length=4,
    periods_to_compare=20,
    start_month='2022-10-23T00:00:00.000Z',
)

res = s.financial_statements.get_cash_flow_statement(req)

if res.accounting_cash_flow_statement is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAccountingCashFlowStatementRequest](../../models/operations/getaccountingcashflowstatementrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |


### Response

**[operations.GetAccountingCashFlowStatementResponse](../../models/operations/getaccountingcashflowstatementresponse.md)**


## get_categorized_balance_sheet

﻿The *Get enhanced balance sheet accounts* endpoint returns a list of categorized accounts that appear on a company’s Balance Sheet along with a balance per financial statement date.

Codat suggests a category for each account automatically, but you can [change it](https://docs.codat.io/lending/enhanced-financials/overview#categorize-accounts) to a more suitable one.

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCategorizedBalanceSheetStatementRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    number_of_periods=216550,
    report_date='29-09-2020',
)

res = s.financial_statements.get_categorized_balance_sheet(req)

if res.enhanced_financial_report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetCategorizedBalanceSheetStatementRequest](../../models/operations/getcategorizedbalancesheetstatementrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |


### Response

**[operations.GetCategorizedBalanceSheetStatementResponse](../../models/operations/getcategorizedbalancesheetstatementresponse.md)**


## get_categorized_profit_and_loss

﻿The *Get enhanced profit and loss accounts* endpoint returns a list of categorized accounts that appear on a company’s Profit and Loss statement. It also includes a balance as of the financial statement date.

Codat suggests a category for each account automatically, but you can [change it](https://docs.codat.io/lending/enhanced-financials/overview#categorize-accounts) to a more suitable one.

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCategorizedProfitAndLossStatementRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    number_of_periods=568434,
    report_date='29-09-2020',
)

res = s.financial_statements.get_categorized_profit_and_loss(req)

if res.enhanced_financial_report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.GetCategorizedProfitAndLossStatementRequest](../../models/operations/getcategorizedprofitandlossstatementrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |


### Response

**[operations.GetCategorizedProfitAndLossStatementResponse](../../models/operations/getcategorizedprofitandlossstatementresponse.md)**


## get_profit_and_loss

Gets the latest profit and loss for a company.

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingProfitAndLossRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    period_length=4,
    periods_to_compare=20,
    start_month='2022-10-23T00:00:00.000Z',
)

res = s.financial_statements.get_profit_and_loss(req)

if res.accounting_profit_and_loss_report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAccountingProfitAndLossRequest](../../models/operations/getaccountingprofitandlossrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |


### Response

**[operations.GetAccountingProfitAndLossResponse](../../models/operations/getaccountingprofitandlossresponse.md)**


## list_accounts

﻿The *List accounts* endpoint returns a list of [accounts](https://docs.codat.io/accounting-api#/schemas/Account) for a given company's connection.

[Accounts](https://docs.codat.io/accounting-api#/schemas/Account) are the categories a business uses to record accounting transactions.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListAccountingAccountsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='perferendis',
)

res = s.financial_statements.list_accounts(req)

if res.accounting_accounts is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingAccountsRequest](../../models/operations/listaccountingaccountsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |


### Response

**[operations.ListAccountingAccountsResponse](../../models/operations/listaccountingaccountsresponse.md)**

