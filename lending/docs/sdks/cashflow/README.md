# FinancialStatements.CashFlow

## Overview

### Available Operations

* [get](#get) - Get cash flow statement

## get

Gets the latest cash flow statement for a company.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-accounting-cash-flow-statement" method="get" path="/companies/{companyId}/data/financials/cashFlowStatement" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_statements.cash_flow.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "period_length": 4,
        "periods_to_compare": 20,
        "start_month": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAccountingCashFlowStatementRequest](../../models/operations/getaccountingcashflowstatementrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[shared.AccountingCashFlowStatement](../../models/shared/accountingcashflowstatement.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 401, 402, 403, 404, 409, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |