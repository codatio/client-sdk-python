# credit_notes

## Overview

Credit notes

### Available Operations

* [create](#create) - Create credit note
* [get](#get) - Get credit note
* [get_create_update_model](#get_create_update_model) - Get create/update credit note model
* [list](#list) - List credit notes
* [update](#update) - Update creditNote

## create

The *Create credit note* endpoint creates a new [credit note](https://docs.codat.io/accounting-api#/schemas/CreditNote) for a given company's connection.

[Credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) are issued to a customer to indicate debt, typically with reference to a previously issued invoice and/or purchase.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateCreditNoteRequest(
    credit_note=shared.CreditNote(
        additional_tax_amount=5321.1,
        additional_tax_percentage=8172.49,
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='natus',
        currency='EUR',
        currency_rate=9143.99,
        customer_ref=shared.CustomerRef(
            company_name='illo',
            id='dd7097b5-da08-4c57-ba6c-78a216e19baf',
        ),
        discount_percentage=9226.4,
        id='ca619149-8140-4b64-bf8a-e170ef03b5f3',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='4aa86855-5966-4732-aa5d-cb6682cb70f8',
                    name='Roman Shanahan',
                ),
                description='tempore',
                discount_amount=3888.51,
                discount_percentage=9347.07,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='91b9a9f7-4846-4e2c-b309-db0536d9e75c',
                    name='Robert Balistreri',
                ),
                quantity=3375.81,
                sub_total=2117.56,
                tax_amount=6091.64,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1500.91,
                    id='c11a25a8-bf92-4f97-828a-d9a9f8bf8221',
                    name='Lori Hammes',
                ),
                total_amount=5929.46,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='98387f7a-79cd-472c-9248-4da21729f2ac',
                            name='Amanda Tromp',
                        ),
                        shared.TrackingCategoryRef(
                            id='725f1169-ac1e-441d-8a23-c23e34f2dfa4',
                            name='Lawrence Metz',
                        ),
                        shared.TrackingCategoryRef(
                            id='6de92215-1fe1-4712-8998-53e9f543d854',
                            name='Rosa Metz',
                        ),
                        shared.TrackingCategoryRef(
                            id='22446044-3bc1-4541-88c2-f56e85da7832',
                            name='Hubert Rempel',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='et',
                        id='7c3b0d51-a44b-4f01-bad8-706d46082bfb',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='41ff5d4e-2ae4-4fb5-8b35-d17638f1edb7',
                        name='Jeffery Hilll',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c5cb860f-8cd5-480b-a738-10e4fe444729',
                        name='Erma Streich',
                    ),
                    shared.TrackingCategoryRef(
                        id='1dd3bbce-247b-4768-8eff-50126d71cffb',
                        name='David Waters',
                    ),
                    shared.TrackingCategoryRef(
                        id='4b842195-3b44-4bd3-8431-59d33e5953c0',
                        name='Cheryl Bins',
                    ),
                    shared.TrackingCategoryRef(
                        id='863aa41e-6c31-4cc2-b1fc-b51c9a41ffbe',
                        name='Forrest Powlowski',
                    ),
                ],
                unit_amount=6205.2,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='5ee65e07-6cc7-4abf-a16e-a5c71641934b',
                    name='Daniel Zemlak',
                ),
                description='sit',
                discount_amount=5776.72,
                discount_percentage=8573.88,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='19d2fc2f-9e2e-4105-944b-935d237a72f9',
                    name='Mattie Gutkowski',
                ),
                quantity=3849.39,
                sub_total=6596.96,
                tax_amount=9303.06,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8266.83,
                    id='4aecb753-7cd9-4222-89ff-57491aabfa2e',
                    name='Agnes Boyle DDS',
                ),
                total_amount=6645.01,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='d456ef10-31e6-4899-b0c2-001e22cd55cc',
                            name='Ida MacGyver',
                        ),
                        shared.TrackingCategoryRef(
                            id='184d76d9-71fc-4820-865b-037bb8e0cc88',
                            name='Carolyn Macejkovic',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='labore',
                        id='de04af28-c5dd-4db4-aaa1-cfd6d828da01',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='91129646-645c-41d8-9f29-042f569b7aff',
                        name='Tasha Pagac',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='6cbe071b-c163-4e27-9a3b-084da99257d0',
                        name='Ms. Ollie Gibson',
                    ),
                ],
                unit_amount=4782.16,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='a742d844-96cb-4dee-8f6b-99bc63562ebf',
                    name='Van Halvorson',
                ),
                description='dolores',
                discount_amount=6102.13,
                discount_percentage=2859.22,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='c060b06a-1287-4764-aef6-d0c6d6ed9c73',
                    name='Lionel Kerluke',
                ),
                quantity=3419.34,
                sub_total=4922.27,
                tax_amount=768.18,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3613.31,
                    id='09a8e870-d3c5-4a1f-9c24-2c7b66a1f30c',
                    name='Ethel Schultz',
                ),
                total_amount=6939.88,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='719890f4-2a4b-4b43-8d85-b260591d745e',
                            name='Mrs. Sheri Cruickshank',
                        ),
                        shared.TrackingCategoryRef(
                            id='c9c3f567-e0e2-4527-a5b1-d62fcdace1f0',
                            name='Christina Bode',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='repudiandae',
                        id='2239e8f2-5cd0-4d19-9959-f439e39266cb',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='5f7aa2b2-4113-4695-91e6-698fcc459621',
                        name='Kendra D'Amore',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='67633425-4038-4bfb-9971-e98190557389',
                        name='Percy Swaniawski',
                    ),
                    shared.TrackingCategoryRef(
                        id='c7fda395-94d6-46bc-aae4-80632b9954b6',
                        name='Mr. Alfonso Dibbert',
                    ),
                ],
                unit_amount=2026.42,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='69828553-cb10-4006-bef4-921ec2053b74',
                    name='Marvin Jacobson',
                ),
                description='quisquam',
                discount_amount=5223.27,
                discount_percentage=9109.84,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='e0f2bf19-588d-440d-83f3-deba297be3e9',
                    name='Maryann Rolfson PhD',
                ),
                quantity=9843.02,
                sub_total=5544.17,
                tax_amount=4169.67,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5023.8,
                    id='fd52405c-b331-4d49-af4f-127fb0e0bf1f',
                    name='Steve Block',
                ),
                total_amount=4940.93,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='d0acca77-aeb7-4b70-a1a5-2046b64e99fb',
                            name='Gretchen Huels',
                        ),
                        shared.TrackingCategoryRef(
                            id='094fdfed-5540-4ef5-ba34-a1b8fe99731a',
                            name='Rodolfo Baumbach',
                        ),
                        shared.TrackingCategoryRef(
                            id='85ae2dfb-70fb-4387-8290-d336561eca16',
                            name='Santos Langosh',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='ad',
                        id='1bd76eee-b518-4c4d-a1fa-d35512f06d4e',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='72f0f548-568a-4042-8e00-a1d6eb943464',
                        name='Cristina Beer V',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='fbba5cce-ff5c-4b01-be51-e528a45ac82b',
                        name='Derrick Wunsch',
                    ),
                    shared.TrackingCategoryRef(
                        id='c2caba8d-a412-47dd-997f-f4711aa1bc74',
                        name='Alberto Hyatt',
                    ),
                ],
                unit_amount=7880.36,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='ducimus',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=4976.33,
                    total_amount=7222,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='4848bd6a-6f04-441d-ac3b-808094373e06',
                        name='Lucille Hermiston',
                    ),
                    currency='EUR',
                    currency_rate=7001.12,
                    id='bad02f25-86bc-4f15-a558-daa95be6cd02',
                    note='in',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='vel',
                    total_amount=7736.78,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=2817.53,
                    total_amount=6681.55,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='a432b47e-1763-4c52-88c2-3e9802d82f0d',
                        name='Dolores Waelchi',
                    ),
                    currency='EUR',
                    currency_rate=5034.79,
                    id='b674ee5c-fc18-4edc-bf78-7e32e04b3d3e',
                    note='facere',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='cumque',
                    total_amount=3532.32,
                ),
            ),
        ],
        remaining_credit=4271.07,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.UNKNOWN,
        sub_total=9262.25,
        supplemental_data=shared.SupplementalData(
            content={
                "dolore": {
                    "harum": 'illum',
                },
                "dolor": {
                    "iste": 'earum',
                    "vitae": 'impedit',
                    "eligendi": 'veniam',
                    "aperiam": 'consectetur',
                },
                "repellat": {
                    "quod": 'nesciunt',
                    "iste": 'distinctio',
                },
                "cumque": {
                    "alias": 'deserunt',
                    "vel": 'qui',
                    "perspiciatis": 'accusantium',
                    "voluptatibus": 'occaecati',
                },
            },
        ),
        total_amount=3658.63,
        total_discount=4626.73,
        total_tax_amount=9704.91,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=5155.49,
                name='Virginia Littel',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=822084,
)

