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

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingInvoiceRequest(
    accounting_invoice=shared.AccountingInvoice(
        additional_tax_amount=7031.89,
        additional_tax_percentage=841.78,
        amount_due=9492.8,
        currency='USD',
        currency_rate=6940.88,
        customer_ref=shared.AccountingCustomerRef(
            company_name='totam',
            id='ca275a60-a04c-4495-8c69-9171b51c1bdb',
        ),
        discount_percentage=1053.72,
        due_date='2022-10-23T00:00:00.000Z',
        id='f4b888eb-dfc4-4ccc-a99b-c7fc0b2dce10',
        invoice_number='laudantium',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='e42b006d-6788-478b-a858-1a58208c54fe',
                    name='Gerard Mraz',
                ),
                description='quaerat',
                discount_amount=9853.79,
                discount_percentage=1560.98,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='eac5565d-307c-4fee-8120-6e2813fa4a41',
                    name='Dr. Herbert Legros',
                ),
                quantity=9998.54,
                sub_total=1323.05,
                tax_amount=802.84,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1932.36,
                    id='2af03102-d514-4f4c-86f1-8bf9621a6a4f',
                    name='Tamara O'Kon',
                ),
                total_amount=9085.39,
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRefsitems(
                            id='3e4be752-c65b-4344-98e3-bb91c8d975e0',
                            name='Miss Dwight Goldner',
                        ),
                        shared.TrackingCategoryRefsitems(
                            id='8f84f144-f3e0-47ed-8c4a-a5f3cabd905a',
                            name='Mitchell Crona II',
                        ),
                        shared.TrackingCategoryRefsitems(
                            id='6728227b-2d30-4947-8bf7-a4fa87cf535a',
                            name='Ora Okuneva',
                        ),
                        shared.TrackingCategoryRefsitems(
                            id='4ebf60c3-21f0-423b-b5d2-367fe1a0cc8d',
                            name='Darren McKenzie V',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='nesciunt',
                        id='96d90c36-4b7c-415d-bbac-e188b1c4ee2c',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.TrackingProjectRef(
                        id='6ce611fe-eb1c-47cb-9b6e-ec74378ba253',
                        name='Heidi Koch',
                    ),
                    record_ref=shared.RecordRef(
                        data_type='transfer',
                        id='c915ad2c-af5d-4d67-a3dc-0f5ae2f3a6b7',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRefsitems(
                        id='08787561-43f5-4a6c-98b5-5554080d40bc',
                        name='Gregg Russel',
                    ),
                ],
                unit_amount=7437.95,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='laboriosam',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.AccountingInvoicePaymentAllocation(
                allocation=shared.AccountingInvoicePaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=8988.26,
                    total_amount=8037.92,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='909304f9-26ba-4d25-9381-9b474b0ed20e',
                        name='Terri Davis',
                    ),
                    currency='EUR',
                    currency_rate=9806.49,
                    id='f639a910-abdc-4ab6-a676-696e1ec00221',
                    note='quidem',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='amet',
                    total_amount=3466.08,
                ),
            ),
            shared.AccountingInvoicePaymentAllocation(
                allocation=shared.AccountingInvoicePaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=6016.26,
                    total_amount=6294.61,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='cb3ecfda-8d0c-4549-af03-004978a61fa1',
                        name='Ms. Darnell Denesik',
                    ),
                    currency='USD',
                    currency_rate=9456.37,
                    id='77c1ffc7-1dca-4163-b2a3-c80a97ff334c',
                    note='illum',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='tenetur',
                    total_amount=5620.66,
                ),
            ),
        ],
        sales_order_refs=[
            shared.AccountingInvoiceSalesOrderReference(
                data_type='esse',
                id='a9e61876-c6ab-421d-a9df-c94d6fecd799',
            ),
            shared.AccountingInvoiceSalesOrderReference(
                data_type='dolor',
                id='90066a6d-2d00-4035-9338-cec086fa21e9',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.SUBMITTED,
        sub_total=1631.81,
        supplemental_data=shared.SupplementalData(
            content={
                "quidem": {
                    "beatae": 'sunt',
                },
                "molestias": {
                    "autem": 'ducimus',
                },
                "libero": {
                    "necessitatibus": 'ipsum',
                    "impedit": 'quos',
                    "illum": 'distinctio',
                },
                "voluptatem": {
                    "quaerat": 'consequatur',
                },
            },
        ),
        total_amount=5154.33,
        total_discount=8310.67,
        total_tax_amount=4159.53,
        withholding_tax=[
            shared.AccountingInvoiceWithholdingTax(
                amount=2312.55,
                name='Michele Wehner',
            ),
            shared.AccountingInvoiceWithholdingTax(
                amount=2941.81,
                name='Ms. Samantha Metz',
            ),
            shared.AccountingInvoiceWithholdingTax(
                amount=1168.67,
                name='Gertrude Doyle',
            ),
            shared.AccountingInvoiceWithholdingTax(
                amount=5231.09,
                name='Alejandro DuBuque',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=175803,
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

