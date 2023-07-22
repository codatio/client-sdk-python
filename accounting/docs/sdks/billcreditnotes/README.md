# bill_credit_notes

## Overview

Bill credit notes

### Available Operations

* [create](#create) - Create bill credit note
* [get](#get) - Get bill credit note
* [get_create_update_model](#get_create_update_model) - Get create/update bill credit note model
* [list](#list) - List bill credit notes
* [update](#update) - Update bill credit note
* [upload_attachment](#upload_attachment) - Push invoice attachment

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
        currency='EUR',
        currency_rate=9654.17,
        discount_percentage=0,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='ba88f3a6-6997-4074-ba44-69b6e2141959',
                    name='Kirk Bartoletti',
                ),
                description='mollitia',
                discount_amount=3209.97,
                discount_percentage=4314.18,
                item_ref=shared.ItemRef(
                    id='3e2516fe-4c8b-4711-a5b7-fd2ed028921c',
                    name='Ervin Schoen',
                ),
                quantity=1399.72,
                sub_total=4071.83,
                tax_amount=332.22,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=691.67,
                    id='fb576b0d-5f0d-430c-9fbb-2587053202c7',
                    name='Eula Hegmann',
                ),
                total_amount=6082.53,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='90c28909-b3fe-449a-8d9c-bf48633323f9',
                            name='Adrian Kuhn',
                        ),
                        shared.TrackingCategoryRef(
                            id='a4100674-ebf6-4928-8d1b-a77a89ebf737',
                            name='Elbert Gislason I',
                        ),
                        shared.TrackingCategoryRef(
                            id='ce5e6a95-d8a0-4d44-ace2-af7a73cf3be4',
                            name='Florence Will',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='sit',
                        id='b326b5a7-3429-4cdb-9a84-22bb679d2322',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='5bf0cbb1-e31b-48b9-8f34-43a1108e0adc',
                        name='Alexander Prosacco',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='879fce95-3f73-4ef7-bbc7-abd74dd39c0f',
                        name='Freda Cormier',
                    ),
                ],
                unit_amount=9850.33,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='7c70a456-26d4-4368-93f1-6d9f5fce6c55',
                    name='Stephanie Gutkowski',
                ),
                description='consectetur',
                discount_amount=9262.13,
                discount_percentage=1324.87,
                item_ref=shared.ItemRef(
                    id='50fb008c-42e1-441a-ac36-6c8dd6b14429',
                    name='Minnie Gutkowski',
                ),
                quantity=4585.15,
                sub_total=4561.41,
                tax_amount=5245.93,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6832.82,
                    id='7bd466d2-8c10-4ab3-8dca-4251904e523c',
                    name='Sophie Bayer',
                ),
                total_amount=4908.19,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='78e4796f-2a70-4c68-8282-aa482562f222',
                            name='Ms. Marion Little',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='accusamus',
                        id='17cbe61e-6b7b-495b-80ab-3c20c4f3789f',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='71f99dd2-efd1-421a-a6f1-e674bdb04f15',
                        name='Ms. Dana Huel',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='68ea19f1-d170-4513-b9d0-8086a1840394',
                        name='Ms. Benjamin Hirthe DVM',
                    ),
                    shared.TrackingCategoryRef(
                        id='93f5f064-2dac-47af-915c-c413aa63aae8',
                        name='Chester Kuphal',
                    ),
                    shared.TrackingCategoryRef(
                        id='4dbb675f-d5e6-40b3-b5ed-4f6fbee41f33',
                        name='Heather Kuhn',
                    ),
                    shared.TrackingCategoryRef(
                        id='35b60eb1-ea42-4655-9ba3-c28744ed53b8',
                        name='Moses Douglas',
                    ),
                ],
                unit_amount=8672.9,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='8f5c0b2f-2fb7-4b19-8a27-6b26916fe1f0',
                    name='Emilio Goodwin',
                ),
                description='eius',
                discount_amount=8967.62,
                discount_percentage=2155.29,
                item_ref=shared.ItemRef(
                    id='698f447f-603e-48b4-85e8-0ca55efd20e4',
                    name='Ms. Pearl Towne',
                ),
                quantity=5106.29,
                sub_total=7400.98,
                tax_amount=3868.27,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6805.15,
                    id='89fbe3a5-aa8e-4482-8d0a-b4075088e518',
                    name='Jane Bailey',
                ),
                total_amount=9061.72,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='04f3b119-4b8a-4bf6-83a7-9f9dfe0ab7da',
                            name='Miss Hubert Hartmann',
                        ),
                        shared.TrackingCategoryRef(
                            id='187f86bc-173d-4689-aee9-526f8d986e88',
                            name='Delia Parisian',
                        ),
                        shared.TrackingCategoryRef(
                            id='f0e10125-63f9-44e2-9e97-3e922a57a15b',
                            name='Ms. Melvin Thiel IV',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quae',
                        id='7e2b6e3a-b884-45f0-997a-60ff2a54a31e',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='764a3e86-5e79-456f-9251-a5a9da660ff5',
                        name='Antoinette Wehner',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='4f9efc1b-4512-4c10-b264-8dc2f615199e',
                        name='Dr. Terrell Stanton',
                    ),
                    shared.TrackingCategoryRef(
                        id='fe6c632c-a3ae-4d01-9799-6312fde04771',
                        name='Tamara Lang',
                    ),
                    shared.TrackingCategoryRef(
                        id='61d01747-6360-4a15-9b6a-660659a1adea',
                        name='Wm Hane',
                    ),
                    shared.TrackingCategoryRef(
                        id='1d6c645b-08b6-4189-9baa-0fe1ade008e6',
                        name='Ian Schinner',
                    ),
                ],
                unit_amount=1905.67,
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
                    currency_rate=7706.75,
                    total_amount=8427.77,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='b5a34181-4301-4042-9813-d5208ece7e25',
                        name='Lula Kemmer',
                    ),
                    currency='GBP',
                    currency_rate=3494.4,
                    id='1c6c6e20-5e16-4dea-b3fe-c9578a645842',
                    note='ducimus',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='fuga',
                    total_amount=5140.54,
                ),
            ),
        ],
        remaining_credit=0,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "rem": {
                    "dicta": 'nisi',
                    "consequuntur": 'consectetur',
                    "aperiam": 'cupiditate',
                    "reiciendis": 'soluta',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='0929921a-efb9-4f58-84d8-6e68e4be0560',
            supplier_name='quasi',
        ),
        total_amount=805.78,
        total_discount=0,
        total_tax_amount=0,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=9785.48,
                name='Bobbie Stokes',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=364463,
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
    bill_credit_note_id='reprehenderit',
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
    query='est',
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
        currency='USD',
        currency_rate=8806.79,
        discount_percentage=0,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='ef66ef1c-aa33-483c-abeb-477373c8d72f',
                    name='Dr. Megan Spinka',
                ),
                description='architecto',
                discount_amount=9754.25,
                discount_percentage=1563.83,
                item_ref=shared.ItemRef(
                    id='c4310661-e963-449e-9cf9-e06e3a437000',
                    name='Clay Jast',
                ),
                quantity=7051.48,
                sub_total=8093.65,
                tax_amount=5960.65,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7090.36,
                    id='8f759eac-55a9-4741-9311-352965bb8a72',
                    name='Mr. Anne Kautzer',
                ),
                total_amount=2082.53,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='e139dbc2-259b-41ab-9a8c-070e1084cb06',
                            name='Miss Wanda Shanahan',
                        ),
                        shared.TrackingCategoryRef(
                            id='879eeb96-65b8-45ef-bd02-bae0be2d7822',
                            name='Natasha Wehner',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='similique',
                        id='4b5197f9-2443-4da7-8e52-b895c537c645',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='fb0b3489-6c3c-4a5a-8fbe-2fd570757792',
                        name='Peter Kuphal',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='ac646ecb-5734-409e-beb1-e5a2b12eb07f',
                        name='Joyce Howe',
                    ),
                    shared.TrackingCategoryRef(
                        id='99545fc9-5fa8-4897-8e18-9dbb30fcb33e',
                        name='Anthony Hayes',
                    ),
                    shared.TrackingCategoryRef(
                        id='197cd44e-2f52-4d82-9351-3bb6f48b656b',
                        name='Carroll Purdy',
                    ),
                    shared.TrackingCategoryRef(
                        id='ff2e4b27-537a-48cd-9e73-19c177d525f7',
                        name='Mrs. Pam Bins',
                    ),
                ],
                unit_amount=9025.81,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='b52ff785-fc37-4814-94c9-8e0c2bb89eb7',
                    name='Cristina Murphy',
                ),
                description='dolorem',
                discount_amount=4138.01,
                discount_percentage=7712.26,
                item_ref=shared.ItemRef(
                    id='600503d8-bb31-4180-b739-ae9e057eb809',
                    name='Mr. Craig Leannon',
                ),
                quantity=2244.13,
                sub_total=1242.89,
                tax_amount=9536.76,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2232.91,
                    id='981d4c70-0b60-47f3-893c-73b9da3f2ced',
                    name='Cody Terry',
                ),
                total_amount=9958.16,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='257411fa-f4b7-4544-a472-e802857a5b40',
                            name='Natalie Dooley',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='fugiat',
                        id='575f1400-e764-4ad7-b34e-c1b781b36a08',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='8d100efa-da20-40ef-8422-eb2164cf9ab8',
                        name='Beth Jenkins',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='3ffda9e0-6bee-4482-9c1f-c0e115c80bff',
                        name='Keith Lueilwitz',
                    ),
                ],
                unit_amount=2662.84,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='ec42defc-ce8f-4197-b773-e63562a7b408',
                    name='Steven Harris',
                ),
                description='facere',
                discount_amount=3071.73,
                discount_percentage=5525.81,
                item_ref=shared.ItemRef(
                    id='fdaf313a-1f5f-4d94-a59c-0b36f25ea944',
                    name='Travis Rempel',
                ),
                quantity=4031.47,
                sub_total=7917.62,
                tax_amount=688.8,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1081.65,
                    id='f6c37a51-2624-4383-9bbc-05a23a45cefc',
                    name='Ora Shields Jr.',
                ),
                total_amount=6339.82,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='ce2169e5-1001-49c6-9c5e-34762799bfbb',
                            name='Brent Mills',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='hic',
                        id='b2bb4eca-e6c3-4d5d-b3ad-ebd5daea4c50',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='8aa94c02-644c-4f5e-9d9a-4578adc1ac60',
                        name='Ernestine Turcotte Jr.',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='ac802e2e-c09f-4f8f-8f81-6ff3477c13e9',
                        name='Mrs. Phyllis Russel Sr.',
                    ),
                ],
                unit_amount=3576.39,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='b0960a66-8151-4a47-aaf9-23c5949f83f3',
                    name='Angela Schaefer',
                ),
                description='molestiae',
                discount_amount=3956.34,
                discount_percentage=9890.33,
                item_ref=shared.ItemRef(
                    id='fb901c6e-cbb4-4e24-bcf7-89ffafeda53e',
                    name='Brandi Turner',
                ),
                quantity=357.42,
                sub_total=6378.4,
                tax_amount=7701.28,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=978.96,
                    id='84c2b9c2-47c8-4837-ba40-e1942f32e550',
                    name='Lynn Kovacek',
                ),
                total_amount=9468.08,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='d56d0bd0-af2d-4fe1-bdb4-f62cba3f8941',
                            name='Erick Pfeffer MD',
                        ),
                        shared.TrackingCategoryRef(
                            id='80a6924d-3b2e-4cfc-88f8-95010f5dd3d6',
                            name='Shaun Bergnaum I',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='voluptates',
                        id='54c82f16-8a36-43c8-873e-484380b1f6b8',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='275a60a0-4c49-45cc-a991-71b51c1bdb1c',
                        name='Leroy Ratke',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='ebdfc4cc-ca99-4bc7-bc0b-2dce10873e42',
                        name='Brian Bartell',
                    ),
                    shared.TrackingCategoryRef(
                        id='678878ba-8581-4a58-a08c-54fefa9c95f2',
                        name='Angelo Runolfsdottir',
                    ),
                    shared.TrackingCategoryRef(
                        id='65d307cf-ee81-4206-a281-3fa4a41c480d',
                        name='Mr. Kristie Cole',
                    ),
                ],
                unit_amount=6854.67,
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
                    currency_rate=449.29,
                    total_amount=1341.73,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='d514f4cc-6f18-4bf9-a21a-6a4f77a87ee3',
                        name='Ray Prosacco',
                    ),
                    currency='USD',
                    currency_rate=1316.87,
                    id='c65b3441-8e3b-4b91-88d9-75e0e8419d8f',
                    note='deleniti',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='earum',
                    total_amount=1013.74,
                ),
            ),
        ],
        remaining_credit=0,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "maiores": {
                    "saepe": 'consequatur',
                },
                "esse": {
                    "facere": 'quisquam',
                    "cumque": 'aliquam',
                    "dolorum": 'deserunt',
                    "ad": 'reiciendis',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='3cabd905-a972-4e05-a728-227b2d309470',
            supplier_name='distinctio',
        ),
        total_amount=805.78,
        total_discount=0,
        total_tax_amount=0,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=4630.5,
                name='Tom Wintheiser',
            ),
            shared.WithholdingTaxitems(
                amount=4826.28,
                name='Jan Hirthe',
            ),
            shared.WithholdingTaxitems(
                amount=6750.58,
                name='Ora Okuneva',
            ),
            shared.WithholdingTaxitems(
                amount=2525.67,
                name='Preston Wyman DDS',
            ),
        ],
    ),
    bill_credit_note_id='sequi',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=125707,
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
        content='vitae'.encode(),
        request_body='voluptatibus',
    ),
    bill_credit_note_id='doloremque',
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

