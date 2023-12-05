# CreditNotes
(*credit_notes*)

## Overview

Credit notes

### Available Operations

* [create](#create) - Create credit note
* [get](#get) - Get credit note
* [get_create_update_model](#get_create_update_model) - Get create/update credit note model
* [list](#list) - List credit notes
* [update](#update) - Update credit note

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
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateCreditNoteRequest(
    credit_note=shared.CreditNote(
        allocated_on_date='2022-10-23T00:00:00.000Z',
        currency='USD',
        customer_ref=shared.AccountingCustomerRef(
            id='<ID>',
        ),
        discount_percentage=Decimal('6384.24'),
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(),
                item_ref=shared.ItemRef(
                    id='<ID>',
                ),
                quantity=Decimal('4174.58'),
                tax_rate_ref=shared.TaxRateRef(),
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='<ID>',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        id='<ID>',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='<ID>',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='transfer',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='<ID>',
                    ),
                ],
                unit_amount=Decimal('690.25'),
            ),
        ],
        metadata=shared.Metadata(),
        modified_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.PaymentAllocationItems(
                allocation=shared.Allocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(),
                    currency='EUR',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                ),
            ),
        ],
        remaining_credit=Decimal('0.86'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.DRAFT,
        sub_total=Decimal('3015.1'),
        supplemental_data=shared.SupplementalData(
            content={
                'key': {
                    'key': 'string',
                },
            },
        ),
        total_amount=Decimal('899.64'),
        total_discount=Decimal('7150.4'),
        total_tax_amount=Decimal('7926.2'),
        withholding_tax=[
            shared.WithholdingTaxItems(
                amount=Decimal('8559.52'),
                name='string',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.credit_notes.create(req)

if res.create_credit_note_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCreditNoteRequest](../../models/operations/createcreditnoterequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.CreateCreditNoteResponse](../../models/operations/createcreditnoteresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |

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
    credit_note_id='string',
)

res = s.credit_notes.get(req)

if res.credit_note is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCreditNoteRequest](../../models/operations/getcreditnoterequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.GetCreditNoteResponse](../../models/operations/getcreditnoteresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |

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
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetCreateUpdateCreditNotesModelRequest](../../models/operations/getcreateupdatecreditnotesmodelrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |


### Response

**[operations.GetCreateUpdateCreditNotesModelResponse](../../models/operations/getcreateupdatecreditnotesmodelresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 400-600                     | */*                         |

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
)

res = s.credit_notes.list(req)

if res.credit_notes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListCreditNotesRequest](../../models/operations/listcreditnotesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |


### Response

**[operations.ListCreditNotesResponse](../../models/operations/listcreditnotesresponse.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.ErrorMessage                 | 400,401,402,403,404,409,429,500,503 | application/json                    |
| errors.SDKError                     | 400-600                             | */*                                 |

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
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateCreditNoteRequest(
    credit_note=shared.CreditNote(
        allocated_on_date='2022-10-23T00:00:00.000Z',
        currency='GBP',
        customer_ref=shared.AccountingCustomerRef(
            id='<ID>',
        ),
        discount_percentage=Decimal('5971.29'),
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(),
                item_ref=shared.ItemRef(
                    id='<ID>',
                ),
                quantity=Decimal('3446.2'),
                tax_rate_ref=shared.TaxRateRef(),
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='<ID>',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        id='<ID>',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='<ID>',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='invoice',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='<ID>',
                    ),
                ],
                unit_amount=Decimal('6276.9'),
            ),
        ],
        metadata=shared.Metadata(),
        modified_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.PaymentAllocationItems(
                allocation=shared.Allocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(),
                    currency='EUR',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                ),
            ),
        ],
        remaining_credit=Decimal('540.62'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.PARTIALLY_PAID,
        sub_total=Decimal('4995.57'),
        supplemental_data=shared.SupplementalData(
            content={
                'key': {
                    'key': 'string',
                },
            },
        ),
        total_amount=Decimal('4468.63'),
        total_discount=Decimal('3691.82'),
        total_tax_amount=Decimal('3115.07'),
        withholding_tax=[
            shared.WithholdingTaxItems(
                amount=Decimal('7884.4'),
                name='string',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    credit_note_id='string',
)

res = s.credit_notes.update(req)

if res.update_credit_note_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateCreditNoteRequest](../../models/operations/updatecreditnoterequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.UpdateCreditNoteResponse](../../models/operations/updatecreditnoteresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |
