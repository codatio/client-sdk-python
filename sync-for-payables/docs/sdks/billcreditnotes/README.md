# BillCreditNotes
(*bill_credit_notes*)

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
        discount_percentage=Decimal('0'),
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(),
                item_ref=shared.BillCreditNoteLineItemItemReference(
                    id='<ID>',
                ),
                quantity=Decimal('8592.13'),
                tax_rate_ref=shared.TaxRateRef(),
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='<ID>',
                        ),
                    ],
                    customer_ref=shared.BillCreditNoteLineItemTrackingCustomerRef(
                        id='<ID>',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.BillCreditNoteLineItemTrackingProjectReference(
                        id='<ID>',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='<ID>',
                    ),
                ],
                unit_amount=Decimal('1343.65'),
            ),
        ],
        metadata=shared.Metadata(),
        modified_date='2022-10-23T00:00:00.000Z',
        note='Bill Credit Note with 1 line items, totaling 805.78',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(),
                    currency='EUR',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                ),
            ),
        ],
        remaining_credit=Decimal('0'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=Decimal('805.78'),
        supplemental_data=shared.SupplementalData(
            content={
                "key": {
                    "key": 'string',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='<ID>',
        ),
        total_amount=Decimal('805.78'),
        total_discount=Decimal('0'),
        total_tax_amount=Decimal('0'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('8915.1'),
                name='string',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bill_credit_notes.create(req)

if res.create_bill_credit_note_response is not None:
    # handle response
    pass
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
    bill_credit_note_id='string',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.bill_credit_notes.get(req)

if res.bill_credit_note is not None:
    # handle response
    pass
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
    pass
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
)

res = s.bill_credit_notes.list(req)

if res.bill_credit_notes is not None:
    # handle response
    pass
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
        currency='GBP',
        discount_percentage=Decimal('0'),
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(),
                item_ref=shared.BillCreditNoteLineItemItemReference(
                    id='<ID>',
                ),
                quantity=Decimal('156.52'),
                tax_rate_ref=shared.TaxRateRef(),
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='<ID>',
                        ),
                    ],
                    customer_ref=shared.BillCreditNoteLineItemTrackingCustomerRef(
                        id='<ID>',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.BillCreditNoteLineItemTrackingProjectReference(
                        id='<ID>',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='<ID>',
                    ),
                ],
                unit_amount=Decimal('9914.64'),
            ),
        ],
        metadata=shared.Metadata(),
        modified_date='2022-10-23T00:00:00.000Z',
        note='Bill Credit Note with 1 line items, totaling 805.78',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(),
                    currency='USD',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                ),
            ),
        ],
        remaining_credit=Decimal('0'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=Decimal('805.78'),
        supplemental_data=shared.SupplementalData(
            content={
                "key": {
                    "key": 'string',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='<ID>',
        ),
        total_amount=Decimal('805.78'),
        total_discount=Decimal('0'),
        total_tax_amount=Decimal('0'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('1341.51'),
                name='string',
            ),
        ],
    ),
    bill_credit_note_id='string',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bill_credit_notes.update(req)

if res.update_bill_credit_note_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateBillCreditNoteRequest](../../models/operations/updatebillcreditnoterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.UpdateBillCreditNoteResponse](../../models/operations/updatebillcreditnoteresponse.md)**

