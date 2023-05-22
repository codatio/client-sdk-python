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

Required data may vary by integration. To see what data to post, first call []().

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating bank accounts.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateBankAccountRequest(
    bank_account=shared.BankAccount(
        account_name='dolor',
        account_number='natus',
        account_type=shared.BankAccountBankAccountType.CREDIT,
        available_balance=9437.49,
        balance=9025.99,
        currency='fuga',
        i_ban='in',
        id='596eb10f-aaa2-4352-8595-5907aff1a3a2',
        institution='repellat',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='mollitia',
        nominal_code='occaecati',
        overdraft_limit=2532.91,
        sort_code='commodi',
        source_modified_date='quam',
    ),
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=474697,
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetBankAccountRequest(
    account_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListBankAccountsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='velit',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.UpdateBankAccountRequest(
    bank_account=shared.BankAccount(
        account_name='error',
        account_number='quia',
        account_type=shared.BankAccountBankAccountType.CREDIT,
        available_balance=1103.75,
        balance=6747.52,
        currency='animi',
        i_ban='enim',
        id='2c3f5ad0-19da-41ff-a78f-097b0074f154',
        institution='iusto',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='dicta',
        nominal_code='harum',
        overdraft_limit=3179.83,
        sort_code='accusamus',
        source_modified_date='commodi',
    ),
    bank_account_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=918236,
)

res = s.bank_accounts.update(req)

if res.update_bank_account_response is not None:
    # handle response
```
