# AccountingInvoices
(*accounting_invoices*)

## Overview

Invoices

### Available Operations

* [create_accounting_invoice](#create_accounting_invoice) - Create invoice

## create_accounting_invoice

The *Create invoice* endpoint creates a new [invoice](https://docs.codat.io/accounting-api#/schemas/Invoice) for a given company's connection.

[Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support creating an account.


### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared
from decimal import Decimal

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingInvoiceRequest(
    accounting_invoice=shared.AccountingInvoice(
        amount_due=Decimal('9907.57'),
        currency='EUR',
        customer_ref=shared.AccountingCustomerRef(
            id='<ID>',
        ),
        due_date='2022-10-23T00:00:00.000Z',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(),
                item_ref=shared.ItemRef(
                    id='<ID>',
                ),
                quantity=Decimal('1021.57'),
                tax_rate_ref=shared.TaxRateRef(),
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRefItems(
                            id='<ID>',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        id='<ID>',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.AccountingProjectReference(
                        id='<ID>',
                    ),
                    record_ref=shared.RecordRef(
                        data_type='journalEntry',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRefItems(
                        id='<ID>',
                    ),
                ],
                unit_amount=Decimal('7432.38'),
            ),
        ],
        metadata=shared.Metadata(),
        modified_date='2022-10-23T00:00:00.000Z',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.AccountingPaymentAllocation(
                allocation=shared.AccountingInvoiceAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(),
                    currency='EUR',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderReference(
                data_type=shared.DataType.INVOICES,
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.PARTIALLY_PAID,
        supplemental_data=shared.SupplementalData(
            content={
                "key": {
                    "key": 'string',
                },
            },
        ),
        total_amount=Decimal('1416.23'),
        total_tax_amount=Decimal('9069.87'),
        withholding_tax=[
            shared.WithholdingTax(
                amount=Decimal('598.23'),
                name='string',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.accounting_invoices.create_accounting_invoice(req)

if res.accounting_create_invoice_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingInvoiceRequest](../../models/operations/createaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.CreateAccountingInvoiceResponse](../../models/operations/createaccountinginvoiceresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |
