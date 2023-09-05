# bill_credit_notes

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

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date='2022-10-23T00:00:00.000Z',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='GBP',
        currency_rate=8700.13,
        discount_percentage=0,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='7cc78ca1-ba92-48fc-8167-42cb73920592',
                    name='Curtis Morissette',
                ),
                description='saepe',
                discount_amount=6818.2,
                discount_percentage=4499.5,
                item_ref=shared.BillCreditNoteLineItemItemReference(
                    id='596eb10f-aaa2-4352-8595-5907aff1a3a2',
                    name='Shaun McCullough',
                ),
                quantity=4663.11,
                sub_total=4746.97,
                tax_amount=2444.25,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6235.1,
                    id='251aa52c-3f5a-4d01-9da1-ffe78f097b00',
                    name='Mrs. April Wuckert',
                ),
                total_amount=4808.94,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='b5e6e13b-99d4-488e-9e91-e450ad2abd44',
                            name='Beth McGlynn Sr.',
                        ),
                    ],
                    customer_ref=shared.BillCreditNoteLineItemTrackingCustomerRef(
                        company_name='assumenda',
                        id='502a94bb-4f63-4c96-9e9a-3efa77dfb14c',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.BillCreditNoteLineItemTrackingProjectReference(
                        id='6ae395ef-b9ba-488f-ba66-997074ba4469',
                        name='Duane Thiel II',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='959890af-a563-4e25-96fe-4c8b711e5b7f',
                        name='Louis Turner Sr.',
                    ),
                ],
                unit_amount=5083.15,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='921cddc6-9260-41fb-976b-0d5f0d30c5fb',
                    name='Ernest Hayes',
                ),
                description='eaque',
                discount_amount=3389.85,
                discount_percentage=1999.96,
                item_ref=shared.BillCreditNoteLineItemItemReference(
                    id='202c73d5-fe9b-490c-a890-9b3fe49a8d9c',
                    name='Toby Hahn',
                ),
                quantity=2123.9,
                sub_total=2098.43,
                tax_amount=2224.43,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1861.93,
                    id='3f9b77f3-a410-4067-8ebf-69280d1ba77a',
                    name='Arturo Treutel',
                ),
                total_amount=4694.97,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='7ae4203c-e5e6-4a95-98a0-d446ce2af7a7',
                            name='Rosalie White',
                        ),
                    ],
                    customer_ref=shared.BillCreditNoteLineItemTrackingCustomerRef(
                        company_name='accusamus',
                        id='453f870b-326b-45a7-b429-cdb1a8422bb6',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.BillCreditNoteLineItemTrackingProjectReference(
                        id='d2322715-bf0c-4bb1-a31b-8b90f3443a11',
                        name='Miss Billie Ward',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='f4b92187-9fce-4953-b73e-f7fbc7abd74d',
                        name='Earl Mosciski DVM',
                    ),
                    shared.TrackingCategoryRef(
                        id='5d2cff7c-70a4-4562-ad43-6813f16d9f5f',
                        name='Elbert Jenkins',
                    ),
                    shared.TrackingCategoryRef(
                        id='56146c3e-250f-4b00-8c42-e141aac366c8',
                        name='Drew Hoeger I',
                    ),
                    shared.TrackingCategoryRef(
                        id='42907474-778a-47bd-866d-28c10ab3cdca',
                        name='Ms. Ruby Hintz II',
                    ),
                ],
                unit_amount=8920.5,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='523c7e0b-c717-48e4-b96f-2a70c688282a',
                    name='Randall Lindgren',
                ),
                description='nisi',
                discount_amount=1470.14,
                discount_percentage=9564.06,
                item_ref=shared.BillCreditNoteLineItemItemReference(
                    id='222e9817-ee17-4cbe-a1e6-b7b95bc0ab3c',
                    name='Elizabeth Schinner',
                ),
                quantity=2328.65,
                sub_total=4581.39,
                tax_amount=5034.27,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5909.84,
                    id='fd871f99-dd2e-4fd1-a1aa-6f1e674bdb04',
                    name='Samuel Hermiston',
                ),
                total_amount=3917.74,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='82d68ea1-9f1d-4170-9133-9d08086a1840',
                            name='Toni Fritsch',
                        ),
                    ],
                    customer_ref=shared.BillCreditNoteLineItemTrackingCustomerRef(
                        company_name='voluptas',
                        id='071f93f5-f064-42da-87af-515cc413aa63',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.BillCreditNoteLineItemTrackingProjectReference(
                        id='e8d67864-dbb6-475f-95e6-0b375ed4f6fb',
                        name='Dr. Terence Gulgowski',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='317fe35b-60eb-41ea-8265-55ba3c28744e',
                        name='Dustin Ferry',
                    ),
                ],
                unit_amount=5553.61,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='f3a8d8f5-c0b2-4f2f-b7b1-94a276b26916',
                    name='Rogelio Bins V',
                ),
                description='maiores',
                discount_amount=2748.23,
                discount_percentage=1484.78,
                item_ref=shared.BillCreditNoteLineItemItemReference(
                    id='94e3698f-447f-4603-a8b4-45e80ca55efd',
                    name='Deborah Turcotte',
                ),
                quantity=4461.35,
                sub_total=8892.34,
                tax_amount=1046.27,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5124.52,
                    id='58b6a89f-be3a-45aa-8e48-24d0ab407508',
                    name='Ms. Lamar Hessel',
                ),
                total_amount=1536.27,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='65e904f3-b119-44b8-abf6-03a79f9dfe0a',
                            name='Ron Schulist',
                        ),
                    ],
                    customer_ref=shared.BillCreditNoteLineItemTrackingCustomerRef(
                        company_name='mollitia',
                        id='50ce187f-86bc-4173-9689-eee9526f8d98',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.BillCreditNoteLineItemTrackingProjectReference(
                        id='881ead4f-0e10-4125-a3f9-4e29e973e922',
                        name='Leo Kiehn II',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='e3e06080-7e2b-46e3-ab88-45f0597a60ff',
                        name='Alberta Harber',
                    ),
                    shared.TrackingCategoryRef(
                        id='31e94764-a3e8-465e-b956-f9251a5a9da6',
                        name='Ruth Zulauf',
                    ),
                    shared.TrackingCategoryRef(
                        id='7bfaad4f-9efc-41b4-912c-1032648dc2f6',
                        name='Cathy Breitenberg',
                    ),
                ],
                unit_amount=9364.69,
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
                    currency_rate=9358.33,
                    total_amount=5962.11,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='fe6c632c-a3ae-4d01-9799-6312fde04771',
                        name='Tamara Lang',
                    ),
                    currency='USD',
                    currency_rate=999.58,
                    id='d0174763-60a1-45db-aa66-0659a1adeaab',
                    note='ad',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='enim',
                    total_amount=1104.77,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=7758.03,
                    total_amount=4053.73,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='45b08b61-891b-4aa0-be1a-de008e6f8c5f',
                        name='Marion Aufderhar',
                    ),
                    currency='EUR',
                    currency_rate=8427.77,
                    id='b5a34181-4301-4042-9813-d5208ece7e25',
                    note='nesciunt',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='eum',
                    total_amount=4269.43,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=3494.4,
                    total_amount=704.1,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='c6c6e205-e16d-4eab-bfec-9578a6458427',
                        name='Lee Larkin IV',
                    ),
                    currency='EUR',
                    currency_rate=1173.8,
                    id='62309fb0-9299-421a-afb9-f58c4d86e68e',
                    note='modi',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='vero',
                    total_amount=329.01,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=13.83,
                    total_amount=938.94,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='3f59da75-7a59-4ecf-af66-ef1caa3383c2',
                        name='Lamar Reichert',
                    ),
                    currency='USD',
                    currency_rate=1940.23,
                    id='73c8d72f-64d1-4db1-b2c4-310661e96349',
                    note='earum',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='impedit',
                    total_amount=9758.84,
                ),
            ),
        ],
        remaining_credit=0,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "alias": {
                    "itaque": 'velit',
                    "laborum": 'non',
                },
                "dolor": {
                    "sit": 'doloremque',
                    "consequatur": 'officia',
                },
                "recusandae": {
                    "quidem": 'voluptas',
                    "facilis": 'placeat',
                },
                "perspiciatis": {
                    "deleniti": 'a',
                    "voluptate": 'ullam',
                    "unde": 'necessitatibus',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='ac55a974-1d31-4135-a965-bb8a72026114',
            supplier_name='neque',
        ),
        total_amount=805.78,
        total_discount=0,
        total_tax_amount=0,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=9323.94,
                name='Tracy Mills',
            ),
            shared.WithholdingTaxitems(
                amount=8028.94,
                name='Marilyn Heaney',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=115661,
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
    bill_credit_note_id='id',
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
    query='libero',
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

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date='2022-10-23T00:00:00.000Z',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='USD',
        currency_rate=5546.03,
        discount_percentage=0,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='70e1084c-b067-42d1-ad87-9eeb9665b85e',
                    name='Mr. Jonathon Swaniawski',
                ),
                description='fuga',
                discount_amount=9195.08,
                discount_percentage=340.7,
                item_ref=shared.BillCreditNoteLineItemItemReference(
                    id='be2d7822-59e3-4ea4-b519-7f92443da7ce',
                    name='Phyllis Quitzon',
                ),
                quantity=3262.69,
                sub_total=8095.94,
                tax_amount=3165.42,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2040.72,
                    id='7c6454ef-b0b3-4489-ac3c-a5acfbe2fd57',
                    name='Viola Hane',
                ),
                total_amount=5678.46,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='9177deac-646e-4cb5-b340-9e3eb1e5a2b1',
                            name='Ms. Kelley Rogahn',
                        ),
                    ],
                    customer_ref=shared.BillCreditNoteLineItemTrackingCustomerRef(
                        company_name='veritatis',
                        id='16db9954-5fc9-45fa-8897-0e189dbb30fc',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.BillCreditNoteLineItemTrackingProjectReference(
                        id='3ea055b1-97cd-444e-af52-d82d3513bb6f',
                        name='Mattie Raynor',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='bcdb35ff-2e4b-4275-b7a8-cd9e7319c177',
                        name='Leon Collier',
                    ),
                    shared.TrackingCategoryRef(
                        id='77b114ee-b52f-4f78-9fc3-7814d4c98e0c',
                        name='Candice Rath',
                    ),
                ],
                unit_amount=9222.99,
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
                    currency='EUR',
                    currency_rate=6293.77,
                    total_amount=8339.82,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='636c6005-03d8-4bb3-9180-f739ae9e057e',
                        name='Johnnie Baumbach',
                    ),
                    currency='GBP',
                    currency_rate=5200.81,
                    id='10331f39-81d4-4c70-8b60-7f3c93c73b9d',
                    note='officia',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='tenetur',
                    total_amount=1339.49,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=8483.46,
                    total_amount=6707.62,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='7e23f225-7411-4faf-8b75-44e472e80285',
                        name='Marguerite Hansen',
                    ),
                    currency='GBP',
                    currency_rate=2667.88,
                    id='63a7d575-f140-40e7-a4ad-7334ec1b781b',
                    note='amet',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='fuga',
                    total_amount=53.1,
                ),
            ),
        ],
        remaining_credit=0,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "quos": {
                    "repellendus": 'veritatis',
                    "quae": 'eaque',
                    "saepe": 'delectus',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='ada200ef-0422-4eb2-964c-f9ab8366c723',
            supplier_name='reiciendis',
        ),
        total_amount=805.78,
        total_discount=0,
        total_tax_amount=0,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=8611.23,
                name='Mrs. Luther Torp',
            ),
            shared.WithholdingTaxitems(
                amount=9248.4,
                name='Kyle Leffler',
            ),
            shared.WithholdingTaxitems(
                amount=7868.6,
                name='Dr. Shari Roob Sr.',
            ),
            shared.WithholdingTaxitems(
                amount=3178.98,
                name='Ian Auer',
            ),
        ],
    ),
    bill_credit_note_id='a',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=615058,
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

