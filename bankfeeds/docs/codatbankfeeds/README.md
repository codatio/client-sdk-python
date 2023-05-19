# CodatBankFeeds SDK

## Overview

Bank Feeds API enables your SMB users to set up bank feeds from accounts in your application to supported accounting platforms.

A bank feed is a connection between a source bank account—in your application—and a target bank account in a supported accounting package.

[Read more...](https://docs.codat.io/bank-feeds-api/overview)

[See our OpenAPI spec](https://github.com/codatio/oas) 

### Available Operations

* [create_bank_feed](#create_bank_feed) - Create bank feed bank accounts
* [create_bank_transactions](#create_bank_transactions) - Create bank transactions
* [get_bank_feeds](#get_bank_feeds) - List bank feed bank accounts
* [get_create_bank_account_model](#get_create_bank_account_model) - List push options for bank account bank transactions
* [list_bank_account_transactions](#list_bank_account_transactions) - List bank transactions for bank account
* [update_bank_feed](#update_bank_feed) - Update bank feed bank account

## create_bank_feed

Put BankFeed BankAccounts for a single data source connected to a single company.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateBankFeedRequest(
    request_body=[
        shared.BankFeedAccount(
            account_name='vitae',
            account_number='laborum',
            account_type='animi',
            balance=3172.02,
            currency='odit',
            feed_start_date='quo',
            id='3f5ad019-da1f-4fe7-8f09-7b0074f15471',
            modified_date='harum',
            sort_code='enim',
            status='accusamus',
        ),
        shared.BankFeedAccount(
            account_name='commodi',
            account_number='repudiandae',
            account_type='quae',
            balance=2168.22,
            currency='quidem',
            feed_start_date='molestias',
            id='9d488e1e-91e4-450a-92ab-d44269802d50',
            modified_date='fugit',
            sort_code='dolorum',
            status='excepturi',
        ),
    ],
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.codat_bank_feeds.create_bank_feed(req)

if res.bank_feed_accounts is not None:
    # handle response
```

## create_bank_transactions

Posts bank transactions to the accounting package for a given company.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) for integrations that support POST methods.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateBankTransactionsRequest(
    bank_transactions=shared.BankTransactions(
        account_id='tempora',
        transactions=[
            shared.BankTransactionLine(
                amount=7351.94,
                balance=2884.76,
                cleared_on_date='delectus',
                counterparty='eum',
                description='non',
                id='c969e9a3-efa7-47df-b14c-d66ae395efb9',
                modified_date='nam',
                reconciled=False,
                reference='id',
                source_modified_date='blanditiis',
                transaction_type=shared.BankTransactionType.POS,
            ),
            shared.BankTransactionLine(
                amount=9560.84,
                balance=2305.33,
                cleared_on_date='deserunt',
                counterparty='nisi',
                description='vel',
                id='997074ba-4469-4b6e-a141-959890afa563',
                modified_date='necessitatibus',
                reconciled=False,
                reference='odit',
                source_modified_date='nemo',
                transaction_type=shared.BankTransactionType.CREDIT,
            ),
            shared.BankTransactionLine(
                amount=4358.65,
                balance=9840.43,
                cleared_on_date='debitis',
                counterparty='eius',
                description='maxime',
                id='8b711e5b-7fd2-4ed0-a892-1cddc692601f',
                modified_date='quidem',
                reconciled=False,
                reference='ipsam',
                source_modified_date='voluptate',
                transaction_type=shared.BankTransactionType.DEP,
            ),
        ],
    ),
    account_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=722056,
)

res = s.codat_bank_feeds.create_bank_transactions(req)

if res.create_bank_transactions_response is not None:
    # handle response
```

## get_bank_feeds

Get BankFeed BankAccounts for a single data source connected to a single company.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetBankFeedsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.codat_bank_feeds.get_bank_feeds(req)

if res.bank_feed_accounts is not None:
    # handle response
```

## get_create_bank_account_model

Gets the options of pushing bank account transactions.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetCreateBankAccountModelRequest(
    account_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.codat_bank_feeds.get_create_bank_account_model(req)

if res.push_option is not None:
    # handle response
```

## list_bank_account_transactions

Gets bank transactions for a given bank account ID

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListBankAccountTransactionsRequest(
    account_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='eaque',
)

res = s.codat_bank_feeds.list_bank_account_transactions(req)

if res.bank_transactions_response is not None:
    # handle response
```

## update_bank_feed

Update a single BankFeed BankAccount for a single data source connected to a single company.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.UpdateBankFeedRequest(
    bank_feed_account=shared.BankFeedAccount(
        account_name='pariatur',
        account_number='nemo',
        account_type='voluptatibus',
        balance=166.27,
        currency='fugiat',
        feed_start_date='amet',
        id='0c5fbb25-8705-4320-ac73-d5fe9b90c289',
        modified_date='eaque',
        sort_code='occaecati',
        status='rerum',
    ),
    account_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.codat_bank_feeds.update_bank_feed(req)

if res.bank_feed_account is not None:
    # handle response
```
