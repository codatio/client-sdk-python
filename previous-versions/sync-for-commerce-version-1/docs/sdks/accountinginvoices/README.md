# AccountingInvoices

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
        additional_tax_amount=Decimal('2282.63'),
        additional_tax_percentage=Decimal('1059.06'),
        amount_due=Decimal('4895.09'),
        currency='EUR',
        currency_rate=Decimal('8915.23'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='consectetur',
            id='5b60eb1e-a426-4555-ba3c-28744ed53b88',
        ),
        discount_percentage=Decimal('9425.84'),
        due_date='2022-10-23T00:00:00.000Z',
        id='a8d8f5c0-b2f2-4fb7-b194-a276b26916fe',
        invoice_number='illo',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='08f4294e-3698-4f44-bf60-3e8b445e80ca',
                    name='Lorraine Walsh',
                ),
                description='magni',
                discount_amount=Decimal('486.9'),
                discount_percentage=Decimal('9014.83'),
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='457e1858-b6a8-49fb-a3a5-aa8e4824d0ab',
                    name='Barbara Koelpin IV',
                ),
                quantity=Decimal('5580.65'),
                sub_total=Decimal('9221.12'),
                tax_amount=Decimal('3611.51'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('894.94'),
                    id='862065e9-04f3-4b11-94b8-abf603a79f9d',
                    name='Noah Armstrong',
                ),
                total_amount=Decimal('4406.66'),
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRefsitems(
                            id='da8a50ce-187f-486b-8173-d689eee9526f',
                            name='Wilfred Mueller',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='repudiandae',
                        id='881ead4f-0e10-4125-a3f9-4e29e973e922',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.TrackingProjectReference(
                        id='7a15be3e-0608-407e-ab6e-3ab8845f0597',
                        name='Shane Abshire',
                    ),
                    record_ref=shared.RecordRef(
                        data_type='journalEntry',
                        id='a54a31e9-4764-4a3e-865e-7956f9251a5a',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRefsitems(
                        id='9da660ff-57bf-4aad-8f9e-fc1b4512c103',
                        name='Agnes Gibson',
                    ),
                ],
                unit_amount=Decimal('7730.84'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='sapiente',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.AccountingInvoicePaymentAllocation(
                allocation=shared.AccountingInvoicePaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=Decimal('1070.04'),
                    total_amount=Decimal('5834.04'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='9ebfd0e9-fe6c-4632-8a3a-ed0117996312',
                        name='Mrs. Orville Treutel',
                    ),
                    currency='USD',
                    currency_rate=Decimal('1158.34'),
                    id='778ff61d-0174-4763-a0a1-5db6a660659a',
                    note='ab',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='possimus',
                    total_amount=Decimal('9139.92'),
                ),
            ),
        ],
        sales_order_refs=[
            shared.AccountingInvoiceSalesOrderReference(
                data_type=shared.DataType.INVOICES,
                id='aab5851d-6c64-45b0-8b61-891baa0fe1ad',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.UNKNOWN,
        sub_total=Decimal('12.07'),
        supplemental_data=shared.SupplementalData(
            content={
                "deleniti": {
                    "earum": 'ex',
                },
            },
        ),
        total_amount=Decimal('9583.08'),
        total_discount=Decimal('5241.84'),
        total_tax_amount=Decimal('7963.2'),
        withholding_tax=[
            shared.AccountingInvoiceWithholdingTax(
                amount=Decimal('3651'),
                name='Dr. Chris Hermiston',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=770675,
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

