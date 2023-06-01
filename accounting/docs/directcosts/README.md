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
            data_type='doloremque',
            id='6d212494-5081-49d7-83b1-b41844060e00',
        ),
        currency='nesciunt',
        currency_rate=827.23,
        id='0d023dc9-01f5-4afd-aa6c-44846ae9d892',
        issue_date='veniam',
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='c8962f48-96bf-451e-8652-d3c343d61778',
                    name='Amos Hahn Sr.',
                ),
                description='numquam',
                discount_amount=4553.55,
                discount_percentage=4837.72,
                item_ref=shared.ItemRef(
                    id='25e62190-9e91-4044-a5de-59ac7706670c',
                    name='Henry Ruecker',
                ),
                quantity=6035.57,
                sub_total=2347.4,
                tax_amount=1862.22,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4003.27,
                    id='05251e66-bb42-4689-bd99-a2d335670e93',
                    name='Clay Hyatt',
                ),
                total_amount=3195.13,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='perspiciatis',
                        id='f358aaea-cae3-423a-b1bf-7ba1cc97716c',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='accusantium',
                            id='2cc9e0c7-d9d3-423f-9aa6-3ed9cf1c856b',
                        ),
                        shared.InvoiceTo(
                            data_type='quo',
                            id='ba51ef24-54a4-47fa-8f11-6cdd5444a756',
                        ),
                        shared.InvoiceTo(
                            data_type='consequuntur',
                            id='873c7dd9-efaf-443d-8623-620f3138f30d',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='3db022fa-a565-4fb8-b652-ebb9d3838387',
                        name='Jason Considine',
                    ),
                    shared.TrackingCategoryRef(
                        id='b293dab3-0e91-47f5-8fda-04c8b1bb55a2',
                        name='Miss Russell Ritchie',
                    ),
                    shared.TrackingCategoryRef(
                        id='3bb74466-4eb1-4d03-b88b-0d1bb17afee7',
                        name='Latoya Hodkiewicz',
                    ),
                    shared.TrackingCategoryRef(
                        id='b9457c7e-daf3-49d1-afbf-76fd162b303e',
                        name='Sarah Cremin',
                    ),
                ],
                unit_amount=5677.5,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='ipsum',
        note='accusamus',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='tempora',
                    currency='sequi',
                    currency_rate=893.2,
                    total_amount=3986.87,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='cf55b431-3553-4ccf-9c20-4c4adcc9904c',
                        name='Debra Medhurst',
                    ),
                    currency='atque',
                    currency_rate=3840.98,
                    id='48cefa78-f1e2-4d3b-901e-0952bbb4cbb1',
                    note='iste',
                    paid_on_date='voluptatibus',
                    reference='odio',
                    total_amount=665.27,
                ),
            ),
        ],
        reference='neque',
        source_modified_date='pariatur',
        sub_total=5685.48,
        supplemental_data=shared.SupplementalData(
            content={
                "culpa": {
                    "sunt": 'nisi',
                    "molestias": 'impedit',
                },
                "quasi": {
                    "corrupti": 'in',
                },
            },
        ),
        tax_amount=1589.19,
        total_amount=4888.02,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=119013,
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
    direct_cost_id='eveniet',
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
    direct_cost_id='vitae',
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
    direct_cost_id='quos',
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
    query='eveniet',
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
    direct_cost_id='officia',
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
        content='perspiciatis'.encode(),
        request_body='debitis',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='non',
)

res = s.direct_costs.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
