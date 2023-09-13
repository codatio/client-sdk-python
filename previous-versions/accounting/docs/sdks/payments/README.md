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
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreatePaymentRequest(
    payment=shared.Payment(
        account_ref=shared.AccountRef(
            id='e71f6c48-252d-4777-9e7f-d074009ef8d2',
            name='Dr. Levi Volkman',
        ),
        currency='USD',
        currency_rate=Decimal('161.58'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='provident',
            id='7b5da08c-57fa-46c7-8a21-6e19bafeca61',
        ),
        date_='2022-10-23T00:00:00.000Z',
        id='1498140b-64ff-48ae-970e-f03b5f37e4aa',
        lines=[
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=Decimal('3819.74'),
                links=[
                    shared.PaymentLineLink(
                        amount=Decimal('5576.51'),
                        currency_rate=Decimal('3385.42'),
                        id='55966732-aa5d-4cb6-a82c-b70f8cfd5fb6',
                        type=shared.PaymentLinkType.DISCOUNT,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='dicta',
        payment_method_ref='quidem',
        reference='omnis',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "molestias": {
                    "a": 'dignissimos',
                },
            },
        ),
        total_amount=Decimal('2883.48'),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=511054,
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
    payment_id='dolore',
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
    query='aliquid',
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

