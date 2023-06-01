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

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) to see which integrations support this endpoint.

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
            id='61e91500-323b-42c0-9b92-4771f5669e5b',
            name='Tricia Sawayn',
        ),
        currency='magni',
        currency_rate=4374.89,
        customer_ref=shared.CustomerRef(
            company_name='ea',
            id='49d84eb9-e4cf-4d22-b6e0-b88fb87d6fa5',
        ),
        date_='cum',
        id='6e8dbf81-2f83-4b1c-a6a9-ffc561929cca',
        lines=[
            shared.PaymentLine(
                allocated_on_date='nemo',
                amount=3864.41,
                links=[
                    shared.PaymentLineLink(
                        amount=6814.58,
                        currency_rate=977.35,
                        id='395918da-1d48-4e78-a3cf-8e1143da9308',
                        type=shared.PaymentLinkType.PAYMENT_ON_ACCOUNT,
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date='magni',
                amount=4682.52,
                links=[
                    shared.PaymentLineLink(
                        amount=137,
                        currency_rate=5312.36,
                        id='af221844-39b3-4de8-b56c-cce470cd2147',
                        type=shared.PaymentLinkType.PAYMENT,
                    ),
                    shared.PaymentLineLink(
                        amount=4308.75,
                        currency_rate=9267.48,
                        id='6152cf01-d0d8-4c3a-8b9a-5bf935dfe974',
                        type=shared.PaymentLinkType.DISCOUNT,
                    ),
                    shared.PaymentLineLink(
                        amount=6309.83,
                        currency_rate=2828,
                        id='b1e9c097-eda6-4234-82e1-a9237e9984c8',
                        type=shared.PaymentLinkType.UNKNOWN,
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date='facilis',
                amount=2810.64,
                links=[
                    shared.PaymentLineLink(
                        amount=5745.91,
                        currency_rate=9051.54,
                        id='891923c1-8ca8-4d69-8568-9214fa20207e',
                        type=shared.PaymentLinkType.INVOICE,
                    ),
                    shared.PaymentLineLink(
                        amount=9643.29,
                        currency_rate=6295.82,
                        id='e038cd7f-1bc2-4cab-af7f-c2ccba4bef0d',
                        type=shared.PaymentLinkType.DISCOUNT,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='nisi',
        note='voluptatum',
        payment_method_ref=shared.PaymentMethodRef(
            id='eaedb2ee-70be-4069-bb36-add704080e0a',
            name='Lorene Schneider',
        ),
        reference='animi',
        source_modified_date='ullam',
        supplemental_data=shared.SupplementalData(
            content={
                "aperiam": {
                    "aliquam": 'soluta',
                },
                "inventore": {
                    "ut": 'sint',
                },
                "sint": {
                    "eius": 'ratione',
                },
            },
        ),
        total_amount=6253.92,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=979832,
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetPaymentRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    payment_id='mollitia',
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

## list

Gets the latest payments for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

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
    query='suscipit',
)

res = s.payments.list(req)

if res.payments is not None:
    # handle response
```
