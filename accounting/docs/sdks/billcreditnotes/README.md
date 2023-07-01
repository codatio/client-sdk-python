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

The *Create bill credit note* endpoint creates a new [bill credit note](https://docs.codat.io/accounting-api#/schemas/BillCreditNote) for a given company's connection.

[Bill credit notes](https://docs.codat.io/accounting-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date='2022-10-23T00:00:00.000Z',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='GBP',
        currency_rate=8289.4,
        discount_percentage=0,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='2a94bb4f-63c9-469e-9a3e-fa77dfb14cd6',
                    name='Kayla Thompson',
                ),
                description='enim',
                discount_amount=8817.36,
                discount_percentage=9654.17,
                item_ref=shared.ItemRef(
                    id='b9ba88f3-a669-4970-b4ba-4469b6e21419',
                    name='Ramona Lueilwitz MD',
                ),
                quantity=9689.62,
                sub_total=6521.03,
                tax_amount=3209.97,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4314.18,
                    id='3e2516fe-4c8b-4711-a5b7-fd2ed028921c',
                    name='Ervin Schoen',
                ),
                total_amount=1399.72,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='01fb576b-0d5f-40d3-8c5f-bb2587053202',
                            name='Darryl Fadel',
                        ),
                        shared.TrackingCategoryRef(
                            id='fe9b90c2-8909-4b3f-a49a-8d9cbf486333',
                            name='Tiffany Welch',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='voluptate',
                        id='7f3a4100-674e-4bf6-9280-d1ba77a89ebf',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='7ae4203c-e5e6-4a95-98a0-d446ce2af7a7',
                        name='Rosalie White',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='453f870b-326b-45a7-b429-cdb1a8422bb6',
                        name='Felicia Spencer',
                    ),
                    shared.TrackingCategoryRef(
                        id='22715bf0-cbb1-4e31-b8b9-0f3443a1108e',
                        name='Jodi Skiles',
                    ),
                    shared.TrackingCategoryRef(
                        id='4b921879-fce9-453f-b3ef-7fbc7abd74dd',
                        name='Dr. Faye Rutherford',
                    ),
                    shared.TrackingCategoryRef(
                        id='d2cff7c7-0a45-4626-9436-813f16d9f5fc',
                        name='Nathaniel Ryan',
                    ),
                ],
                unit_amount=3994.99,
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
                    currency_rate=2322.34,
                    total_amount=9262.13,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='250fb008-c42e-4141-aac3-66c8dd6b1442',
                        name='Jose Kreiger',
                    ),
                    currency='GBP',
                    currency_rate=4585.15,
                    id='78a7bd46-6d28-4c10-ab3c-dca4251904e5',
                    note='aspernatur',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='quo',
                    total_amount=4598.56,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=7151.79,
                    total_amount=7997.96,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='7178e479-6f2a-470c-a882-82aa482562f2',
                        name='Rose Turner',
                    ),
                    currency='GBP',
                    currency_rate=4569.11,
                    id='ee17cbe6-1e6b-47b9-9bc0-ab3c20c4f378',
                    note='provident',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='nulla',
                    total_amount=5578.11,
                ),
            ),
        ],
        remaining_credit=0,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "a": {
                    "sint": 'pariatur',
                    "possimus": 'quia',
                    "eveniet": 'asperiores',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='d121aa6f-1e67-44bd-b04f-15756082d68e',
            supplier_name='dolorum',
        ),
        total_amount=805.78,
        total_discount=0,
        total_tax_amount=0,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=6091.78,
                name='Ms. Roger Strosin II',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=86532,
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
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetBillCreditNoteRequest(
    bill_credit_note_id='consectetur',
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
from codataccounting.models import operations

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
from codataccounting.models import operations

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
    query='adipisci',
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

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date='2022-10-23T00:00:00.000Z',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='EUR',
        currency_rate=330.74,
        discount_percentage=0,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='86a18403-94c2-4607-9f93-f5f0642dac7a',
                    name='Vernon Bergnaum',
                ),
                description='quod',
                discount_amount=2883.98,
                discount_percentage=704.47,
                item_ref=shared.ItemRef(
                    id='3aa63aae-8d67-4864-9bb6-75fd5e60b375',
                    name='Carroll Gerhold',
                ),
                quantity=9689.72,
                sub_total=6971.42,
                tax_amount=9049.49,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8970.71,
                    id='41f33317-fe35-4b60-ab1e-a426555ba3c2',
                    name='Harvey Gulgowski',
                ),
                total_amount=8391.89,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='3b88f3a8-d8f5-4c0b-af2f-b7b194a276b2',
                            name='Geneva Bradtke',
                        ),
                        shared.TrackingCategoryRef(
                            id='e1f08f42-94e3-4698-b447-f603e8b445e8',
                            name='Della Muller',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='recusandae',
                        id='fd20e457-e185-48b6-a89f-be3a5aa8e482',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='0ab40750-88e5-4186-a065-e904f3b1194b',
                        name='Cameron Reilly',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='3a79f9df-e0ab-47da-8a50-ce187f86bc17',
                        name='Angelina Jenkins',
                    ),
                ],
                unit_amount=8872.65,
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
                    currency_rate=1334.61,
                    total_amount=4044.25,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='f8d986e8-81ea-4d4f-8e10-12563f94e29e',
                        name='Arnold Ferry',
                    ),
                    currency='GBP',
                    currency_rate=1458.7,
                    id='a57a15be-3e06-4080-be2b-6e3ab8845f05',
                    note='perspiciatis',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='mollitia',
                    total_amount=3782.45,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=9702.22,
                    total_amount=1746.58,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='a54a31e9-4764-4a3e-865e-7956f9251a5a',
                        name='Rufus Okuneva',
                    ),
                    currency='GBP',
                    currency_rate=9992.78,
                    id='f57bfaad-4f9e-4fc1-b451-2c1032648dc2',
                    note='sapiente',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='dicta',
                    total_amount=3251.18,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=5896.95,
                    total_amount=9364.69,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='bfd0e9fe-6c63-42ca-baed-0117996312fd',
                        name='Jeffrey Goldner',
                    ),
                    currency='GBP',
                    currency_rate=4797.54,
                    id='78ff61d0-1747-4636-8a15-db6a660659a1',
                    note='error',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='voluptates',
                    total_amount=6534.21,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=3240.83,
                    total_amount=5369.23,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='51d6c645-b08b-4618-91ba-a0fe1ade008e',
                        name='Miranda Ledner',
                    ),
                    currency='EUR',
                    currency_rate=1905.67,
                    id='50d8cdb5-a341-4814-b010-421813d5208e',
                    note='impedit',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='esse',
                    total_amount=8972.77,
                ),
            ),
        ],
        remaining_credit=0,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "nesciunt": {
                    "eum": 'vel',
                    "voluptatum": 'magnam',
                    "exercitationem": 'ab',
                },
                "porro": {
                    "nobis": 'laboriosam',
                    "recusandae": 'consequuntur',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='05e16dea-b3fe-4c95-b8a6-4584273a8418',
            supplier_name='fugiat',
        ),
        total_amount=805.78,
        total_discount=0,
        total_tax_amount=0,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=3955.44,
                name='Edith Beahan',
            ),
        ],
    ),
    bill_credit_note_id='soluta',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=3860,
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

