# CodatLendingSuppliers
(*loan_writeback.suppliers*)

### Available Operations

* [create](#create) - Create supplier
* [get_create_update_model](#get_create_update_model) - Get create/update supplier model

## create

The *Create supplier* endpoint creates a new [supplier](https://docs.codat.io/lending-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/lending-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/lending-api#/operations/get-create-update-suppliers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating an account.


### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateSupplierRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    accounting_supplier=shared.AccountingSupplier(
        status=shared.SupplierStatus.UNKNOWN,
        addresses=[
            shared.AccountingAddress(
                type=shared.AccountingAddressType.BILLING,
                city='Bakersfield',
                country='USA',
                line1='Unit 51',
                line2='Bakersfield Industrial Estate',
                region='California',
            ),
        ],
        contact_name='Kelly\'s Industrial Supplies',
        default_currency='string',
        email_address='sales@kellysupplies.com',
        id='C520FFD4-F6F6-4FC2-A6D2-5D7088B2B14F',
        metadata=shared.Metadata(
            is_deleted=True,
        ),
        modified_date='2022-10-23T00:00:00Z',
        phone='07999 999999',
        registration_number='string',
        source_modified_date='2022-10-23T00:00:00Z',
        supplemental_data=shared.SupplementalData(
            content={
                'property1': {
                    'property1': None,
                    'property2': None,
                },
                'property2': {
                    'property1': None,
                    'property2': None,
                },
            },
        ),
        supplier_name='Kelly\'s Industrial Supplies',
        tax_number='string',
    ),
)

res = s.loan_writeback.suppliers.create(req)

if res.accounting_create_supplier_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateSupplierRequest](../../models/operations/createsupplierrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.CreateSupplierResponse](../../models/operations/createsupplierresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4x-5xx                          | */*                             |

## get_create_update_model

The *Get create/update supplier model* endpoint returns the expected data for the request payload when creating and updating a [supplier](https://docs.codat.io/lending-api#/schemas/Supplier) for a given company and integration.

[Suppliers](https://docs.codat.io/lending-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating and updating a supplier.


### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateSuppliersModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.loan_writeback.suppliers.get_create_update_model(req)

if res.push_option is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetCreateUpdateSuppliersModelRequest](../../models/operations/getcreateupdatesuppliersmodelrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |


### Response

**[operations.GetCreateUpdateSuppliersModelResponse](../../models/operations/getcreateupdatesuppliersmodelresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |
