# supplemental_data

## Overview

View and configure supplemental data for supported data types.

### Available Operations

* [configure](#configure) - Configure
* [get_configuration](#get_configuration) - Get configuration

## configure

The *Configure* endpoint allows you to maintain or change configuration required to return supplemental data for each integration and data type combination.

[Supplemental data](https://docs.codat.io/using-the-api/additional-data) is additional data you can include in Codat's standard data types.

**Integration-specific behaviour**
See the *examples* for integration-specific frequently requested properties.

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.ConfigureSupplementalDataRequest(
    supplemental_data_configuration=shared.SupplementalDataConfiguration(
        supplemental_data_config={
            "dolor": shared.SupplementalDataConfigurationSupplementalDataSourceConfiguration(
                data_source='natus',
                pull_data={
                    "laboriosam": 'hic',
                },
                push_data={
                    "saepe": 'fuga',
                },
            ),
        },
    ),
    data_type=operations.ConfigureSupplementalDataDataType.INVOICES,
    platform_key='in',
)

res = s.supplemental_data.configure(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ConfigureSupplementalDataRequest](../../models/operations/configuresupplementaldatarequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.ConfigureSupplementalDataResponse](../../models/operations/configuresupplementaldataresponse.md)**


## get_configuration

The *Get configuration* endpoint returns supplemental data configuration previously created for each integration and data type combination.

[Supplemental data](https://docs.codat.io/using-the-api/additional-data) is additional data you can include in Codat's standard data types.

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.GetSupplementalDataConfigurationRequest(
    data_type=operations.GetSupplementalDataConfigurationDataType.INVOICES,
    platform_key='corporis',
)

res = s.supplemental_data.get_configuration(req)

if res.supplemental_data_configuration is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetSupplementalDataConfigurationRequest](../../models/operations/getsupplementaldataconfigurationrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |


### Response

**[operations.GetSupplementalDataConfigurationResponse](../../models/operations/getsupplementaldataconfigurationresponse.md)**

