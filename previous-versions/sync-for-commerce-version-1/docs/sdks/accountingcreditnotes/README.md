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

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingCreditNoteRequest(
    accounting_credit_note=shared.AccountingCreditNote(
        additional_tax_amount=8700.13,
        additional_tax_percentage=8700.88,
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='molestiae',
        currency='EUR',
        currency_rate=8009.11,
        customer_ref=shared.AccountingCustomerRef(
            company_name='esse',
            id='8ca1ba92-8fc8-4167-82cb-739205929396',
        ),
        discount_percentage=9437.49,
        id='ea7596eb-10fa-4aa2-b52c-5955907aff1a',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='2fa94677-3925-41aa-92c3-f5ad019da1ff',
                    name='Jessie Langosh V',
                ),
                description='voluptate',
                discount_amount=7392.64,
                discount_percentage=199.87,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='074f1547-1b5e-46e1-bb99-d488e1e91e45',
                    name='Monique Spinka',
                ),
                quantity=7163.27,
                sub_total=8413.86,
                tax_amount=2894.06,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2647.3,
                    id='269802d5-02a9-44bb-8f63-c969e9a3efa7',
                    name='Angel Wolff II',
                ),
                total_amount=7670.24,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRefsitems(
                            id='66ae395e-fb9b-4a88-b3a6-6997074ba446',
                            name='Robin Keebler',
                        ),
                        shared.TrackingCategoryRefsitems(
                            id='14195989-0afa-4563-a251-6fe4c8b711e5',
                            name='Jessie Zulauf',
                        ),
                        shared.TrackingCategoryRefsitems(
                            id='ed028921-cddc-4692-a01f-b576b0d5f0d3',
                            name='Erma Hessel',
                        ),
                        shared.TrackingCategoryRefsitems(
                            id='b2587053-202c-473d-9fe9-b90c28909b3f',
                            name='Edwin Morar',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='pariatur',
                        id='9cbf4863-3323-4f9b-b7f3-a4100674ebf6',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.CreditNoteLineItemTrackingProjectReference(
                        id='80d1ba77-a89e-4bf7-b7ae-4203ce5e6a95',
                        name='Dr. Jimmie Murphy',
                    ),
                    record_ref=shared.RecordRef(
                        data_type='invoice',
                        id='6ce2af7a-73cf-43be-853f-870b326b5a73',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRefsitems(
                        id='29cdb1a8-422b-4b67-9d23-22715bf0cbb1',
                        name='Dale Boehm',
                    ),
                    shared.TrackingCategoryRefsitems(
                        id='b90f3443-a110-48e0-adcf-4b921879fce9',
                        name='Tiffany Willms',
                    ),
                ],
                unit_amount=8788.7,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='f7fbc7ab-d74d-4d39-80f5-d2cff7c70a45',
                    name='Judy Keebler',
                ),
                description='ratione',
                discount_amount=4011.32,
                discount_percentage=5113.19,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='13f16d9f-5fce-46c5-9614-6c3e250fb008',
                    name='Jim Corkery I',
                ),
                quantity=896.03,
                sub_total=6774.12,
                tax_amount=6720.48,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8104.24,
                    id='366c8dd6-b144-4290-b474-778a7bd466d2',
                    name='Miss Devin Bogan',
                ),
                total_amount=2065.94,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRefsitems(
                            id='dca42519-04e5-423c-be0b-c7178e4796f2',
                            name='Fernando Barton',
                        ),
                        shared.TrackingCategoryRefsitems(
                            id='88282aa4-8256-42f2-a2e9-817ee17cbe61',
                            name='Cecil Pollich',
                        ),
                        shared.TrackingCategoryRefsitems(
                            id='95bc0ab3-c20c-44f3-b89f-d871f99dd2ef',
                            name='Miss Peter Cronin',
                        ),
                        shared.TrackingCategoryRefsitems(
                            id='6f1e674b-db04-4f15-b560-82d68ea19f1d',
                            name='Allison Bednar I',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='adipisci',
                        id='9d08086a-1840-4394-8260-71f93f5f0642',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.CreditNoteLineItemTrackingProjectReference(
                        id='c7af515c-c413-4aa6-baae-8d67864dbb67',
                        name='Lela Shields',
                    ),
                    record_ref=shared.RecordRef(
                        data_type='invoice',
                        id='0b375ed4-f6fb-4ee4-9f33-317fe35b60eb',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRefsitems(
                        id='ea426555-ba3c-4287-84ed-53b88f3a8d8f',
                        name='Della Bailey',
                    ),
                ],
                unit_amount=9679.66,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='2fb7b194-a276-4b26-916f-e1f08f4294e3',
                    name='Kristina Lueilwitz',
                ),
                description='tempora',
                discount_amount=4554.44,
                discount_percentage=9700.76,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='603e8b44-5e80-4ca5-9efd-20e457e1858b',
                    name='Lee Lehner',
                ),
                quantity=7105.29,
                sub_total=8928.63,
                tax_amount=2049.23,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6771.15,
                    id='5aa8e482-4d0a-4b40-b508-8e51862065e9',
                    name='Eva Wisozk',
                ),
                total_amount=1157.03,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRefsitems(
                            id='94b8abf6-03a7-49f9-9fe0-ab7da8a50ce1',
                            name='Mitchell Zboncak',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='quidem',
                        id='c173d689-eee9-4526-b8d9-86e881ead4f0',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.CreditNoteLineItemTrackingProjectReference(
                        id='012563f9-4e29-4e97-be92-2a57a15be3e0',
                        name='Ms. Melissa Larson',
                    ),
                    record_ref=shared.RecordRef(
                        data_type='journalEntry',
                        id='b6e3ab88-45f0-4597-a60f-f2a54a31e947',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRefsitems(
                        id='4a3e865e-7956-4f92-91a5-a9da660ff57b',
                        name='Oliver Osinski',
                    ),
                    shared.TrackingCategoryRefsitems(
                        id='f9efc1b4-512c-4103-a648-dc2f615199eb',
                        name='Gilberto Bechtelar',
                    ),
                ],
                unit_amount=9834.27,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='aliquid',
        payment_allocations=[
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=1478.08,
                    total_amount=7649.95,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='a3aed011-7996-4312-bde0-4771778ff61d',
                        name='Cheryl Kub',
                    ),
                    currency='USD',
                    currency_rate=2352.63,
                    id='60a15db6-a660-4659-a1ad-eaab5851d6c6',
                    note='ut',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='expedita',
                    total_amount=299.5,
                ),
            ),
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=3996.6,
                    total_amount=1097.84,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='891baa0f-e1ad-4e00-8e6f-8c5f350d8cdb',
                        name='Molly Fadel IV',
                    ),
                    currency='GBP',
                    currency_rate=2745.75,
                    id='30104218-13d5-4208-ace7-e253b668451c',
                    note='autem',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='laboriosam',
                    total_amount=9272.12,
                ),
            ),
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=3502.07,
                    total_amount=8956.92,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='16deab3f-ec95-478a-a458-4273a8418d16',
                        name='Edith Beahan',
                    ),
                    currency='EUR',
                    currency_rate=38.6,
                    id='929921ae-fb9f-458c-8d86-e68e4be05601',
                    note='non',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='enim',
                    total_amount=5752.13,
                ),
            ),
            shared.PaymentAllocationsitems(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=4585.03,
                    total_amount=3644.63,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='7a59ecfe-f66e-4f1c-aa33-83c2beb47737',
                        name='Angelica Leuschke',
                    ),
                    currency='GBP',
                    currency_rate=9749.9,
                    id='64d1db1f-2c43-4106-a1e9-6349e1cf9e06',
                    note='itaque',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='laborum',
                    total_amount=2503.98,
                ),
            ),
        ],
        remaining_credit=2244.67,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.UNKNOWN,
        sub_total=399.92,
        supplemental_data=shared.SupplementalData(
            content={
                "officia": {
                    "ea": 'quidem',
                    "voluptas": 'facilis',
                    "placeat": 'perspiciatis',
                    "expedita": 'deleniti',
                },
            },
        ),
        total_amount=9543.34,
        total_discount=4555.79,
        total_tax_amount=3519.36,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=8975.43,
                name='Rodolfo Hintz',
            ),
            shared.WithholdingTaxitems(
                amount=6216.66,
                name='Lucille Bogan',
            ),
            shared.WithholdingTaxitems(
                amount=1124.27,
                name='Florence Hand',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=403026,
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

