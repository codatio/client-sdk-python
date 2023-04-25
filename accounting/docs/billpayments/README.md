# bill_payments

## Overview

Bill payments

### Available Operations

* [create_bill_payment](#create_bill_payment) - Create bill payments
* [delete_bill_payment](#delete_bill_payment) - Delete bill payment
* [get_bill_payments](#get_bill_payments) - Get bill payment
* [get_create_bill_payments_model](#get_create_bill_payments_model) - Get create bill payment model
* [list_bill_payments](#list_bill_payments) - List bill payments

## create_bill_payment

Posts a new bill payment to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create bill payment model](https://docs.codat.io/accounting-api#/operations/get-create-billPayments-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating bill payments.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateBillPaymentRequest(
    bill_payment=shared.BillPayment(
        account_ref=shared.AccountRef(
            id="b7008787-5614-43f5-a6c9-8b55554080d4",
            name="Celia Rolfson",
        ),
        currency="impedit",
        currency_rate=3947.24,
        date_="cumque",
        id="bd6b5f3e-c909-4304-b926-bad2553819b4",
        lines=[
            shared.BillPaymentLine(
                allocated_on_date="eius",
                amount=7137.18,
                links=[
                    shared.BillPaymentLineLink(
                        amount=9154.08,
                        currency_rate=8227.11,
                        id="20e56248-fff6-439a-910a-bdcab6267669",
                        type="Other",
                    ),
                ],
            ),
            shared.BillPaymentLine(
                allocated_on_date="accusamus",
                amount=682.92,
                links=[
                    shared.BillPaymentLineLink(
                        amount=7903.05,
                        currency_rate=535.29,
                        id="0221b335-d89a-4cb3-acfd-a8d0c549ef03",
                        type="Unknown",
                    ),
                    shared.BillPaymentLineLink(
                        amount=437.15,
                        currency_rate=2737.32,
                        id="978a61fa-1cf2-4068-8f77-c1ffc71dca16",
                        type="Bill",
                    ),
                    shared.BillPaymentLineLink(
                        amount=9824.09,
                        currency_rate=1530.97,
                        id="a3c80a97-ff33-44cd-9f85-7a9e61876c6a",
                        type="PaymentOnAccount",
                    ),
                    shared.BillPaymentLineLink(
                        amount=1265.12,
                        currency_rate=928.51,
                        id="d29dfc94-d6fe-4cd7-9939-0066a6d2d000",
                        type="Bill",
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="ullam",
        note="quis",
        payment_method_ref=shared.PaymentMethodRef(
            id="338cec08-6fa2-41e9-952c-b3119167b8e3",
            name="Julian Stanton I",
        ),
        reference="quaerat",
        source_modified_date="consequatur",
        supplemental_data=shared.SupplementalData(
            content={
                "repellendus": {
                    "quibusdam": "consectetur",
                    "voluptas": "quaerat",
                },
                "earum": {
                    "assumenda": "dolore",
                    "enim": "ullam",
                    "perspiciatis": "alias",
                    "ex": "quibusdam",
                },
                "dicta": {
                    "commodi": "neque",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="d48e935c-2c9e-481f-b0be-3e43202d7216",
            supplier_name="ad",
        ),
        total_amount=4531.98,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=426594,
)

res = s.bill_payments.create_bill_payment(req)

if res.create_bill_payment_response is not None:
    # handle response
```

## delete_bill_payment

Deletes a bill payment from the accounting package for a given company.

> **Supported Integrations**
> 
> This functionality is currently only supported for our Oracle NetSuite integration. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteBillPaymentRequest(
    bill_payment_id="minima",
    company_id="sit",
    connection_id="vel",
)

res = s.bill_payments.delete_bill_payment(req)

if res.push_operation_summary is not None:
    # handle response
```

## get_bill_payments

Get a bill payment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetBillPaymentsRequest(
    bill_payment_id="laboriosam",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.bill_payments.get_bill_payments(req)

if res.bill_payment is not None:
    # handle response
```

## get_create_bill_payments_model

Get create bill payment model.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating and deleting bill payments.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateBillPaymentsModelRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.bill_payments.get_create_bill_payments_model(req)

if res.push_option is not None:
    # handle response
```

## list_bill_payments

Gets the latest billPayments for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBillPaymentsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="quaerat",
)

res = s.bill_payments.list_bill_payments(req)

if res.bill_payments is not None:
    # handle response
```
