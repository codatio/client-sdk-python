# transactions

## Overview

Transactions represent debits and credits from a source account.

### Available Operations

* [create](#create) - Create bank account transactions
* [get_operation](#get_operation) - Get push operation
* [list_operations](#list_operations) - List push operations

## create

﻿The *Create bank account transactions* endpoint creates new [bank account transactions](https://docs.codat.io/bank-feeds-api#/schemas/BankTransactions) for a given company's connection.

[Bank account transactions](https://docs.codat.io/bank-feeds-api#/schemas/BankTransactions) are records of monetary amounts that have moved in and out of an SMB's bank account.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create bank transaction model](https://docs.codat.io/bank-feeds-api#/operations/get-create-bankTransactions-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) for integrations that support creating a bank account transactions.


### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBankTransactionsRequest(
    create_bank_transactions=shared.CreateBankTransactions(
        account_id='corporis',
        transactions=[
            shared.CreateBankAccountTransaction(
                amount=7506.86,
                balance=3154.28,
                date_='2022-10-23T00:00:00.000Z',
                description='nemo',
                id='5907aff1-a3a2-4fa9-8677-39251aa52c3f',
            ),
        ],
    ),
    account_id='9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=662527,
)

res = s.transactions.create(req)

if res.create_bank_transactions_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateBankTransactionsRequest](../../models/operations/createbanktransactionsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |


### Response

**[operations.CreateBankTransactionsResponse](../../models/operations/createbanktransactionsresponse.md)**


## get_operation

Retrieve push operation.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetPushOperationRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    push_operation_key='d019da1f-fe78-4f09-bb00-74f15471b5e6',
)

res = s.transactions.get_operation(req)

if res.push_operation is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPushOperationRequest](../../models/operations/getpushoperationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.GetPushOperationResponse](../../models/operations/getpushoperationresponse.md)**


## list_operations

List push operation records.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCompanyPushHistoryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='repudiandae',
)

res = s.transactions.list_operations(req)

if res.push_history_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetCompanyPushHistoryRequest](../../models/operations/getcompanypushhistoryrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |


### Response

**[operations.GetCompanyPushHistoryResponse](../../models/operations/getcompanypushhistoryresponse.md)**

