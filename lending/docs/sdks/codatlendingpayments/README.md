# LoanWriteback.Payments

## Overview

### Available Operations

* [create](#create) - Create payment
* [get_create_model](#get_create_model) - Get create payment model

## create

The *Create payment* endpoint creates a new [payment](https://docs.codat.io/lending-api#/schemas/Payment) for a given company's connection.

[Payments](https://docs.codat.io/lending-api#/schemas/Payment) represent an allocation of money within any customer accounts receivable account.

**Integration-specific behavior**

Required data may vary by integration. To see what data to post, first call [Get create payment model](https://docs.codat.io/lending-api#/operations/get-create-payments-model).

### Example Usage

<!-- UsageSnippet language="python" operationID="create-payment" method="post" path="/companies/{companyId}/connections/{connectionId}/push/payments" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared
from decimal import Decimal


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.create(request={
        "accounting_payment": {
            "account_ref": {
                "id": "8000002E-1675267199",
                "name": "Undeposited Funds",
            },
            "currency": "USD",
            "currency_rate": Decimal("1"),
            "customer_ref": {
                "company_name": "string",
                "id": "80000002-1674552702",
            },
            "date_": "2023-02-10T11:47:04.792Z",
            "lines": [
                {
                    "allocated_on_date": "2023-02-11T11:47:04.792Z",
                    "amount": Decimal("28"),
                    "links": [
                        {
                            "amount": Decimal("-28"),
                            "currency_rate": Decimal("1"),
                            "id": "181-1676374586",
                            "type": shared.PaymentLinkType.INVOICE,
                        },
                    ],
                },
            ],
            "note": "note 14/02 1147",
            "payment_method_ref": {
                "id": "string",
                "name": "string",
            },
            "reference": "ref 14/02 1147",
            "total_amount": Decimal("28"),
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
| `request`                                                                          | [operations.CreatePaymentRequest](../../models/operations/createpaymentrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[shared.AccountingCreatePaymentResponse](../../models/shared/accountingcreatepaymentresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_create_model

The *Get create payment model* endpoint returns the expected data for the request payload when creating a [payment](https://docs.codat.io/lending-api#/schemas/Payment) for a given company and integration.

[Payments](https://docs.codat.io/lending-api#/schemas/Payment) represent an allocation of money within any customer accounts receivable account.

**Integration-specific behavior**

See the *response examples* for integration-specific indicative models.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetCreatePaymentModelRequest](../../models/operations/getcreatepaymentmodelrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[shared.PushOption](../../models/shared/pushoption.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |