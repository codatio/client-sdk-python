# Customers

## Overview

Customers

### Available Operations

* [create](#create) - Create customer
* [get](#get) - Get customer
* [list](#list) - List customers
* [update](#update) - Update customer

## create

The *Create customer* endpoint creates a new [customer](https://docs.codat.io/accounting-api#/schemas/Customer) for a given company's connection.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating an account.


### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateCustomerRequest(
    customer=shared.Customer(
        addresses=[
            shared.Items(
                city='New Humberto',
                country='Trinidad and Tobago',
                line1='quidem',
                line2='architecto',
                postal_code='96661',
                region='dolorem',
                type=shared.AccountingAddressType.BILLING,
            ),
        ],
        contact_name='explicabo',
        contacts=[
            shared.Contact(
                address=shared.Items(
                    city='Halvorsonstead',
                    country='Guinea',
                    line1='minima',
                    line2='excepturi',
                    postal_code='46991',
                    region='mollitia',
                    type=shared.AccountingAddressType.UNKNOWN,
                ),
                email='Caroline_Ziemann@yahoo.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Claudia Krajcik',
                phone=[
                    shared.ContactPhone(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                ],
                status=shared.CustomerStatus.UNKNOWN,
            ),
        ],
        customer_name='laborum',
        default_currency='USD',
        email_address='enim',
        id='2c3f5ad0-19da-41ff-a78f-097b0074f154',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='(738) 590-2655',
        registration_number='pariatur',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CustomerStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "rem": {
                    "voluptates": 'quasi',
                },
            },
        ),
        tax_number='repudiandae',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=575947,
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


## get

The *Get customer* endpoint returns a single customer for a given customerId.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support getting a specific customer.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-expenses-api#/operations/refresh-company-data).


### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCustomerRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    customer_id='veritatis',
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


## list

The *List customers* endpoint returns a list of [customers](https://docs.codat.io/accounting-api#/schemas/Customer) for a given company's connection.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-expenses-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListCustomersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='itaque',
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


## update

The *Update customer* endpoint updates an existing [customer](https://docs.codat.io/accounting-api#/schemas/Customer) for a given company's connection.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating an account.


### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateCustomerRequest(
    customer=shared.Customer(
        addresses=[
            shared.Items(
                city='West Adele',
                country='Norway',
                line1='quibusdam',
                line2='explicabo',
                postal_code='78221-3550',
                region='magni',
                type=shared.AccountingAddressType.DELIVERY,
            ),
        ],
        contact_name='ipsam',
        contacts=[
            shared.Contact(
                address=shared.Items(
                    city='East Marianostead',
                    country='Estonia',
                    line1='facilis',
                    line2='tempore',
                    postal_code='94275',
                    region='aliquid',
                    type=shared.AccountingAddressType.BILLING,
                ),
                email='Kianna89@hotmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Arnold Kirlin',
                phone=[
                    shared.ContactPhone(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                ],
                status=shared.CustomerStatus.UNKNOWN,
            ),
        ],
        customer_name='cumque',
        default_currency='EUR',
        email_address='ea',
        id='6ae395ef-b9ba-488f-ba66-997074ba4469',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='1-911-405-3555 x069',
        registration_number='mollitia',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CustomerStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "dolor": {
                    "necessitatibus": 'odit',
                },
            },
        ),
        tax_number='nemo',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='quasi',
    force_update=False,
    timeout_in_minutes=435865,
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

