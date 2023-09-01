# accounting_customers

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
                city='Reingerstad',
                country='Palau',
                line1='odio',
                line2='fugit',
                postal_code='14002',
                region='neque',
                type=shared.AccountingAddressType.BILLING,
            ),
            shared.Items1(
                city='Blaine',
                country='Croatia',
                line1='unde',
                line2='nulla',
                postal_code='81136-7167',
                region='fugiat',
                type=shared.AccountingAddressType.BILLING,
            ),
        ],
        contact_name='quos',
        contacts=[
            shared.Contact(
                address=shared.Items1(
                    city='South Anastacioshire',
                    country='Belarus',
                    line1='aperiam',
                    line2='totam',
                    postal_code='77044',
                    region='dolores',
                    type=shared.AccountingAddressType.DELIVERY,
                ),
                email='Marcella.Schumm@gmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Terence Reynolds',
                phone=[
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.FAX,
                    ),
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                ],
                status=shared.CustomerStatus.ARCHIVED,
            ),
            shared.Contact(
                address=shared.Items1(
                    city='Reno',
                    country='Taiwan',
                    line1='alias',
                    line2='quia',
                    postal_code='69078-1845',
                    region='odit',
                    type=shared.AccountingAddressType.UNKNOWN,
                ),
                email='Lillie92@yahoo.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Miss Alison Hayes',
                phone=[
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.MOBILE,
                    ),
                ],
                status=shared.CustomerStatus.ARCHIVED,
            ),
            shared.Contact(
                address=shared.Items1(
                    city='Grand Prairie',
                    country='Cocos (Keeling) Islands',
                    line1='expedita',
                    line2='voluptatum',
                    postal_code='38324-7423',
                    region='magnam',
                    type=shared.AccountingAddressType.DELIVERY,
                ),
                email='Mose.Bayer28@hotmail.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Glen Satterfield',
                phone=[
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.FAX,
                    ),
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                    shared.PhoneNumbersitems(
                        number='01224 658 999',
                        type=shared.PhoneNumberType.UNKNOWN,
                    ),
                ],
                status=shared.CustomerStatus.UNKNOWN,
            ),
            shared.Contact(
                address=shared.Items1(
                    city='Stillwater',
                    country='Guinea',
                    line1='reprehenderit',
                    line2='aperiam',
                    postal_code='34451',
                    region='error',
                    type=shared.AccountingAddressType.UNKNOWN,
                ),
                email='Jabari_Streich76@yahoo.com',
                modified_date='2022-10-23T00:00:00.000Z',
                name='Tonya Towne',
                phone=[
                    shared.PhoneNumbersitems(
                        number='(877) 492-8687',
                        type=shared.PhoneNumberType.LANDLINE,
                    ),
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
        ],
        customer_name='vero',
        default_currency='GBP',
        email_address='repudiandae',
        id='b1e5a2b1-2eb0-47f1-96db-99545fc95fa8',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='(509) 256-8772 x0977',
        registration_number='ipsum',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CustomerStatus.ARCHIVED,
        supplemental_data=shared.SupplementalData(
            content={
                "doloremque": {
                    "veniam": 'libero',
                    "architecto": 'cupiditate',
                },
                "molestiae": {
                    "possimus": 'non',
                    "magnam": 'itaque',
                    "sed": 'asperiores',
                    "veniam": 'consequuntur',
                },
                "facere": {
                    "odit": 'pariatur',
                    "amet": 'exercitationem',
                    "ab": 'velit',
                },
            },
        ),
        tax_number='facilis',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=731065,
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