res = s.credit_notes.create(req)

if res.create_credit_note_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCreditNoteRequest](../../models/operations/createcreditnoterequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.CreateCreditNoteResponse](../../models/operations/createcreditnoteresponse.md)**


## get

The *Get credit note* endpoint returns a single credit note for a given creditNoteId.

[Credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) are issued to a customer to indicate debt, typically with reference to a previously issued invoice and/or purchase.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support getting a specific credit note.

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

req = operations.GetCreditNoteRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    credit_note_id='molestiae',
)

res = s.credit_notes.get(req)

if res.credit_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCreditNoteRequest](../../models/operations/getcreditnoterequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.GetCreditNoteResponse](../../models/operations/getcreditnoteresponse.md)**


## get_create_update_model

﻿The *Get create/update credit note model* endpoint returns the expected data for the request payload when creating and updating a [credit note](https://docs.codat.io/accounting-api#/schemas/CreditNote) for a given company and integration.

[Credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) are issued to a customer to indicate debt, typically with reference to a previously issued invoice and/or purchase.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating and updating a credit note.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateCreditNotesModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.credit_notes.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetCreateUpdateCreditNotesModelRequest](../../models/operations/getcreateupdatecreditnotesmodelrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |


### Response

**[operations.GetCreateUpdateCreditNotesModelResponse](../../models/operations/getcreateupdatecreditnotesmodelresponse.md)**


## list

The *List credit notes* endpoint returns a list of [credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) for a given company's connection.

[Credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) are issued to a customer to indicate debt, typically with reference to a previously issued invoice and/or purchase.

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

req = operations.ListCreditNotesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='officiis',
)

res = s.credit_notes.list(req)

if res.credit_notes is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListCreditNotesRequest](../../models/operations/listcreditnotesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |


### Response

**[operations.ListCreditNotesResponse](../../models/operations/listcreditnotesresponse.md)**


## update

The *Update credit note* endpoint updates an existing [credit note](https://docs.codat.io/accounting-api#/schemas/CreditNote) for a given company's connection.

[Credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) are issued to a customer to indicate debt, typically with reference to a previously issued invoice and/or purchase.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateCreditNoteRequest(
    credit_note=shared.CreditNote(
        additional_tax_amount=9713.93,
        additional_tax_percentage=5288.35,
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='reprehenderit',
        currency='USD',
        currency_rate=6380.92,
        customer_ref=shared.CustomerRef(
            company_name='eveniet',
            id='03f33ca7-9fb9-4de4-832b-a26fd368ba92',
        ),
        discount_percentage=1199.03,
        id='6bcb4158-35c7-4364-9723-133edc046bc5',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='3bbca492-27c4-42c2-ac55-350495c5dbb3',
                    name='Derek Kihn DVM',
                ),
                description='tempora',
                discount_amount=6128.36,
                discount_percentage=5607.36,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='1e8aa257-ddc1-4912-abde-64bfcc5469d4',
                    name='Diane Hayes',
                ),
                quantity=6658.07,
                sub_total=4582.2,
                tax_amount=6140.01,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4054.19,
                    id='206bef2b-0a3e-442c-9aa0-10e9aac2e913',
                    name='Erica Luettgen',
                ),
                total_amount=1161.94,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='f9f97a4b-fad2-4bf7-967c-a84ad99b41d6',
                            name='Sara Funk',
                        ),
                        shared.TrackingCategoryRef(
                            id='31870cf6-8b03-4ad4-a1bd-43d1f0cb0a00',
                            name='Carmen Weber',
                        ),
                        shared.TrackingCategoryRef(
                            id='2d9b3a70-d94f-4aa7-81c5-7d1fedc2050d',
                            name='Olga Stracke',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quo',
                        id='e185472f-9ee6-4916-aa8b-e3444eac8b3a',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='75c6c1fe-606d-407d-aa9c-87ae50c16661',
                        name='Harold Smith I',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a7e8d532-13f3-4f65-8752-db764c59f0a5',
                        name='Nichole Treutel',
                    ),
                    shared.TrackingCategoryRef(
                        id='ada29ca7-9181-4c95-a716-63c530b56651',
                        name='Carmen Nicolas',
                    ),
                ],
                unit_amount=2274.7,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='8512ab25-21b9-4f2e-8724-67b8a40bc05f',
                    name='Wm Bartoletti',
                ),
                description='quis',
                discount_amount=196.1,
                discount_percentage=9319.91,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='df22a94d-20ec-490e-a41d-1f465e85156f',
                    name='Randal Kris',
                ),
                quantity=8372.02,
                sub_total=9459.21,
                tax_amount=3424.58,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2726.64,
                    id='fdd5ea95-4339-48da-bb42-a8d63388e4d8',
                    name='Peggy Muller',
                ),
                total_amount=3381.03,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='9b18a244-fd61-4903-9dac-d38ed0dc671d',
                            name='Dr. Jamie Wintheiser',
                        ),
                        shared.TrackingCategoryRef(
                            id='af15920c-90d1-4b49-81f2-bd89c8a32639',
                            name='Donnie Hauck',
                        ),
                        shared.TrackingCategoryRef(
                            id='b6902b88-1a94-4f64-b664-a8f0af8c691d',
                            name='Carmen Crist',
                        ),
                        shared.TrackingCategoryRef(
                            id='fbaf9476-a2ae-48dc-850c-8a3512c73784',
                            name='Ms. Eduardo Effertz',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='eaque',
                        id='a00e966e-c736-4d43-9943-98c783c92398',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='3d3ab7ca-3c5c-4a86-89a7-0cfd5d6989b7',
                        name='Betty Hirthe',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='077d19ea-83d4-492e-914b-8a2c1954545e',
                        name='Derrick Halvorson',
                    ),
                ],
                unit_amount=7659,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='praesentium',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=3007.59,
                    total_amount=6029.32,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='01c7c43a-d2da-4a78-8aba-3d230edf7381',
                        name='Mrs. Maggie Breitenberg',
                    ),
                    currency='USD',
                    currency_rate=1641.54,
                    id='bd7ed565-0762-41c5-8f4d-7396564c20a0',
                    note='reprehenderit',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='veritatis',
                    total_amount=6283.25,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=1166.35,
                    total_amount=8489.26,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='24a7dbb8-f532-4d89-acf7-812cb512c878',
                        name='Monica Bashirian',
                    ),
                    currency='USD',
                    currency_rate=2743.68,
                    id='8f88f8f1-bf0b-4c8e-9f20-6d5d831d0081',
                    note='voluptatem',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='ipsa',
                    total_amount=9652.07,
                ),
            ),
        ],
        remaining_credit=3763.41,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.UNKNOWN,
        sub_total=3777.59,
        supplemental_data=shared.SupplementalData(
            content={
                "ducimus": {
                    "doloribus": 'ratione',
                },
                "id": {
                    "quos": 'dicta',
                    "minus": 'exercitationem',
                },
            },
        ),
        total_amount=4741.06,
        total_discount=4348.74,
        total_tax_amount=5007,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=7742.94,
                name='Clinton Hackett',
            ),
            shared.WithholdingTaxitems(
                amount=334.24,
                name='Mrs. Gerard Collins',
            ),
            shared.WithholdingTaxitems(
                amount=532.16,
                name='Mrs. Shane Armstrong',
            ),
            shared.WithholdingTaxitems(
                amount=5831.69,
                name='Darrell Yost',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    credit_note_id='debitis',
    force_update=False,
    timeout_in_minutes=207202,
)

res = s.credit_notes.update(req)

if res.update_credit_note_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateCreditNoteRequest](../../models/operations/updatecreditnoterequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.UpdateCreditNoteResponse](../../models/operations/updatecreditnoteresponse.md)**

