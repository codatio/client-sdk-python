# AccountingCreditNotes
(*accounting_credit_notes*)

## Overview

Credit notes

### Available Operations

* [create_accounting_credit_note](#create_accounting_credit_note) - Create credit note

## create_accounting_credit_note

The *Create credit note* endpoint creates a new [credit note](https://docs.codat.io/accounting-api#/schemas/CreditNote) for a given company's connection.

[Credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) are issued to a customer to indicate debt, typically with reference to a previously issued invoice and/or purchase.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating an account.


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

req = operations.CreateAccountingCreditNoteRequest(
    accounting_credit_note=shared.AccountingCreditNote(
        additional_tax_amount=Decimal('6733.79'),
        additional_tax_percentage=Decimal('612.72'),
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='lavender Planner',
        currency='USD',
        currency_rate=Decimal('2314.32'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='Swaniawski - Okuneva',
            id='<ID>',
        ),
        discount_percentage=Decimal('1210.61'),
        id='<ID>',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='<ID>',
                    name='candela Metal policy',
                ),
                description='Universal 4th generation model',
                discount_amount=Decimal('6593.55'),
                discount_percentage=Decimal('3629.12'),
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='<ID>',
                    name='Titusville Car',
                ),
                quantity=Decimal('9339.43'),
                sub_total=Decimal('9776.2'),
                tax_amount=Decimal('4570.33'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('2840.32'),
                    id='<ID>',
                    name='Nissan Shirt',
                ),
                total_amount=Decimal('3862.17'),
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRefsitems(
                            id='<ID>',
                            name='system',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='Labadie and Sons',
                        id='<ID>',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.CreditNoteLineItemTrackingProjectReference(
                        id='<ID>',
                        name='Mann second siemens',
                    ),
                    record_ref=shared.RecordRef(
                        data_type='transfer',
                        id='<ID>',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRefsitems(
                        id='<ID>',
                        name='scalable',
                    ),
                ],
                unit_amount=Decimal('9063.02'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='Conroy fuzzy Mobility',
        payment_allocations=[
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=Decimal('5905.56'),
                    total_amount=Decimal('8276.36'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='<ID>',
                        name='synthesizing becquerel Operations',
                    ),
                    currency='GBP',
                    currency_rate=Decimal('8697.42'),
                    id='<ID>',
                    note='Convertible',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='Grenada networks Fantastic',
                    total_amount=Decimal('5575.36'),
                ),
            ),
        ],
        remaining_credit=Decimal('4029.48'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.DRAFT,
        sub_total=Decimal('8342.79'),
        supplemental_data=shared.SupplementalData(
            content={
                "quos": {
                    "nihil": 'Concrete',
                },
            },
        ),
        total_amount=Decimal('1868.28'),
        total_discount=Decimal('4123.14'),
        total_tax_amount=Decimal('8369.46'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('879.63'),
                name='male Bedfordshire architectures',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=814888,
)

res = s.accounting_credit_notes.create_accounting_credit_note(req)

if res.accounting_create_credit_note_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreateAccountingCreditNoteRequest](../../models/operations/createaccountingcreditnoterequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |


### Response

**[operations.CreateAccountingCreditNoteResponse](../../models/operations/createaccountingcreditnoteresponse.md)**

