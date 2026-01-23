# Transactions

## Overview

Create new bank account transactions for a company's connections, and see previous operations.

### Available Operations

* [create](#create) - Create bank transactions
* [get_create_model](#get_create_model) - Get create bank transactions model
* [get_create_operation](#get_create_operation) - Get create operation
* [list_create_operations](#list_create_operations) - List create operations

## create

﻿The *Create bank transactions* endpoint creates new [bank transactions](https://docs.codat.io/bank-feeds-api#/schemas/BankTransactions) for a given company's connection.

[Bank transactions](https://docs.codat.io/bank-feeds-api#/schemas/BankTransactions) are records of monetary amounts that have moved in and out of an SMB's bank account.

**Integration-specific behavior**

The required properties may vary based on the integration. For detailed requirements specific to each accounting software, refer to the API reference examples.
Alternatively, you can view the [Get create bank transaction model](https://docs.codat.io/bank-feeds-api#/operations/get-create-bank-transactions-model) for more information.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-bank-transactions" method="post" path="/companies/{companyId}/connections/{connectionId}/push/bankAccounts/{accountId}/bankTransactions" -->
```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared
from decimal import Decimal


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.transactions.create(request={
        "create_bank_transactions": {
            "account_id": "49cd5a42-b311-4750-9361-52e2ed1d4653",
            "transactions": [
                {
                    "amount": Decimal("100"),
                    "balance": Decimal("100"),
                    "counterparty": "Bank of Example",
                    "date_": "2023-08-22T10:21:00",
                    "description": "Repayment of Credit Card",
                    "id": "716422529",
                    "reconciled": True,
                    "reference": "Ref-12345",
                    "transaction_type": shared.BankTransactionType.CREDIT,
                },
                {
                    "amount": Decimal("-100"),
                    "balance": Decimal("0"),
                    "counterparty": "Amazon",
                    "date_": "2023-08-22T10:22:00",
                    "description": "Amazon Purchase",
                    "id": "716422530",
                    "reconciled": False,
                    "reference": "Ref-12346",
                    "transaction_type": shared.BankTransactionType.DEBIT,
                },
                {
                    "amount": Decimal("-60"),
                    "balance": Decimal("-60"),
                    "counterparty": "Office Mart",
                    "date_": "2023-08-22T10:23:00",
                    "description": "Office Supplies",
                    "id": "716422531",
                    "reconciled": False,
                    "reference": "Ref-12347",
                    "transaction_type": shared.BankTransactionType.DEBIT,
                },
            ],
        },
        "account_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateBankTransactionsRequest](../../models/operations/createbanktransactionsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[shared.CreateBankTransactionsResponse](../../models/shared/createbanktransactionsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_create_model

The *Get create bank account transactions model* endpoint returns the expected data for the request payload when creating [bank account transactions](https://docs.codat.io/bank-feeds-api#/schemas/BankTransactions) for a given company and integration.

[Bank account transactions](https://docs.codat.io/bank-feeds-api#/schemas/BankTransactions) are records of money that has moved in and out of an SMB's bank account.

**Integration-specific behavior**

See the *response examples* for integration-specific indicative models.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-create-bank-transactions-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/bankAccounts/{accountId}/bankTransactions" -->
```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.transactions.get_create_model(request={
        "account_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetCreateBankTransactionsModelRequest](../../models/operations/getcreatebanktransactionsmodelrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[shared.PushOption](../../models/shared/pushoption.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_create_operation

The **Get create operation** endpoint returns a specific [write operation](/using-the-api/push) identified by the `pushOperationKey` that was performed on the company.

Write operations are actions that send requests to Codat, enabling the creation, updating, deletion of records, or uploading attachments in the connected accounting software.

For bank feeds, your push operations will only relate to the `bankTransactions` data type.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-create-operation" method="get" path="/companies/{companyId}/push/{pushOperationKey}" -->
```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.transactions.get_create_operation(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "push_operation_key": "23a26d56-6e3d-4414-865c-4fa7ebbb43e3",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetCreateOperationRequest](../../models/operations/getcreateoperationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[shared.PushOperation](../../models/shared/pushoperation.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_create_operations

The **List create operations** endpoint returns a list of [write operations](/using-the-api/push) performed on the company.

Write operations are actions that send requests to Codat, enabling the creation, updating, deletion of records, or uploading attachments in the connected accounting software. 

For bank feeds, use this endpoint to view write operations related to the `bankTransactions` data type.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-create-operations" method="get" path="/companies/{companyId}/push" -->
```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.transactions.list_create_operations(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListCreateOperationsRequest](../../models/operations/listcreateoperationsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[shared.PushOperations](../../models/shared/pushoperations.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |