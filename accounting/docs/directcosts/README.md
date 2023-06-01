# direct_costs

## Overview

Direct costs

### Available Operations

* [create](#create) - Create direct cost
* [download_attachment](#download_attachment) - Download direct cost attachment
* [get](#get) - Get direct cost
* [get_attachment](#get_attachment) - Get direct cost attachment
* [get_create_model](#get_create_model) - Get create direct cost model
* [list](#list) - List direct costs
* [list_attachments](#list_attachments) - List direct cost attachments
* [upload_attachment](#upload_attachment) - Upload direct cost attachment

## create

Posts a new direct cost to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create direct cost model](https://docs.codat.io/accounting-api#/operations/get-create-directCosts-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) to see which integrations support this endpoint.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateDirectCostRequest(
    direct_cost=shared.DirectCost(
        contact_ref=shared.ContactRef(
            data_type='consequuntur',
            id='bd7ed565-0762-41c5-8f4d-7396564c20a0',
        ),
        currency='reprehenderit',
        currency_rate=1171.17,
        id='1a961d24-a7db-4b8f-932d-892cf7812cb5',
        issue_date='architecto',
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='c878240b-f548-4f88-b8f1-bf0bc8e1f206',
                    name='Corey Streich',
                ),
                description='illo',
                discount_amount=8384.02,
                discount_percentage=403.46,
                item_ref=shared.ItemRef(
                    id='081090f6-7066-473f-ba68-1c5768dce742',
                    name='Donna Mann',
                ),
                quantity=1058.74,
                sub_total=3497.12,
                tax_amount=8881.17,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=532.16,
                    id='8601489a-5f63-4e3a-b3dd-9dda33dcd634',
                    name='Nathan Ward',
                ),
                total_amount=4568.09,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='id',
                        id='98e4df37-e45b-4895-9d41-3e13a4823109',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='iure',
                            id='bd354c09-2bd7-434f-8244-9d86f4bb20fe',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='d911cbfe-749c-4af4-9a27-f69e2c9e6d10',
                        name='Arturo Smith',
                    ),
                    shared.TrackingCategoryRef(
                        id='ad4c6b03-108d-49c3-b747-3082b94f2ab1',
                        name='Rufus Hickle',
                    ),
                ],
                unit_amount=837,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='voluptates',
        note='unde',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='amet',
                    currency='dolores',
                    currency_rate=4167.82,
                    total_amount=2051.5,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='50a46714-3789-4ce0-a991-594d93a74c02',
                        name='Jane Wilkinson',
                    ),
                    currency='quidem',
                    currency_rate=3102.12,
                    id='b4db8b77-8ebb-46e1-92cf-502bafb2cbc4',
                    note='aliquid',
                    paid_on_date='adipisci',
                    reference='ipsam',
                    total_amount=8526.23,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='enim',
                    currency='eveniet',
                    currency_rate=4330.83,
                    total_amount=3470.5,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='da028c3e-951a-41e3-8fda-966489d7b786',
                        name='Mrs. Josephine Tromp',
                    ),
                    currency='quasi',
                    currency_rate=1772.5,
                    id='a6b99249-4594-4487-b5c8-43836b86b3cd',
                    note='a',
                    paid_on_date='ex',
                    reference='dolore',
                    total_amount=1158.7,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='minima',
                    currency='facilis',
                    currency_rate=223.76,
                    total_amount=2799.72,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='49f9df13-f4ee-4dbe-b8bf-606825894ea7',
                        name='Grace Stehr',
                    ),
                    currency='in',
                    currency_rate=1479.33,
                    id='795b7851-48d6-4d54-9e56-35b33bc0f970',
                    note='placeat',
                    paid_on_date='dolore',
                    reference='magni',
                    total_amount=9730.03,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='quod',
                    currency='provident',
                    currency_rate=9624.68,
                    total_amount=2930.13,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='844225e7-5b79-4606-9c0e-fa6f93b90a1b',
                        name='Colin Mills',
                    ),
                    currency='accusamus',
                    currency_rate=1147.52,
                    id='254b739f-4fe7-4721-8d1f-6558c99c722d',
                    note='fugit',
                    paid_on_date='nam',
                    reference='optio',
                    total_amount=349.2,
                ),
            ),
        ],
        reference='earum',
        source_modified_date='excepturi',
        sub_total=2568.9,
        supplemental_data=shared.SupplementalData(
            content={
                "voluptatum": {
                    "possimus": 'unde',
                    "maxime": 'culpa',
                },
            },
        ),
        tax_amount=6428.58,
        total_amount=9268.79,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=42929,
)

res = s.direct_costs.create(req)

if res.create_direct_cost_response is not None:
    # handle response
```

## download_attachment

Downloads an attachment for the specified direct cost for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadDirectCostAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='magnam',
)

res = s.direct_costs.download_attachment(req)

if res.data is not None:
    # handle response
```

## get

Gets the specified direct cost for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectCostRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='quia',
)

res = s.direct_costs.get(req)

if res.direct_cost is not None:
    # handle response
```

## get_attachment

Gets the specified direct cost attachment for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectCostAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='quibusdam',
)

res = s.direct_costs.get_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_create_model

Get create direct cost model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support creating direct costs.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateDirectCostsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.direct_costs.get_create_model(req)

if res.push_option is not None:
    # handle response
```

## list

Gets the direct costs for the company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDirectCostsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='temporibus',
)

res = s.direct_costs.list(req)

if res.direct_costs is not None:
    # handle response
```

## list_attachments

Gets all attachments for the specified direct cost for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDirectCostAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='voluptate',
)

res = s.direct_costs.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## upload_attachment

Posts a new direct cost attachment for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadDirectCostAttachmentRequest(
    request_body=operations.UploadDirectCostAttachmentRequestBody(
        content='placeat'.encode(),
        request_body='est',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='est',
)

res = s.direct_costs.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
