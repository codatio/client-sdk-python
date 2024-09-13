# TransactionsSDK
(*transactions*)

## Overview

Retrieve standardized data from linked commerce software.

### Available Operations

* [get](#get) - Get transaction
* [list](#list) - List transactions

## get

The *Get transaction* endpoint returns a single transaction for a given transactionId.

[Transactions](https://docs.codat.io/commerce-api#/schemas/Transaction) detail all financial affairs recorded in the commerce or point of sale system.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=commerce-transactions) for integrations that support getting a specific transaction.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
from codat_commerce import CodatCommerce

s = CodatCommerce(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.transactions.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "transaction_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.GetTransactionRequest](../../models/gettransactionrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.Transaction](../../models/transaction.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| models.SDKError                 | 4xx-5xx                         | */*                             |


## list

The *List transactions* endpoint returns a list of [transactions](https://docs.codat.io/commerce-api#/schemas/Transaction) for a given company's connection.

[Transactions](https://docs.codat.io/commerce-api#/schemas/Transaction) detail all financial affairs recorded in the commerce or point of sale system.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
from codat_commerce import CodatCommerce

s = CodatCommerce(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.transactions.list(request={
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

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.ListTransactionsRequest](../../models/listtransactionsrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.Transactions](../../models/transactions.md)**

### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.ErrorMessage                 | 400,401,402,403,404,409,429,500,503 | application/json                    |
| models.SDKError                     | 4xx-5xx                             | */*                                 |
