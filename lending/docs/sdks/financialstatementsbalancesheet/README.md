# financial_statements_balance_sheet

### Available Operations

* [get](#get) - Get balance sheet
* [get_categorized_accounts](#get_categorized_accounts) - Get categorized balance sheet statement

## get

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

res = s.financial_statements_balance_sheet.get(req)

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


## get_categorized_accounts

The *Get categorized balance sheet statement* endpoint returns a list of categorized accounts that appear on a company’s Balance Sheet along with a balance per financial statement date.

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
    number_of_periods=568434,
    report_date='29-09-2020',
)

res = s.financial_statements_balance_sheet.get_categorized_accounts(req)

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

