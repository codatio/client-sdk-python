# accounts

## Overview

Accounts

### Available Operations

* [create](#create) - Create account
* [get](#get) - Get account
* [get_create_model](#get_create_model) - Get create account model
* [list](#list) - List accounts

## create

Creates a new account for a given company.

Required data may vary by integration. To see what data to post, first call [Get create account model](https://docs.codat.io/accounting-api#/operations/get-create-chartOfAccounts-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support creating an account.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateAccountRequest(
    account=shared.Account(
        currency='quibusdam',
        current_balance=6027.63,
        description='Invoices the business has issued but has not yet collected payment on.',
        fully_qualified_category='Asset.Current',
        fully_qualified_name='Asset.Current.Accounts Receivable',
        id='1b6266d1-1e44-46c5-8eb5-a8f98e03124e',
        is_bank_account=False,
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='nulla',
        name='Accounts Receivable',
        nominal_code='610',
        source_modified_date='corrupti',
        status=shared.AccountStatusEnum.ACTIVE,
        type=shared.AccountTypeEnum.ASSET,
        valid_datatype_links=[
            shared.ValidDataTypeLinks(
                links=[
                    'error',
                    'deserunt',
                ],
                property='suscipit',
            ),
            shared.ValidDataTypeLinks(
                links=[
                    'magnam',
                    'debitis',
                ],
                property='ipsa',
            ),
            shared.ValidDataTypeLinks(
                links=[
                    'tempora',
                    'suscipit',
                    'molestiae',
                    'minus',
                ],
                property='placeat',
            ),
            shared.ValidDataTypeLinks(
                links=[
                    'iusto',
                    'excepturi',
                    'nisi',
                ],
                property='recusandae',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=836079,
)

res = s.accounts.create(req)

if res.create_account_response is not None:
    # handle response
```

## get

Gets a single account corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountRequest(
    account_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.accounts.get(req)

if res.account is not None:
    # handle response
```

## get_create_model

Get create account model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support creating an account.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateChartOfAccountsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.accounts.get_create_model(req)

if res.push_option is not None:
    # handle response
```

## list

Gets the latest accounts for a company

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListAccountsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='ab',
)

res = s.accounts.list(req)

if res.accounts is not None:
    # handle response
```
