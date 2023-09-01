# categories

## Overview

Categorisation

### Available Operations

* [~~get_account_category~~](#get_account_category) - Get suggested and/or confirmed category for a specific account :warning: **Deprecated**
* [~~list_accounts_categories~~](#list_accounts_categories) - List suggested and confirmed account categories :warning: **Deprecated**
* [~~list_available_account_categories~~](#list_available_account_categories) - List account categories :warning: **Deprecated**
* [~~update_account_category~~](#update_account_category) - Update account categories :warning: **Deprecated**
* [~~update_accounts_categories~~](#update_accounts_categories) - Confirm categories for accounts :warning: **Deprecated**

## ~~get_account_category~~

Get category for specific nominal account.

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountCategoryRequest(
    account_id='provident',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.categories.get_account_category(req)

if res.categorised_account is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAccountCategoryRequest](../../models/operations/getaccountcategoryrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.GetAccountCategoryResponse](../../models/operations/getaccountcategoryresponse.md)**


## ~~list_accounts_categories~~

Lists suggested and confirmed chart of account categories for the given company and data connection.

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListAccountsCategoriesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='distinctio',
)

res = s.categories.list_accounts_categories(req)

if res.categorised_accounts is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountsCategoriesRequest](../../models/operations/listaccountscategoriesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |


### Response

**[operations.ListAccountsCategoriesResponse](../../models/operations/listaccountscategoriesresponse.md)**


## ~~list_available_account_categories~~

Lists available account categories Codat's categorisation engine can provide. 

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import codatassess


s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)


res = s.categories.list_available_account_categories()

if res.categories is not None:
    # handle response
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.ListAvailableAccountCategoriesResponse](../../models/operations/listavailableaccountcategoriesresponse.md)**


## ~~update_account_category~~

Update category for a specific nominal account

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateAccountCategoryRequest(
    confirm_category=shared.ConfirmCategory(
        confirmed=shared.AccountCategory(
            detail_type='quibusdam',
            subtype='unde',
            type='nulla',
        ),
    ),
    account_id='corrupti',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.categories.update_account_category(req)

if res.categorised_account is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAccountCategoryRequest](../../models/operations/updateaccountcategoryrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |


### Response

**[operations.UpdateAccountCategoryResponse](../../models/operations/updateaccountcategoryresponse.md)**


## ~~update_accounts_categories~~

Comfirms the categories for all or a batch of accounts for a specific connection.

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateAccountsCategoriesRequest(
    confirm_categories=shared.ConfirmCategories(
        categories=[
            shared.ConfirmCategoriesCategories(
                account_ref=shared.ConfirmCategoriesCategoriesAccountRef(
                    id='9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
                ),
                confirmed=shared.AccountCategory(
                    detail_type='error',
                    subtype='deserunt',
                    type='suscipit',
                ),
            ),
            shared.ConfirmCategoriesCategories(
                account_ref=shared.ConfirmCategoriesCategoriesAccountRef(
                    id='9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
                ),
                confirmed=shared.AccountCategory(
                    detail_type='magnam',
                    subtype='debitis',
                    type='ipsa',
                ),
            ),
            shared.ConfirmCategoriesCategories(
                account_ref=shared.ConfirmCategoriesCategoriesAccountRef(
                    id='EILBDVJVNUAGVKRQ',
                ),
                confirmed=shared.AccountCategory(
                    detail_type='tempora',
                    subtype='suscipit',
                    type='molestiae',
                ),
            ),
            shared.ConfirmCategoriesCategories(
                account_ref=shared.ConfirmCategoriesCategoriesAccountRef(
                    id='EILBDVJVNUAGVKRQ',
                ),
                confirmed=shared.AccountCategory(
                    detail_type='placeat',
                    subtype='voluptatum',
                    type='iusto',
                ),
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.categories.update_accounts_categories(req)

if res.categorised_accounts is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAccountsCategoriesRequest](../../models/operations/updateaccountscategoriesrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |


### Response

**[operations.UpdateAccountsCategoriesResponse](../../models/operations/updateaccountscategoriesresponse.md)**

