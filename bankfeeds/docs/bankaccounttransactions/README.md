# bank_account_transactions

## Overview

Bank feed bank accounts

### Available Operations

* [create](#create) - Create bank transactions
* [get](#get) - List push options for bank account bank transactions
* [list](#list) - List bank transactions for bank account

## create

Posts bank transactions to the accounting package for a given company.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) to see which integrations support this endpoint.

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
    bank_transactions=shared.BankTransactions(
        account_id='molestiae',
        amount=7991.59,
        balance=8009.11,
        cleared_on_date='2022-10-23T00:00:00.000Z',
        description='totam',
        id='ca1ba928-fc81-4674-acb7-39205929396f',
        modified_date='2022-10-23T00:00:00.000Z',
        reconciled=False,
        source_modified_date='2022-10-23T00:00:00.000Z',
        transaction_type=shared.BankTransactionType.ATM,
    ),
    account_id='9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=613064,
)

res = s.bank_account_transactions.create(req)

if res.create_bank_transactions_response is not None:
    # handle response
```

## get

Gets the options of pushing bank account transactions.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateBankAccountModelRequest(
    account_id='9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_account_transactions.get(req)

if res.push_option is not None:
    # handle response
```

## list

Gets bank transactions for a given bank account ID

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBankAccountTransactionsRequest(
    account_id='EILBDVJVNUAGVKRQ',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='quidem',
)

res = s.bank_account_transactions.list(req)

if res.bank_transactions_response is not None:
    # handle response
```
