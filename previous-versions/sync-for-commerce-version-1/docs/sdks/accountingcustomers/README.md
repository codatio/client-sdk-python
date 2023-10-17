# AccountingCustomers
(*accounting_customers*)

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
                type=shared.AccountingAddressType.DELIVERY,
            ),
        ],
        contacts=[
            shared.Contact(
                address=shared.Items1(
                    type=shared.AccountingAddressType.UNKNOWN,
                ),
                modified_date='2022-10-23T00:00:00.000Z',
                phone=[
                    shared.PhoneNumbersitems(
                        number='+44 25691 154789',
                        type=shared.PhoneNumberType.PRIMARY,
                    ),
                ],
                status=shared.CustomerStatus.ACTIVE,
            ),
        ],
        default_currency='GBP',
        metadata=shared.Metadata(),
        modified_date='2022-10-23T00:00:00.000Z',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CustomerStatus.UNKNOWN,
        supplemental_data=shared.SupplementalData(
            content={
                "California": {
                    "systems": 'North',
                },
            },
        ),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.accounting_customers.create_accounting_customer(req)

if res.accounting_create_customer_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAccountingCustomerRequest](../../models/operations/createaccountingcustomerrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |


### Response

**[operations.CreateAccountingCustomerResponse](../../models/operations/createaccountingcustomerresponse.md)**

