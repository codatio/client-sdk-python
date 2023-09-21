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
                city='East Kylie',
                country='Slovakia (Slovak Republic)',
                line1='pariatur',
                line2='soluta',
                postal_code='65211',
                region='distinctio',
                type=shared.AccountingAddressType.DELIVERY,
            ),
        ],
        contact_name='aliquid',
        contacts=[
            shared.Contact(
                address=shared.Items1(
                    city='Kennedyhaven',
                    country='Christmas Island',
                    line1='neque',
                    line2='fugit',
                    postal_code='41379',
                    region='voluptatem',
                    type=shared.AccountingAddressType.DELIVERY,
                ),
                email='Nella.Bosco8@hotmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Dr. Randolph McDermott',
                phone=[
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                ],
                status=shared.CustomerStatus.UNKNOWN,
            ),
        ],
        customer_name='dolorum',
        default_currency='GBP',
        email_address='quae',
        id='08e0adcf-4b92-4187-9fce-953f73ef7fbc',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='1-784-488-1670 x9381',
        registration_number='porro',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CustomerStatus.ARCHIVED,
        supplemental_data=shared.SupplementalData(
            content={
                "iusto": {
                    "eligendi": 'ducimus',
                },
            },
        ),
        tax_number='alias',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=639473,
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

