# bank_accounts

## Overview

Bank accounts

### Available Operations

* [create](#create) - Create bank account
* [get](#get) - Get bank account
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
        account_name="natus",
        account_number="laboriosam",
        account_type="Debit",
        available_balance=9025.99,
        balance=6818.2,
        currency="in",
        i_ban="corporis",
        id="96eb10fa-aa23-452c-9955-907aff1a3a2f",
        institution="mollitia",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="occaecati",
        nominal_code="numquam",
        overdraft_limit=4143.69,
        sort_code="quam",
        source_modified_date="molestiae",
    ),
    allow_sync_on_push_complete=False,
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=244425,
)

res = s.bank_accounts.create(req)

if res.create_bank_account_response is not None:
    # handle response
```

## get

Gets the bank account with a given ID

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
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="error",
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
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support updating bank accounts.

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
        account_name="quia",
        account_number="quis",
        account_type="Unknown",
        available_balance=6747.52,
        balance=6563.3,
        currency="enim",
        i_ban="odit",
        id="c3f5ad01-9da1-4ffe-b8f0-97b0074f1547",
        institution="dicta",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="harum",
        nominal_code="enim",
        overdraft_limit=8804.76,
        sort_code="commodi",
        source_modified_date="repudiandae",
    ),
    bank_account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    timeout_in_minutes=64147,
)

res = s.bank_accounts.update(req)

if res.update_bank_account_response is not None:
    # handle response
```
