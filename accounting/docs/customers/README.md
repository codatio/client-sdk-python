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
                city='Port Clevelandtown',
                country='Turkmenistan',
                line1='culpa',
                line2='at',
                postal_code='10296',
                region='dolore',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='Abbyport',
                country='Philippines',
                line1='voluptatibus',
                line2='sequi',
                postal_code='37221',
                region='quas',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='Burdetteland',
                country='Vietnam',
                line1='nulla',
                line2='libero',
                postal_code='94593',
                region='unde',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='South Paul',
                country='Lesotho',
                line1='ab',
                line2='quo',
                postal_code='58178-2135',
                region='temporibus',
                type=shared.AddressType.UNKNOWN,
            ),
        ],
        contact_name='amet',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='Margaretestad',
                    country='Burkina Faso',
                    line1='placeat',
                    line2='rem',
                    postal_code='59914',
                    region='ullam',
                    type=shared.AddressType.UNKNOWN,
                ),
                email='Buster49@hotmail.com',
                modified_date='quod',
                name='Marjorie Funk',
                phone=[
                    shared.PhoneNumbersitems(
                        number='quaerat',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                ],
                status=shared.CustomerStatus.ARCHIVED,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Howellland',
                    country='Mayotte',
                    line1='distinctio',
                    line2='cum',
                    postal_code='82083',
                    region='laborum',
                    type=shared.AddressType.UNKNOWN,
                ),
                email='Warren19@gmail.com',
                modified_date='autem',
                name='Edgar Cremin',
                phone=[
                    shared.PhoneNumbersitems(
                        number='velit',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                ],
                status=shared.CustomerStatus.ARCHIVED,
            ),
        ],
        customer_name='natus',
        default_currency='minima',
        email_address='minus',
        id='9d237397-c785-4b5d-b4f5-00183febdf67',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='aliquid',
        phone='510.586.7430 x0316',
        registration_number='ad',
        source_modified_date='nisi',
        status=shared.CustomerStatus.UNKNOWN,
        supplemental_data=shared.SupplementalData(
            content={
                "officiis": {
                    "minus": 'tempora',
                    "sequi": 'natus',
                    "saepe": 'quibusdam',
                    "corrupti": 'maxime',
                },
                "aliquam": {
                    "explicabo": 'eaque',
                },
            },
        ),
        tax_number='hic',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=276828,
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
    customer_id='quae',
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
    customer_id='eos',
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
    customer_id='eius',
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
    query='voluptatem',
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
    customer_id='temporibus',
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
                city='New Jayde',
                country='Nigeria',
                line1='porro',
                line2='voluptas',
                postal_code='27537-1668',
                region='magni',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='Joanhaven',
                country='Lebanon',
                line1='unde',
                line2='ad',
                postal_code='62198-2033',
                region='laboriosam',
                type=shared.AddressType.BILLING,
            ),
        ],
        contact_name='tenetur',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='O'Konton',
                    country='Argentina',
                    line1='voluptas',
                    line2='pariatur',
                    postal_code='01252',
                    region='ullam',
                    type=shared.AddressType.UNKNOWN,
                ),
                email='Aurelia.Mraz77@yahoo.com',
                modified_date='ipsum',
                name='Carl Pollich IV',
                phone=[
                    shared.PhoneNumbersitems(
                        number='incidunt',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                    shared.PhoneNumbersitems(
                        number='nisi',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                ],
                status=shared.CustomerStatus.ARCHIVED,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='North Cloydton',
                    country='Austria',
                    line1='possimus',
                    line2='perferendis',
                    postal_code='28760',
                    region='beatae',
                    type=shared.AddressType.DELIVERY,
                ),
                email='Mae.Willms66@yahoo.com',
                modified_date='commodi',
                name='Tom Gutkowski',
                phone=[
                    shared.PhoneNumbersitems(
                        number='id',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                    shared.PhoneNumbersitems(
                        number='molestias',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
        ],
        customer_name='occaecati',
        default_currency='eos',
        email_address='veniam',
        id='3c8962f4-896b-4f51-a465-2d3c343d6177',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='atque',
        phone='1-935-212-4413 x9410',
        registration_number='iste',
        source_modified_date='aut',
        status=shared.CustomerStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "error": {
                    "ipsa": 'dolore',
                },
                "labore": {
                    "ullam": 'quibusdam',
                    "recusandae": 'ad',
                    "omnis": 'mollitia',
                },
                "placeat": {
                    "ducimus": 'eaque',
                    "aliquid": 'ea',
                },
                "odio": {
                    "quisquam": 'delectus',
                },
            },
        ),
        tax_number='et',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='optio',
    force_update=False,
    timeout_in_minutes=953679,
)

res = s.customers.update(req)

if res.update_customer_response is not None:
    # handle response
```
