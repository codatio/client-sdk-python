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

The *Create customer* endpoint creates a new [customer](https://docs.codat.io/accounting-api#/schemas/Customer) for a given company's connection.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating an account.


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
                city='New Jerrell',
                country='Mauritius',
                line1='aperiam',
                line2='fugit',
                postal_code='27161',
                region='facere',
                type=shared.AddressType.BILLING,
            ),
            shared.Addressesitems(
                city='DuBuquetown',
                country='Tanzania',
                line1='excepturi',
                line2='dicta',
                postal_code='93098',
                region='animi',
                type=shared.AddressType.UNKNOWN,
            ),
            shared.Addressesitems(
                city='Port Kaci',
                country='Reunion',
                line1='quasi',
                line2='quidem',
                postal_code='33615-1707',
                region='quo',
                type=shared.AddressType.UNKNOWN,
            ),
        ],
        contact_name='libero',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='Elwinborough',
                    country='Honduras',
                    line1='nisi',
                    line2='labore',
                    postal_code='71802-2557',
                    region='consequatur',
                    type=shared.AddressType.DELIVERY,
                ),
                email='Monica44@gmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Bert Vandervort',
                phone=[
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.FAX,
                    ),
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Preciousport',
                    country='Tuvalu',
                    line1='illum',
                    line2='laborum',
                    postal_code='25804-9694',
                    region='nisi',
                    type=shared.AddressType.DELIVERY,
                ),
                email='Annetta69@hotmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Carmen Toy Sr.',
                phone=[
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.MOBILE,
                    ),
                ],
                status=shared.CustomerStatus.UNKNOWN,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Dearborn Heights',
                    country='Ethiopia',
                    line1='sequi',
                    line2='et',
                    postal_code='89337',
                    region='magnam',
                    type=shared.AddressType.UNKNOWN,
                ),
                email='Darlene.Herman@gmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Amos Brown',
                phone=[
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                ],
                status=shared.CustomerStatus.UNKNOWN,
            ),
        ],
        customer_name='culpa',
        default_currency='EUR',
        email_address='quod',
        id='c9904c51-95b8-4648-8efa-78f1e2d3b901',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='631-766-2766',
        registration_number='inventore',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CustomerStatus.ARCHIVED,
        supplemental_data=shared.SupplementalData(
            content={
                "ab": {
                    "pariatur": 'excepturi',
                },
                "enim": {
                    "dolore": 'sunt',
                    "nisi": 'molestias',
                    "impedit": 'quasi',
                },
            },
        ),
        tax_number='nesciunt',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=547077,
)

res = s.customers.create(req)

if res.create_customer_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateCustomerRequest](../../models/operations/createcustomerrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.CreateCustomerResponse](../../models/operations/createcustomerresponse.md)**


## download_attachment

The *Download customer attachment* endpoint downloads a specific attachment for a given `customerId` and `attachmentId`.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support downloading a customer attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadCustomerAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='in',
)

res = s.customers.download_attachment(req)

if res.data is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.DownloadCustomerAttachmentRequest](../../models/operations/downloadcustomerattachmentrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |


### Response

**[operations.DownloadCustomerAttachmentResponse](../../models/operations/downloadcustomerattachmentresponse.md)**


## get

The *Get customer* endpoint returns a single customer for a given customerId.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support getting a specific customer.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCustomerRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    customer_id='quia',
)

res = s.customers.get(req)

if res.customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetCustomerRequest](../../models/operations/getcustomerrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |


### Response

**[operations.GetCustomerResponse](../../models/operations/getcustomerresponse.md)**


## get_attachment

The *Get customer attachment* endpoint returns a specific attachment for a given `customerId` and `attachmentId`.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support getting a customer attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCustomerAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='odio',
)

res = s.customers.get_attachment(req)

if res.attachment is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetCustomerAttachmentRequest](../../models/operations/getcustomerattachmentrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |


### Response

**[operations.GetCustomerAttachmentResponse](../../models/operations/getcustomerattachmentresponse.md)**


## get_create_update_model

﻿The *Get create/update customer model* endpoint returns the expected data for the request payload when creating and updating a [customer](https://docs.codat.io/accounting-api#/schemas/Customer) for a given company and integration.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating and updating a customer.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

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

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetCreateUpdateCustomersModelRequest](../../models/operations/getcreateupdatecustomersmodelrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |


### Response

**[operations.GetCreateUpdateCustomersModelResponse](../../models/operations/getcreateupdatecustomersmodelresponse.md)**


## list

The *List customers* endpoint returns a list of [customers](https://docs.codat.io/accounting-api#/schemas/Customer) for a given company's connection.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

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
    query='dicta',
)

res = s.customers.list(req)

if res.customers is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListCustomersRequest](../../models/operations/listcustomersrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.ListCustomersResponse](../../models/operations/listcustomersresponse.md)**


## list_attachments

The *List customer attachments* endpoint returns a list of attachments avialable to download for given `customerId`.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support listing customer attachments.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListCustomerAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='eveniet',
)

res = s.customers.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListCustomerAttachmentsRequest](../../models/operations/listcustomerattachmentsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.ListCustomerAttachmentsResponse](../../models/operations/listcustomerattachmentsresponse.md)**


## update

The *Update customer* endpoint updates an existing [customer](https://docs.codat.io/accounting-api#/schemas/Customer) for a given company's connection.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating an account.


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
                city='Tamarafurt',
                country='Montserrat',
                line1='debitis',
                line2='non',
                postal_code='00571',
                region='optio',
                type=shared.AddressType.DELIVERY,
            ),
        ],
        contact_name='minima',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='Rancho Cucamonga',
                    country='Spain',
                    line1='aliquid',
                    line2='alias',
                    postal_code='16459-8156',
                    region='occaecati',
                    type=shared.AddressType.DELIVERY,
                ),
                email='Tod_Waters@gmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Renee Littel',
                phone=[
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.FAX,
                    ),
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.MOBILE,
                    ),
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                ],
                status=shared.CustomerStatus.UNKNOWN,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Canton',
                    country='Republic of Korea',
                    line1='quas',
                    line2='tenetur',
                    postal_code='64448-2483',
                    region='dicta',
                    type=shared.AddressType.DELIVERY,
                ),
                email='Wendell_Zulauf@gmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Gustavo Schinner',
                phone=[
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                ],
                status=shared.CustomerStatus.ARCHIVED,
            ),
        ],
        customer_name='natus',
        default_currency='USD',
        email_address='veniam',
        id='b9bdf219-0abd-49bb-8c27-25ec2659ce02',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='620-835-9945',
        registration_number='voluptates',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CustomerStatus.UNKNOWN,
        supplemental_data=shared.SupplementalData(
            content={
                "blanditiis": {
                    "quibusdam": 'possimus',
                    "maiores": 'est',
                    "optio": 'voluptate',
                },
                "nostrum": {
                    "enim": 'ipsa',
                    "ipsa": 'quaerat',
                },
                "nesciunt": {
                    "optio": 'eum',
                },
                "commodi": {
                    "quia": 'facilis',
                },
            },
        ),
        tax_number='magnam',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='dolor',
    force_update=False,
    timeout_in_minutes=588801,
)

res = s.customers.update(req)

if res.update_customer_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateCustomerRequest](../../models/operations/updatecustomerrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.UpdateCustomerResponse](../../models/operations/updatecustomerresponse.md)**

