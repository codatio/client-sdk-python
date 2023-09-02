# bill_payments

## Overview

Bill payments

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

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBillPaymentRequest(
    bill_payment=shared.BillPayment(
        account_ref=shared.AccountRef(
            id='23b75d23-67fe-41a0-8c8d-f79f0a396d90',
            name='Jimmy Jerde',
        ),
        currency='USD',
        currency_rate=7898.7,
        date_='2022-10-23T00:00:00.000Z',
        id='3d5a8e00-d108-4045-8823-7f342676cffa',
        lines=[
            shared.BillPaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=9792.71,
                links=[
                    shared.BillPaymentLineLink(
                        amount=6496.57,
                        currency_rate=7709.97,
                        id='e188b1c4-ee2c-48c6-8e61-1feeb1c7cbdb',
                        type=shared.BillPaymentLineLinkType.OTHER,
                    ),
                    shared.BillPaymentLineLink(
                        amount=9064.95,
                        currency_rate=9347.82,
                        id='c74378ba-2531-4774-bdc9-15ad2caf5dd6',
                        type=shared.BillPaymentLineLinkType.CREDIT_NOTE,
                    ),
                    shared.BillPaymentLineLink(
                        amount=1274.99,
                        currency_rate=2337.08,
                        id='dc0f5ae2-f3a6-4b70-8878-756143f5a6c9',
                        type=shared.BillPaymentLineLinkType.BILL_PAYMENT,
                    ),
                ],
            ),
            shared.BillPaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=3661.47,
                links=[
                    shared.BillPaymentLineLink(
                        amount=3712.13,
                        currency_rate=3289.54,
                        id='4080d40b-cacc-46cb-96b5-f3ec909304f9',
                        type=shared.BillPaymentLineLinkType.UNLINKED,
                    ),
                    shared.BillPaymentLineLink(
                        amount=4258.17,
                        currency_rate=7403.47,
                        id='ad255381-9b47-44b0-ad20-e56248fff639',
                        type=shared.BillPaymentLineLinkType.PAYMENT_ON_ACCOUNT,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='Bill Payment against bill c13e37b6-dfaa-4894-b3be-9fe97bda9f44',
        payment_method_ref='beatae',
        reference='ipsa',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "assumenda": {
                    "fuga": 'tempore',
                    "commodi": 'fugit',
                    "suscipit": 'voluptate',
                    "nisi": 'aliquid',
                },
                "provident": {
                    "accusamus": 'ab',
                    "itaque": 'quisquam',
                },
                "eaque": {
                    "qui": 'consequuntur',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='1b335d89-acb3-4ecf-9a8d-0c549ef03004',
            supplier_name='perspiciatis',
        ),
        total_amount=1329.54,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=462097,
)

res = s.bill_payments.create(req)

if res.create_bill_payment_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateBillPaymentRequest](../../models/operations/createbillpaymentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |


### Response

**[operations.CreateBillPaymentResponse](../../models/operations/createbillpaymentresponse.md)**


## delete

﻿The *Delete bill payment* endpoint allows you to delete a specified bill payment from an accounting platform.

[Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

### Process
1. Pass the `{billPaymentId}` to the *Delete bill payment* endpoint and store the `pushOperationKey` returned.
2. Check the status of the delete operation by checking the status of push operation either via
    1. [Push operation webhook](https://docs.codat.io/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),
    2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation).

   A `Success` status indicates that the bill payment object was deleted from the accounting platform.
3. (Optional) Check that the bill payment was deleted from the accounting platform.

### Effect on related objects
Be aware that deleting a bill payment from an accounting platform might cause related objects to be modified.

## Integration specifics
Integrations that support soft delete do not permanently delete the object in the accounting platform.

| Integration | Soft Delete | Details                                                                                             |  
|-------------|-------------|-----------------------------------------------------------------------------------------------------|
| Oracle NetSuite   | No          | See [here](/integrations/accounting/netsuite/how-deleting-bill-payments-works) to learn more. |

> **Supported Integrations**
>
> This functionality is currently only supported for our QuickBooks Online abd Oracle NetSuite integrations. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DeleteBillPaymentRequest(
    bill_payment_id='atque',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bill_payments.delete(req)

if res.push_operation_summary is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteBillPaymentRequest](../../models/operations/deletebillpaymentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |


### Response

**[operations.DeleteBillPaymentResponse](../../models/operations/deletebillpaymentresponse.md)**


## get

The *Get bill payment* endpoint returns a single bill payment for a given billPaymentId.

[Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support getting a specific bill payment.

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

req = operations.GetBillPaymentsRequest(
    bill_payment_id='officia',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.bill_payments.get(req)

if res.bill_payment is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetBillPaymentsRequest](../../models/operations/getbillpaymentsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |


### Response

**[operations.GetBillPaymentsResponse](../../models/operations/getbillpaymentsresponse.md)**


## get_create_model

The *Get create bill payment model* endpoint returns the expected data for the request payload when creating a [bill payment](https://docs.codat.io/accounting-api#/schemas/BillPayment) for a given company and integration.

[Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating a bill payment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateBillPaymentsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bill_payments.get_create_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetCreateBillPaymentsModelRequest](../../models/operations/getcreatebillpaymentsmodelrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |


### Response

**[operations.GetCreateBillPaymentsModelResponse](../../models/operations/getcreatebillpaymentsmodelresponse.md)**


## list

The *List bill payments* endpoint returns a list of [bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) for a given company's connection.

[Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

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

req = operations.ListBillPaymentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='ex',
)

res = s.bill_payments.list(req)

if res.bill_payments is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListBillPaymentsRequest](../../models/operations/listbillpaymentsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.ListBillPaymentsResponse](../../models/operations/listbillpaymentsresponse.md)**

