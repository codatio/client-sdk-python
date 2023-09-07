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

The *Create bank account* endpoint creates a new [bank account](https://docs.codat.io/accounting-api#/schemas/BankAccount) for a given company's connection.

[Bank accounts](https://docs.codat.io/accounting-api#/schemas/BankAccount) are financial accounts maintained by a bank or other financial institution.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bank account model](https://docs.codat.io/accounting-api#/operations/get-create-update-bankAccounts-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating an account.

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
        account_name='deleniti',
        account_number='hic',
        account_type=shared.BankAccountBankAccountType.DEBIT,
        available_balance=5218.48,
        balance=1059.07,
        currency='USD',
        i_ban='molestiae',
        id='42cb7392-0592-4939-afea-7596eb10faaa',
        institution='dolores',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        nominal_code='corporis',
        overdraft_limit=1289.26,
        sort_code='nobis',
        source_modified_date='2022-10-23T00:00:00.000Z',
    ),
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=607831,
)

res = s.bank_accounts.create(req)

if res.create_bank_account_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateBankAccountRequest](../../models/operations/createbankaccountrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |


### Response

**[operations.CreateBankAccountResponse](../../models/operations/createbankaccountresponse.md)**


## get

The *Get bank account* endpoint returns a single account for a given accountId.

[Bank accounts](https://docs.codat.io/accounting-api#/schemas/BankAccount) are financial accounts maintained by a bank or other financial institution.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support getting a specific bank account.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetBankAccountRequest(
    account_id='nemo',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_accounts.get(req)

if res.bank_account is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetBankAccountRequest](../../models/operations/getbankaccountrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.GetBankAccountResponse](../../models/operations/getbankaccountresponse.md)**


## get_create_update_model

The *Get create/update bank account model* endpoint returns the expected data for the request payload when creating and updating a [bank account](https://docs.codat.io/accounting-api#/schemas/BankAccount) for a given company and integration.

[Bank accounts](https://docs.codat.io/accounting-api#/schemas/BankAccount) are financial accounts maintained by a bank or other financial institution.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating and updating a bank account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

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

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetCreateUpdateBankAccountsModelRequest](../../models/operations/getcreateupdatebankaccountsmodelrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |


### Response

**[operations.GetCreateUpdateBankAccountsModelResponse](../../models/operations/getcreateupdatebankaccountsmodelresponse.md)**


## list

The *List bank accounts* endpoint returns a list of [bank accounts](https://docs.codat.io/accounting-api#/schemas/BankAccount) for a given company's connection.

[Bank accounts](https://docs.codat.io/accounting-api#/schemas/BankAccount) are financial accounts maintained by a bank or other financial institution.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

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
    query='minima',
)

res = s.bank_accounts.list(req)

if res.bank_accounts is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListBankAccountsRequest](../../models/operations/listbankaccountsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.ListBankAccountsResponse](../../models/operations/listbankaccountsresponse.md)**


## update

The *Update bank account* endpoint updates an existing [bank account](https://docs.codat.io/accounting-api#/schemas/BankAccount) for a given company's connection.

[Bank accounts](https://docs.codat.io/accounting-api#/schemas/BankAccount) are financial accounts maintained by a bank or other financial institution.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bank account model](https://docs.codat.io/accounting-api#/operations/get-create-update-bankAccounts-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating an account.


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
        account_name='excepturi',
        account_number='accusantium',
        account_type=shared.BankAccountBankAccountType.CREDIT,
        available_balance=6342.74,
        balance=9883.74,
        currency='EUR',
        i_ban='architecto',
        id='a3a2fa94-6773-4925-9aa5-2c3f5ad019da',
        institution='quasi',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        nominal_code='voluptatibus',
        overdraft_limit=8781.94,
        sort_code='nihil',
        source_modified_date='2022-10-23T00:00:00.000Z',
    ),
    bank_account_id='voluptatibus',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=55714,
)

res = s.bank_accounts.update(req)

if res.update_bank_account_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateBankAccountRequest](../../models/operations/updatebankaccountrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |


### Response

**[operations.UpdateBankAccountResponse](../../models/operations/updatebankaccountresponse.md)**

