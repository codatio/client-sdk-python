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
        additional_tax_amount=6522.45,
        additional_tax_percentage=2425.82,
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='est',
        currency='GBP',
        currency_rate=7021.83,
        customer_ref=shared.CustomerRef(
            company_name='blanditiis',
            id='fe99731a-dc05-4d85-ae2d-fb70fb387429',
        ),
        discount_percentage=101.8,
        id='d336561e-ca16-4ef8-9451-bd76eeeb518c',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='a1fad355-12f0-46d4-a5b7-2f0f548568a0',
                    name='Bonnie Greenfelder Jr.',
                ),
                description='officia',
                discount_amount=1009.76,
                discount_percentage=8459.84,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='6eb94346-45d0-4308-8fbb-a5cceff5cb01',
                    name='Dr. Rogelio Haley',
                ),
                quantity=1344.12,
                sub_total=5425.06,
                tax_amount=6556.94,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2635.77,
                    id='5ac82b85-f8bc-42ca-ba8d-a4127dd597ff',
                    name='Miss Joy Boyer',
                ),
                total_amount=909.26,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='c74b86ce-cc74-4f77-b484-8bd6a6f0441d',
                            name='Jody Dickens',
                        ),
                        shared.TrackingCategoryRef(
                            id='08094373-e060-4459-bebb-ad02f2586bcf',
                            name='Holly Dare',
                        ),
                        shared.TrackingCategoryRef(
                            id='8daa95be-6cd0-4275-ac35-4aa432b47e17',
                            name='Cindy Schiller',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='alias',
                        id='8c23e980-2d82-4f0d-85eb-4a8b674ee5cf',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='8edc7f78-7e32-4e04-b3d3-ed0c5670ef42',
                        name='Clint Ernser',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='transfer',
                        id='1cc503f6-c39b-4cd0-a629-0f957f385189',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='d7ef807a-ae03-4f33-8a79-fb9de4032ba2',
                        name='Jeannie Smith',
                    ),
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
                    customer_ref=shared.CustomerRef(
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
                    customer_ref=shared.CustomerRef(
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
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='4d739656-4c20-4a07-91a9-61d24a7dbb8f',
                    name='Shannon Cremin',
                ),
                description='perspiciatis',
                discount_amount=1421.56,
                discount_percentage=7540.53,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='f7812cb5-12c8-4782-80bf-548f88f8f1bf',
                    name='Hannah Schmidt',
                ),
                quantity=1202.57,
                sub_total=9822.77,
                tax_amount=1756.76,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=195.51,
                    id='6d5d831d-0081-4090-b670-6673f3a681c5',
                    name='Vera Kutch',
                ),
                total_amount=9328.07,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='42409a21-5e08-4601-889a-5f63e3af3dd9',
                            name='Marty Nikolaus',
                        ),
                        shared.TrackingCategoryRef(
                            id='dcd63483-e4a7-4a98-a4df-37e45b8955d4',
                            name='Mrs. Tracy Walker',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='numquam',
                        id='82310907-bd35-44c0-92bd-734f02449d86',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='bb20fe5d-911c-4bfe-b49c-af45a27f69e2',
                        name='Tracy Weber',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='journalEntry',
                        id='0e9db3ad-4c6b-4031-88d9-c337473082b9',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='f2ab1fd5-671e-49c3-a635-0a467143789c',
                        name='William Walker',
                    ),
                    shared.TrackingCategoryRef(
                        id='1594d93a-74c0-4252-be3b-4b4db8b778eb',
                        name='Dr. Ramon Towne',
                    ),
                ],
                unit_amount=7725.93,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='ad',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=6732.9,
                    total_amount=9436.82,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='b2cbc463-5d5e-465d-a028-c3e951a1e30f',
                        name='Doug Marquardt',
                    ),
                    currency='GBP',
                    currency_rate=5226.16,
                    id='9d7b7867-3e13-4a12-a6b9-92494594487f',
                    note='veniam',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='praesentium',
                    total_amount=2852.56,
                ),
            ),
        ],
        remaining_credit=2293.64,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.DRAFT,
        sub_total=4060.7,
        supplemental_data=shared.SupplementalData(
            content={
                "rem": {
                    "harum": 'consectetur',
                    "quisquam": 'nulla',
                },
                "a": {
                    "dolore": 'dicta',
                    "minima": 'facilis',
                },
                "sit": {
                    "magnam": 'molestias',
                    "hic": 'error',
                },
            },
        ),
        total_amount=8334,
        total_discount=9625.75,
        total_tax_amount=1189.86,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=9646.4,
                name='Gretchen Waters',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=923982,
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
    credit_note_id='in',
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
    query='deleniti',
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
        additional_tax_amount=7347.74,
        additional_tax_percentage=9709.57,
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='sit',
        currency='USD',
        currency_rate=5624.3,
        customer_ref=shared.CustomerRef(
            company_name='quia',
            id='5894ea76-3d5c-4727-95b7-85148d6d549e',
        ),
        discount_percentage=3248.72,
        id='635b33bc-0f97-40c4-afc9-f4844225e75b',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='6065c0ef-a6f9-43b9-8a1b-8c95be1254b7',
                    name='Ramona Wisoky',
                ),
                description='eveniet',
                discount_amount=4855.06,
                discount_percentage=4518.47,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='210d1f65-58c9-49c7-a2d2-bc0f94087d9c',
                    name='Mrs. Gerard Walter',
                ),
                quantity=8445.66,
                sub_total=8404.68,
                tax_amount=4522.21,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8119.81,
                    id='aac9b4ca-a1cf-4e9e-95df-903907f37831',
                    name='Isaac Dickinson',
                ),
                total_amount=1409.72,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='54a85466-597c-4502-b3c1-471d51aaa6dd',
                            name='Corey Pacocha',
                        ),
                        shared.TrackingCategoryRef(
                            id='6487c5fc-2b86-42a0-8bef-69e100157630',
                            name='Taylor Paucek',
                        ),
                        shared.TrackingCategoryRef(
                            id='fded84a3-5a41-4238-a1a7-35ac26ae33be',
                            name='Miss Terrence Kulas',
                        ),
                        shared.TrackingCategoryRef(
                            id='f46bca11-06fe-4965-b711-d08cf88ec9f7',
                            name='Freddie Mayert',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quis',
                        id='0a656ed3-33bb-40ce-8aa6-5432a986eb7e',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='ca564089-1500-4970-99a4-8f88ece7bf90',
                        name='Mr. Kerry Adams II',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='transfer',
                        id='38908162-c6be-4b68-a0f6-57b7d03a1480',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='8de30f06-9d81-4061-8d97-e152297510da',
                        name='Mr. Kenneth Fay',
                    ),
                    shared.TrackingCategoryRef(
                        id='92cc61c2-a702-4bb9-bee1-02da2de35f8e',
                        name='Diane Rempel',
                    ),
                    shared.TrackingCategoryRef(
                        id='3eaab454-02ac-4170-8bf1-cc9fc61aae5e',
                        name='Miss Jon Willms',
                    ),
                    shared.TrackingCategoryRef(
                        id='92b5744d-08a2-4267-aaee-79e3c71ad31b',
                        name='Benny Raynor',
                    ),
                ],
                unit_amount=8588.02,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='2378ae3b-fc23-4d94-90a9-86a495bac707',
                    name='Timothy Jaskolski',
                ),
                description='laudantium',
                discount_amount=9219.81,
                discount_percentage=7954.89,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='c8649238-6f62-4c96-9c4c-c6b78890a3fd',
                    name='Dr. Kara Lowe',
                ),
                quantity=1194.73,
                sub_total=207.35,
                tax_amount=9901.69,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5342.04,
                    id='c23df931-da3e-4db5-9fad-94acc9435137',
                    name='Sara Jast II',
                ),
                total_amount=2426.06,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='1b832a56-d691-480f-b60e-b9a6658e69a4',
                            name='Jimmie Grady',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='adipisci',
                        id='82dbec75-c68c-4606-9946-8ce304d8849b',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='214c337f-96bb-40c6-9e37-2db1344ba9f7',
                        name='Ernesto Heaney PhD',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='transfer',
                        id='7aab62e9-7261-4fb0-858d-27b51996b5b4',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='50eef712-b7a7-4ab0-b44b-1710688deebe',
                        name='Wallace Medhurst',
                    ),
                    shared.TrackingCategoryRef(
                        id='3dd0ccd3-3f11-4b3e-8e08-0aa104186ec7',
                        name='Mr. Sherri Torphy',
                    ),
                    shared.TrackingCategoryRef(
                        id='3702c5c8-e2d3-40ea-9310-4fa44707bf37',
                        name='Jeannette Graham',
                    ),
                ],
                unit_amount=5596.68,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='2821fdb2-f69e-4592-a7c7-1cc8d3cd4258',
                    name='Anthony Fahey',
                ),
                description='laborum',
                discount_amount=5588.69,
                discount_percentage=1387.08,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='c808fe27-51a2-4047-8044-9e143f9619bb',
                    name='Dr. Estelle Goyette',
                ),
                quantity=6731.58,
                sub_total=640.7,
                tax_amount=641.84,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9726.54,
                    id='a436e625-9233-4f95-89d2-37397c785b5d',
                    name='Miguel Wuckert Jr.',
                ),
                total_amount=1104.36,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='3febdf67-6b72-406d-ab75-0052a5647edc',
                            name='Annie Morissette',
                        ),
                        shared.TrackingCategoryRef(
                            id='8c4320f4-1240-4d44-87ac-693b94c3b9d2',
                            name='Leah Kuvalis',
                        ),
                        shared.TrackingCategoryRef(
                            id='95aa42fc-4056-469f-a9a0-06d212494508',
                            name='Natasha Stark',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='ipsum',
                        id='b1b41844-060e-4003-90d0-23dc901f5afd',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='6c44846a-e9d8-4925-bc89-62f4896bf51e',
                        name='Eileen Hegmann',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='journalEntry',
                        id='c343d617-78af-4491-a477-25e621909e91',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='44a5de59-ac77-4066-b0cf-1cf593260525',
                        name='Elvira Jacobson',
                    ),
                ],
                unit_amount=7414,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='quia',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=4937.34,
                    total_amount=8134.63,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='99a2d335-670e-493e-a6cf-59f358aaeaca',
                        name='Philip Crooks',
                    ),
                    currency='GBP',
                    currency_rate=799.07,
                    id='bf7ba1cc-9771-46c8-82cc-9e0c7d9d323f',
                    note='quae',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='est',
                    total_amount=4209.27,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=8610.9,
                    total_amount=5823.51,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='cf1c856b-cba5-41ef-a454-a47facf116cd',
                        name='Jorge Grady',
                    ),
                    currency='USD',
                    currency_rate=4413.58,
                    id='562873c7-dd9e-4faf-83dc-623620f3138f',
                    note='nesciunt',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='at',
                    total_amount=9458.52,
                ),
            ),
        ],
        remaining_credit=1945.26,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.VOID,
        sub_total=224.79,
        supplemental_data=shared.SupplementalData(
            content={
                "aspernatur": {
                    "similique": 'id',
                    "exercitationem": 'commodi',
                    "nostrum": 'delectus',
                    "quidem": 'rem',
                },
            },
        ),
        total_amount=9947.56,
        total_discount=3840.74,
        total_tax_amount=3327.12,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=9230.44,
                name='Pete Metz',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    credit_note_id='praesentium',
    force_update=False,
    timeout_in_minutes=249962,
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

