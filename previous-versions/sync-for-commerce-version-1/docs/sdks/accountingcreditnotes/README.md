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
        additional_tax_amount=Decimal('3927.85'),
        additional_tax_percentage=Decimal('9255.97'),
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='ab',
        currency='USD',
        currency_rate=Decimal('871.29'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='deserunt',
            id='05dfc2dd-f7cc-478c-a1ba-928fc816742c',
        ),
        discount_percentage=Decimal('7369.18'),
        id='73920592-9396-4fea-b596-eb10faaa2352',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='5955907a-ff1a-43a2-ba94-67739251aa52',
                    name='Jimmy Wiegand',
                ),
                description='possimus',
                discount_amount=Decimal('135.71'),
                discount_percentage=Decimal('971.01'),
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='9da1ffe7-8f09-47b0-874f-15471b5e6e13',
                    name='Virgil Mante',
                ),
                quantity=Decimal('5089.69'),
                sub_total=Decimal('5232.48'),
                tax_amount=Decimal('9167.23'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('939.4'),
                    id='e91e450a-d2ab-4d44-a698-02d502a94bb4',
                    name='Andre Franey',
                ),
                total_amount=Decimal('3960.98'),
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRefsitems(
                            id='9e9a3efa-77df-4b14-8d66-ae395efb9ba8',
                            name='Timmy Feeney',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='vel',
                        id='997074ba-4469-4b6e-a141-959890afa563',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.CreditNoteLineItemTrackingProjectReference(
                        id='516fe4c8-b711-4e5b-bfd2-ed028921cddc',
                        name='Miriam Connelly Jr.',
                    ),
                    record_ref=shared.RecordRef(
                        data_type='transfer',
                        id='b576b0d5-f0d3-40c5-bbb2-587053202c73',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRefsitems(
                        id='d5fe9b90-c289-409b-bfe4-9a8d9cbf4863',
                        name='Rosa Dibbert',
                    ),
                ],
                unit_amount=Decimal('5695.74'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='voluptate',
        payment_allocations=[
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=Decimal('2274.14'),
                    total_amount=Decimal('6805.45'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='4100674e-bf69-4280-91ba-77a89ebf737a',
                        name='Mrs. Ray Collins',
                    ),
                    currency='EUR',
                    currency_rate=Decimal('3200.17'),
                    id='e6a95d8a-0d44-46ce-aaf7-a73cf3be453f',
                    note='totam',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='sit',
                    total_amount=Decimal('7115.84'),
                ),
            ),
        ],
        remaining_credit=Decimal('2074.7'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.SUBMITTED,
        sub_total=Decimal('7304.42'),
        supplemental_data=shared.SupplementalData(
            content={
                "voluptas": {
                    "deserunt": 'quam',
                },
            },
        ),
        total_amount=Decimal('2148.8'),
        total_discount=Decimal('2776.28'),
        total_tax_amount=Decimal('1864.58'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('5867.84'),
                name='Miss Jody Rogahn',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=276894,
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

