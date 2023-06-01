# customers

## Overview

Customers

### Available Operations

* [create](#create) - Create customer
* [download_attachment](#download_attachment) - Download customer attachment
* [get](#get) - Get customer
* [get_attachment](#get_attachment) - Get customer attachment
* [get_create_update_model](#get_create_update_model) - Get create/update customer model
* [list](#list) - List customers
* [list_attachments](#list_attachments) - List customer attachments
* [update](#update) - Update customer

## create

Posts an individual customer for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) to see which integrations support this endpoint.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateCustomerRequest(
    customer=shared.Customer(
        addresses=[
            shared.Addressesitems(
                city='South Carterboro',
                country='Ireland',
                line1='reprehenderit',
                line2='quidem',
                postal_code='62077-0396',
                region='libero',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='Hicksville',
                country='Greenland',
                line1='perferendis',
                line2='itaque',
                postal_code='91165-2810',
                region='itaque',
                type=shared.AddressType.DELIVERY,
            ),
            shared.Addressesitems(
                city='Alfonsoside',
                country='Niue',
                line1='aliquam',
                line2='quasi',
                postal_code='19233-9530',
                region='minima',
                type=shared.AddressType.BILLING,
            ),
            shared.Addressesitems(
                city='Wesley Chapel',
                country='Uruguay',
                line1='molestiae',
                line2='amet',
                postal_code='89329-8839',
                region='deserunt',
                type=shared.AddressType.BILLING,
            ),
        ],
        contact_name='minima',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='East Korbinstad',
                    country='Svalbard & Jan Mayen Islands',
                    line1='laborum',
                    line2='sapiente',
                    postal_code='21658-4225',
                    region='quos',
                    type=shared.AddressType.DELIVERY,
                ),
                email='Samanta20@gmail.com',
                modified_date='error',
                name='Trevor Hauck',
                phone=[
                    shared.PhoneNumbersitems(
                        number='sunt',
                        type=shared.PhoneNumberType.MOBILE,
                    ),
                    shared.PhoneNumbersitems(
                        number='similique',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                    shared.PhoneNumbersitems(
                        number='tempora',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                ],
                status=shared.CustomerStatus.ARCHIVED,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Hicksville',
                    country='Bahrain',
                    line1='omnis',
                    line2='aut',
                    postal_code='68688',
                    region='velit',
                    type=shared.AddressType.BILLING,
                ),
                email='Roosevelt_Batz38@hotmail.com',
                modified_date='esse',
                name='Dianna Ruecker',
                phone=[
                    shared.PhoneNumbersitems(
                        number='vero',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
        ],
        customer_name='asperiores',
        default_currency='quasi',
        email_address='veniam',
        id='920c90d1-b490-41f2-bd89-c8a32639da5b',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='in',
        phone='560.375.5065 x2942',
        registration_number='sequi',
        source_modified_date='nisi',
        status=shared.CustomerStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "mollitia": {
                    "hic": 'doloremque',
                    "id": 'asperiores',
                    "rem": 'quod',
                },
                "commodi": {
                    "beatae": 'placeat',
                    "molestiae": 'dolor',
                    "quia": 'nulla',
                },
            },
        ),
        tax_number='occaecati',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=983596,
)

res = s.customers.create(req)

if res.create_customer_response is not None:
    # handle response
```

## download_attachment

﻿Download customer attachment.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadCustomerAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='libero',
)

res = s.customers.download_attachment(req)

if res.data is not None:
    # handle response
```

## get

﻿Gets a single customer corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCustomerRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    customer_id='culpa',
)

res = s.customers.get(req)

if res.customer is not None:
    # handle response
```

## get_attachment

﻿Get  customer attachment.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCustomerAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='tenetur',
)

res = s.customers.get_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_create_update_model

﻿Get create/update customer model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating and updating customers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateCustomersModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.customers.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

## list

﻿Gets the latest customers for a company, with pagination.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListCustomersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='molestias',
)

res = s.customers.list(req)

if res.customers is not None:
    # handle response
```

## list_attachments

﻿List customer attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListCustomerAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='magnam',
)

res = s.customers.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## update

﻿Posts an updated customer for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support updating customers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateCustomerRequest(
    customer=shared.Customer(
        addresses=[
            shared.Addressesitems(
                city='Lake Christ',
                country='Norfolk Island',
                line1='vero',
                line2='quas',
                postal_code='77308-5623',
                region='dicta',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='Kshlerinberg',
                country='Kazakhstan',
                line1='blanditiis',
                line2='dolore',
                postal_code='52043-0600',
                region='accusamus',
                type=shared.AddressType.BILLING,
            ),
        ],
        contact_name='commodi',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='Rockwall',
                    country='Liberia',
                    line1='dolorem',
                    line2='eum',
                    postal_code='22063-1657',
                    region='molestiae',
                    type=shared.AddressType.BILLING,
                ),
                email='Nils22@gmail.com',
                modified_date='cupiditate',
                name='Sheldon Stiedemann',
                phone=[
                    shared.PhoneNumbersitems(
                        number='deserunt',
                        type=shared.PhoneNumberType.FAX,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Pasco',
                    country='Ecuador',
                    line1='placeat',
                    line2='veniam',
                    postal_code='65336-6407',
                    region='reiciendis',
                    type=shared.AddressType.DELIVERY,
                ),
                email='Salvador_Johnson@gmail.com',
                modified_date='iste',
                name='Mrs. Harvey Crooks',
                phone=[
                    shared.PhoneNumbersitems(
                        number='quae',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                    shared.PhoneNumbersitems(
                        number='iure',
                        type=shared.PhoneNumberType.MOBILE,
                    ),
                ],
                status=shared.CustomerStatus.ARCHIVED,
            ),
        ],
        customer_name='et',
        default_currency='perspiciatis',
        email_address='accusamus',
        id='a83d492e-d14b-48a2-8195-4545e955dcc1',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='praesentium',
        phone='(963) 601-7473 x168',
        registration_number='explicabo',
        source_modified_date='nulla',
        status=shared.CustomerStatus.ARCHIVED,
        supplemental_data=shared.SupplementalData(
            content={
                "quam": {
                    "incidunt": 'similique',
                    "nobis": 'culpa',
                    "ratione": 'illum',
                },
                "sed": {
                    "aut": 'voluptates',
                },
                "nulla": {
                    "dignissimos": 'dolor',
                    "totam": 'beatae',
                    "vitae": 'laborum',
                    "beatae": 'vitae',
                },
            },
        ),
        tax_number='veniam',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='non',
    force_update=False,
    timeout_in_minutes=516231,
)

res = s.customers.update(req)

if res.update_customer_response is not None:
    # handle response
```
