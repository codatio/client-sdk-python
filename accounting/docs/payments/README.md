# payments

## Overview

Payments

### Available Operations

* [create](#create) - Create payment
* [get](#get) - Get payment
* [get_create_model](#get_create_model) - Get create payment model
* [list](#list) - List payments

## create

Posts a new payment to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create payment model](https://docs.codat.io/accounting-api#/operations/get-create-payments-model).

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support creating payments.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreatePaymentRequest(
    payment=shared.Payment(
        account_ref=shared.AccountRef(
            id='def9c765-dfd7-4354-a5cb-94977017a262',
            name='Monica Reinger',
        ),
        currency='eum',
        currency_rate=7979.17,
        customer_ref=shared.CustomerRef(
            company_name='laborum',
            id='4e999828-79de-4fc0-b239-606cf90ad989',
        ),
        date_='recusandae',
        id='1a34715a-cda0-444f-aaed-6e13a620e2e9',
        lines=[
            shared.PaymentLine(
                allocated_on_date='totam',
                amount=7539.55,
                links=[
                    shared.PaymentLineLink(
                        amount=3390.23,
                        currency_rate=7169.63,
                        id='0486cf39-8a0b-4374-a17d-d95ce3044be4',
                        type=shared.PaymentLinkType.DISCOUNT,
                    ),
                    shared.PaymentLineLink(
                        amount=7139.18,
                        currency_rate=2076.75,
                        id='b31cb503-c314-40d8-b72c-535e1dd6bf64',
                        type=shared.PaymentLinkType.PAYMENT_ON_ACCOUNT,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='non',
        note='quis',
        payment_method_ref=shared.PaymentMethodRef(
            id='4e9831e7-95f0-4e57-b54e-bf2d2b46097e',
            name='Carlton Grady',
        ),
        reference='voluptatum',
        source_modified_date='quibusdam',
        supplemental_data=shared.SupplementalData(
            content={
                "earum": {
                    "sit": 'cumque',
                    "quibusdam": 'quibusdam',
                },
                "inventore": {
                    "enim": 'perferendis',
                    "soluta": 'tenetur',
                    "ipsam": 'dolorum',
                },
                "ipsa": {
                    "soluta": 'impedit',
                    "quas": 'facilis',
                    "quam": 'blanditiis',
                    "commodi": 'eaque',
                },
                "similique": {
                    "voluptates": 'similique',
                    "autem": 'nobis',
                    "laboriosam": 'non',
                    "corporis": 'ab',
                },
            },
        ),
        total_amount=1991.9,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=179221,
)

res = s.payments.create(req)

if res.create_payment_response is not None:
    # handle response
```

## get

Get payment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetPaymentRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    payment_id='repellendus',
)

res = s.payments.get(req)

if res.payment is not None:
    # handle response
```

## get_create_model

Get create payment model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support creating payments.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
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

## list

Gets the latest payments for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListPaymentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='ipsam',
)

res = s.payments.list(req)

if res.payments is not None:
    # handle response
```
