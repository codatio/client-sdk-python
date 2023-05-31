# accounts

## Overview

Accounts

### Available Operations

* [create](#create) - Create account
* [get](#get) - Get account
* [get_create_model](#get_create_model) - Get create account model
* [list](#list) - List accounts

## create

The *Create accounts* endpoint creates a new [account](https://docs.codat.io/accounting-api#/schemas/Account) for a given company's connection.

[Accounts](https://docs.codat.io/accounting-api#/schemas/Account) are the categories a business uses to record accounting transactions.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create account model](https://docs.codat.io/accounting-api#/operations/get-create-chartOfAccounts-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support creating an account.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
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
        status=shared.AccountStatus.ACTIVE,
        type=shared.AccountType.ASSET,
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

﻿The *Get account* endpoint returns a single [account](https://docs.codat.io/accounting-api#/schemas/Account) for a given `accountId`.

[Accounts](https://docs.codat.io/accounting-api#/schemas/Account) are the categories a business uses to record accounting transactions.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
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

﻿The *Get create account model* endpoint returns the expected data for the request payload when creating an [account](https://docs.codat.io/accounting-api#/schemas/Account) for a given company and integration.

[Accounts](https://docs.codat.io/accounting-api#/schemas/Account) are the categories a business uses to record accounting transactions.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support creating an account.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
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

﻿The *List accounts* endpoint returns a list of [accounts](https://docs.codat.io/accounting-api#/schemas/Account) for a given company's connection.

[Accounts](https://docs.codat.io/accounting-api#/schemas/Account) are the categories a business uses to record accounting transactions.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
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
