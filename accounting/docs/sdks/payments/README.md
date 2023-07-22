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
            id='211ce46b-9516-452b-958c-a9142f052632',
            name='Earl Bergnaum',
        ),
        currency='EUR',
        currency_rate=4054.28,
        customer_ref=shared.CustomerRef(
            company_name='unde',
            id='2ffc8745-005e-49d3-9934-e036f5c38866',
        ),
        date_='2022-10-23T00:00:00.000Z',
        id='f6985530-a2e2-4aed-aaaf-863c28d040c6',
        lines=[
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=2296.56,
                links=[
                    shared.PaymentLineLink(
                        amount=6128.01,
                        currency_rate=326.23,
                        id='6f6ebd5a-d7ec-4739-8f25-f634b3730714',
                        type=shared.PaymentLinkType.DISCOUNT,
                    ),
                    shared.PaymentLineLink(
                        amount=4161.71,
                        currency_rate=7445.43,
                        id='e8c3e09c-64d3-442a-8299-a6e5e7aef134',
                        type=shared.PaymentLinkType.UNKNOWN,
                    ),
                    shared.PaymentLineLink(
                        amount=1852.99,
                        currency_rate=9217.07,
                        id='945f5374-3efd-4e11-9822-1f9b1f7d9aff',
                        type=shared.PaymentLinkType.DISCOUNT,
                    ),
                    shared.PaymentLineLink(
                        amount=4322.15,
                        currency_rate=6074.58,
                        id='682aceef-b04f-48c5-92ca-abea708ed579',
                        type=shared.PaymentLinkType.REFUND,
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=2443.59,
                links=[
                    shared.PaymentLineLink(
                        amount=3304.22,
                        currency_rate=8493.01,
                        id='460599d5-c334-4957-ad55-209e9a2253b6',
                        type=shared.PaymentLinkType.MANUAL_JOURNAL,
                    ),
                    shared.PaymentLineLink(
                        amount=4763.88,
                        currency_rate=3916.82,
                        id='5886eeae-5fd4-4b39-b8a1-490678f13c68',
                        type=shared.PaymentLinkType.CREDIT_NOTE,
                    ),
                    shared.PaymentLineLink(
                        amount=8309.31,
                        currency_rate=5517.59,
                        id='39fc9e17-5ffa-4906-ae55-9b72eb674603',
                        type=shared.PaymentLinkType.UNKNOWN,
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=8814.78,
                links=[
                    shared.PaymentLineLink(
                        amount=5605.61,
                        currency_rate=2034.92,
                        id='76c2bede-e767-490e-90c1-6a7ba4784044',
                        type=shared.PaymentLinkType.REFUND,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='repellat',
        payment_method_ref=shared.PaymentMethodRef(
            id='6770ef04-8091-4a2b-a25e-e6c75af8a60a',
            name='Janie Vandervort',
        ),
        reference='vel',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "iste": {
                    "cupiditate": 'debitis',
                    "nemo": 'officia',
                },
            },
        ),
        total_amount=9569.24,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=893129,
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
    payment_id='eum',
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
    query='consequatur',
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

