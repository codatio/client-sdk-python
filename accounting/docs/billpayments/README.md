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
            id="57eb809e-2810-4331-b398-1d4c700b607f",
            name="Francis McKenzie",
        ),
        currency="dignissimos",
        currency_rate=2358.34,
        date_="soluta",
        id="3d5a8e00-d108-4045-8823-7f342676cffa",
        lines=[
            shared.BillPaymentLine(
                allocated_on_date="temporibus",
                amount=6396.22,
                links=[
                    shared.BillPaymentLineLink(
                        amount=9485.41,
                        currency_rate=1339.49,
                        id="ceda7e23-f225-4741-9faf-4b7544e472e8",
                        type="Unknown",
                    ),
                ],
            ),
            shared.BillPaymentLine(
                allocated_on_date="odit",
                amount=5358.02,
                links=[
                    shared.BillPaymentLineLink(
                        amount=4527.3,
                        currency_rate=6267.07,
                        id="5b40463a-7d57-45f1-800e-764ad7334ec1",
                        type="Refund",
                    ),
                    shared.BillPaymentLineLink(
                        amount=4813.75,
                        currency_rate=5580.51,
                        id="1b36a080-88d1-400e-bada-200ef0422eb2",
                        type="Unlinked",
                    ),
                ],
            ),
            shared.BillPaymentLine(
                allocated_on_date="aliquid",
                amount=2646.49,
                links=[
                    shared.BillPaymentLineLink(
                        amount=9750.95,
                        currency_rate=5629.48,
                        id="ab8366c7-23ff-4da9-a06b-ee4825c1fc0e",
                        type="Unlinked",
                    ),
                    shared.BillPaymentLineLink(
                        amount=1002.51,
                        currency_rate=3178.98,
                        id="c80bff91-8544-4ec4-adef-cce8f1977773",
                        type="ManualJournal",
                    ),
                    shared.BillPaymentLineLink(
                        amount=4235.88,
                        currency_rate=2086.83,
                        id="562a7b40-8f05-4e3d-88fd-af313a1f5fd9",
                        type="Bill",
                    ),
                    shared.BillPaymentLineLink(
                        amount=1280.21,
                        currency_rate=3684.91,
                        id="9c0b36f2-5ea9-444f-bb75-6c11f6c37a51",
                        type="Unlinked",
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="aliquid",
        note="Bill Payment against bill c13e37b6-dfaa-4894-b3be-9fe97bda9f44",
        payment_method_ref=shared.PaymentMethodRef(
            id="243835bb-c05a-423a-85ce-fc5fde10a0ce",
            name="Mildred Kautzer",
        ),
        reference="ullam",
        source_modified_date="architecto",
        supplemental_data=shared.SupplementalData(
            content={
                "perferendis": {
                    "provident": "cumque",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="6dc5e347-6279-49bf-bbe6-949fb2bb4eca",
            supplier_name="saepe",
        ),
        total_amount=1329.54,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=423054,
)

res = s.bill_payments.create(req)

if res.create_bill_payment_response is not None:
    # handle response
```

## delete

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
    bill_payment_id="quo",
    company_id="nesciunt",
    connection_id="illum",
)

res = s.bill_payments.delete(req)

if res.push_operation_summary is not None:
    # handle response
```

## get

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
    bill_payment_id="nemo",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.bill_payments.get(req)

if res.bill_payment is not None:
    # handle response
```

## get_create_model

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

res = s.bill_payments.get_create_model(req)

if res.push_option is not None:
    # handle response
```

## list

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
    query="illum",
)

res = s.bill_payments.list(req)

if res.bill_payments is not None:
    # handle response
```
