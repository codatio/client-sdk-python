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
        additional_tax_amount=6319.04,
        additional_tax_percentage=8377.39,
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='ad',
        currency='USD',
        currency_rate=3831.96,
        customer_ref=shared.CustomerRef(
            company_name='reiciendis',
            id='df1ad837-ae80-4c1c-99c9-5ba998678fa3',
        ),
        discount_percentage=9409.51,
        id='696991af-388c-4e03-a144-48c7977a0ef2',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='36028efe-ef93-4415-aed7-e253f4c157de',
                    name='Ms. Ernesto King DVM',
                ),
                description='incidunt',
                discount_amount=2930.23,
                discount_percentage=3626.93,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='accf667a-af9b-4bad-985f-e431d6bf5c83',
                    name='Emilio Ratke',
                ),
                quantity=7992.36,
                sub_total=1330.76,
                tax_amount=538.69,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7734.55,
                    id='b67fc4b4-25e9-49e6-a34c-9f7b79dfeb77',
                    name='Tommy Schmidt',
                ),
                total_amount=8736.81,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='baf91e50-6ef8-490a-94b4-75f16f56d385',
                            name='Earl Schoen',
                        ),
                        shared.TrackingCategoryRef(
                            id='c631b99e-26ce-4d8f-9fdb-9410f63bbf81',
                            name='Kay Frami',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='aperiam',
                        id='1afdd788-6241-489e-b448-73f5033f19db',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='25ce4152-eab9-4cd7-a522-4a6a0e123b78',
                        name='Tamara Terry',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='e1f67f3c-4cce-44b6-9769-6ff3c5747501',
                        name='Stacy Kovacek',
                    ),
                    shared.TrackingCategoryRef(
                        id='4f51f8b0-84c3-4197-a193-a245467f9487',
                        name='Rachael Corkery',
                    ),
                    shared.TrackingCategoryRef(
                        id='cc497223-3e66-4bd8-be5d-00b979ef2038',
                        name='Mrs. Gladys Collins',
                    ),
                ],
                unit_amount=155.63,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='ccc10964-0031-43b3-a504-4f65fe72dc40',
                    name='Miss Constance Shanahan',
                ),
                description='adipisci',
                discount_amount=9504.86,
                discount_percentage=2527.17,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='08efc15c-eb4d-46e1-aae0-f75aedf2acab',
                    name='Tracey Rodriguez',
                ),
                quantity=912.7,
                sub_total=7863.19,
                tax_amount=6004.71,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1535.13,
                    id='6ddb5894-61e7-4421-8be6-d9502f0ea930',
                    name='Hector Mayer',
                ),
                total_amount=6813.31,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='2f72f885-0090-4491-9608-207888ec6618',
                            name='Latoya West',
                        ),
                        shared.TrackingCategoryRef(
                            id='659eb40e-c16f-4af7-9b0b-532a4da37cba',
                            name='Tommie Gutkowski',
                        ),
                        shared.TrackingCategoryRef(
                            id='2c4842c9-b2ad-432d-afe8-1a88f4444573',
                            name='Alonzo Schmidt',
                        ),
                        shared.TrackingCategoryRef(
                            id='7353f63c-8209-4379-aa69-cd5fbcf79da1',
                            name='Blake Kuhic',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='eos',
                        id='bf95894e-6861-4adb-95f9-e5d751c9fe8f',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='02bfdc34-5084-41f1-b644-56379f3fb27e',
                        name='Stephanie Yundt',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='657b36fc-6b9f-4587-8e52-5c67641a8312',
                        name='Jerome Berge',
                    ),
                ],
                unit_amount=7303.7,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='cumque',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=7678.8,
                    total_amount=7149.33,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='423abcdc-91fa-4abd-988e-71f6c48252d7',
                        name='Delores Bosco',
                    ),
                    currency='EUR',
                    currency_rate=8719.69,
                    id='074009ef-8d29-4de1-9d70-97b5da08c57f',
                    note='id',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='cumque',
                    total_amount=4846.96,
                ),
            ),
        ],
        remaining_credit=5395.02,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.UNKNOWN,
        sub_total=991.6,
        supplemental_data=shared.SupplementalData(
            content={
                "accusamus": {
                    "excepturi": 'harum',
                },
                "laborum": {
                    "repudiandae": 'minus',
                    "officia": 'laboriosam',
                    "illo": 'cupiditate',
                    "veritatis": 'aliquam',
                },
            },
        ),
        total_amount=5682.31,
        total_discount=5410.46,
        total_tax_amount=1166.65,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=428.84,
                name='Sam Gerlach',
            ),
            shared.WithholdingTaxitems(
                amount=5497.1,
                name='Erick Bernhard DVM',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=997047,
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
    credit_note_id='voluptatem',
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
    query='dolor',
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
        additional_tax_amount=7194.5,
        additional_tax_percentage=3125.63,
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='neque',
        currency='USD',
        currency_rate=9281.02,
        customer_ref=shared.CustomerRef(
            company_name='numquam',
            id='aa868555-9667-432a-a5dc-b6682cb70f8c',
        ),
        discount_percentage=9497.96,
        id='d5fb6e91-b9a9-4f74-846e-2c3309db0536',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='e75ca006-f539-42c1-9a25-a8bf92f97428',
                    name='Al Mills',
                ),
                description='hic',
                discount_amount=5458.54,
                discount_percentage=7433.13,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='f8221125-359d-4983-87f7-a79cd72cd248',
                    name='Krystal Pagac IV',
                ),
                quantity=1794.33,
                sub_total=6090.79,
                tax_amount=9701.08,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1847.74,
                    id='ac41ef57-25f1-4169-ac1e-41d8a23c23e3',
                    name='Kristie Daugherty',
                ),
                total_amount=6505.38,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='a197f6de-9221-451f-a171-2099853e9f54',
                            name='Meredith Langosh',
                        ),
                        shared.TrackingCategoryRef(
                            id='439ee224-4604-443b-8154-188c2f56e85d',
                            name='Jessie Larkin',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='officiis',
                        id='abd617c3-b0d5-41a4-8bf0-1bad8706d460',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='bfbdc41f-f5d4-4e2a-a4fb-5cb35d17638f',
                        name='Delia Schuppe',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='359ecc5c-b860-4f8c-9580-ba73810e4fe4',
                        name='Megan Kling',
                    ),
                    shared.TrackingCategoryRef(
                        id='7cd3b1dd-3bbc-4e24-bb76-84eff50126d7',
                        name='Vicky Wolf',
                    ),
                    shared.TrackingCategoryRef(
                        id='d0eb74b8-4219-453b-84bd-3c43159d33e5',
                        name='Gordon Ernser Jr.',
                    ),
                ],
                unit_amount=1167.42,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='139863aa-41e6-4c31-8c2f-1fcb51c9a41f',
                    name='Rudy Waters',
                ),
                description='quidem',
                discount_amount=8383.74,
                discount_percentage=4379.79,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='95ee65e0-76cc-47ab-b616-ea5c71641934',
                    name='Tracy Bahringer',
                ),
                quantity=8851.03,
                sub_total=252.1,
                tax_amount=5776.72,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8573.88,
                    id='19d2fc2f-9e2e-4105-944b-935d237a72f9',
                    name='Mattie Gutkowski',
                ),
                total_amount=3849.39,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='ed4aecb7-537c-4d92-a2c9-ff57491aabfa',
                            name='Eula Kuhic DVM',
                        ),
                        shared.TrackingCategoryRef(
                            id='0ca4d456-ef10-431e-a899-f0c2001e22cd',
                            name='June Schmeler III',
                        ),
                        shared.TrackingCategoryRef(
                            id='84a184d7-6d97-41fc-820c-65b037bb8e0c',
                            name='Byron MacGyver V',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='molestiae',
                        id='e4de04af-28c5-4ddd-b46a-a1cfd6d828da',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='31911296-4664-45c1-981f-29042f569b7a',
                        name='Randal Altenwerth',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='216cbe07-1bc1-463e-a79a-3b084da99257',
                        name='Gary Gorczany',
                    ),
                ],
                unit_amount=572.07,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='847a742d-8449-46cb-9eec-f6b99bc63562',
                    name='Jonathon Zboncak',
                ),
                description='enim',
                discount_amount=3686.58,
                discount_percentage=7835.08,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='294c060b-06a1-4287-b64e-ef6d0c6d6ed9',
                    name='Arnold Dooley',
                ),
                quantity=4337.98,
                sub_total=2479.27,
                tax_amount=2855.44,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3419.34,
                    id='71509a8e-870d-43c5-a1f9-c242c7b66a1f',
                    name='Michelle Schmeler',
                ),
                total_amount=8150.46,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='5b671989-0f42-4a4b-b438-d85b260591d7',
                            name='Geraldine Von',
                        ),
                        shared.TrackingCategoryRef(
                            id='2059c9c3-f567-4e0e-a527-65b1d62fcdac',
                            name='Mr. Joe Wisozk',
                        ),
                        shared.TrackingCategoryRef(
                            id='16ce2239-e8f2-45cd-8d19-d959f439e392',
                            name='Gertrude Runte',
                        ),
                        shared.TrackingCategoryRef(
                            id='95f7aa2b-2411-4369-9d1e-6698fcc45962',
                            name='Minnie Schneider',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quam',
                        id='76763342-5403-48bf-b597-1e9819055738',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='edbac7fd-a395-494d-a6bc-2ae480632b99',
                        name='Hazel Renner',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='22063698-2855-43cb-9000-6bef4921ec20',
                        name='Robin Rempel',
                    ),
                    shared.TrackingCategoryRef(
                        id='9366ac8e-e0f2-4bf1-9588-d40d03f3deba',
                        name='Faye Kreiger',
                    ),
                    shared.TrackingCategoryRef(
                        id='3e90bc40-df86-48fd-9240-5cb331d492f4',
                        name='Douglas Denesik',
                    ),
                ],
                unit_amount=6941.48,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='saepe',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=1087.18,
                    total_amount=9623.97,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='8217978d-0acc-4a77-aeb7-b7021a52046b',
                        name='Michele Waelchi',
                    ),
                    currency='EUR',
                    currency_rate=7063.51,
                    id='0e67e094-fdfe-4d55-80ef-53a34a1b8fe9',
                    note='natus',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='dolorem',
                    total_amount=1243.81,
                ),
            ),
        ],
        remaining_credit=6824.3,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.VOID,
        sub_total=442.64,
        supplemental_data=shared.SupplementalData(
            content={
                "fugiat": {
                    "quis": 'fuga',
                    "eveniet": 'consequuntur',
                    "illum": 'delectus',
                },
                "rerum": {
                    "perferendis": 'maiores',
                    "harum": 'ratione',
                },
            },
        ),
        total_amount=5618.25,
        total_discount=4837.74,
        total_tax_amount=2521.83,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=5768.7,
                name='Desiree Ferry',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    credit_note_id='quis',
    force_update=False,
    timeout_in_minutes=431131,
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

