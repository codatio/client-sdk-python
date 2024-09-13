# BillPayments
(*bill_payments*)

## Overview

Access standardized Bill payments from linked accounting software.

### Available Operations

* [create](#create) - Create bill payments
* [delete](#delete) - Delete bill payment
* [get](#get) - Get bill payment
* [get_create_model](#get_create_model) - Get create bill payment model
* [list](#list) - List bill payments

## create

The *Create bill payment* endpoint creates a new [bill payment](https://docs.codat.io/accounting-api#/schemas/BillPayment) for a given company's connection.

[Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create bill payment model](https://docs.codat.io/accounting-api#/operations/get-create-billPayments-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating a bill payment.


### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared
from decimal import Decimal

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.bill_payments.create(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "bill_payment": {
        "date_": "2023-01-05T12:33:25.339Z",
        "account_ref": {
            "id": "1200",
            "name": "string",
        },
        "currency": "GBP",
        "currency_rate": Decimal("1"),
        "id": "3d5a8e00-d108-4045-8823-7f342676cffa",
        "lines": [
            {
                "amount": Decimal("15.38"),
                "allocated_on_date": "2023-01-05T12:33:25.339Z",
                "links": [
                    {
                        "type": shared.BillPaymentLineLinkType.BILL,
                        "amount": Decimal("-15.38"),
                        "currency_rate": Decimal("1"),
                        "id": "3",
                    },
                ],
            },
        ],
        "metadata": {
            "is_deleted": True,
        },
        "modified_date": "2023-01-05T12:33:25.339Z",
        "note": "note - billpayment on 20230220 of 15.38",
        "payment_method_ref": {
            "id": "string",
            "name": "string",
        },
        "reference": "reference 20230220 15.38",
        "source_modified_date": "2023-01-05T12:33:25.339Z",
        "supplier_ref": {
            "id": "SUPP1",
            "supplier_name": "string",
        },
        "total_amount": Decimal("15.38"),
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateBillPaymentRequest](../../models/operations/createbillpaymentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[shared.CreateBillPaymentResponse](../../models/shared/createbillpaymentresponse.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |


## delete

The *Delete bill payment* endpoint allows you to delete a specified bill payment from an accounting software.

[Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

### Process
1. Pass the `{billPaymentId}` to the *Delete bill payment* endpoint and store the `pushOperationKey` returned.
2. Check the status of the delete operation by checking the status of the push operation either via
   1. [Push operation webhook](https://docs.codat.io/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),
   2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation).

   A `Success` status indicates that the bill payment object was deleted from the accounting software.
3. (Optional) Check that the bill payment was deleted from the accounting software.

### Effect on related objects
Be aware that deleting a bill payment from an accounting software might cause related objects to be modified.

## Integration specifics
Integrations that support soft delete do not permanently delete the object in the accounting software.

| Integration | Soft Delete | Details |
|-------------|-------------|---------|
| QuickBooks Online  | No  | -
| QuickBooks Desktop | No  | -
| Oracle NetSuite    | No  | See [here](/integrations/accounting/netsuite/accounting-netsuite-how-deleting-bill-payments-works) to learn more.
| Xero               | Yes | -     
| Sage Intacct       | No  | Some bill payments in Sage Intacct can only be deleted, whilst others can only be voided. Codat have applied logic to handle this complexity. 

> **Supported integrations**
>
> This functionality is currently supported for our QuickBooks Online, QuickBooks Desktop, Oracle NetSuite, Xero and Sage Intacct integrations.

### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.bill_payments.delete(request={
    "bill_payment_id": "<value>",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteBillPaymentRequest](../../models/operations/deletebillpaymentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[shared.PushOperationSummary](../../models/shared/pushoperationsummary.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## get

The *Get bill payment* endpoint returns a single bill payment for a given billPaymentId.

[Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support getting a specific bill payment.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.bill_payments.get(request={
    "bill_payment_id": "<value>",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetBillPaymentsRequest](../../models/operations/getbillpaymentsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[shared.BillPayment](../../models/shared/billpayment.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |


## get_create_model

The *Get create bill payment model* endpoint returns the expected data for the request payload when creating a [bill payment](https://docs.codat.io/accounting-api#/schemas/BillPayment) for a given company and integration.

[Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating a bill payment.


### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.bill_payments.get_create_model(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetCreateBillPaymentsModelRequest](../../models/operations/getcreatebillpaymentsmodelrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[shared.PushOption](../../models/shared/pushoption.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## list

The *List bill payments* endpoint returns a list of [bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) for a given company's connection.

[Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.bill_payments.list(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "order_by": "-modifiedDate",
    "page": 1,
    "page_size": 100,
    "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListBillPaymentsRequest](../../models/operations/listbillpaymentsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[shared.BillPayments](../../models/shared/billpayments.md)**

### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.ErrorMessage                 | 400,401,402,403,404,409,429,500,503 | application/json                    |
| errors.SDKError                     | 4xx-5xx                             | */*                                 |
