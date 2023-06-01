# bank_accounts

## Overview

Bank accounts

### Available Operations

* [create](#create) - Create bank account
* [~~get~~](#get) - Get bank account :warning: **Deprecated**
* [get_create_update_model](#get_create_update_model) - Get create/update bank account model
* [list](#list) - List bank accounts
* [update](#update) - Update bank account

## create

Posts a new bank account to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bank account model](https://docs.codat.io/accounting-api#/operations/get-create-update-bankAccounts-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) to see which integrations support this endpoint.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBankAccountRequest(
    bank_account=shared.BankAccount(
        account_name='iusto',
        account_number='dicta',
        account_type=shared.BankAccountBankAccountType.DEBIT,
        available_balance=3179.83,
        balance=8804.76,
        currency='commodi',
        i_ban='repudiandae',
        id='13b99d48-8e1e-491e-850a-d2abd4426980',
        institution='magni',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='assumenda',
        nominal_code='ipsam',
        overdraft_limit=46.95,
        sort_code='fugit',
        source_modified_date='dolorum',
    ),
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=569618,
)

res = s.bank_accounts.create(req)

if res.create_bank_account_response is not None:
    # handle response
```

## ~~get~~

Gets the bank account with a given ID

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetBankAccountRequest(
    account_id='tempora',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_accounts.get(req)

if res.bank_account is not None:
    # handle response
```

## get_create_update_model

Get create/update bank account model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating and updating bank accounts.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateBankAccountsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_accounts.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

## list

Gets the list of bank accounts for a given connection

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBankAccountsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='facilis',
)

res = s.bank_accounts.list(req)

if res.bank_accounts is not None:
    # handle response
```

## update

Posts an updated bank account to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call []().

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support updating bank accounts.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateBankAccountRequest(
    bank_account=shared.BankAccount(
        account_name='tempore',
        account_number='labore',
        account_type=shared.BankAccountBankAccountType.DEBIT,
        available_balance=4332.88,
        balance=2487.53,
        currency='eligendi',
        i_ban='sint',
        id='69e9a3ef-a77d-4fb1-8cd6-6ae395efb9ba',
        institution='blanditiis',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='deleniti',
        nominal_code='sapiente',
        overdraft_limit=2305.33,
        sort_code='deserunt',
        source_modified_date='nisi',
    ),
    bank_account_id='vel',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=618809,
)

res = s.bank_accounts.update(req)

if res.update_bank_account_response is not None:
    # handle response
```
