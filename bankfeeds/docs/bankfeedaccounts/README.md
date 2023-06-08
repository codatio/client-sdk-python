# bank_feed_accounts

## Overview

Bank feed bank accounts

### Available Operations

* [create](#create) - Create bank feed bank accounts
* [get](#get) - List bank feed bank accounts
* [update](#update) - Update bank feed bank account

## create

Put BankFeed BankAccounts for a single data source connected to a single company.

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
    request_body=[
        shared.BankFeedAccount(
            account_name='ipsa',
            account_number='reiciendis',
            account_type='est',
            balance=6531.4,
            currency='laborum',
            feed_start_date='2022-10-23T00:00:00.000Z',
            id='352c5955-907a-4ff1-a3a2-fa9467739251',
            modified_date='2022-10-23T00:00:00.000Z',
            sort_code='animi',
            status='enim',
        ),
    ],
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_feed_accounts.create(req)

if res.bank_feed_accounts is not None:
    # handle response
```

## get

Get BankFeed BankAccounts for a single data source connected to a single company.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetBankFeedsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_feed_accounts.get(req)

if res.bank_feed_accounts is not None:
    # handle response
```

## update

Update a single BankFeed BankAccount for a single data source connected to a single company.

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
        account_name='odit',
        account_number='quo',
        account_type='sequi',
        balance=9495.72,
        currency='ipsam',
        feed_start_date='2022-10-23T00:00:00.000Z',
        id='d019da1f-fe78-4f09-bb00-74f15471b5e6',
        modified_date='2022-10-23T00:00:00.000Z',
        sort_code='quae',
        status='ipsum',
    ),
    account_id='7110701885',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_feed_accounts.update(req)

if res.bank_feed_account is not None:
    # handle response
```
