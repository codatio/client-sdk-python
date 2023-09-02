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
        additional_tax_amount=5662.62,
        additional_tax_percentage=5345.33,
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='perspiciatis',
        currency='GBP',
        currency_rate=3581.57,
        customer_ref=shared.AccountingCustomerRef(
            company_name='ullam',
            id='7389cedb-ac7f-4da3-9594-d66bc2ae4806',
        ),
        discount_percentage=2099.2,
        id='2b9954b6-fa22-4063-a982-8553cb10006b',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='4921ec20-53b7-4493-a6ac-8ee0f2bf1958',
                    name='Dr. Irving Gislason I',
                ),
                description='reiciendis',
                discount_amount=2044.66,
                discount_percentage=8285.71,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='eba297be-3e90-4bc4-8df8-68fd52405cb3',
                    name='Evelyn Stracke',
                ),
                quantity=1574.21,
                sub_total=9699.11,
                tax_amount=2650.6,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9870.85,
                    id='127fb0e0-bf1f-4821-b978-d0acca77aeb7',
                    name='Erik Abbott MD',
                ),
                total_amount=3636.6,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='046b64e9-9fb0-4e67-a094-fdfed5540ef5',
                            name='Angie Flatley',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='quasi',
                        id='b8fe9973-1adc-405d-85ae-2dfb70fb3874',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='0d336561-eca1-46ef-8945-1bd76eeeb518',
                        name='Joel Senger DVM',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='accountTransaction',
                        id='d35512f0-6d4e-45b7-af0f-548568a0424e',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='0a1d6eb9-4346-445d-8308-4fbba5cceff5',
                        name='Dr. Malcolm Bauch',
                    ),
                ],
                unit_amount=3147.28,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='1e528a45-ac82-4b85-b8bc-2caba8da4127',
                    name='Drew Hickle',
                ),
                description='hic',
                discount_amount=9598.28,
                discount_percentage=2621.78,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='711aa1bc-74b8-46ce-8c74-f77b4848bd6a',
                    name='Darla Aufderhar',
                ),
                quantity=997.32,
                sub_total=8603.83,
                tax_amount=1859.83,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8035.05,
                    id='3b808094-373e-4060-859b-ebbad02f2586',
                    name='Mrs. Forrest Wilkinson',
                ),
                total_amount=3465.57,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='8daa95be-6cd0-4275-ac35-4aa432b47e17',
                            name='Cindy Schiller',
                        ),
                        shared.TrackingCategoryRef(
                            id='08c23e98-02d8-42f0-945e-b4a8b674ee5c',
                            name='Lucas Cartwright',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='assumenda',
                        id='c7f787e3-2e04-4b3d-bed0-c5670ef42bd3',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='f1cc503f-6c39-4bcd-8a62-90f957f38518',
                        name='Shannon Schuster',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='transfer',
                        id='807aae03-f33c-4a79-bb9d-e4032ba26fd3',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='8ba9216b-cb41-4583-9c73-641723133edc',
                        name='Juanita Kemmer',
                    ),
                    shared.TrackingCategoryRef(
                        id='5163bbca-4922-47c4-ac22-c55350495c5d',
                        name='Roderick Fisher',
                    ),
                ],
                unit_amount=4435.65,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='c1e4981e-8aa2-457d-9c19-12ebde64bfcc',
                    name='Megan Kertzmann',
                ),
                description='quaerat',
                discount_amount=133.69,
                discount_percentage=994.67,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='5dfa7962-06be-4f2b-8a3e-42c1aa010e9a',
                    name='Garrett Cassin',
                ),
                quantity=826.45,
                sub_total=2403.52,
                tax_amount=3369.7,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3367.21,
                    id='86d18f9f-97a4-4bfa-92bf-7d67ca84ad99',
                    name='Ray Botsford',
                ),
                total_amount=984.52,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='43531870-cf68-4b03-ad42-1bd43d1f0cb0',
                            name='Mrs. Brian Adams',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='facilis',
                        id='22d9b3a7-0d94-4faa-b41c-57d1fedc2050',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='8dc3ce18-5472-4f9e-a691-66a8be3444ea',
                        name='Clayton Reinger',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='journalEntry',
                        id='875c6c1f-e606-4d07-92a9-c87ae50c1666',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a1d9136a-7e8d-4532-93f3-f658752db764',
                        name='Dean Mayert MD',
                    ),
                ],
                unit_amount=3349.54,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='6cebcada-29ca-4791-81c9-5671663c530b',
                    name='Kristin Hudson III',
                ),
                description='dolor',
                discount_amount=6359.03,
                discount_percentage=2495.41,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='638512ab-2521-4b9f-ae07-2467b8a40bc0',
                    name='May Parisian PhD',
                ),
                quantity=3937.88,
                sub_total=3385.42,
                tax_amount=196.1,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9319.91,
                    id='df22a94d-20ec-490e-a41d-1f465e85156f',
                    name='Randal Kris',
                ),
                total_amount=8372.02,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='54fdd5ea-9543-4398-9afb-42a8d63388e4',
                            name='Casey Anderson',
                        ),
                        shared.TrackingCategoryRef(
                            id='ea5f9b18-a244-4fd6-9903-9dacd38ed0dc',
                            name='Tamara Borer',
                        ),
                        shared.TrackingCategoryRef(
                            id='7f1e3af1-5920-4c90-91b4-901f2bd89c8a',
                            name='Wanda Kassulke',
                        ),
                        shared.TrackingCategoryRef(
                            id='da5b7b69-02b8-481a-94f6-43664a8f0af8',
                            name='Dr. Edgar Mosciski',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='dolor',
                        id='2d9fbaf9-476a-42ae-8dcc-50c8a3512c73',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='48930750-a00e-4966-ac73-6d43194398c7',
                        name='Curtis Rosenbaum',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='journalEntry',
                        id='98ed3d3a-b7ca-43c5-8a86-49a70cfd5d69',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='9b720645-1077-4d19-aa83-d492ed14b8a2',
                        name='Ralph Marquardt',
                    ),
                    shared.TrackingCategoryRef(
                        id='545e955d-cc18-45ea-8901-c7c43ad2daa7',
                        name='Troy Murphy',
                    ),
                    shared.TrackingCategoryRef(
                        id='3d230edf-7381-41a1-9538-2bd7ed565076',
                        name='Christine Sauer',
                    ),
                ],
                unit_amount=9851.55,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='nulla',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=3759.62,
                    total_amount=3441.48,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='64c20a07-11a9-461d-a4a7-dbb8f532d892',
                        name='Amos Kshlerin Sr.',
                    ),
                    currency='EUR',
                    currency_rate=7206.43,
                    id='512c8782-40bf-4548-b88f-8f1bf0bc8e1f',
                    note='dolores',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='eum',
                    total_amount=8596.04,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=5581.38,
                    total_amount=1927.18,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='1d008109-0f67-4066-b3f3-a681c5768dce',
                        name='Gail Christiansen V',
                    ),
                    currency='USD',
                    currency_rate=1374.14,
                    id='15e08601-489a-45f6-be3a-f3dd9dda33dc',
                    note='pariatur',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='non',
                    total_amount=2799.65,
                ),
            ),
        ],
        remaining_credit=5083.73,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.PARTIALLY_PAID,
        sub_total=2523.23,
        supplemental_data=shared.SupplementalData(
            content={
                "esse": {
                    "natus": 'quas',
                    "saepe": 'modi',
                    "assumenda": 'maiores',
                },
                "neque": {
                    "debitis": 'quaerat',
                    "nostrum": 'libero',
                },
                "totam": {
                    "veniam": 'nostrum',
                    "facere": 'aliquam',
                    "vitae": 'ipsum',
                },
            },
        ),
        total_amount=9233.27,
        total_discount=784.86,
        total_tax_amount=2180.93,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=2578.35,
                name='Mr. Todd Feil',
            ),
            shared.WithholdingTaxitems(
                amount=189.01,
                name='Karla Schumm',
            ),
            shared.WithholdingTaxitems(
                amount=2666.43,
                name='Charles McGlynn',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=874446,
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
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreditNoteRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    credit_note_id='nihil',
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
from codataccounting.models import operations, shared

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
from codataccounting.models import operations, shared

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
    query='velit',
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
        additional_tax_amount=2769.16,
        additional_tax_percentage=9539.59,
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='consequuntur',
        currency='GBP',
        currency_rate=2532.61,
        customer_ref=shared.AccountingCustomerRef(
            company_name='excepturi',
            id='d86f4bb2-0fe5-4d91-9cbf-e749caf45a27',
        ),
        discount_percentage=9648.57,
        id='69e2c9e6-d10e-49db-bad4-c6b03108d9c3',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='473082b9-4f2a-4b1f-9567-1e9c326350a4',
                    name='Tanya Braun',
                ),
                description='nihil',
                discount_amount=5004.45,
                discount_percentage=6160.39,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='ce0e9915-94d9-43a7-8c02-52fe3b4b4db8',
                    name='Lance Kilback',
                ),
                quantity=7170.18,
                sub_total=7252.47,
                tax_amount=3909.37,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8879.8,
                    id='1d2cf502-bafb-42cb-8463-5d5e65da028c',
                    name='Sophia Marvin MD',
                ),
                total_amount=847.08,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='30fda966-489d-47b7-8673-e13a12a6b992',
                            name='Katrina Grimes',
                        ),
                        shared.TrackingCategoryRef(
                            id='4487f5c8-4383-46b8-ab3c-df6415b0449f',
                            name='Mr. Marcos Windler',
                        ),
                        shared.TrackingCategoryRef(
                            id='4eedbe78-bf60-4682-9894-ea763d5c7279',
                            name='Lula Koepp',
                        ),
                        shared.TrackingCategoryRef(
                            id='148d6d54-9e56-435b-b3bc-0f970c42fc9f',
                            name='Lena Green Sr.',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='veniam',
                        id='e75b7960-65c0-4efa-af93-b90a1b8c95be',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='54b739f4-fe77-4210-91f6-558c99c722d2',
                        name='Lucas Barton',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='invoice',
                        id='087d9caa-e042-4dd7-8aac-9b4caa1cfe9e',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='5df90390-7f37-4831-983d-42e54a854665',
                        name='Tyrone Ruecker Sr.',
                    ),
                ],
                unit_amount=2138.71,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='3c1471d5-1aaa-46dd-b5ab-d6487c5fc2b8',
                    name='Mr. Kelly Orn',
                ),
                description='saepe',
                discount_amount=9832.72,
                discount_percentage=4228.23,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='9e100157-630b-4da7-afde-d84a35a41238',
                    name='Walter Nitzsche',
                ),
                quantity=3217.24,
                sub_total=6847.17,
                tax_amount=7905.34,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1866.88,
                    id='6ae33bef-971a-48f4-abca-1106fe965b71',
                    name='Meredith Barrows',
                ),
                total_amount=9475.73,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='8ec9f7b9-9a55-40a6-96ed-333bb0ce8aa6',
                            name='Pauline Feeney',
                        ),
                        shared.TrackingCategoryRef(
                            id='986eb7e1-4ca5-4640-8915-0097019a48f8',
                            name='Darin Ryan',
                        ),
                        shared.TrackingCategoryRef(
                            id='bf904e01-105d-4389-8816-2c6beb68a0f6',
                            name='Jo Pouros',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='alias',
                        id='3a1480f8-de30-4f06-9d81-0618d97e1522',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='510da803-1229-42cc-a1c2-a702bb97ee10',
                        name='Ginger O'Reilly',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='transfer',
                        id='35f8e01b-f33e-4aab-8540-2ac1704bf1cc',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='fc61aae5-eb5f-40c4-92b5-744d08a2267a',
                        name='Sheldon Toy',
                    ),
                    shared.TrackingCategoryRef(
                        id='e3c71ad3-1bec-4b83-9237-8ae3bfc23d94',
                        name='Sarah Okuneva',
                    ),
                    shared.TrackingCategoryRef(
                        id='6a495bac-707f-406b-a8ec-c86492386f62',
                        name='Wade Kemmer',
                    ),
                ],
                unit_amount=2765.07,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='quod',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=5109.78,
                    total_amount=5207.16,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='90a3fd3c-81da-410f-8c23-df931da3edb5',
                        name='Winifred O'Reilly',
                    ),
                    currency='GBP',
                    currency_rate=6313.52,
                    id='cc943513-7726-4d15-b21b-832a56d69180',
                    note='hic',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='iure',
                    total_amount=84.69,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=5778.54,
                    total_amount=6825.06,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='6658e69a-4b84-43d3-82db-ec75c68c6065',
                        name='Tom Homenick',
                    ),
                    currency='EUR',
                    currency_rate=2073.26,
                    id='04d8849b-f821-44c3-b7f9-6bb0c69e372d',
                    note='libero',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='non',
                    total_amount=2896.81,
                ),
            ),
        ],
        remaining_credit=2774.88,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.PAID,
        sub_total=6213.54,
        supplemental_data=shared.SupplementalData(
            content={
                "reprehenderit": {
                    "est": 'quis',
                    "impedit": 'accusantium',
                    "necessitatibus": 'facere',
                },
                "reprehenderit": {
                    "officia": 'soluta',
                    "suscipit": 'explicabo',
                    "recusandae": 'unde',
                },
                "iusto": {
                    "ea": 'architecto',
                },
                "earum": {
                    "alias": 'quod',
                    "veniam": 'corrupti',
                    "temporibus": 'odit',
                },
            },
        ),
        total_amount=4514.48,
        total_discount=7493.43,
        total_tax_amount=3483.86,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=5878.17,
                name='Ruben Rice',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    credit_note_id='modi',
    force_update=False,
    timeout_in_minutes=711732,
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

