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
            id='cbf18685-6a7e-482c-9f9d-0fc282c666af',
            name='Jacquelyn Dicki',
        ),
        currency='USD',
        currency_rate=5194.41,
        customer_ref=shared.CustomerRef(
            company_name='provident',
            id='bea5d264-e41e-42ca-8482-2e513f6d9d2a',
        ),
        date_='2022-10-23T00:00:00.000Z',
        id='37c30990-77c1-40b6-8792-163e67d48860',
        lines=[
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=2316.11,
                links=[
                    shared.PaymentLineLink(
                        amount=470,
                        currency_rate=6419.14,
                        id='3049c3cf-6c02-476e-bb21-bad90d2743fd',
                        type=shared.PaymentLinkType.OTHER,
                    ),
                    shared.PaymentLineLink(
                        amount=7649.53,
                        currency_rate=1702.52,
                        id='a10e6c29-78ec-4256-a5b0-9227fcc47996',
                        type=shared.PaymentLinkType.PAYMENT_ON_ACCOUNT,
                    ),
                    shared.PaymentLineLink(
                        amount=5744.03,
                        currency_rate=4585.85,
                        id='7bbc57f3-8928-4a86-80c5-8d67d63e4aa5',
                        type=shared.PaymentLinkType.CREDIT_NOTE,
                    ),
                    shared.PaymentLineLink(
                        amount=5547.96,
                        currency_rate=3030.69,
                        id='64579cfc-6c0e-4503-b568-31f1d8ed87b2',
                        type=shared.PaymentLinkType.REFUND,
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=5394.5,
                links=[
                    shared.PaymentLineLink(
                        amount=9515.01,
                        currency_rate=6325.21,
                        id='bc986e24-1e43-4b23-8241-7d13e3f62aa9',
                        type=shared.PaymentLinkType.PAYMENT,
                    ),
                    shared.PaymentLineLink(
                        amount=9236.58,
                        currency_rate=2889.02,
                        id='ae8ab4a9-c492-4c5e-8ba5-d4aa4a508bd3',
                        type=shared.PaymentLinkType.REFUND,
                    ),
                    shared.PaymentLineLink(
                        amount=544.9,
                        currency_rate=7608.41,
                        id='29aa8dd7-1bdd-4aa3-8b7b-91449ae69c08',
                        type=shared.PaymentLinkType.REFUND,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='labore',
        payment_method_ref=shared.PaymentMethodRef(
            id='18bb7180-4f42-43d5-8393-5f377ac5c9b7',
            name='Joey Frami',
        ),
        reference='id',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "minima": {
                    "amet": 'quasi',
                },
                "doloremque": {
                    "recusandae": 'iusto',
                    "impedit": 'dolor',
                },
                "quaerat": {
                    "deserunt": 'distinctio',
                    "alias": 'voluptates',
                    "optio": 'libero',
                    "voluptatum": 'beatae',
                },
                "explicabo": {
                    "laboriosam": 'ea',
                    "beatae": 'eius',
                    "atque": 'unde',
                },
            },
        ),
        total_amount=2811.64,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=302190,
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
    payment_id='fuga',
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
    query='voluptatum',
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

