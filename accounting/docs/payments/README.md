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
            id='306f5576-f5cd-4eb0-a86d-0bc43b18ab37',
            name='Darrin Crooks',
        ),
        currency='EUR',
        currency_rate=9819.74,
        customer_ref=shared.CustomerRef(
            company_name='laudantium',
            id='1ddf7e08-8f74-4ef5-8c92-16e8926313bb',
        ),
        date_='2022-10-23T00:00:00.000Z',
        id='fc2c8d27-0109-46b6-aad6-e3e1d9d3b660',
        lines=[
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=3089.27,
                links=[
                    shared.PaymentLineLink(
                        amount=1192.28,
                        currency_rate=1231.37,
                        id='aa1d5d22-47de-49b3-9461-70e768a96bb3',
                        type=shared.PaymentLinkType.PAYMENT,
                    ),
                    shared.PaymentLineLink(
                        amount=5218.9,
                        currency_rate=4416.03,
                        id='88398eba-1bbf-4714-b356-f6349a164249',
                        type=shared.PaymentLinkType.PAYMENT_ON_ACCOUNT,
                    ),
                    shared.PaymentLineLink(
                        amount=1747.15,
                        currency_rate=1088.29,
                        id='1ce46b95-1652-4b15-8ca9-142f052632b3',
                        type=shared.PaymentLinkType.UNKNOWN,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='harum',
        payment_method_ref=shared.PaymentMethodRef(
            id='d692ffc8-7450-405e-9d3d-934e036f5c38',
            name='Brett Hudson',
        ),
        reference='ea',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "corporis": {
                    "ipsum": 'perferendis',
                    "est": 'fugit',
                },
                "repudiandae": {
                    "similique": 'repudiandae',
                },
                "assumenda": {
                    "fuga": 'est',
                    "tenetur": 'atque',
                },
            },
        ),
        total_amount=4072.09,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=199180,
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
    payment_id='impedit',
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
    query='eos',
)

res = s.payments.list(req)

if res.payments is not None:
    # handle response
```
