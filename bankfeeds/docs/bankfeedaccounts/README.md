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
            account_name='dolor',
            account_number='debitis',
            account_type='a',
            balance=6800.56,
            currency='in',
            feed_start_date='2022-10-23T00:00:00.000Z',
            id='dfb14cd6-6ae3-495e-bb9b-a88f3a669970',
            modified_date='2022-10-23T00:00:00.000Z',
            sort_code='magnam',
            status='distinctio',
        ),
        shared.BankFeedAccount(
            account_name='id',
            account_number='labore',
            account_type='labore',
            balance=3834.62,
            currency='natus',
            feed_start_date='2022-10-23T00:00:00.000Z',
            id='6e214195-9890-4afa-963e-2516fe4c8b71',
            modified_date='2022-10-23T00:00:00.000Z',
            sort_code='repudiandae',
            status='ullam',
        ),
        shared.BankFeedAccount(
            account_name='expedita',
            account_number='nihil',
            account_type='repellat',
            balance=8411.4,
            currency='sed',
            feed_start_date='2022-10-23T00:00:00.000Z',
            id='d028921c-ddc6-4926-81fb-576b0d5f0d30',
            modified_date='2022-10-23T00:00:00.000Z',
            sort_code='corporis',
            status='hic',
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
        account_name='libero',
        account_number='nobis',
        account_type='dolores',
        balance=3394.04,
        currency='totam',
        feed_start_date='2022-10-23T00:00:00.000Z',
        id='053202c7-3d5f-4e9b-90c2-8909b3fe49a8',
        modified_date='2022-10-23T00:00:00.000Z',
        sort_code='provident',
        status='nobis',
    ),
    account_id='7110701885',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_feed_accounts.update(req)

if res.bank_feed_account is not None:
    # handle response
```
