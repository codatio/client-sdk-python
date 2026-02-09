# BillPayments

## Overview

Get, create, and update Bill payments.

### Available Operations

* [get_payment_options](#get_payment_options) - Get payment mapping options
* [create](#create) - Create bill payment

## get_payment_options

Use the *Get mapping options - Payments* endpoint to return a list of available mapping options for a given company's connection ID.

By default, this endpoint returns a list of active bank accounts. You can use [querying](https://docs.codat.io/using-the-api/querying) to change that.

Mapping options are a set of bank accounts used to configure the SMB's payables integration.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-mapping-options-payments" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/mappingOptions/payments" example="Mapping options" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bill_payments.get_payment_options(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
        "status_query": "status=Archived",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetMappingOptionsPaymentsRequest](../../models/operations/getmappingoptionspaymentsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[shared.PaymentMappingOptions](../../models/shared/paymentmappingoptions.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create

The *Create bill payment* endpoint creates a new [bill payment](https://docs.codat.io/sync-for-payables-api#/schemas/BillPayment) for a given company's connection.

[Bill payments](https://docs.codat.io/sync-for-payables-api#/schemas/BillPayment) are an allocation of money within any Accounts Payable account.

### Example Usage: Bill payment

<!-- UsageSnippet language="python" operationID="create-bill-payment" method="post" path="/companies/{companyId}/connections/{connectionId}/payables/bills/{billId}/payment" example="Bill payment" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared
from decimal import Decimal


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bill_payments.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bill_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "bill_payment_prototype": {
            "amount": Decimal("1329.54"),
            "date_": "2022-10-23T00:00:00Z",
            "reference": "Bill Payment against bill c13e37b6-dfaa-4894-b3be-9fe97bda9f44",
            "account_ref": {
                "id": "<id>",
            },
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Bill payment example

<!-- UsageSnippet language="python" operationID="create-bill-payment" method="post" path="/companies/{companyId}/connections/{connectionId}/payables/bills/{billId}/payment" example="Bill payment example" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared
from decimal import Decimal


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bill_payments.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bill_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "bill_payment_prototype": {
            "amount": Decimal("22"),
            "date_": "2022-10-23T00:00:00.000Z",
            "reference": "Bill Payment against bill c13e37b6 dfaa-4894-b3be-9fe97bda9f44",
            "account_ref": {
                "id": "7bda9f44sr56",
            },
            "currency_rate": Decimal("1"),
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="create-bill-payment" method="post" path="/companies/{companyId}/connections/{connectionId}/payables/bills/{billId}/payment" example="Malformed query" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared
from decimal import Decimal


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bill_payments.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bill_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "bill_payment_prototype": {
            "amount": Decimal("1329.54"),
            "date_": "2022-10-23T00:00:00Z",
            "reference": "Bill Payment against bill c13e37b6-dfaa-4894-b3be-9fe97bda9f44",
            "account_ref": {
                "id": "<id>",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateBillPaymentRequest](../../models/operations/createbillpaymentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[shared.BillPayment](../../models/shared/billpayment.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 409, 429 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |