# BillCreditNotes

## Overview

Bill credit notes

### Available Operations

* [create](#create) - Create bill credit note
* [get](#get) - Get bill credit note
* [get_create_update_model](#get_create_update_model) - Get create/update bill credit note model
* [list](#list) - List bill credit notes
* [update](#update) - Update bill credit note

## create

The *Create bill credit note* endpoint creates a new [bill credit note](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) for a given company's connection.

[Bill credit notes](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/sync-for-payables-api#/operations/get-create-update-billCreditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating a bill credit note.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared
from decimal import Decimal

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date='2022-10-23T00:00:00.000Z',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='USD',
        currency_rate=Decimal('3927.85'),
        discount_percentage=Decimal('0'),
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='d151a05d-fc2d-4df7-8c78-ca1ba928fc81',
                    name='Tanya Gleason',
                ),
                description='cum',
                discount_amount=Decimal('4561.5'),
                discount_percentage=Decimal('2165.5'),
                item_ref=shared.BillCreditNoteLineItemItemReference(
                    id='92059293-96fe-4a75-96eb-10faaa2352c5',
                    name='Corey Hane III',
                ),
                quantity=Decimal('6342.74'),
                sub_total=Decimal('9883.74'),
                tax_amount=Decimal('9589.5'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('1020.44'),
                    id='a3a2fa94-6773-4925-9aa5-2c3f5ad019da',
                    name='Johanna Wolf',
                ),
                total_amount=Decimal('5096.24'),
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='f097b007-4f15-4471-b5e6-e13b99d488e1',
                            name='Kirk Boehm',
                        ),
                    ],
                    customer_ref=shared.BillCreditNoteLineItemTrackingCustomerRef(
                        company_name='enim',
                        id='0ad2abd4-4269-4802-9502-a94bb4f63c96',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.BillCreditNoteLineItemTrackingProjectReference(
                        id='9a3efa77-dfb1-44cd-a6ae-395efb9ba88f',
                        name='Sandy Huels',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='97074ba4-469b-46e2-9419-59890afa563e',
                        name='Vivian Boyle',
                    ),
                ],
                unit_amount=Decimal('8919.24'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='Bill Credit Note with 1 line items, totaling 805.78',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=Decimal('7038.89'),
                    total_amount=Decimal('4479.26'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='11e5b7fd-2ed0-4289-a1cd-dc692601fb57',
                        name='Candice Beatty',
                    ),
                    currency='EUR',
                    currency_rate=Decimal('166.27'),
                    id='d30c5fbb-2587-4053-a02c-73d5fe9b90c2',
                    note='blanditiis',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='eaque',
                    total_amount=Decimal('5772.29'),
                ),
            ),
        ],
        remaining_credit=Decimal('0'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=Decimal('805.78'),
        supplemental_data=shared.SupplementalData(
            content={
                "adipisci": {
                    "asperiores": 'earum',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='49a8d9cb-f486-4333-a3f9-b77f3a410067',
            supplier_name='quaerat',
        ),
        total_amount=Decimal('805.78'),
        total_discount=Decimal('0'),
        total_tax_amount=Decimal('0'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('8810.05'),
                name='Jan Hodkiewicz',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=542499,
)

res = s.bill_credit_notes.create(req)

if res.create_bill_credit_note_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateBillCreditNoteRequest](../../models/operations/createbillcreditnoterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.CreateBillCreditNoteResponse](../../models/operations/createbillcreditnoteresponse.md)**


## get

The *Get bill credit note* endpoint returns a single bill credit note for a given `billCreditNoteId`.

[Bill credit notes](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support getting a specific bill credit note.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetBillCreditNoteRequest(
    bill_credit_note_id='sit',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.bill_credit_notes.get(req)

if res.bill_credit_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetBillCreditNoteRequest](../../models/operations/getbillcreditnoterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |


### Response

**[operations.GetBillCreditNoteResponse](../../models/operations/getbillcreditnoteresponse.md)**


## get_create_update_model

The *Get create/update bill credit note model* endpoint returns the expected data for the request payload when creating and updating a [bill credit note](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) for a given company and integration.

[Bill credit notes](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating and updating a bill credit note.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateBillCreditNoteModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bill_credit_notes.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetCreateUpdateBillCreditNoteModelRequest](../../models/operations/getcreateupdatebillcreditnotemodelrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |


### Response

**[operations.GetCreateUpdateBillCreditNoteModelResponse](../../models/operations/getcreateupdatebillcreditnotemodelresponse.md)**


## list

The *List bill credit notes* endpoint returns a list of [bill credit notes](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) for a given company's connection.

[Bill credit notes](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBillCreditNotesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='fugiat',
)

res = s.bill_credit_notes.list(req)

if res.bill_credit_notes is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListBillCreditNotesRequest](../../models/operations/listbillcreditnotesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |


### Response

**[operations.ListBillCreditNotesResponse](../../models/operations/listbillcreditnotesresponse.md)**


## update

The *Update bill credit note* endpoint updates an existing [bill credit note](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) for a given company's connection.

[Bill credit notes](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/sync-for-payables-api#/operations/get-create-update-billCreditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating a bill credit note.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared
from decimal import Decimal

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date='2022-10-23T00:00:00.000Z',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='EUR',
        currency_rate=Decimal('6793.93'),
        discount_percentage=Decimal('0'),
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='7a89ebf7-37ae-4420-bce5-e6a95d8a0d44',
                    name='Bernadette Torp',
                ),
                description='a',
                discount_amount=Decimal('4561.3'),
                discount_percentage=Decimal('6874.88'),
                item_ref=shared.BillCreditNoteLineItemItemReference(
                    id='73cf3be4-53f8-470b-b26b-5a73429cdb1a',
                    name='Randall Cole',
                ),
                quantity=Decimal('7044.74'),
                sub_total=Decimal('3960.6'),
                tax_amount=Decimal('4631.5'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('5654.21'),
                    id='d2322715-bf0c-4bb1-a31b-8b90f3443a11',
                    name='Miss Billie Ward',
                ),
                total_amount=Decimal('7851.53'),
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='f4b92187-9fce-4953-b73e-f7fbc7abd74d',
                            name='Earl Mosciski DVM',
                        ),
                    ],
                    customer_ref=shared.BillCreditNoteLineItemTrackingCustomerRef(
                        company_name='exercitationem',
                        id='d2cff7c7-0a45-4626-9436-813f16d9f5fc',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.BillCreditNoteLineItemTrackingProjectReference(
                        id='c556146c-3e25-40fb-808c-42e141aac366',
                        name='Clifton Simonis',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='b1442907-4747-478a-bbd4-66d28c10ab3c',
                        name='Salvatore Parker',
                    ),
                ],
                unit_amount=Decimal('3738.13'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='Bill Credit Note with 1 line items, totaling 805.78',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=Decimal('2728.22'),
                    total_amount=Decimal('8920.5'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='523c7e0b-c717-48e4-b96f-2a70c688282a',
                        name='Randall Lindgren',
                    ),
                    currency='USD',
                    currency_rate=Decimal('1470.14'),
                    id='f222e981-7ee1-47cb-a61e-6b7b95bc0ab3',
                    note='cumque',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='consequatur',
                    total_amount=Decimal('7963.92'),
                ),
            ),
        ],
        remaining_credit=Decimal('0'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=Decimal('805.78'),
        supplemental_data=shared.SupplementalData(
            content={
                "sapiente": {
                    "consectetur": 'esse',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='89fd871f-99dd-42ef-9121-aa6f1e674bdb',
            supplier_name='accusantium',
        ),
        total_amount=Decimal('805.78'),
        total_discount=Decimal('0'),
        total_tax_amount=Decimal('0'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('3069.86'),
                name='Samuel Hermiston',
            ),
        ],
    ),
    bill_credit_note_id='nisi',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=16328,
)

res = s.bill_credit_notes.update(req)

if res.update_bill_credit_note_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateBillCreditNoteRequest](../../models/operations/updatebillcreditnoterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.UpdateBillCreditNoteResponse](../../models/operations/updatebillcreditnoteresponse.md)**

