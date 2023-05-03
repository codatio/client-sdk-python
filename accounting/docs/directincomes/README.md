# direct_incomes

## Overview

Direct incomes

### Available Operations

* [create](#create) - Create direct income
* [download_attachment](#download_attachment) - Download direct income attachment
* [get](#get) - Get direct income
* [get_attachment](#get_attachment) - Get direct income attachment
* [get_create_model](#get_create_model) - Get create direct income model
* [list](#list) - List direct incomes
* [list_attachments](#list_attachments) - List direct income attachments
* [upload_attachment](#upload_attachment) - Create direct income attachment

## create

Posts a new direct income to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create direct income model](https://docs.codat.io/accounting-api#/operations/get-create-directIncomes-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateDirectIncomeRequest(
    direct_income=shared.DirectIncome(
        contact_ref=shared.ContactRef(
            data_type='amet',
            id='d5c72795-b785-4148-96d5-49e5635b33bc',
        ),
        currency='voluptatem',
        currency_rate=9791.61,
        id='970c42fc-9f48-4442-a5e7-5b796065c0ef',
        issue_date='culpa',
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='f93b90a1-b8c9-45be-9254-b739f4fe7721',
                    name='Muriel Carroll',
                ),
                description='exercitationem',
                discount_amount=3381.01,
                discount_percentage=5546.44,
                item_ref=shared.ItemRef(
                    id='c99c722d-2bc0-4f94-887d-9caae042dd7c',
                    name='Carlton Schowalter',
                ),
                quantity=2667.52,
                sub_total=7955.01,
                tax_amount=6633.35,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6360.7,
                    id='1cfe9e15-df90-4390-bf37-831983d42e54',
                    name='Ken Herzog',
                ),
                total_amount=4168.84,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='97c50233-c147-41d5-9aaa-6ddf5abd6487',
                        name='Bill Wisoky',
                    ),
                    shared.TrackingCategoryRef(
                        id='b862a00b-ef69-4e10-8157-630bda7afded',
                        name='Eddie Murazik',
                    ),
                ],
                unit_amount=6774.73,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='41238e1a-735a-4c26-ae33-bef971a8f46b',
                    name='Mr. Angelo Brakus',
                ),
                description='delectus',
                discount_amount=8871.37,
                discount_percentage=6076.72,
                item_ref=shared.ItemRef(
                    id='65b711d0-8cf8-48ec-9f7b-99a550a656ed',
                    name='Paula Frami',
                ),
                quantity=375.63,
                sub_total=7773.99,
                tax_amount=8863.66,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5147.78,
                    id='aa65432a-986e-4b7e-94ca-564089150097',
                    name='Catherine Mitchell',
                ),
                total_amount=5264.96,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='88ece7bf-904e-4011-85d3-8908162c6beb',
                        name='Dr. Mattie Nader',
                    ),
                    shared.TrackingCategoryRef(
                        id='57b7d03a-1480-4f8d-a30f-069d810618d9',
                        name='Alyssa Casper',
                    ),
                    shared.TrackingCategoryRef(
                        id='297510da-8031-4229-acc6-1c2a702bb97e',
                        name='Carl Batz',
                    ),
                    shared.TrackingCategoryRef(
                        id='a2de35f8-e01b-4f33-aaab-45402ac1704b',
                        name='Justin Schmitt',
                    ),
                ],
                unit_amount=9890.79,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='maxime',
        note='ex',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='deserunt',
                    currency='laborum',
                    currency_rate=9299.41,
                    total_amount=3241.51,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='eb5f0c49-2b57-444d-88a2-267aaee79e3c',
                        name='Martha Orn',
                    ),
                    currency='et',
                    currency_rate=7321.72,
                    id='ecb83d23-78ae-43bf-823d-9450a986a495',
                    note='cum',
                    paid_on_date='dolorum',
                    reference='quod',
                    total_amount=4715.35,
                ),
            ),
        ],
        reference='quae',
        source_modified_date='ducimus',
        sub_total=9483.77,
        supplemental_data=shared.SupplementalData(
            content={
                "ex": {
                    "magni": 'laudantium',
                    "repudiandae": 'minus',
                    "porro": 'atque',
                },
            },
        ),
        tax_amount=4203.54,
        total_amount=2588.07,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=599915,
)

res = s.direct_incomes.create(req)

if res.create_direct_income_response is not None:
    # handle response
```

## download_attachment

Downloads an attachment for the specified direct income for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadDirectIncomeAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.direct_incomes.download_attachment(req)

if res.data is not None:
    # handle response
```

## get

Gets the specified direct income for a given company and connection.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDirectIncomeRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='sunt',
)

res = s.direct_incomes.get(req)

if res.direct_income is not None:
    # handle response
```

## get_attachment

Gets the specified direct income attachment for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDirectIncomeAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    timeout_in_minutes=226197,
)

res = s.direct_incomes.get_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_create_model

Get create direct income model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateDirectIncomesModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.direct_incomes.get_create_model(req)

if res.push_option is not None:
    # handle response
```

## list

Lists the direct incomes for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListDirectIncomesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='laudantium',
)

res = s.direct_incomes.list(req)

if res.direct_incomes is not None:
    # handle response
```

## list_attachments

Gets all attachments for the specified direct income for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListDirectIncomeAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.direct_incomes.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## upload_attachment

Posts a new direct income attachment for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UploadDirectIncomeAttachmentRequest(
    request_body=operations.UploadDirectIncomeAttachmentRequestBody(
        content='commodi'.encode(),
        request_body='a',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='aliquid',
)

res = s.direct_incomes.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
