# Accounts

## Overview

Create accounts and view create account options.

### Available Operations

* [create](#create) - Create account
* [get_create_model](#get_create_model) - Get create account model

## create

The *Create account* endpoint creates a new [account](https://docs.codat.io/sync-for-expenses-api#/schemas/Account) for a given company's connection.

[Accounts](https://docs.codat.io/sync-for-expenses-api#/schemas/Account) are the categories a business uses to record accounting transactions.

**Integration-specific behavior**

Required data may vary by integration. To see what data to post, first call [Get create account model](https://docs.codat.io/sync-for-expenses-api#/operations/get-create-chartOfAccounts-model).

### Example Usage

<!-- UsageSnippet language="python" operationID="create-account" method="post" path="/companies/{companyId}/connections/{connectionId}/push/accounts" example="Malformed query" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared
from decimal import Decimal


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.accounts.create(request={
        "account_prototype": {
            "currency": "GBP",
            "current_balance": Decimal("0"),
            "description": "Invoices the business has issued but has not yet collected payment on.",
            "fully_qualified_category": "Asset.Current",
            "fully_qualified_name": "Cash On Hand",
            "name": "Accounts Receivable",
            "nominal_code": "610",
            "status": shared.AccountStatus.ACTIVE,
            "type": shared.AccountType.ASSET,
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateAccountRequest](../../models/operations/createaccountrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[shared.CreateAccountResponse](../../models/shared/createaccountresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_create_model

The *Get create account model* endpoint returns the expected data for the request payload when creating an [account](https://docs.codat.io/sync-for-expenses-api#/schemas/Account) for a given company and integration.

[Accounts](https://docs.codat.io/sync-for-expenses-api#/schemas/Account) are the categories a business uses to record accounting transactions.

**Integration-specific behavior**

See the *response examples* for integration-specific indicative models.

### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="get-create-chartOfAccounts-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts" example="Exact (Netherlands)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.accounts.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="get-create-chartOfAccounts-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts" example="Exact (UK)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.accounts.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: MYOB AccountRight and Essentials

<!-- UsageSnippet language="python" operationID="get-create-chartOfAccounts-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts" example="MYOB AccountRight and Essentials" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.accounts.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="get-create-chartOfAccounts-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts" example="QuickBooks Desktop" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.accounts.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="get-create-chartOfAccounts-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts" example="QuickBooks Online" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.accounts.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="get-create-chartOfAccounts-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts" example="QuickBooks Online Sandbox" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.accounts.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="get-create-chartOfAccounts-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts" example="Sage Business Cloud Accounting" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.accounts.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="get-create-chartOfAccounts-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts" example="Sage Intacct" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.accounts.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Sandbox

<!-- UsageSnippet language="python" operationID="get-create-chartOfAccounts-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts" example="Sandbox" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.accounts.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="get-create-chartOfAccounts-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts" example="Xero" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.accounts.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetCreateChartOfAccountsModelRequest](../../models/operations/getcreatechartofaccountsmodelrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[shared.PushOption](../../models/shared/pushoption.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |