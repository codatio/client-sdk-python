# bank_feed_accounts

## Overview

Bank feed bank accounts

### Available Operations

* [create](#create) - Create a bank feed bank account
* [delete](#delete) - delete bank feed bank account
* [list](#list) - List bank feed bank accounts
* [~~put_bank_feed~~](#put_bank_feed) - Create bank feed bank accounts :warning: **Deprecated**
* [update](#update) - Update bank feed bank account

## create

Post a BankFeed BankAccount for a single data source connected to a single company.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBankFeedRequest(
    bank_feed_account=shared.BankFeedAccount(
        account_name='maiores',
        account_number='dicta',
        account_type='corporis',
        balance=2961.4,
        currency='USD',
        feed_start_date='2022-10-23T00:00:00.000Z',
        id='b5e6e13b-99d4-488e-9e91-e450ad2abd44',
        modified_date='2022-10-23T00:00:00.000Z',
        sort_code='aliquid',
        status='cupiditate',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_feed_accounts.create(req)

if res.bank_feed_account is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateBankFeedRequest](../../models/operations/createbankfeedrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.CreateBankFeedResponse](../../models/operations/createbankfeedresponse.md)**


## delete

The *delete bank feed bank account* endpoint enables you to remove a source account.

Removing a source account will also remove any mapping between the source bank feed bank accounts and the target bankfeed bank account.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DeleteBankFeedBankAccountRequest(
    bank_feed_account=shared.BankFeedAccount(
        account_name='quos',
        account_number='perferendis',
        account_type='magni',
        balance=8289.4,
        currency='USD',
        feed_start_date='2022-10-23T00:00:00.000Z',
        id='2a94bb4f-63c9-469e-9a3e-fa77dfb14cd6',
        modified_date='2022-10-23T00:00:00.000Z',
        sort_code='laborum',
        status='accusamus',
    ),
    account_id='13d946f0-c5d5-42bc-b092-97ece17923ab',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_feed_accounts.delete(req)

if res.push_operation is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DeleteBankFeedBankAccountRequest](../../models/operations/deletebankfeedbankaccountrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.DeleteBankFeedBankAccountResponse](../../models/operations/deletebankfeedbankaccountresponse.md)**


## list

﻿The *List bank feed bank accounts* endpoint returns a list of [bank feed accounts](https://docs.codat.io/bank-feeds-api#/schemas/BankFeedAccount) for a given company's connection.

[Bank feed accounts](https://docs.codat.io/bank-feeds-api#/schemas/BankFeedAccount) are the bank's bank account from which transactions are synced into the accounting platform.



### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBankFeedsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_feed_accounts.list(req)

if res.bank_feed_account is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListBankFeedsRequest](../../models/operations/listbankfeedsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.ListBankFeedsResponse](../../models/operations/listbankfeedsresponse.md)**


## ~~put_bank_feed~~

Put BankFeed BankAccounts for a single data source connected to a single company.

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.PutBankFeedRequest(
    request_body=[
        shared.BankFeedAccount(
            account_name='enim',
            account_number='accusamus',
            account_type='delectus',
            balance=6925.32,
            currency='USD',
            feed_start_date='2022-10-23T00:00:00.000Z',
            id='a88f3a66-9970-474b-a446-9b6e21419598',
            modified_date='2022-10-23T00:00:00.000Z',
            sort_code='accusantium',
            status='mollitia',
        ),
        shared.BankFeedAccount(
            account_name='reiciendis',
            account_number='mollitia',
            account_type='ad',
            balance=4314.18,
            currency='GBP',
            feed_start_date='2022-10-23T00:00:00.000Z',
            id='2516fe4c-8b71-41e5-b7fd-2ed028921cdd',
            modified_date='2022-10-23T00:00:00.000Z',
            sort_code='ea',
            status='excepturi',
        ),
        shared.BankFeedAccount(
            account_name='odit',
            account_number='ea',
            account_type='accusantium',
            balance=691.67,
            currency='EUR',
            feed_start_date='2022-10-23T00:00:00.000Z',
            id='576b0d5f-0d30-4c5f-bb25-87053202c73d',
            modified_date='2022-10-23T00:00:00.000Z',
            sort_code='hic',
            status='recusandae',
        ),
    ],
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_feed_accounts.put_bank_feed(req)

if res.bank_feed_accounts is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PutBankFeedRequest](../../models/operations/putbankfeedrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |


### Response

**[operations.PutBankFeedResponse](../../models/operations/putbankfeedresponse.md)**


## update

﻿The *Update bank feed bank account* endpoint updates a single bank feed bank account for a single data source connected to a single company.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateBankFeedRequest(
    bank_feed_account=shared.BankFeedAccount(
        account_name='omnis',
        account_number='facilis',
        account_type='perspiciatis',
        balance=318.38,
        currency='EUR',
        feed_start_date='2022-10-23T00:00:00.000Z',
        id='8909b3fe-49a8-4d9c-bf48-633323f9b77f',
        modified_date='2022-10-23T00:00:00.000Z',
        sort_code='dolorum',
        status='numquam',
    ),
    account_id='13d946f0-c5d5-42bc-b092-97ece17923ab',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_feed_accounts.update(req)

if res.bank_feed_account is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateBankFeedRequest](../../models/operations/updatebankfeedrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.UpdateBankFeedResponse](../../models/operations/updatebankfeedresponse.md)**

