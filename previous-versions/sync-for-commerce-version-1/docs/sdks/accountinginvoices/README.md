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
        additional_tax_amount=Decimal('9907.57'),
        additional_tax_percentage=Decimal('9015.63'),
        amount_due=Decimal('195.45'),
        currency='EUR',
        currency_rate=Decimal('1021.57'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='Runte Inc',
            id='<ID>',
        ),
        discount_percentage=Decimal('7432.38'),
        due_date='2022-10-23T00:00:00.000Z',
        id='<ID>',
        invoice_number='Manors',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='<ID>',
                    name='as',
                ),
                description='Visionary discrete task-force',
                discount_amount=Decimal('1010.92'),
                discount_percentage=Decimal('6455.29'),
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='<ID>',
                    name='Shoes Tennessee',
                ),
                quantity=Decimal('8154.23'),
                sub_total=Decimal('7362.43'),
                tax_amount=Decimal('6235.41'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('9166.8'),
                    id='<ID>',
                    name='yellow Chair',
                ),
                total_amount=Decimal('1049.23'),
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRefsitems(
                            id='<ID>',
                            name='rural Bulgarian Producer',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='Grimes, Yost and Champlin',
                        id='<ID>',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.TrackingProjectReference(
                        id='<ID>',
                        name='Organized UDP',
                    ),
                    record_ref=shared.RecordRef(
                        data_type='journalEntry',
                        id='<ID>',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRefsitems(
                        id='<ID>',
                        name='Garden',
                    ),
                ],
                unit_amount=Decimal('5528.53'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='Home Applications Fermium',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.AccountingInvoicePaymentAllocation(
                allocation=shared.AccountingInvoicePaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=Decimal('4747.86'),
                    total_amount=Decimal('8682.37'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='<ID>',
                        name='West Avon Herzegovina',
                    ),
                    currency='GBP',
                    currency_rate=Decimal('7606.26'),
                    id='<ID>',
                    note='Berkshire',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='Palm scam',
                    total_amount=Decimal('2223.49'),
                ),
            ),
        ],
        sales_order_refs=[
            shared.AccountingInvoiceSalesOrderReference(
                data_type=shared.DataType.INVOICES,
                id='<ID>',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.UNKNOWN,
        sub_total=Decimal('7559.48'),
        supplemental_data=shared.SupplementalData(
            content={
                "explicabo": {
                    "fugiat": 'definition',
                },
            },
        ),
        total_amount=Decimal('2429.55'),
        total_discount=Decimal('6497.09'),
        total_tax_amount=Decimal('337.26'),
        withholding_tax=[
            shared.AccountingInvoiceWithholdingTax(
                amount=Decimal('676.3'),
                name='whether Division so',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=658558,
)

res = s.accounting_invoices.create_accounting_invoice(req)

if res.accounting_create_invoice_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingInvoiceRequest](../../models/operations/createaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.CreateAccountingInvoiceResponse](../../models/operations/createaccountinginvoiceresponse.md)**

