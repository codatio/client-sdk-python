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

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating suppliers.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.Addressesitems(
                city='Madelynnberg',
                country='Denmark',
                line1='culpa',
                line2='corrupti',
                postal_code='77168',
                region='voluptatibus',
                type=shared.AddressType.BILLING,
            ),
            shared.Addressesitems(
                city='East Isabella',
                country='British Indian Ocean Territory (Chagos Archipelago)',
                line1='est',
                line2='consequatur',
                postal_code='32501',
                region='incidunt',
                type=shared.AddressType.DELIVERY,
            ),
            shared.Addressesitems(
                city='Arlington',
                country='Mongolia',
                line1='assumenda',
                line2='alias',
                postal_code='74089-9599',
                region='aut',
                type=shared.AddressType.DELIVERY,
            ),
        ],
        contact_name='eaque',
        default_currency='officiis',
        email_address='tempora',
        id='6f225e29-d79d-439d-8790-e2e6014a33d9',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='iusto',
        phone='717-420-7972',
        registration_number='doloremque',
        source_modified_date='necessitatibus',
        status=shared.SupplierStatus.ARCHIVED,
        supplemental_data=shared.SupplementalData(
            content={
                "dolor": {
                    "rem": 'eveniet',
                    "veniam": 'vero',
                    "dolor": 'occaecati',
                    "explicabo": 'delectus',
                },
                "fugit": {
                    "dolorum": 'voluptate',
                },
                "ducimus": {
                    "rerum": 'iusto',
                    "deserunt": 'asperiores',
                    "ab": 'tempore',
                    "suscipit": 'neque',
                },
            },
        ),
        supplier_name='eveniet',
        tax_number='placeat',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=867440,
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DownloadSupplierAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    supplier_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetSupplierRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    supplier_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetSupplierAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    supplier_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListSuppliersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='officiis',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListSupplierAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    supplier_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.UpdateSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.Addressesitems(
                city='Alyceworth',
                country='Peru',
                line1='deleniti',
                line2='consequatur',
                postal_code='03324-7318',
                region='ut',
                type=shared.AddressType.UNKNOWN,
            ),
        ],
        contact_name='ipsam',
        default_currency='occaecati',
        email_address='error',
        id='55c5c717-6045-497f-b771-9dd8c8482c02',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='aliquid',
        phone='(851) 827-5759 x560',
        registration_number='deserunt',
        source_modified_date='impedit',
        status=shared.SupplierStatus.UNKNOWN,
        supplemental_data=shared.SupplementalData(
            content={
                "perferendis": {
                    "illum": 'aspernatur',
                    "officia": 'cumque',
                },
                "eveniet": {
                    "aut": 'minus',
                    "temporibus": 'repudiandae',
                    "perferendis": 'aperiam',
                },
                "itaque": {
                    "necessitatibus": 'quisquam',
                    "delectus": 'blanditiis',
                    "inventore": 'quos',
                },
                "culpa": {
                    "amet": 'consequatur',
                    "dolor": 'saepe',
                    "sint": 'dolorem',
                },
            },
        ),
        supplier_name='doloribus',
        tax_number='sit',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    supplier_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    timeout_in_minutes=40967,
)

res = s.suppliers.update(req)

if res.update_supplier_response is not None:
    # handle response
```
