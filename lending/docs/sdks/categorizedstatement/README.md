# CategorizedStatement
(*banking.categorized_statement*)

### Available Operations

* [get](#get) - Get categorized bank statement

## get

﻿> **Categorization engine**
>
> The categorization engine uses machine learning and has been fully trained against Plaid and TrueLayer banking data sources. It is not fully trained against the Basiq banking data source.

The _Get categorized bank statement_ endpoint provides a fully categorized list of banking transactions for a company. Accounts and transaction data are obtained from the company's banking data sources.

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCategorizedBankStatementRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    page=1,
    page_size=100,
)

res = s.banking.categorized_statement.get(req)

if res.enhanced_cash_flow_transactions is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetCategorizedBankStatementRequest](../../models/operations/getcategorizedbankstatementrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |


### Response

**[operations.GetCategorizedBankStatementResponse](../../models/operations/getcategorizedbankstatementresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4x-5xx                          | */*                             |
