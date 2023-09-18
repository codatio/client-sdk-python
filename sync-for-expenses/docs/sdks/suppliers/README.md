# Suppliers

## Overview

Suppliers

### Available Operations

* [create](#create) - Create supplier
* [get](#get) - Get supplier
* [list](#list) - List suppliers
* [update](#update) - Update supplier

## create

The *Create supplier* endpoint creates a new [supplier](https://docs.codat.io/accounting-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating an account.


### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.SupplierAccountingAddress(
                city='Purdystead',
                country='Antarctica (the territory South of 60 deg S)',
                line1='porro',
                line2='consequuntur',
                postal_code='60562-9926',
                region='dolorum',
                type=shared.AccountingAddressType.BILLING,
            ),
        ],
        contact_name='pariatur',
        default_currency='provident',
        email_address='nobis',
        id='bf486333-23f9-4b77-b3a4-100674ebf692',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='+44 25691 154789',
        registration_number='fugiat',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.SupplierStatus.ARCHIVED,
        supplemental_data=shared.SupplierSupplementalData(
            content={
                "dolorum": {
                    "iusto": 'voluptate',
                },
            },
        ),
        supplier_name='dolorum',
        tax_number='deleniti',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=607045,
)

res = s.suppliers.create(req)

if res.create_supplier_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateSupplierRequest](../../models/operations/createsupplierrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.CreateSupplierResponse](../../models/operations/createsupplierresponse.md)**


## get

The *Get supplier* endpoint returns a single supplier for a given supplierId.

[Suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support getting a specific supplier.

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

req = operations.GetSupplierRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    supplier_id='EILBDVJVNUAGVKRQ',
)

res = s.suppliers.get(req)

if res.supplier is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetSupplierRequest](../../models/operations/getsupplierrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |


### Response

**[operations.GetSupplierResponse](../../models/operations/getsupplierresponse.md)**


## list

The *List suppliers* endpoint returns a list of [suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

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

req = operations.ListSuppliersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='distinctio',
)

res = s.suppliers.list(req)

if res.suppliers is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListSuppliersRequest](../../models/operations/listsuppliersrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.ListSuppliersResponse](../../models/operations/listsuppliersresponse.md)**


## update

The *Update supplier* endpoint updates an existing [supplier](https://docs.codat.io/accounting-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating an account.


### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.SupplierAccountingAddress(
                city='Lake Havasu City',
                country='Croatia',
                line1='voluptate',
                line2='id',
                postal_code='21027-8393',
                region='deserunt',
                type=shared.AccountingAddressType.BILLING,
            ),
        ],
        contact_name='minima',
        default_currency='repellendus',
        email_address='totam',
        id='a0d446ce-2af7-4a73-8f3b-e453f870b326',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='(877) 492-8687',
        registration_number='deserunt',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.SupplierStatus.UNKNOWN,
        supplemental_data=shared.SupplierSupplementalData(
            content={
                "incidunt": {
                    "qui": 'cupiditate',
                },
            },
        ),
        supplier_name='maxime',
        tax_number='pariatur',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    supplier_id='7110701885',
    timeout_in_minutes=117531,
)

res = s.suppliers.update(req)

if res.update_supplier_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateSupplierRequest](../../models/operations/updatesupplierrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.UpdateSupplierResponse](../../models/operations/updatesupplierresponse.md)**

