# BankAccounts

## Overview

Create a bank account for a given company's connection.

### Available Operations

* [create](#create) - Create bank account

## create

The *Create bank account* endpoint creates a new [bank account](https://docs.codat.io/sync-for-payables-api#/schemas/BankAccount) for a given company's connection.

[Bank accounts](https://docs.codat.io/sync-for-payables-api#/schemas/BankAccount) are financial accounts maintained by a bank or other financial institution.

### Example Usage: Bank account example

<!-- UsageSnippet language="python" operationID="create-bank-account" method="post" path="/companies/{companyId}/connections/{connectionId}/payables/bankAccounts" example="Bank account example" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bank_accounts.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bank_account_prototype": {
            "nominal_code": "22",
            "name": "Plutus - Payables - Bank Account 12",
            "account_type": shared.BankAccountType.DEBIT,
            "account_number": "0120 0440",
            "sort_code": "50-50-50",
            "currency": "GBP",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="create-bank-account" method="post" path="/companies/{companyId}/connections/{connectionId}/payables/bankAccounts" example="Malformed query" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bank_accounts.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bank_account_prototype": {
            "name": "<value>",
            "account_type": shared.BankAccountType.DEBIT,
            "account_number": "<value>",
            "currency": "GBP",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateBankAccountRequest](../../models/operations/createbankaccountrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[shared.BankAccount](../../models/shared/bankaccount.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |