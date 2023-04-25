# accounts

## Overview

Accounts

### Available Operations

* [create_account](#create_account) - Create account
* [get_account](#get_account) - Get account
* [get_create_chart_of_accounts_model](#get_create_chart_of_accounts_model) - Get create account model
* [list_accounts](#list_accounts) - List accounts

## create_account

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
        currency="quibusdam",
        current_balance=6027.63,
        description="nulla",
        fully_qualified_category="corrupti",
        fully_qualified_name="illum",
        id="69a674e0-f467-4cc8-b96e-d151a05dfc2d",
        is_bank_account=False,
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="at",
        name="Javier Schmidt",
        nominal_code="totam",
        source_modified_date="porro",
        status="Archived",
        type="Unknown",
        valid_datatype_links=[
            shared.ValidDataTypeLinks(
                links=[
                    "occaecati",
                    "fugit",
                    "deleniti",
                ],
                property="hic",
            ),
            shared.ValidDataTypeLinks(
                links=[
                    "totam",
                    "beatae",
                    "commodi",
                    "molestiae",
                ],
                property="modi",
            ),
            shared.ValidDataTypeLinks(
                links=[
                    "impedit",
                ],
                property="cum",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=456150,
)

res = s.accounts.create_account(req)

if res.create_account_response is not None:
    # handle response
```

## get_account

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
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.accounts.get_account(req)

if res.account is not None:
    # handle response
```

## get_create_chart_of_accounts_model

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.accounts.get_create_chart_of_accounts_model(req)

if res.push_option is not None:
    # handle response
```

## list_accounts

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="ipsum",
)

res = s.accounts.list_accounts(req)

if res.accounts is not None:
    # handle response
```
