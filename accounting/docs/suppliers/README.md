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
                city='Stephaniastead',
                country='Swaziland',
                line1='laudantium',
                line2='eos',
                postal_code='38203-9334',
                region='aliquid',
                type=shared.AddressType.DELIVERY,
            ),
            shared.Addressesitems(
                city='Port Rosalinda',
                country='Turkmenistan',
                line1='cum',
                line2='consequatur',
                postal_code='54807',
                region='maxime',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='Lake Arnoldo',
                country='Martinique',
                line1='id',
                line2='expedita',
                postal_code='45919',
                region='quisquam',
                type=shared.AddressType.DELIVERY,
            ),
        ],
        contact_name='maiores',
        default_currency='laudantium',
        email_address='beatae',
        id='ddf7e088-f74e-4f54-8921-6e8926313bb6',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='hic',
        phone='375-814-0006 x46446',
        registration_number='fugiat',
        source_modified_date='laboriosam',
        status=shared.SupplierStatus.ARCHIVED,
        supplemental_data=shared.SupplementalData(
            content={
                "recusandae": {
                    "pariatur": 'excepturi',
                },
            },
        ),
        supplier_name='fugiat',
        tax_number='ipsum',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=730689,
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
    supplier_id='voluptas',
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
    supplier_id='aliquid',
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
    supplier_id='perferendis',
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
    query='nesciunt',
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
    supplier_id='non',
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
                city='Carterland',
                country='Northern Mariana Islands',
                line1='id',
                line2='ab',
                postal_code='38112-4885',
                region='libero',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='Enterprise',
                country='Honduras',
                line1='quasi',
                line2='ducimus',
                postal_code='84456',
                region='perspiciatis',
                type=shared.AddressType.BILLING,
            ),
        ],
        contact_name='nobis',
        default_currency='facilis',
        email_address='sequi',
        id='98788398-eba1-4bbf-b143-356f6349a164',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='explicabo',
        phone='671-217-9347 x630',
        registration_number='vel',
        source_modified_date='enim',
        status=shared.SupplierStatus.UNKNOWN,
        supplemental_data=shared.SupplementalData(
            content={
                "beatae": {
                    "atque": 'optio',
                    "culpa": 'excepturi',
                },
                "et": {
                    "odit": 'reiciendis',
                    "voluptatem": 'veniam',
                },
                "consequuntur": {
                    "dolor": 'quia',
                    "harum": 'sequi',
                },
            },
        ),
        supplier_name='quae',
        tax_number='porro',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    supplier_id='harum',
    timeout_in_minutes=868742,
)

res = s.suppliers.update(req)

if res.update_supplier_response is not None:
    # handle response
```
