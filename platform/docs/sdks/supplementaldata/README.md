# SupplementalData

## Overview

Configure and pull additional data you can include in Codat's standard data types.

### Available Operations

* [configure](#configure) - Configure
* [get_configuration](#get_configuration) - Get configuration

## configure

The *Configure* endpoint allows you to maintain or change configuration required to return supplemental data for each integration and data type combination.

[Supplemental data](https://docs.codat.io/using-the-api/supplemental-data/overview) is additional data you can include in Codat's standard data types.

**Integration-specific behavior**
See the *examples* for integration-specific frequently requested properties.

### Example Usage: QBO - Customers

<!-- UsageSnippet language="python" operationID="configure-supplemental-data" method="put" path="/integrations/{platformKey}/dataTypes/{dataType}/supplementalDataConfig" example="QBO - Customers" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import operations, shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.supplemental_data.configure(request={
        "supplemental_data_configuration": {},
        "data_type": operations.DataType.INVOICES,
        "platform_key": "gbol",
    })

    # Use the SDK ...

```
### Example Usage: QBO - Invoices

<!-- UsageSnippet language="python" operationID="configure-supplemental-data" method="put" path="/integrations/{platformKey}/dataTypes/{dataType}/supplementalDataConfig" example="QBO - Invoices" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import operations, shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.supplemental_data.configure(request={
        "supplemental_data_configuration": {},
        "data_type": operations.DataType.INVOICES,
        "platform_key": "gbol",
    })

    # Use the SDK ...

```
### Example Usage: Unauthorized

<!-- UsageSnippet language="python" operationID="configure-supplemental-data" method="put" path="/integrations/{platformKey}/dataTypes/{dataType}/supplementalDataConfig" example="Unauthorized" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import operations, shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.supplemental_data.configure(request={
        "supplemental_data_configuration": {
            "supplemental_data_config": {
                "orders-supplemental-data": {
                    "data_source": "/orders",
                    "pull_data": {
                        "orderNumber": "order_num",
                    },
                    "push_data": {
                        "orderNumber": "order_num",
                    },
                },
            },
        },
        "data_type": operations.DataType.INVOICES,
        "platform_key": "gbol",
    })

    # Use the SDK ...

```
### Example Usage: Xero - Accounts

<!-- UsageSnippet language="python" operationID="configure-supplemental-data" method="put" path="/integrations/{platformKey}/dataTypes/{dataType}/supplementalDataConfig" example="Xero - Accounts" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import operations, shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.supplemental_data.configure(request={
        "supplemental_data_configuration": {},
        "data_type": operations.DataType.INVOICES,
        "platform_key": "gbol",
    })

    # Use the SDK ...

```
### Example Usage: Xero - Contacts

<!-- UsageSnippet language="python" operationID="configure-supplemental-data" method="put" path="/integrations/{platformKey}/dataTypes/{dataType}/supplementalDataConfig" example="Xero - Contacts" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import operations, shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.supplemental_data.configure(request={
        "supplemental_data_configuration": {},
        "data_type": operations.DataType.INVOICES,
        "platform_key": "gbol",
    })

    # Use the SDK ...

```
### Example Usage: Xero - Invoices

<!-- UsageSnippet language="python" operationID="configure-supplemental-data" method="put" path="/integrations/{platformKey}/dataTypes/{dataType}/supplementalDataConfig" example="Xero - Invoices" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import operations, shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.supplemental_data.configure(request={
        "supplemental_data_configuration": {},
        "data_type": operations.DataType.INVOICES,
        "platform_key": "gbol",
    })

    # Use the SDK ...

```
### Example Usage: Xero - Items

<!-- UsageSnippet language="python" operationID="configure-supplemental-data" method="put" path="/integrations/{platformKey}/dataTypes/{dataType}/supplementalDataConfig" example="Xero - Items" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import operations, shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.supplemental_data.configure(request={
        "supplemental_data_configuration": {},
        "data_type": operations.DataType.INVOICES,
        "platform_key": "gbol",
    })

    # Use the SDK ...

```
### Example Usage: Xero - Tax rates

<!-- UsageSnippet language="python" operationID="configure-supplemental-data" method="put" path="/integrations/{platformKey}/dataTypes/{dataType}/supplementalDataConfig" example="Xero - Tax rates" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import operations, shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.supplemental_data.configure(request={
        "supplemental_data_configuration": {},
        "data_type": operations.DataType.INVOICES,
        "platform_key": "gbol",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ConfigureSupplementalDataRequest](../../models/operations/configuresupplementaldatarequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_configuration

The *Get configuration* endpoint returns supplemental data configuration previously created for each integration and data type combination.

[Supplemental data](https://docs.codat.io/using-the-api/supplemental-data/overview) is additional data you can include in Codat's standard data types.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-supplemental-data-configuration" method="get" path="/integrations/{platformKey}/dataTypes/{dataType}/supplementalDataConfig" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import operations, shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.supplemental_data.get_configuration(request={
        "data_type": operations.PathParamDataType.INVOICES,
        "platform_key": "gbol",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetSupplementalDataConfigurationRequest](../../models/operations/getsupplementaldataconfigurationrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[shared.SupplementalDataConfiguration](../../models/shared/supplementaldataconfiguration.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |