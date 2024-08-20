# CodatLendingBankingTransactions
(*banking.transactions*)

### Available Operations

* [get](#get) - Get bank transaction
* [list](#list) - List transactions

## get

The *Get transaction* endpoint returns a single transaction for a given transactionId.

[Transactions](https://docs.codat.io/lending-api#/schemas/Transaction) provide an immutable source of up-to-date information on income and expenditure.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/banking?view=tab-by-data-type&dataType=banking-transactions) for integrations that support getting a specific transaction.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).


### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

s = CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)


res = s.banking.transactions.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "transaction_id": "<value>",
})

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetBankingTransactionRequest](../../models/operations/getbankingtransactionrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |


### Response

**[shared.BankingTransaction](../../models/shared/bankingtransaction.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |

## list

The *List transactions* endpoint returns a list of [transactions](https://docs.codat.io/lending-api#/schemas/Transaction) for a given company's connection.

[Transactions](https://docs.codat.io/lending-api#/schemas/Transaction) provide an immutable source of up-to-date information on income and expenditure.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).
    

### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

s = CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)


res = s.banking.transactions.list(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "order_by": "-modifiedDate",
    "page": 1,
    "page_size": 100,
    "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
})

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListBankingTransactionsRequest](../../models/operations/listbankingtransactionsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[shared.BankingTransactions](../../models/shared/bankingtransactions.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.ErrorMessage                 | 400,401,402,403,404,409,429,500,503 | application/json                    |
| errors.SDKError                     | 4xx-5xx                             | */*                                 |
