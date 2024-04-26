# CustomDataType
(*custom_data_type*)

## Overview

Configure and pull additional data types that are not included in Codat's standardized data model.

### Available Operations

* [configure](#configure) - Configure custom data type
* [get_configuration](#get_configuration) - Get custom data configuration
* [list](#list) - List custom data type records
* [refresh](#refresh) - Refresh custom data type

## configure

The *Configure custom data type* endpoint allows you to maintain or change the configuration required to return a custom data type for a specific integration. 

A [custom data type](https://docs.codat.io/using-the-api/custom-data) is an additional data type you can create that is not included in Codat's standardized data model.

### Tips and traps

- You can only configure a single custom data type for a single platform at a time. Use the endpoint multiple times if you need to configure it for multiple platforms. 

- You can only indicate a single data source for each customer data type. 

- Make your custom configuration as similar as possible to our standard data types so you can interact with them in exactly the same way.

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ConfigureCustomDataTypeRequest(
    custom_data_identifier='DynamicsPurchaseOrders',
    platform_key='gbol',
    custom_data_type_configuration=shared.CustomDataTypeConfiguration(
        data_source='api/purchaseOrders?$filter=currencyCode eq \'NOK\'',
        key_by=[
            '$[*].id',
        ],
        required_data={
            'currencyCode': '$[*].currencyCode',
            'id': '$[*].id',
            'number': '$[*].number',
            'orderDate': '$[*].orderDate',
            'totalAmountExcludingTax': '$[*].totalAmountExcludingTax',
            'totalTaxAmount': '$[*].totalTaxAmount',
            'vendorName': '$[*].number',
        },
        source_modified_date=[
            '$[*].lastModifiedDateTime',
        ],
    ),
)

res = s.custom_data_type.configure(req)

if res.custom_data_type_configuration is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ConfigureCustomDataTypeRequest](../../models/operations/configurecustomdatatyperequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.ConfigureCustomDataTypeResponse](../../models/operations/configurecustomdatatyperesponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## get_configuration

The *Get custom data configuration* endpoint returns existing configuration details for the specified custom data type and integration pair you previously configured.

A [custom data type](https://docs.codat.io/using-the-api/custom-data) is an additional data type you can create that is not included in Codat's standardized data model.

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCustomDataTypeConfigurationRequest(
    custom_data_identifier='DynamicsPurchaseOrders',
    platform_key='gbol',
)

res = s.custom_data_type.get_configuration(req)

if res.custom_data_type_records is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetCustomDataTypeConfigurationRequest](../../models/operations/getcustomdatatypeconfigurationrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |


### Response

**[operations.GetCustomDataTypeConfigurationResponse](../../models/operations/getcustomdatatypeconfigurationresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## list

The *List custom data type records* endpoint returns a paginated list of records pulled for the specified custom data type you previously configured.

A [custom data type](https://docs.codat.io/using-the-api/custom-data) is an additional data type you can create that is not included in Codat's standardized data model.s endpoint returns a paginated list of records whose schema is defined [Configure custom data type](https://docs.codat.io/platform-api#/operations/configure-custom-data-type)

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListCustomDataTypeRecordsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    custom_data_identifier='DynamicsPurchaseOrders',
    page=1,
    page_size=100,
)

res = s.custom_data_type.list(req)

if res.custom_data_type_records is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListCustomDataTypeRecordsRequest](../../models/operations/listcustomdatatyperecordsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.ListCustomDataTypeRecordsResponse](../../models/operations/listcustomdatatyperecordsresponse.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.ErrorMessage                 | 400,401,402,403,404,429,451,500,503 | application/json                    |
| errors.SDKError                     | 4xx-5xx                             | */*                                 |

## refresh

The *Refresh custom data type* endpoint refreshes the specified custom data type for a given company. This is an asynchronous operation that will sync updated data from the linked integration into Codat for you to view.

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.RefreshCustomDataTypeRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    custom_data_identifier='DynamicsPurchaseOrders',
)

res = s.custom_data_type.refresh(req)

if res.pull_operation is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RefreshCustomDataTypeRequest](../../models/operations/refreshcustomdatatyperequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |


### Response

**[operations.RefreshCustomDataTypeResponse](../../models/operations/refreshcustomdatatyperesponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,429,451,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |
