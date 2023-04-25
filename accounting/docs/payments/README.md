# payments

## Overview

Payments

### Available Operations

* [create_payment](#create_payment) - Create payment
* [get_create_payments_model](#get_create_payments_model) - Get create payment model
* [get_payment](#get_payment) - Get payment
* [list_payments](#list_payments) - List payments

## create_payment

Posts a new payment to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create payment model](https://docs.codat.io/accounting-api#/operations/get-create-payments-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support creating payments.

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
            id="cf63b215-186a-4b5e-ba02-2614315d1568",
            name="Violet McClure",
        ),
        currency="architecto",
        currency_rate=6396.52,
        customer_ref=shared.CustomerRef(
            company_name="reiciendis",
            id="c7186ff2-0b7a-473d-b40c-a0d7657c1641",
        ),
        date_="distinctio",
        id="bf055271-b251-41dd-a06d-d1b28272bc9c",
        lines=[
            shared.PaymentLine(
                allocated_on_date="magni",
                amount=1257.69,
                links=[
                    shared.PaymentLineLink(
                        amount=4058.4,
                        currency_rate=5724.81,
                        id="7b1880fc-bb2b-493c-95f6-70bd17848316",
                        type="CreditNote",
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="dolor",
        note="debitis",
        payment_method_ref=shared.PaymentMethodRef(
            id="eb3b6e24-1c31-4099-8366-3c66dcbb7df6",
            name="Gerardo Baumbach",
        ),
        reference="totam",
        source_modified_date="distinctio",
        supplemental_data=shared.SupplementalData(
            content={
                "aperiam": {
                    "recusandae": "eaque",
                    "nihil": "dicta",
                    "adipisci": "molestiae",
                },
                "in": {
                    "repellendus": "saepe",
                    "non": "a",
                },
            },
        ),
        total_amount=9140.93,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=878742,
)

res = s.payments.create_payment(req)

if res.create_payment_response is not None:
    # handle response
```

## get_create_payments_model

Get create payment model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support creating payments.

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.payments.get_create_payments_model(req)

if res.push_option is not None:
    # handle response
```

## get_payment

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    payment_id="quae",
)

res = s.payments.get_payment(req)

if res.payment is not None:
    # handle response
```

## list_payments

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="doloremque",
)

res = s.payments.list_payments(req)

if res.payments is not None:
    # handle response
```
