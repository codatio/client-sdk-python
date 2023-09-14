# configuration

## Overview

Manage mapping options and sync configuration.

### Available Operations

* [get](#get) - Get company configuration
* [get_mapping_options](#get_mapping_options) - Mapping options
* [set](#set) - Set company configuration

## get

Gets a companies expense sync configuration

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCompanyConfigurationRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.configuration.get(req)

if res.company_configuration is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetCompanyConfigurationRequest](../../models/operations/getcompanyconfigurationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.GetCompanyConfigurationResponse](../../models/operations/getcompanyconfigurationresponse.md)**


## get_mapping_options

Gets the expense mapping options for a companies accounting software

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetMappingOptionsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.configuration.get_mapping_options(req)

if res.mapping_options is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetMappingOptionsRequest](../../models/operations/getmappingoptionsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |


### Response

**[operations.GetMappingOptionsResponse](../../models/operations/getmappingoptionsresponse.md)**


## set

Sets a companies expense sync configuration

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.SetCompanyConfigurationRequest(
    company_configuration=shared.CompanyConfiguration(
        bank_account=shared.BankAccount(
            id='32',
        ),
        customer=shared.Customer(
            addresses=[
                shared.Items(
                    city='Fort Donnybury',
                    country='Kyrgyz Republic',
                    line1='minus',
                    line2='placeat',
                    postal_code='45398-0306',
                    region='perferendis',
                    type=shared.AccountingAddressType.BILLING,
                ),
            ],
            contact_name='repellendus',
            contacts=[
                shared.Contact(
                    address=shared.Items(
                        city='San Antonio',
                        country='Burundi',
                        line1='at',
                        line2='at',
                        postal_code='47845-7617',
                        region='officia',
                        type=shared.AccountingAddressType.BILLING,
                    ),
                    email='Kale_Welch10@gmail.com',
                    modified_date='2022-10-23T00:00:00.000Z',
                    name='Pauline Dibbert',
                    phone=[
                        shared.ContactPhone(
                            number='(877) 492-8687',
                            type=shared.PhoneNumberType.LANDLINE,
                        ),
                    ],
                    status=shared.CustomerStatus.ACTIVE,
                ),
            ],
            customer_name='aspernatur',
            default_currency='GBP',
            email_address='ad',
            id='929396fe-a759-46eb-90fa-aa2352c59559',
            metadata=shared.Metadata(
                is_deleted=False,
            ),
            modified_date='2022-10-23T00:00:00.000Z',
            phone='799.262.6196 x524',
            registration_number='quam',
            source_modified_date='2022-10-23T00:00:00.000Z',
            status=shared.CustomerStatus.UNKNOWN,
            supplemental_data=shared.SupplementalData(
                content={
                    "error": {
                        "quia": 'quis',
                    },
                },
            ),
            tax_number='vitae',
        ),
        supplier=shared.Supplier(
            addresses=[
                shared.SupplierAccountingAddress(
                    city='O'Konborough',
                    country='Burkina Faso',
                    line1='quo',
                    line2='sequi',
                    postal_code='36800-6860',
                    region='reiciendis',
                    type=shared.AccountingAddressType.DELIVERY,
                ),
            ],
            contact_name='vero',
            default_currency='nihil',
            email_address='praesentium',
            id='f097b007-4f15-4471-b5e6-e13b99d488e1',
            metadata=shared.Metadata(
                is_deleted=False,
            ),
            modified_date='2022-10-23T00:00:00.000Z',
            phone='(877) 492-8687',
            registration_number='veritatis',
            source_modified_date='2022-10-23T00:00:00.000Z',
            status=shared.SupplierStatus.UNKNOWN,
            supplemental_data=shared.SupplierSupplementalData(
                content={
                    "enim": {
                        "consequatur": 'est',
                    },
                },
            ),
            supplier_name='quibusdam',
            tax_number='explicabo',
        ),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.configuration.set(req)

if res.company_configuration is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.SetCompanyConfigurationRequest](../../models/operations/setcompanyconfigurationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.SetCompanyConfigurationResponse](../../models/operations/setcompanyconfigurationresponse.md)**

