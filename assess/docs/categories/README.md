# categories

## Overview

Categorisation

### Available Operations

* [get_account_category](#get_account_category) - Get suggested and/or confirmed category for a specific account
* [list_accounts_categories](#list_accounts_categories) - List suggested and confirmed account categories
* [list_available_account_categories](#list_available_account_categories) - List account categories
* [update_account_category](#update_account_category) - Patch account categories
* [update_accounts_categories](#update_accounts_categories) - Confirm categories for accounts

## get_account_category

Get category for specific nominal account.

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountCategoryRequest(
    account_id="provident",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.categories.get_account_category(req)

if res.categorised_account is not None:
    # handle response
```

## list_accounts_categories

Lists suggested and confirmed chart of account categories for the given company and data connection.

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListAccountsCategoriesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="distinctio",
)

res = s.categories.list_accounts_categories(req)

if res.categorised_accounts is not None:
    # handle response
```

## list_available_account_categories

Lists available account categories Codat's categorisation engine can provide. 

### Example Usage

```python
import codatassess


s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


res = s.categories.list_available_account_categories()

if res.categories is not None:
    # handle response
```

## update_account_category

Update category for a specific nominal account

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateAccountCategoryRequest(
    confirm_category=shared.ConfirmCategory(
        confirmed=shared.AccountCategory(
            detail_type="quibusdam",
            subtype="unde",
            type="nulla",
        ),
    ),
    account_id="corrupti",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.categories.update_account_category(req)

if res.categorised_account is not None:
    # handle response
```

## update_accounts_categories

Comfirms the categories for all or a batch of accounts for a specific connection.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateAccountsCategoriesRequest(
    confirm_categories=shared.ConfirmCategories(
        categories=[
            shared.ConfirmCategoriesCategories(
                account_ref=shared.ConfirmCategoriesCategoriesAccountRef(
                    id="69a674e0-f467-4cc8-b96e-d151a05dfc2d",
                ),
                confirmed=shared.AccountCategory(
                    detail_type="at",
                    subtype="maiores",
                    type="molestiae",
                ),
            ),
            shared.ConfirmCategoriesCategories(
                account_ref=shared.ConfirmCategoriesCategoriesAccountRef(
                    id="cc78ca1b-a928-4fc8-9674-2cb739205929",
                ),
                confirmed=shared.AccountCategory(
                    detail_type="dolor",
                    subtype="natus",
                    type="laboriosam",
                ),
            ),
            shared.ConfirmCategoriesCategories(
                account_ref=shared.ConfirmCategoriesCategoriesAccountRef(
                    id="fea7596e-b10f-4aaa-a352-c5955907aff1",
                ),
                confirmed=shared.AccountCategory(
                    detail_type="mollitia",
                    subtype="dolorem",
                    type="culpa",
                ),
            ),
            shared.ConfirmCategoriesCategories(
                account_ref=shared.ConfirmCategoriesCategoriesAccountRef(
                    id="2fa94677-3925-41aa-92c3-f5ad019da1ff",
                ),
                confirmed=shared.AccountCategory(
                    detail_type="vero",
                    subtype="nihil",
                    type="praesentium",
                ),
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.categories.update_accounts_categories(req)

if res.categorised_accounts is not None:
    # handle response
```
