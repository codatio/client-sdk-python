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

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating customers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateCustomerRequest(
    customer=shared.Customer(
        addresses=[
            shared.Addressesitems(
                city='Cartwrightstad',
                country='Ukraine',
                line1='assumenda',
                line2='optio',
                postal_code='94549',
                region='adipisci',
                type=shared.AddressTypeEnum.UNKNOWN,
            ),
            shared.Addressesitems(
                city='Apopka',
                country='Equatorial Guinea',
                line1='rerum',
                line2='nesciunt',
                postal_code='28807-3440',
                region='recusandae',
                type=shared.AddressTypeEnum.DELIVERY,
            ),
            shared.Addressesitems(
                city='East Martina',
                country='Svalbard & Jan Mayen Islands',
                line1='dolor',
                line2='porro',
                postal_code='91773-0293',
                region='quod',
                type=shared.AddressTypeEnum.UNKNOWN,
            ),
            shared.Addressesitems(
                city='Reichelfort',
                country='South Africa',
                line1='alias',
                line2='deserunt',
                postal_code='15095',
                region='nemo',
                type=shared.AddressTypeEnum.BILLING,
            ),
        ],
        contact_name='reiciendis',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='Freedaton',
                    country='Mali',
                    line1='natus',
                    line2='culpa',
                    postal_code='48950-4669',
                    region='quae',
                    type=shared.AddressTypeEnum.UNKNOWN,
                ),
                email='Cristal_Fisher48@hotmail.com',
                modified_date='unde',
                name='Alton McKenzie',
                phone=[
                    shared.PhoneNumbersitems(
                        number='aut',
                        type=shared.PhoneNumberTypeEnum.LANDLINE,
                    ),
                    shared.PhoneNumbersitems(
                        number='quia',
                        type=shared.PhoneNumberTypeEnum.FAX,
                    ),
                ],
                status=shared.CustomerStatusEnum.ARCHIVED,
            ),
        ],
        customer_name='qui',
        default_currency='commodi',
        email_address='a',
        id='d368ba92-16bc-4b41-9835-c73641723133',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='recusandae',
        phone='(802) 568-3142 x77862',
        registration_number='molestias',
        source_modified_date='dolores',
        status=shared.CustomerStatusEnum.UNKNOWN,
        supplemental_data=shared.SupplementalData(
            content={
                "minus": {
                    "odit": 'maxime',
                    "aspernatur": 'magni',
                },
                "minus": {
                    "ipsam": 'sequi',
                    "quaerat": 'accusantium',
                },
            },
        ),
        tax_number='incidunt',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=583959,
)

res = s.customers.create(req)

if res.create_customer_response is not None:
    # handle response
```

## download_attachment

Download customer attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadCustomerAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='minima',
)

res = s.customers.download_attachment(req)

if res.data is not None:
    # handle response
```

## get

Gets a single customer corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCustomerRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    customer_id='quo',
)

res = s.customers.get(req)

if res.customer is not None:
    # handle response
```

## get_attachment

Get  customer attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCustomerAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='quis',
)

res = s.customers.get_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_create_update_model

Get create/update customer model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating and updating customers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
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

Gets the latest customers for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListCustomersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='facere',
)

res = s.customers.list(req)

if res.customers is not None:
    # handle response
```

## list_attachments

List customer attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListCustomerAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='quidem',
)

res = s.customers.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## update

Posts an updated customer for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support updating customers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateCustomerRequest(
    customer=shared.Customer(
        addresses=[
            shared.Addressesitems(
                city='Port Eriberto',
                country='Jersey',
                line1='quo',
                line2='vitae',
                postal_code='26519-5661',
                region='enim',
                type=shared.AddressTypeEnum.BILLING,
            ),
            shared.Addressesitems(
                city='South San Francisco',
                country='Sao Tome and Principe',
                line1='quasi',
                line2='sint',
                postal_code='19688',
                region='eum',
                type=shared.AddressTypeEnum.UNKNOWN,
            ),
            shared.Addressesitems(
                city='Williamsonfield',
                country='Samoa',
                line1='veniam',
                line2='magnam',
                postal_code='68300',
                region='quis',
                type=shared.AddressTypeEnum.DELIVERY,
            ),
        ],
        contact_name='reiciendis',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='Lesterview',
                    country='Burundi',
                    line1='voluptatem',
                    line2='voluptas',
                    postal_code='89160-6192',
                    region='quia',
                    type=shared.AddressTypeEnum.DELIVERY,
                ),
                email='Lydia7@gmail.com',
                modified_date='perferendis',
                name='Andy Paucek',
                phone=[
                    shared.PhoneNumbersitems(
                        number='necessitatibus',
                        type=shared.PhoneNumberTypeEnum.FAX,
                    ),
                ],
                status=shared.CustomerStatusEnum.UNKNOWN,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='West Ethelyn',
                    country='Martinique',
                    line1='ea',
                    line2='fugiat',
                    postal_code='59595',
                    region='reprehenderit',
                    type=shared.AddressTypeEnum.BILLING,
                ),
                email='Mittie_Williamson13@gmail.com',
                modified_date='nam',
                name='Erik Stehr',
                phone=[
                    shared.PhoneNumbersitems(
                        number='deserunt',
                        type=shared.PhoneNumberTypeEnum.MOBILE,
                    ),
                    shared.PhoneNumbersitems(
                        number='modi',
                        type=shared.PhoneNumberTypeEnum.FAX,
                    ),
                    shared.PhoneNumbersitems(
                        number='repellendus',
                        type=shared.PhoneNumberTypeEnum.MOBILE,
                    ),
                    shared.PhoneNumbersitems(
                        number='unde',
                        type=shared.PhoneNumberTypeEnum.FAX,
                    ),
                ],
                status=shared.CustomerStatusEnum.UNKNOWN,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Port Gavinland',
                    country='Central African Republic',
                    line1='numquam',
                    line2='velit',
                    postal_code='21540',
                    region='cumque',
                    type=shared.AddressTypeEnum.DELIVERY,
                ),
                email='Josiah19@yahoo.com',
                modified_date='fuga',
                name='Miss Don Dach',
                phone=[
                    shared.PhoneNumbersitems(
                        number='nesciunt',
                        type=shared.PhoneNumberTypeEnum.UNKNOWN,
                    ),
                    shared.PhoneNumbersitems(
                        number='beatae',
                        type=shared.PhoneNumberTypeEnum.UNKNOWN,
                    ),
                ],
                status=shared.CustomerStatusEnum.UNKNOWN,
            ),
        ],
        customer_name='quo',
        default_currency='libero',
        email_address='eaque',
        id='a0003eb2-2d9b-43a7-8d94-faa741c57d1f',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='vero',
        phone='(810) 408-1587 x17905',
        registration_number='nostrum',
        source_modified_date='labore',
        status=shared.CustomerStatusEnum.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "tenetur": {
                    "necessitatibus": 'necessitatibus',
                    "autem": 'natus',
                    "quasi": 'iure',
                },
            },
        ),
        tax_number='ex',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='error',
    force_update=False,
    timeout_in_minutes=535903,
)

res = s.customers.update(req)

if res.update_customer_response is not None:
    # handle response
```
