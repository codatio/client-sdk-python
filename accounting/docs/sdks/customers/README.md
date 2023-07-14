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
                city='San Antonio',
                country='New Zealand',
                line1='architecto',
                line2='iure',
                postal_code='95623-0684',
                region='nisi',
                type=shared.AddressType.DELIVERY,
            ),
        ],
        contact_name='officiis',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='Hilllton',
                    country='Mauritius',
                    line1='impedit',
                    line2='modi',
                    postal_code='61968-2330',
                    region='odit',
                    type=shared.AddressType.DELIVERY,
                ),
                email='Gina93@gmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Lance Cruickshank DVM',
                phone=[
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.MOBILE,
                    ),
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.MOBILE,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Adamsboro',
                    country='Chile',
                    line1='labore',
                    line2='earum',
                    postal_code='06184',
                    region='voluptates',
                    type=shared.AddressType.DELIVERY,
                ),
                email='Domenick41@yahoo.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Cristina Beer V',
                phone=[
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.FAX,
                    ),
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.FAX,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Runolfssonside',
                    country='Uruguay',
                    line1='tenetur',
                    line2='ipsam',
                    postal_code='70098-3083',
                    region='aspernatur',
                    type=shared.AddressType.BILLING,
                ),
                email='Diana_Hammes@yahoo.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Verna Lang',
                phone=[
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.FAX,
                    ),
                ],
                status=shared.CustomerStatus.ARCHIVED,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Reychester',
                    country='French Guiana',
                    line1='veritatis',
                    line2='fugit',
                    postal_code='88364',
                    region='hic',
                    type=shared.AddressType.DELIVERY,
                ),
                email='Jaden62@gmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Verna Sauer',
                phone=[
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.FAX,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
        ],
        customer_name='incidunt',
        default_currency='EUR',
        email_address='nihil',
        id='7b4848bd-6a6f-4044-9d2c-3b808094373e',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='1-223-679-7768 x019',
        registration_number='sunt',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CustomerStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "quidem": {
                    "a": 'et',
                    "ipsam": 'eos',
                    "exercitationem": 'minima',
                    "laudantium": 'quibusdam',
                },
                "fuga": {
                    "excepturi": 'corporis',
                    "nam": 'itaque',
                    "suscipit": 'porro',
                },
            },
        ),
        tax_number='nulla',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=10447,
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
    customer_id='qui',
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
    customer_id='in',
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
    customer_id='enim',
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
    query='vel',
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
    customer_id='impedit',
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
                city='West Marcelina',
                country='Palestinian Territory',
                line1='labore',
                line2='adipisci',
                postal_code='73480',
                region='esse',
                type=shared.AddressType.BILLING,
            ),
        ],
        contact_name='amet',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='East Abdul',
                    country='Libyan Arab Jamahiriya',
                    line1='eligendi',
                    line2='qui',
                    postal_code='95501',
                    region='repellendus',
                    type=shared.AddressType.BILLING,
                ),
                email='Verona.Abshire34@gmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Ray Pfannerstill',
                phone=[
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Windlerfort',
                    country='Brazil',
                    line1='rem',
                    line2='itaque',
                    postal_code='74945-4921',
                    region='recusandae',
                    type=shared.AddressType.UNKNOWN,
                ),
                email='May.Donnelly89@gmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Myra Hermann',
                phone=[
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                ],
                status=shared.CustomerStatus.UNKNOWN,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Lake Roxaneburgh',
                    country='Sao Tome and Principe',
                    line1='iste',
                    line2='earum',
                    postal_code='77302',
                    region='repellat',
                    type=shared.AddressType.BILLING,
                ),
                email='Columbus_Moore82@hotmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Duane Dibbert DVM',
                phone=[
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.MOBILE,
                    ),
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                ],
                status=shared.CustomerStatus.UNKNOWN,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Lexifurt',
                    country='Somalia',
                    line1='molestiae',
                    line2='officiis',
                    postal_code='50466-9029',
                    region='dolorem',
                    type=shared.AddressType.UNKNOWN,
                ),
                email='Lizeth_Kuhlman@hotmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Nicolas Walker I',
                phone=[
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.FAX,
                    ),
                ],
                status=shared.CustomerStatus.UNKNOWN,
            ),
        ],
        customer_name='commodi',
        default_currency='EUR',
        email_address='temporibus',
        id='368ba921-6bcb-4415-835c-73641723133e',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='224-783-1427 x78625',
        registration_number='dolores',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CustomerStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "non": {
                    "maxime": 'aspernatur',
                },
                "magni": {
                    "minima": 'ipsam',
                    "sequi": 'quaerat',
                    "accusantium": 'incidunt',
                    "cupiditate": 'minima',
                },
                "quo": {
                    "facere": 'quidem',
                    "harum": 'adipisci',
                },
                "optio": {
                    "reprehenderit": 'quo',
                    "vitae": 'voluptates',
                },
            },
        ),
        tax_number='tempora',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='iste',
    force_update=False,
    timeout_in_minutes=560736,
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

