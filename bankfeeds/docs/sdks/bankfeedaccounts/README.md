# bank_feed_accounts

## Overview

Bank feed bank accounts

### Available Operations

* [create](#create) - Create a bank feed bank account
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
            account_name='perferendis',
            account_number='magni',
            account_type='assumenda',
            balance=3698.08,
            currency='GBP',
            feed_start_date='2022-10-23T00:00:00.000Z',
            id='a94bb4f6-3c96-49e9-a3ef-a77dfb14cd66',
            modified_date='2022-10-23T00:00:00.000Z',
            sort_code='accusamus',
            status='non',
        ),
        shared.BankFeedAccount(
            account_name='occaecati',
            account_number='enim',
            account_type='accusamus',
            balance=9654.17,
            currency='EUR',
            feed_start_date='2022-10-23T00:00:00.000Z',
            id='ba88f3a6-6997-4074-ba44-69b6e2141959',
            modified_date='2022-10-23T00:00:00.000Z',
            sort_code='sint',
            status='accusantium',
        ),
        shared.BankFeedAccount(
            account_name='mollitia',
            account_number='reiciendis',
            account_type='mollitia',
            balance=3209.97,
            currency='USD',
            feed_start_date='2022-10-23T00:00:00.000Z',
            id='e2516fe4-c8b7-411e-9b7f-d2ed028921cd',
            modified_date='2022-10-23T00:00:00.000Z',
            sort_code='maxime',
            status='ea',
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
        account_name='excepturi',
        account_number='odit',
        account_type='ea',
        balance=332.22,
        currency='GBP',
        feed_start_date='2022-10-23T00:00:00.000Z',
        id='b576b0d5-f0d3-40c5-bbb2-587053202c73',
        modified_date='2022-10-23T00:00:00.000Z',
        sort_code='nostrum',
        status='hic',
    ),
    account_id='EILBDVJVNUAGVKRQ',
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

