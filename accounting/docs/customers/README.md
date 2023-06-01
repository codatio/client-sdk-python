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
                city='Kassandrafield',
                country='Ireland',
                line1='aut',
                line2='nisi',
                postal_code='53357',
                region='debitis',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='West Rorystad',
                country='Martinique',
                line1='magnam',
                line2='cupiditate',
                postal_code='95102-7224',
                region='hic',
                type=shared.AddressType.BILLING,
            ),
            shared.Addressesitems(
                city='Monroefort',
                country='Australia',
                line1='porro',
                line2='vel',
                postal_code='92418-7122',
                region='incidunt',
                type=shared.AddressType.DELIVERY,
            ),
            shared.Addressesitems(
                city='Mrazworth',
                country='Jersey',
                line1='rem',
                line2='est',
                postal_code='70884',
                region='laborum',
                type=shared.AddressType.BILLING,
            ),
        ],
        contact_name='soluta',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='Fort Leifmouth',
                    country='Bulgaria',
                    line1='ea',
                    line2='architecto',
                    postal_code='70835-8147',
                    region='exercitationem',
                    type=shared.AddressType.UNKNOWN,
                ),
                email='Krystel.Jakubowski71@yahoo.com',
                modified_date='modi',
                name='Jon Bashirian',
                phone=[
                    shared.PhoneNumbersitems(
                        number='iusto',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                    shared.PhoneNumbersitems(
                        number='odit',
                        type=shared.PhoneNumberType.FAX,
                    ),
                    shared.PhoneNumbersitems(
                        number='ducimus',
                        type=shared.PhoneNumberType.FAX,
                    ),
                    shared.PhoneNumbersitems(
                        number='ducimus',
                        type=shared.PhoneNumberType.FAX,
                    ),
                ],
                status=shared.CustomerStatus.ARCHIVED,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='East Dorcasboro',
                    country='Saint Helena',
                    line1='inventore',
                    line2='ducimus',
                    postal_code='04558',
                    region='necessitatibus',
                    type=shared.AddressType.DELIVERY,
                ),
                email='Stanley_Zboncak@hotmail.com',
                modified_date='quam',
                name='Lee Steuber DDS',
                phone=[
                    shared.PhoneNumbersitems(
                        number='pariatur',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                    shared.PhoneNumbersitems(
                        number='amet',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                    shared.PhoneNumbersitems(
                        number='quasi',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                    shared.PhoneNumbersitems(
                        number='rerum',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                ],
                status=shared.CustomerStatus.ARCHIVED,
            ),
        ],
        customer_name='aliquam',
        default_currency='voluptates',
        email_address='alias',
        id='80aa1041-86ec-4759-a02f-3702c5c8e2d3',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='consequatur',
        phone='1-782-202-9622 x40479',
        registration_number='sequi',
        source_modified_date='ducimus',
        status=shared.CustomerStatus.UNKNOWN,
        supplemental_data=shared.SupplementalData(
            content={
                "ut": {
                    "sed": 'quas',
                    "aspernatur": 'laudantium',
                },
                "fugit": {
                    "reiciendis": 'nulla',
                },
                "libero": {
                    "hic": 'eum',
                },
            },
        ),
        tax_number='sint',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=909351,
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
    customer_id='veniam',
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
    customer_id='unde',
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
    customer_id='consequuntur',
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
    query='laboriosam',
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
    customer_id='iusto',
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
                city='Annabelfort',
                country='Saint Martin',
                line1='voluptatum',
                line2='pariatur',
                postal_code='78213',
                region='voluptatum',
                type=shared.AddressType.DELIVERY,
            ),
            shared.Addressesitems(
                city='East Fridastad',
                country='Oman',
                line1='quas',
                line2='odit',
                postal_code='50599-1430',
                region='laborum',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='West Jeromefield',
                country='American Samoa',
                line1='numquam',
                line2='numquam',
                postal_code='90329-6305',
                region='distinctio',
                type=shared.AddressType.DELIVERY,
            ),
            shared.Addressesitems(
                city='Robbboro',
                country='Aruba',
                line1='vero',
                line2='corporis',
                postal_code='00962-1494',
                region='sed',
                type=shared.AddressType.BILLING,
            ),
        ],
        contact_name='natus',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='East Trystan',
                    country='Nauru',
                    line1='minima',
                    line2='minus',
                    postal_code='81241-6474',
                    region='quas',
                    type=shared.AddressType.BILLING,
                ),
                email='Fay.Stokes97@hotmail.com',
                modified_date='quis',
                name='Helen Brown',
                phone=[
                    shared.PhoneNumbersitems(
                        number='accusamus',
                        type=shared.PhoneNumberType.FAX,
                    ),
                    shared.PhoneNumbersitems(
                        number='vero',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                    shared.PhoneNumbersitems(
                        number='ea',
                        type=shared.PhoneNumberType.MOBILE,
                    ),
                    shared.PhoneNumbersitems(
                        number='aliquid',
                        type=shared.PhoneNumberType.FAX,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
        ],
        customer_name='consequuntur',
        default_currency='accusantium',
        email_address='autem',
        id='dab75005-2a56-447e-9c43-9ed8c4320f41',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='eos',
        phone='283-454-6735 x275',
        registration_number='quaerat',
        source_modified_date='nobis',
        status=shared.CustomerStatus.UNKNOWN,
        supplemental_data=shared.SupplementalData(
            content={
                "unde": {
                    "magni": 'modi',
                    "atque": 'blanditiis',
                    "quibusdam": 'odio',
                    "unde": 'ad',
                },
                "officia": {
                    "incidunt": 'aspernatur',
                    "asperiores": 'maxime',
                    "dolore": 'accusantium',
                },
                "corporis": {
                    "laboriosam": 'omnis',
                    "tenetur": 'vel',
                },
            },
        ),
        tax_number='iste',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='animi',
    force_update=False,
    timeout_in_minutes=60491,
)

res = s.customers.update(req)

if res.update_customer_response is not None:
    # handle response
```
