# CustomDataType

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

### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="configure-custom-data-type" method="put" path="/integrations/{platformKey}/dataTypes/custom/{customDataIdentifier}" example="Dynamics 365 Business Central" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.custom_data_type.configure(request={
        "custom_data_type_configuration": {
            "data_source": "api/purchaseOrders",
            "key_by": [
                "$[*].id",
            ],
            "required_data": {
                "currency": "$[*].currencyCode",
                "number": "$[*].number",
                "date": "$[*].orderDate",
                "totalexvat": "$[*].totalAmountExcludingTax",
                "totaltax": "$[*].totalTaxAmount",
                "vendor": "$[*].number",
            },
            "source_modified_date": [
                "$[*].lastModifiedDateTime",
            ],
        },
        "custom_data_identifier": "DynamicsPurchaseOrders",
        "platform_key": "gbol",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="configure-custom-data-type" method="put" path="/integrations/{platformKey}/dataTypes/custom/{customDataIdentifier}" example="QuickBooks Online" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.custom_data_type.configure(request={
        "custom_data_type_configuration": {
            "data_source": "/query?query=select * from Account",
            "key_by": [
                "$.Id",
            ],
            "required_data": {
                "id": "$.Id",
                "Currentbal": "$.CurrentBalance",
                "SubAcc": "$.SubAccount",
            },
            "source_modified_date": [
                "$.time",
            ],
        },
        "custom_data_identifier": "DynamicsPurchaseOrders",
        "platform_key": "gbol",
    })

    # Handle response
    print(res)

```
### Example Usage: Unauthorized

<!-- UsageSnippet language="python" operationID="configure-custom-data-type" method="put" path="/integrations/{platformKey}/dataTypes/custom/{customDataIdentifier}" example="Unauthorized" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.custom_data_type.configure(request={
        "custom_data_type_configuration": {
            "data_source": "api/purchaseOrders?$filter=currencyCode eq 'NOK'",
            "key_by": [
                "$[*].id",
            ],
            "required_data": {
                "currencyCode": "$[*].currencyCode",
                "id": "$[*].id",
                "number": "$[*].number",
                "orderDate": "$[*].orderDate",
                "totalAmountExcludingTax": "$[*].totalAmountExcludingTax",
                "totalTaxAmount": "$[*].totalTaxAmount",
                "vendorName": "$[*].number",
            },
            "source_modified_date": [
                "$[*].lastModifiedDateTime",
            ],
        },
        "custom_data_identifier": "DynamicsPurchaseOrders",
        "platform_key": "gbol",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero Mapping Arrays

<!-- UsageSnippet language="python" operationID="configure-custom-data-type" method="put" path="/integrations/{platformKey}/dataTypes/custom/{customDataIdentifier}" example="Xero Mapping Arrays" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.custom_data_type.configure(request={
        "custom_data_type_configuration": {
            "data_source": "/api.xro/2.0/Invoices",
            "key_by": [
                "$.InvoiceID",
            ],
            "required_data": {
                "invNumber": "$.InvoiceNumber",
                "type": "$.Type",
                "InvoiceID": "$.InvoiceID",
                "lines": "$.LineItems[*]",
            },
            "source_modified_date": [
                "$.UpdatedDateUTC",
            ],
        },
        "custom_data_identifier": "DynamicsPurchaseOrders",
        "platform_key": "gbol",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero Simple Record

<!-- UsageSnippet language="python" operationID="configure-custom-data-type" method="put" path="/integrations/{platformKey}/dataTypes/custom/{customDataIdentifier}" example="Xero Simple Record" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.custom_data_type.configure(request={
        "custom_data_type_configuration": {
            "data_source": "/api.xro/2.0/Accounts",
            "key_by": [
                "$.AccountID",
            ],
            "required_data": {
                "code": "$.Code",
                "accountId": "$.AccountID",
                "type": "$.Type",
                "SysAcc": "$.SystemAccount",
            },
        },
        "custom_data_identifier": "DynamicsPurchaseOrders",
        "platform_key": "gbol",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ConfigureCustomDataTypeRequest](../../models/operations/configurecustomdatatyperequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[shared.CustomDataTypeConfiguration](../../models/shared/customdatatypeconfiguration.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_configuration

The *Get custom data configuration* endpoint returns existing configuration details for the specified custom data type and integration pair you previously configured.

A [custom data type](https://docs.codat.io/using-the-api/custom-data) is an additional data type you can create that is not included in Codat's standardized data model.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-custom-data-type-configuration" method="get" path="/integrations/{platformKey}/dataTypes/custom/{customDataIdentifier}" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.custom_data_type.get_configuration(request={
        "custom_data_identifier": "DynamicsPurchaseOrders",
        "platform_key": "gbol",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetCustomDataTypeConfigurationRequest](../../models/operations/getcustomdatatypeconfigurationrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[shared.CustomDataTypeRecords](../../models/shared/customdatatyperecords.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list

The *List custom data type records* endpoint returns a paginated list of records pulled for the specified custom data type you previously configured.

A [custom data type](https://docs.codat.io/using-the-api/custom-data) is an additional data type you can create that is not included in Codat's standardized data model.s endpoint returns a paginated list of records whose schema is defined [Configure custom data type](https://docs.codat.io/platform-api#/operations/configure-custom-data-type)

### Example Usage

<!-- UsageSnippet language="python" operationID="list-custom-data-type-records" method="get" path="/companies/{companyId}/connections/{connectionId}/data/custom/{customDataIdentifier}" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.custom_data_type.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "custom_data_identifier": "DynamicsPurchaseOrders",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListCustomDataTypeRecordsRequest](../../models/operations/listcustomdatatyperecordsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[shared.CustomDataTypeRecords](../../models/shared/customdatatyperecords.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 429, 451 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## refresh

The *Refresh custom data type* endpoint refreshes the specified custom data type for a given company. This is an asynchronous operation that will sync updated data from the linked integration into Codat for you to view.

### Example Usage

<!-- UsageSnippet language="python" operationID="refresh-custom-data-type" method="post" path="/companies/{companyId}/connections/{connectionId}/data/queue/custom/{customDataIdentifier}" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.custom_data_type.refresh(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "custom_data_identifier": "DynamicsPurchaseOrders",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RefreshCustomDataTypeRequest](../../models/operations/refreshcustomdatatyperequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[shared.PullOperation](../../models/shared/pulloperation.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 401, 402, 403, 404, 429, 451 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |