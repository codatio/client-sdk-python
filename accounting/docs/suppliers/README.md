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
                city='Kirkland',
                country='Netherlands',
                line1='doloremque',
                line2='autem',
                postal_code='25088',
                region='laudantium',
                type=shared.AddressType.DELIVERY,
            ),
            shared.Addressesitems(
                city='Ankundingfort',
                country='Kyrgyz Republic',
                line1='repellendus',
                line2='beatae',
                postal_code='42514',
                region='facilis',
                type=shared.AddressType.UNKNOWN,
            ),
        ],
        contact_name='cumque',
        default_currency='doloribus',
        email_address='minima',
        id='e6cb6eba-be5e-40b9-9f3b-1358d6a87bb7',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='est',
        phone='1-869-446-8407 x70355',
        registration_number='sit',
        source_modified_date='dignissimos',
        status=shared.SupplierStatus.ARCHIVED,
        supplemental_data=shared.SupplementalData(
            content={
                "praesentium": {
                    "incidunt": 'incidunt',
                    "vitae": 'incidunt',
                    "nostrum": 'explicabo',
                },
                "culpa": {
                    "voluptatibus": 'ipsa',
                    "quasi": 'sapiente',
                    "dolorem": 'quaerat',
                },
                "incidunt": {
                    "cumque": 'vel',
                },
            },
        ),
        supplier_name='inventore',
        tax_number='quidem',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=894398,
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
    supplier_id='quae',
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
    supplier_id='ipsum',
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
    supplier_id='nesciunt',
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
    query='distinctio',
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
    supplier_id='dolorum',
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
                city='The Hammocks',
                country='Guinea',
                line1='neque',
                line2='eos',
                postal_code='43139-5315',
                region='corporis',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='Towson',
                country='Christmas Island',
                line1='laudantium',
                line2='enim',
                postal_code='88211-1109',
                region='earum',
                type=shared.AddressType.BILLING,
            ),
            shared.Addressesitems(
                city='South Electa',
                country='Saint Lucia',
                line1='numquam',
                line2='quae',
                postal_code='19763-8760',
                region='eum',
                type=shared.AddressType.BILLING,
            ),
            shared.Addressesitems(
                city='Littlehaven',
                country='Cambodia',
                line1='cupiditate',
                line2='dicta',
                postal_code='97500-6166',
                region='atque',
                type=shared.AddressType.BILLING,
            ),
        ],
        contact_name='aliquam',
        default_currency='perspiciatis',
        email_address='labore',
        id='79edd4fc-f7b5-40cf-87f0-8f39271076a2',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='dolore',
        phone='407.690.5799 x0051',
        registration_number='saepe',
        source_modified_date='laudantium',
        status=shared.SupplierStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "blanditiis": {
                    "occaecati": 'natus',
                    "voluptas": 'optio',
                },
                "totam": {
                    "odit": 'eos',
                    "libero": 'eveniet',
                    "aut": 'similique',
                    "ipsum": 'maxime',
                },
                "tenetur": {
                    "voluptate": 'blanditiis',
                    "sint": 'dolorem',
                },
                "soluta": {
                    "fugit": 'neque',
                    "asperiores": 'corrupti',
                    "autem": 'autem',
                    "alias": 'eaque',
                },
            },
        ),
        supplier_name='minus',
        tax_number='commodi',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    supplier_id='inventore',
    timeout_in_minutes=784398,
)

res = s.suppliers.update(req)

if res.update_supplier_response is not None:
    # handle response
```
