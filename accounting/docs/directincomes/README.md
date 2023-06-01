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

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) to see which integrations support this endpoint.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateDirectIncomeRequest(
    direct_income=shared.DirectIncome(
        contact_ref=shared.ContactRef(
            data_type='veniam',
            id='118c2cc5-7fbd-460b-9a78-ed29a9d4eea8',
        ),
        currency='ullam',
        currency_rate=3917.15,
        id='58c2d4f4-c88b-4e4f-a78f-d9667e46c51d',
        issue_date='dolores',
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='faa58dce-f234-4c95-9b9b-df2190abd9bb',
                    name='Delbert Cummerata',
                ),
                description='ullam',
                discount_amount=9045.07,
                discount_percentage=7703.76,
                item_ref=shared.ItemRef(
                    id='2659ce02-8084-40c6-9ef6-8e45c8addfac',
                    name='Bernice Gottlieb Jr.',
                ),
                quantity=3079.36,
                sub_total=2029.21,
                tax_amount=462.58,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7597.31,
                    id='6632b439-1fdf-401c-be91-e8f7bc69d460',
                    name='Tyrone Kuhn',
                ),
                total_amount=9053.64,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='26d10f1e-f263-41c7-80f0-f873f9d5c25f',
                        name='Miss Alfred VonRueden',
                    ),
                    shared.TrackingCategoryRef(
                        id='a4a4253c-3025-4711-b42c-7e7dc548be09',
                        name='Bradley Boyle',
                    ),
                    shared.TrackingCategoryRef(
                        id='a215ca12-a4ba-49d5-9988-192cfd0c77c5',
                        name='Meghan Koelpin',
                    ),
                ],
                unit_amount=8136.42,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='4ee6e8b9-0bac-4384-a239-6703fec31c50',
                    name='Shawn Gulgowski IV',
                ),
                description='perspiciatis',
                discount_amount=6461.08,
                discount_percentage=2236.36,
                item_ref=shared.ItemRef(
                    id='6a6b2d27-eb70-47aa-a0c8-fe46e6177db9',
                    name='Dominic Ernser',
                ),
                quantity=508.59,
                sub_total=9759.09,
                tax_amount=9767,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7372.75,
                    id='b6970ee7-70e3-4609-bef7-c206e61b0d30',
                    name='Kelly Blick',
                ),
                total_amount=1644.32,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a3d98637-ca85-4c3f-a655-74dbaf94a7c9',
                        name='Randal Blanda',
                    ),
                ],
                unit_amount=9616.33,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='28db2cf2-bf4f-43de-9356-d7e14b21cd98',
                    name='Faye Jacobi',
                ),
                description='quis',
                discount_amount=6606.91,
                discount_percentage=9651.45,
                item_ref=shared.ItemRef(
                    id='69a1c4b7-9ae3-4368-9c23-c39a7c0e17cb',
                    name='Jacqueline Russel',
                ),
                quantity=6321.21,
                sub_total=5137.34,
                tax_amount=1478.83,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3588.82,
                    id='fe22cd5c-ba6f-4bfe-8932-af6813d65bfe',
                    name='Elbert Schmidt',
                ),
                total_amount=8717.9,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='916f7fc7-dda7-40ec-a0e6-075894d61c14',
                        name='Mr. Irving Mann',
                    ),
                    shared.TrackingCategoryRef(
                        id='7e37c0d9-77f1-4a54-91ab-e9751b106d23',
                        name='Kenneth Effertz',
                    ),
                ],
                unit_amount=6179.29,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='815aae99-fcde-49e7-a9c9-d4f2d8a44640',
                    name='Dr. Wilbur Jerde',
                ),
                description='nihil',
                discount_amount=2079.6,
                discount_percentage=6657.15,
                item_ref=shared.ItemRef(
                    id='2f93f467-dc0d-48da-9612-2026ab8f2774',
                    name='Ms. Greg Sanford',
                ),
                quantity=3771.77,
                sub_total=6271.29,
                tax_amount=9494,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6235.78,
                    id='80da7a08-9fc4-44db-a745-30e5cc7c6d0c',
                    name='Spencer Wintheiser',
                ),
                total_amount=8196.32,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='34b6f623-bcec-4ab5-8aee-5e0da8b9af6a',
                        name='Christopher Hermiston',
                    ),
                ],
                unit_amount=3905.07,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='repudiandae',
        note='odio',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='aliquam',
                    currency='quasi',
                    currency_rate=2144.25,
                    total_amount=7771.39,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='be2d176d-c1c4-43d4-8f61-d171157cbe5e',
                        name='Francis Weimann',
                    ),
                    currency='quasi',
                    currency_rate=933.86,
                    id='840772f3-2e3b-449d-be0f-23b7b6d9948d',
                    note='aliquid',
                    paid_on_date='saepe',
                    reference='facere',
                    total_amount=8999.7,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='fugiat',
                    currency='eius',
                    currency_rate=4515.93,
                    total_amount=4844.89,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='680fc7a1-7a82-4e5e-82fd-28d1040a7e91',
                        name='Belinda Denesik',
                    ),
                    currency='incidunt',
                    currency_rate=3084.29,
                    id='cb183500-8f46-41ce-93e9-14498a9ba460',
                    note='similique',
                    paid_on_date='nulla',
                    reference='pariatur',
                    total_amount=9692.94,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='temporibus',
                    currency='officiis',
                    currency_rate=2522.9,
                    total_amount=826.1,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='0c37daa9-182a-449d-9625-d3caffc198ee',
                        name='Edwin Hagenes',
                    ),
                    currency='dignissimos',
                    currency_rate=6043.08,
                    id='2bcd440e-a98b-4ecc-a048-6de0d56d73b0',
                    note='quae',
                    paid_on_date='quis',
                    reference='nemo',
                    total_amount=345.89,
                ),
            ),
        ],
        reference='neque',
        source_modified_date='voluptates',
        sub_total=5187.95,
        supplemental_data=shared.SupplementalData(
            content={
                "impedit": {
                    "explicabo": 'ea',
                    "doloribus": 'maiores',
                },
                "nihil": {
                    "impedit": 'iure',
                    "ullam": 'aliquid',
                },
                "odio": {
                    "delectus": 'nostrum',
                    "harum": 'reprehenderit',
                },
                "sit": {
                    "consectetur": 'vero',
                    "eius": 'optio',
                    "sapiente": 'porro',
                    "impedit": 'vel',
                },
            },
        ),
        tax_amount=6786.31,
        total_amount=5828.22,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=69650,
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadDirectIncomeAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='necessitatibus',
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectIncomeRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='maxime',
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectIncomeAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='veniam',
    timeout_in_minutes=181673,
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
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDirectIncomesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='aliquid',
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDirectIncomeAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='sed',
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadDirectIncomeAttachmentRequest(
    request_body=operations.UploadDirectIncomeAttachmentRequestBody(
        content='modi'.encode(),
        request_body='at',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='aperiam',
)

res = s.direct_incomes.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
