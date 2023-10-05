# FinancialStatementsCashFlow
(*financial_statements.cash_flow*)

### Available Operations

* [get](#get) - Get cash flow statement

## get

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

res = s.financial_statements.cash_flow.get(req)

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

