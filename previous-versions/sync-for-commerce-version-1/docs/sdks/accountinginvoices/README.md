# accounting_invoices

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
        additional_tax_amount=Decimal('7386.83'),
        additional_tax_percentage=Decimal('2326.27'),
        amount_due=Decimal('4490.83'),
        currency='USD',
        currency_rate=Decimal('9372.85'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='facere',
            id='4f6fbee4-1f33-4317-be35-b60eb1ea4265',
        ),
        discount_percentage=Decimal('3742.96'),
        due_date='2022-10-23T00:00:00.000Z',
        id='ba3c2874-4ed5-43b8-8f3a-8d8f5c0b2f2f',
        invoice_number='facilis',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='b194a276-b269-416f-a1f0-8f4294e3698f',
                    name='Rhonda Klocko',
                ),
                description='sit',
                discount_amount=Decimal('2484.13'),
                discount_percentage=Decimal('8880.44'),
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='8b445e80-ca55-4efd-a0e4-57e1858b6a89',
                    name='Rudolph Trantow',
                ),
                quantity=Decimal('3416.98'),
                sub_total=Decimal('6390.28'),
                tax_amount=Decimal('6762.43'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('5483.61'),
                    id='e4824d0a-b407-4508-8e51-862065e904f3',
                    name='Gerald Bradtke',
                ),
                total_amount=Decimal('6952.7'),
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRefsitems(
                            id='8abf603a-79f9-4dfe-8ab7-da8a50ce187f',
                            name='Sam Powlowski IV',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='amet',
                        id='d689eee9-526f-48d9-86e8-81ead4f0e101',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.TrackingProjectReference(
                        id='63f94e29-e973-4e92-aa57-a15be3e06080',
                        name='Tricia Denesik',
                    ),
                    record_ref=shared.RecordRef(
                        data_type='transfer',
                        id='3ab8845f-0597-4a60-bf2a-54a31e94764a',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRefsitems(
                        id='3e865e79-56f9-4251-a5a9-da660ff57bfa',
                        name='Irving Gleichner',
                    ),
                ],
                unit_amount=Decimal('8897.94'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='cumque',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.AccountingInvoicePaymentAllocation(
                allocation=shared.AccountingInvoicePaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=Decimal('3354.98'),
                    total_amount=Decimal('820.57'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='2c103264-8dc2-4f61-9199-ebfd0e9fe6c6',
                        name='Denise Runolfsdottir',
                    ),
                    currency='USD',
                    currency_rate=Decimal('8987.6'),
                    id='d0117996-312f-4de0-8771-778ff61d0174',
                    note='esse',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='consectetur',
                    total_amount=Decimal('3998.12'),
                ),
            ),
        ],
        sales_order_refs=[
            shared.AccountingInvoiceSalesOrderReference(
                data_type='ipsa',
                id='a15db6a6-6065-49a1-adea-ab5851d6c645',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.UNKNOWN,
        sub_total=Decimal('5615.77'),
        supplemental_data=shared.SupplementalData(
            content={
                "cum": {
                    "aliquid": 'beatae',
                },
            },
        ),
        total_amount=Decimal('5308.6'),
        total_discount=Decimal('6063.08'),
        total_tax_amount=Decimal('852.33'),
        withholding_tax=[
            shared.AccountingInvoiceWithholdingTax(
                amount=Decimal('7032.18'),
                name='Trevor Bartell',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=103298,
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

