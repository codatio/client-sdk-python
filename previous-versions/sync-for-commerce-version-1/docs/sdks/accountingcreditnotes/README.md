# accounting_credit_notes

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
        additional_tax_amount=Decimal('3834.41'),
        additional_tax_percentage=Decimal('4776.65'),
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='placeat',
        currency='USD',
        currency_rate=Decimal('4799.77'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='excepturi',
            id='6ed151a0-5dfc-42dd-b7cc-78ca1ba928fc',
        ),
        discount_percentage=Decimal('5218.48'),
        id='16742cb7-3920-4592-9396-fea7596eb10f',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='aa2352c5-9559-407a-bf1a-3a2fa9467739',
                    name='Beatrice Brown',
                ),
                description='enim',
                discount_amount=Decimal('1381.83'),
                discount_percentage=Decimal('7783.46'),
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='3f5ad019-da1f-4fe7-8f09-7b0074f15471',
                    name='Bill Thompson',
                ),
                quantity=Decimal('641.47'),
                sub_total=Decimal('2168.22'),
                tax_amount=Decimal('6924.72'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('5651.89'),
                    id='9d488e1e-91e4-450a-92ab-d44269802d50',
                    name='Sonya Marks',
                ),
                total_amount=Decimal('7351.94'),
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRefsitems(
                            id='4f63c969-e9a3-4efa-b7df-b14cd66ae395',
                            name='Toby Pouros',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='id',
                        id='88f3a669-9707-44ba-8469-b6e214195989',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.CreditNoteLineItemTrackingProjectReference(
                        id='fa563e25-16fe-44c8-b711-e5b7fd2ed028',
                        name='Victor Casper',
                    ),
                    record_ref=shared.RecordRef(
                        data_type='transfer',
                        id='c692601f-b576-4b0d-9f0d-30c5fbb25870',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRefsitems(
                        id='53202c73-d5fe-49b9-8c28-909b3fe49a8d',
                        name='Loren Renner',
                    ),
                ],
                unit_amount=Decimal('5542.42'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='dolorem',
        payment_allocations=[
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=Decimal('1861.93'),
                    total_amount=Decimal('2187.49'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='f9b77f3a-4100-4674-abf6-9280d1ba77a8',
                        name='Terence Rau',
                    ),
                    currency='GBP',
                    currency_rate=Decimal('4560.15'),
                    id='ae4203ce-5e6a-495d-8a0d-446ce2af7a73',
                    note='quisquam',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='amet',
                    total_amount=Decimal('7308.56'),
                ),
            ),
        ],
        remaining_credit=Decimal('8802.98'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.DRAFT,
        sub_total=Decimal('2133.12'),
        supplemental_data=shared.SupplementalData(
            content={
                "sapiente": {
                    "totam": 'nihil',
                },
            },
        ),
        total_amount=Decimal('256.62'),
        total_discount=Decimal('7115.84'),
        total_tax_amount=Decimal('2074.7'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('1536.94'),
                name='Kelli Hintz',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=214880,
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

