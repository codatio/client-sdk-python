# bill_credit_notes

## Overview

Bill credit notes

### Available Operations

* [create](#create) - Create bill credit note
* [get](#get) - Get bill credit note
* [get_create_update_model](#get_create_update_model) - Get create/update bill credit note model
* [list](#list) - List bill credit notes
* [update](#update) - Update bill credit note
* [upload_attachment](#upload_attachment) - Upload bill credit note attachment

## create

The *Create bill credit note* endpoint creates a new [bill credit note](https://docs.codat.io/accounting-api#/schemas/BillCreditNote) for a given company's connection.

[Bill credit notes](https://docs.codat.io/accounting-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date='2022-10-23T00:00:00.000Z',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='USD',
        currency_rate=Decimal('7392.64'),
        discount_percentage=Decimal('0'),
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='074f1547-1b5e-46e1-bb99-d488e1e91e45',
                    name='Monique Spinka',
                ),
                description='distinctio',
                discount_amount=Decimal('8413.86'),
                discount_percentage=Decimal('2894.06'),
                item_ref=shared.ItemRef(
                    id='4269802d-502a-494b-b4f6-3c969e9a3efa',
                    name='Arlene Stamm',
                ),
                quantity=Decimal('1162.02'),
                sub_total=Decimal('2974.37'),
                tax_amount=Decimal('7670.24'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('8137.98'),
                    id='66ae395e-fb9b-4a88-b3a6-6997074ba446',
                    name='Robin Keebler',
                ),
                total_amount=Decimal('1028.63'),
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='41959890-afa5-463e-a516-fe4c8b711e5b',
                            name='Kristie Spencer',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='pariatur',
                        id='028921cd-dc69-4260-9fb5-76b0d5f0d30c',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='bb258705-3202-4c73-95fe-9b90c28909b3',
                        name='Merle Gleichner',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='8d9cbf48-6333-423f-9b77-f3a4100674eb',
                        name='Hector Mosciski',
                    ),
                ],
                unit_amount=Decimal('246.78'),
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
                    currency_rate=Decimal('6793.93'),
                    total_amount=Decimal('4785.96'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='7a89ebf7-37ae-4420-bce5-e6a95d8a0d44',
                        name='Bernadette Torp',
                    ),
                    currency='EUR',
                    currency_rate=Decimal('4561.3'),
                    id='a73cf3be-453f-4870-b326-b5a73429cdb1',
                    note='laborum',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='incidunt',
                    total_amount=Decimal('1320.68'),
                ),
            ),
        ],
        remaining_credit=Decimal('0'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=Decimal('805.78'),
        supplemental_data=shared.SupplementalData(
            content={
                "distinctio": {
                    "facilis": 'aliquid',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='79d23227-15bf-40cb-b1e3-1b8b90f3443a',
            supplier_name='architecto',
        ),
        total_amount=Decimal('805.78'),
        total_discount=Decimal('0'),
        total_tax_amount=Decimal('0'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('630.38'),
                name='Miss Billie Ward',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=785153,
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

The *Get bill credit note* endpoint returns a single bill credit note for a given billCreditNoteId.

[Bill credit notes](https://docs.codat.io/accounting-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support getting a specific bill credit note.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetBillCreditNoteRequest(
    bill_credit_note_id='doloribus',
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

The *Get create/update bill credit note model* endpoint returns the expected data for the request payload when creating and updating a [bill credit note](https://docs.codat.io/accounting-api#/schemas/BillCreditNote) for a given company and integration.

[Bill credit notes](https://docs.codat.io/accounting-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating and updating a bill credit note.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateBillCreditNotesModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bill_credit_notes.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetCreateUpdateBillCreditNotesModelRequest](../../models/operations/getcreateupdatebillcreditnotesmodelrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |


### Response

**[operations.GetCreateUpdateBillCreditNotesModelResponse](../../models/operations/getcreateupdatebillcreditnotesmodelresponse.md)**


## list

The *List bill credit notes* endpoint returns a list of [bill credit notes](https://docs.codat.io/accounting-api#/schemas/BillCreditNote) for a given company's connection.

[Bill credit notes](https://docs.codat.io/accounting-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBillCreditNotesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='ut',
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

The *Update bill credit note* endpoint updates an existing [bill credit note](https://docs.codat.io/accounting-api#/schemas/BillCreditNote) for a given company's connection.

[Bill credit notes](https://docs.codat.io/accounting-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date='2022-10-23T00:00:00.000Z',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='USD',
        currency_rate=Decimal('1816.31'),
        discount_percentage=Decimal('0'),
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='879fce95-3f73-4ef7-bbc7-abd74dd39c0f',
                    name='Freda Cormier',
                ),
                description='doloribus',
                discount_amount=Decimal('4783.7'),
                discount_percentage=Decimal('7535.7'),
                item_ref=shared.ItemRef(
                    id='70a45626-d436-4813-b16d-9f5fce6c5561',
                    name='Rosemary Ryan',
                ),
                quantity=Decimal('1324.87'),
                sub_total=Decimal('3253.1'),
                tax_amount=Decimal('534.27'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('9528.71'),
                    id='b008c42e-141a-4ac3-a6c8-dd6b14429074',
                    name='Esther Koch',
                ),
                total_amount=Decimal('6832.82'),
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='7bd466d2-8c10-4ab3-8dca-4251904e523c',
                            name='Sophie Bayer',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='dignissimos',
                        id='178e4796-f2a7-40c6-8828-2aa482562f22',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='9817ee17-cbe6-41e6-b7b9-5bc0ab3c20c4',
                        name='Glenn Koch',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='fd871f99-dd2e-4fd1-a1aa-6f1e674bdb04',
                        name='Samuel Hermiston',
                    ),
                ],
                unit_amount=Decimal('3917.74'),
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
                    currency_rate=Decimal('8453.58'),
                    total_amount=Decimal('4012.59'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='8ea19f1d-1705-4133-9d08-086a1840394c',
                        name='Loretta Anderson DVM',
                    ),
                    currency='USD',
                    currency_rate=Decimal('2446.51'),
                    id='f5f0642d-ac7a-4f51-9cc4-13aa63aae8d6',
                    note='ducimus',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='vel',
                    total_amount=Decimal('2870.51'),
                ),
            ),
        ],
        remaining_credit=Decimal('0'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=Decimal('805.78'),
        supplemental_data=shared.SupplementalData(
            content={
                "facilis": {
                    "cum": 'commodi',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='75fd5e60-b375-4ed4-b6fb-ee41f33317fe',
            supplier_name='consectetur',
        ),
        total_amount=Decimal('805.78'),
        total_discount=Decimal('0'),
        total_tax_amount=Decimal('0'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('3581.07'),
                name='Rick Beer',
            ),
        ],
    ),
    bill_credit_note_id='vitae',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=881721,
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


## upload_attachment

---
stoplight-id: c26f5b1b19168
---

The *Upload bill credit note attachment* endpoint uploads an attachment and assigns it against a specific `billCreditNoteId`.

[Bill Credit Notes](https://docs.codat.io/accounting-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

**Integration-specific behaviour**

For more details on supported file types by integration see [Attachments](https://docs.codat.io/accounting-api#/schemas/Attachment).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support uploading a bill credit note attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadBillCreditNoteAttachmentRequest(
    request_body=operations.UploadBillCreditNoteAttachmentRequestBody(
        content='similique'.encode(),
        request_body='tempora',
    ),
    bill_credit_note_id='aspernatur',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bill_credit_notes.upload_attachment(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.UploadBillCreditNoteAttachmentRequest](../../models/operations/uploadbillcreditnoteattachmentrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |


### Response

**[operations.UploadBillCreditNoteAttachmentResponse](../../models/operations/uploadbillcreditnoteattachmentresponse.md)**

