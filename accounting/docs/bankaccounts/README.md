# bank_accounts

## Overview

Bank accounts

### Available Operations

* [create_bank_account](#create_bank_account) - Create bank account
* [get_all_bank_account](#get_all_bank_account) - Get bank account
* [get_bank_account](#get_bank_account) - Get bank account
* [get_create_update_bank_accounts_model](#get_create_update_bank_accounts_model) - Get create/update bank account model
* [list_bank_accounts](#list_bank_accounts) - List bank accounts
* [update_bank_account](#update_bank_account) - Update bank account

## create_bank_account

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
        account_name="repellat",
        account_number="mollitia",
        account_type="Credit",
        available_balance=2532.91,
        balance=4143.69,
        currency="quam",
        i_ban="molestiae",
        id="39251aa5-2c3f-45ad-819d-a1ffe78f097b",
        institution="perferendis",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="doloremque",
        nominal_code="reprehenderit",
        overdraft_limit=2828.07,
        sort_code="maiores",
        source_modified_date="dicta",
    ),
    allow_sync_on_push_complete=False,
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=359444,
)

res = s.bank_accounts.create_bank_account(req)

if res.create_bank_account_response is not None:
    # handle response
```

## get_all_bank_account

Gets the bank account for given account ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAllBankAccountRequest(
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    query="dolore",
)

res = s.bank_accounts.get_all_bank_account(req)

if res.bank_statement_account is not None:
    # handle response
```

## get_bank_account

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

res = s.bank_accounts.get_bank_account(req)

if res.bank_account is not None:
    # handle response
```

## get_create_update_bank_accounts_model

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

res = s.bank_accounts.get_create_update_bank_accounts_model(req)

if res.push_option is not None:
    # handle response
```

## list_bank_accounts

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
    query="iusto",
)

res = s.bank_accounts.list_bank_accounts(req)

if res.bank_accounts is not None:
    # handle response
```

## update_bank_account

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
        account_name="dicta",
        account_number="harum",
        account_type="Unknown",
        available_balance=8804.76,
        balance=4142.63,
        currency="repudiandae",
        i_ban="quae",
        id="3b99d488-e1e9-41e4-90ad-2abd44269802",
        institution="assumenda",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="ipsam",
        nominal_code="alias",
        overdraft_limit=1464.41,
        sort_code="dolorum",
        source_modified_date="excepturi",
    ),
    bank_account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    timeout_in_minutes=270008,
)

res = s.bank_accounts.update_bank_account(req)

if res.update_bank_account_response is not None:
    # handle response
```
