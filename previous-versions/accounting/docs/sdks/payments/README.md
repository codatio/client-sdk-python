# payments

## Overview

Payments

### Available Operations

* [create](#create) - Create payment
* [get](#get) - Get payment
* [get_create_model](#get_create_model) - Get create payment model
* [list](#list) - List payments

## create

The *Create payment* endpoint creates a new [payment](https://docs.codat.io/accounting-api#/schemas/Payment) for a given company's connection.

[Payments](https://docs.codat.io/accounting-api#/schemas/Payment) represent an allocation of money within any customer accounts receivable account.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create payment model](https://docs.codat.io/accounting-api#/operations/get-create-payments-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreatePaymentRequest(
    payment=shared.Payment(
        account_ref=shared.AccountRef(
            id='871a88ed-72a2-4d4a-b415-8ac2d0f0f58c',
            name='Pam Leannon',
        ),
        currency='GBP',
        currency_rate=4766.68,
        customer_ref=shared.AccountingCustomerRef(
            company_name='eaque',
            id='40d0d98e-9d82-4c5e-b06f-5576f5cdeb02',
        ),
        date_='2022-10-23T00:00:00.000Z',
        id='6d0bc43b-18ab-4378-b2fc-ff81ddf7e088',
        lines=[
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=2892.95,
                links=[
                    shared.PaymentLineLink(
                        amount=9630.72,
                        currency_rate=3403.92,
                        id='4c9216e8-9263-413b-b6fc-2c8d2701096b',
                        type=shared.PaymentLinkType.OTHER,
                    ),
                    shared.PaymentLineLink(
                        amount=4190.01,
                        currency_rate=6641.93,
                        id='d6e3e1d9-d3b6-4603-b4a1-1aa1d5d2247d',
                        type=shared.PaymentLinkType.MANUAL_JOURNAL,
                    ),
                    shared.PaymentLineLink(
                        amount=5974.19,
                        currency_rate=7299.26,
                        id='3d46170e-768a-496b-b398-788398eba1bb',
                        type=shared.PaymentLinkType.DISCOUNT,
                    ),
                    shared.PaymentLineLink(
                        amount=4939.36,
                        currency_rate=676.61,
                        id='43356f63-49a1-4642-89b2-11ce46b95165',
                        type=shared.PaymentLinkType.UNLINKED,
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=1068.42,
                links=[
                    shared.PaymentLineLink(
                        amount=5418.42,
                        currency_rate=7604.45,
                        id='a9142f05-2632-4b31-8ad6-92ffc8745005',
                        type=shared.PaymentLinkType.DISCOUNT,
                    ),
                    shared.PaymentLineLink(
                        amount=6124.56,
                        currency_rate=8634.66,
                        id='3d934e03-6f5c-4388-a64f-6985530a2e2a',
                        type=shared.PaymentLinkType.DISCOUNT,
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=4284.76,
                links=[
                    shared.PaymentLineLink(
                        amount=6672.29,
                        currency_rate=9471.82,
                        id='863c28d0-40c6-49a3-9906-f6ebd5ad7ec7',
                        type=shared.PaymentLinkType.INVOICE,
                    ),
                    shared.PaymentLineLink(
                        amount=5908.32,
                        currency_rate=2922.91,
                        id='f25f634b-3730-4714-a6be-8c3e09c64d34',
                        type=shared.PaymentLinkType.UNLINKED,
                    ),
                    shared.PaymentLineLink(
                        amount=6784.76,
                        currency_rate=8087.97,
                        id='299a6e5e-7aef-4134-82e9-45f53743efde',
                        type=shared.PaymentLinkType.UNKNOWN,
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=5754.71,
                links=[
                    shared.PaymentLineLink(
                        amount=1577.51,
                        currency_rate=1756.68,
                        id='1f9b1f7d-9aff-4e69-a82a-ceefb04f8c51',
                        type=shared.PaymentLinkType.UNLINKED,
                    ),
                    shared.PaymentLineLink(
                        amount=8001.68,
                        currency_rate=6586.25,
                        id='abea708e-d579-48d3-85d4-60599d5c3349',
                        type=shared.PaymentLinkType.CREDIT_NOTE,
                    ),
                    shared.PaymentLineLink(
                        amount=4904.31,
                        currency_rate=4326.34,
                        id='d55209e9-a225-43b6-9765-886eeae5fd4b',
                        type=shared.PaymentLinkType.INVOICE,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='voluptatibus',
        payment_method_ref='totam',
        reference='mollitia',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "provident": {
                    "aliquid": 'in',
                },
                "quos": {
                    "sunt": 'dolor',
                    "quisquam": 'commodi',
                    "laudantium": 'laboriosam',
                    "repellendus": 'quos',
                },
            },
        ),
        total_amount=2068.12,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=608738,
)

res = s.payments.create(req)

if res.create_payment_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreatePaymentRequest](../../models/operations/createpaymentrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.CreatePaymentResponse](../../models/operations/createpaymentresponse.md)**


## get

The *Get payment* endpoint returns a single payment for a given paymentId.

[Payments](https://docs.codat.io/accounting-api#/schemas/Payment) represent an allocation of money within any customer accounts receivable account.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support getting a specific payment.

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

req = operations.GetPaymentRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    payment_id='earum',
)

res = s.payments.get(req)

if res.payment is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetPaymentRequest](../../models/operations/getpaymentrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.GetPaymentResponse](../../models/operations/getpaymentresponse.md)**


## get_create_model

The *Get create payment model* endpoint returns the expected data for the request payload when creating a [payment](https://docs.codat.io/accounting-api#/schemas/Payment) for a given company and integration.

[Payments](https://docs.codat.io/accounting-api#/schemas/Payment) represent an allocation of money within any customer accounts receivable account.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support creating a payment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreatePaymentsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.payments.get_create_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCreatePaymentsModelRequest](../../models/operations/getcreatepaymentsmodelrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |


### Response

**[operations.GetCreatePaymentsModelResponse](../../models/operations/getcreatepaymentsmodelresponse.md)**


## list

The *List payments* endpoint returns a list of [payments](https://docs.codat.io/accounting-api#/schemas/Payment) for a given company's connection.

[Payments](https://docs.codat.io/accounting-api#/schemas/Payment) represent an allocation of money within any customer accounts receivable account.

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

req = operations.ListPaymentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='eligendi',
)

res = s.payments.list(req)

if res.payments is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListPaymentsRequest](../../models/operations/listpaymentsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |


### Response

**[operations.ListPaymentsResponse](../../models/operations/listpaymentsresponse.md)**

