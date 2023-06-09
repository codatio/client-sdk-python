# suppliers

## Overview

Suppliers

### Available Operations

* [create](#create) - Create supplier
* [download_attachment](#download_attachment) - Download supplier attachment
* [get](#get) - Get supplier
* [get_attachment](#get_attachment) - Get supplier attachment
* [get_create_update_model](#get_create_update_model) - Get create/update supplier model
* [list](#list) - List suppliers
* [list_attachments](#list_attachments) - List supplier attachments
* [update](#update) - Update supplier

## create

Push suppliers

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) to see which integrations support this endpoint.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.Addressesitems(
                city='Syracuse',
                country='Turks and Caicos Islands',
                line1='sit',
                line2='aut',
                postal_code='87647',
                region='hic',
                type=shared.AddressType.BILLING,
            ),
            shared.Addressesitems(
                city='Connieland',
                country='Panama',
                line1='eveniet',
                line2='quis',
                postal_code='57305',
                region='quam',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='North Van',
                country='Austria',
                line1='aliquid',
                line2='maiores',
                postal_code='77933',
                region='officia',
                type=shared.AddressType.BILLING,
            ),
        ],
        contact_name='ex',
        default_currency='voluptatum',
        email_address='iure',
        id='143c9790-5ff7-497a-9da6-64b7e778a74b',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='(877) 492-8687',
        registration_number='culpa',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.SupplierStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "consequuntur": {
                    "libero": 'eum',
                    "ad": 'totam',
                    "laboriosam": 'fugit',
                },
            },
        ),
        supplier_name='illum',
        tax_number='odit',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=681125,
)

res = s.suppliers.create(req)

if res.create_supplier_response is not None:
    # handle response
```

## download_attachment

Download supplier attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadSupplierAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    supplier_id='velit',
)

res = s.suppliers.download_attachment(req)

if res.data is not None:
    # handle response
```

## get

Gets a single supplier corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetSupplierRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    supplier_id='veritatis',
)

res = s.suppliers.get(req)

if res.supplier is not None:
    # handle response
```

## get_attachment

﻿Get supplier attachment.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetSupplierAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    supplier_id='doloribus',
)

res = s.suppliers.get_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_create_update_model

Get create/update supplier model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating and updating suppliers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateSuppliersModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.suppliers.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

## list

Gets the latest suppliers for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListSuppliersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='molestias',
)

res = s.suppliers.list(req)

if res.suppliers is not None:
    # handle response
```

## list_attachments

Get supplier attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListSupplierAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    supplier_id='distinctio',
)

res = s.suppliers.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## update

Update supplier

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support updating suppliers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.Addressesitems(
                city='Lake Lukas',
                country='Hungary',
                line1='harum',
                line2='placeat',
                postal_code='74922-2111',
                region='voluptates',
                type=shared.AddressType.BILLING,
            ),
        ],
        contact_name='mollitia',
        default_currency='veniam',
        email_address='at',
        id='ee1acd72-a899-481b-98fe-682e1c2dbe23',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='(877) 492-8687',
        registration_number='voluptatum',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.SupplierStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "magnam": {
                    "facere": 'beatae',
                    "consequuntur": 'sed',
                },
            },
        ),
        supplier_name='minus',
        tax_number='provident',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    supplier_id='doloribus',
    timeout_in_minutes=396101,
)

res = s.suppliers.update(req)

if res.update_supplier_response is not None:
    # handle response
```
