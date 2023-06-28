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
                city='Diamond Bar',
                country='Switzerland',
                line1='vero',
                line2='natus',
                postal_code='86228-8842',
                region='incidunt',
                type=shared.AddressType.BILLING,
            ),
            shared.Addressesitems(
                city='Fort Dena',
                country='Palau',
                line1='esse',
                line2='id',
                postal_code='59289-2483',
                region='nostrum',
                type=shared.AddressType.DELIVERY,
            ),
            shared.Addressesitems(
                city='Lenoreborough',
                country='Grenada',
                line1='facere',
                line2='aliquam',
                postal_code='29026',
                region='numquam',
                type=shared.AddressType.BILLING,
            ),
        ],
        contact_name='dolores',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='North Kristatown',
                    country='Japan',
                    line1='cum',
                    line2='facere',
                    postal_code='32705',
                    region='sed',
                    type=shared.AddressType.DELIVERY,
                ),
                email='Janie95@hotmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Marjorie Fritsch',
                phone=[
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.FAX,
                    ),
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                ],
                status=shared.CustomerStatus.UNKNOWN,
            ),
        ],
        customer_name='asperiores',
        default_currency='EUR',
        email_address='nostrum',
        id='d911cbfe-749c-4af4-9a27-f69e2c9e6d10',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='(862) 782-7470 x2005',
        registration_number='facere',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CustomerStatus.ARCHIVED,
        supplemental_data=shared.SupplementalData(
            content={
                "sequi": {
                    "modi": 'nihil',
                    "velit": 'aut',
                },
            },
        ),
        tax_number='rem',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=142520,
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
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCustomerRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    customer_id='error',
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
    customer_id='incidunt',
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
    query='asperiores',
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
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListCustomerAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='eos',
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
                city='Cartershire',
                country='Somalia',
                line1='nemo',
                line2='eum',
                postal_code='09572',
                region='dolores',
                type=shared.AddressType.BILLING,
            ),
            shared.Addressesitems(
                city='West Amira',
                country='Nicaragua',
                line1='tempora',
                line2='eum',
                postal_code='13245',
                region='natus',
                type=shared.AddressType.DELIVERY,
            ),
            shared.Addressesitems(
                city='Allen',
                country='Tuvalu',
                line1='iste',
                line2='error',
                postal_code='36286',
                region='amet',
                type=shared.AddressType.BILLING,
            ),
        ],
        contact_name='ducimus',
        contacts=[
            shared.Contact(
                address=shared.Addressesitems(
                    city='Beerberg',
                    country='Guatemala',
                    line1='sed',
                    line2='a',
                    postal_code='26372-8757',
                    region='odio',
                    type=shared.AddressType.BILLING,
                ),
                email='Taryn.Raynor88@yahoo.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Brandon Rutherford',
                phone=[
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.FAX,
                    ),
                ],
                status=shared.CustomerStatus.ARCHIVED,
            ),
            shared.Contact(
                address=shared.Addressesitems(
                    city='Plymouth',
                    country='Brunei Darussalam',
                    line1='eligendi',
                    line2='nam',
                    postal_code='33238-3943',
                    region='at',
                    type=shared.AddressType.BILLING,
                ),
                email='Charity.Lubowitz88@gmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Dr. Marie O'Hara',
                phone=[
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
        ],
        customer_name='sint',
        default_currency='USD',
        email_address='commodi',
        id='489d7b78-673e-413a-92a6-b99249459448',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='475.425.1475 x36278',
        registration_number='a',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CustomerStatus.UNKNOWN,
        supplemental_data=shared.SupplementalData(
            content={
                "minima": {
                    "sit": 'incidunt',
                    "magnam": 'molestias',
                    "hic": 'error',
                },
            },
        ),
        tax_number='repellendus',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='delectus',
    force_update=False,
    timeout_in_minutes=118986,
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

