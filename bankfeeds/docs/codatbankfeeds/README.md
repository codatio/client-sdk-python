# CodatBankFeeds SDK

## Overview

Bank Feeds API enables your SMB users to set up bank feeds from accounts in your application to supported accounting platforms.

A bank feed is a connection between a source bank account—in your application—and a target bank account in a supported accounting package.

[Read more...](https://docs.codat.io/bank-feeds-api/overview)

[See our OpenAPI spec](https://github.com/codatio/oas) 

### Available Operations

* [create](#create) - Create bank transactions
* [create](#create) - Create bank feed bank accounts
* [create](#create) - Create connection
* [create](#create) - Create company
* [delete](#delete) - Delete connection
* [delete](#delete) - Delete a company
* [get](#get) - List push options for bank account bank transactions
* [get](#get) - List bank feed bank accounts
* [get](#get) - Get connection
* [get](#get) - Get company
* [list](#list) - List bank transactions for bank account
* [list](#list) - List connections
* [list](#list) - List companies
* [proxy](#proxy) - A proxy or passthrough endpoint used to query unsupported third party endpoints.
* [unlink_connection](#unlink_connection) - Unlink connection
* [update](#update) - Update bank feed bank account
* [update](#update) - Update company

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
        account_id='animi',
        transactions=[
            shared.BankTransactionLine(
                amount=1381.83,
                balance=7783.46,
                cleared_on_date='sequi',
                counterparty='tenetur',
                description='ipsam',
                id='ad019da1-ffe7-48f0-97b0-074f15471b5e',
                modified_date='commodi',
                reconciled=False,
                reference='repudiandae',
                source_modified_date='quae',
                transaction_type=shared.BankTransactionType.INT,
            ),
            shared.BankTransactionLine(
                amount=6924.72,
                balance=5651.89,
                cleared_on_date='excepturi',
                counterparty='pariatur',
                description='modi',
                id='88e1e91e-450a-4d2a-bd44-269802d502a9',
                modified_date='tempora',
                reconciled=False,
                reference='facilis',
                source_modified_date='tempore',
                transaction_type=shared.BankTransactionType.FEE,
            ),
        ],
    ),
    account_id='delectus',
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=433288,
)

res = s.codat_bank_feeds.create(req)

if res.create_bank_transactions_response is not None:
    # handle response
```

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
            account_name='eligendi',
            account_number='sint',
            account_type='aliquid',
            balance=5920.42,
            currency='necessitatibus',
            feed_start_date='sint',
            id='a3efa77d-fb14-4cd6-aae3-95efb9ba88f3',
            modified_date='deserunt',
            sort_code='nisi',
            status='vel',
        ),
    ],
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.codat_bank_feeds.create(req)

if res.bank_feed_accounts is not None:
    # handle response
```

## create

Create a data connection for a company

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateDataConnectionRequest(
    request_body=operations.CreateDataConnectionRequestBody(
        platform_key='natus',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.codat_bank_feeds.create(req)

if res.connection is not None:
    # handle response
```

## create

Create a new company

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    description='Requested early access to the new financing scheme.',
    name='Bank of Dave',
)

res = s.codat_bank_feeds.create(req)

if res.company is not None:
    # handle response
```

## delete

Revoke and remove a connection from a company.
This operation is not reversible - the end user would need to reauthorize a new data connection if you wish to view new data for this company.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DeleteCompanyConnectionRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.codat_bank_feeds.delete(req)

if res.status_code == 200:
    # handle response
```

## delete

Delete the given company from Codat.
This operation is not reversible.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DeleteCompanyRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.codat_bank_feeds.delete(req)

if res.status_code == 200:
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
    account_id='omnis',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.codat_bank_feeds.get(req)

if res.push_option is not None:
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

res = s.codat_bank_feeds.get(req)

if res.bank_feed_accounts is not None:
    # handle response
```

## get

Get a single connection for a company

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCompanyConnectionRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.codat_bank_feeds.get(req)

if res.connection is not None:
    # handle response
```

## get

Get metadata for a single company

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCompanyRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.codat_bank_feeds.get(req)

if res.company is not None:
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
    account_id='molestiae',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='perferendis',
)

res = s.codat_bank_feeds.list(req)

if res.bank_transactions_response is not None:
    # handle response
```

## list

List the connections for a company

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListCompanyConnectionsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='nihil',
)

res = s.codat_bank_feeds.list(req)

if res.connections is not None:
    # handle response
```

## list

List all companies that you have created in Codat.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListCompaniesRequest(
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='magnam',
)

res = s.codat_bank_feeds.list(req)

if res.companies is not None:
    # handle response
```

## proxy

A proxy or passthrough endpoint used to query unsupported third party endpoints.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ProxyRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    endpoint='generatecredentials?dataconnectionid={connectionId}',
)

res = s.codat_bank_feeds.proxy(req)

if res.proxy_response is not None:
    # handle response
```

## unlink_connection

This allows you to deauthorize a connection, without deleting it from Codat. This means you can still view any data that has previously been pulled into Codat, and also lets you re-authorize in future if your customer wishes to resume sharing their data.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UnlinkConnectionRequest(
    request_body=operations.UnlinkConnectionRequestBody(
        status='distinctio',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.codat_bank_feeds.unlink_connection(req)

if res.connection is not None:
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
        account_name='id',
        account_number='labore',
        account_type='labore',
        balance=3834.62,
        currency='natus',
        feed_start_date='nobis',
        id='6e214195-9890-4afa-963e-2516fe4c8b71',
        modified_date='architecto',
        sort_code='repudiandae',
        status='ullam',
    ),
    account_id='expedita',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.codat_bank_feeds.update(req)

if res.bank_feed_account is not None:
    # handle response
```

## update

Updates the given company with a new name and description

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateCompanyRequest(
    company_request_body=shared.CompanyRequestBody(
        description='Requested early access to the new financing scheme.',
        name='Bank of Dave',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.codat_bank_feeds.update(req)

if res.company is not None:
    # handle response
```
