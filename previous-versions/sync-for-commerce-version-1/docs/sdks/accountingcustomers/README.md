# AccountingCustomers

## Overview

Customers

### Available Operations

* [create_accounting_customer](#create_accounting_customer) - Create customer

## create_accounting_customer

The *Create customer* endpoint creates a new [customer](https://docs.codat.io/accounting-api#/schemas/Customer) for a given company's connection.

[Customers](https://docs.codat.io/accounting-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/accounting-api#/operations/get-create-update-customers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers) for integrations that support creating an account.


### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingCustomerRequest(
    accounting_customer=shared.AccountingCustomer(
        addresses=[
            shared.Items1(
                city='East Mikaylacester',
                country='Hungary',
                line1='quam',
                line2='molestias',
                postal_code='12114-1379',
                region='voluptatem',
                type=shared.AccountingAddressType.DELIVERY,
            ),
        ],
        contact_name='soluta',
        contacts=[
            shared.Contact(
                address=shared.Items1(
                    city='Boscoside',
                    country='Cuba',
                    line1='veritatis',
                    line2='nobis',
                    postal_code='75092-2226',
                    region='architecto',
                    type=shared.AccountingAddressType.UNKNOWN,
                ),
                email='Kayleigh66@gmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Domingo Grady',
                phone=[
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
        ],
        customer_name='odio',
        default_currency='USD',
        email_address='voluptatibus',
        id='ce953f73-ef7f-4bc7-abd7-4dd39c0f5d2c',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='574.262.3414 x82145',
        registration_number='dicta',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CustomerStatus.ARCHIVED,
        supplemental_data=shared.SupplementalData(
            content={
                "quasi": {
                    "ex": 'nulla',
                },
            },
        ),
        tax_number='excepturi',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=972920,
)

res = s.accounting_customers.create_accounting_customer(req)

if res.accounting_create_customer_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAccountingCustomerRequest](../../models/operations/createaccountingcustomerrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |


### Response

**[operations.CreateAccountingCustomerResponse](../../models/operations/createaccountingcustomerresponse.md)**

