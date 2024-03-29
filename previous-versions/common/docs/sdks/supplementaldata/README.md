# SupplementalData
(*supplemental_data*)

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
import codatcommon
from codatcommon.models import operations, shared

s = codatcommon.CodatCommon(
    auth_header="",
)

req = operations.ConfigureSupplementalDataRequest(
    supplemental_data_configuration=shared.SupplementalDataConfiguration(
        supplemental_data_config={
            "Cutler": shared.SupplementalDataConfigurationSupplementalDataSourceConfiguration(
                pull_data={
                    "North": 'transmitter',
                },
                push_data={
                    "infrastructure": 'Northeast',
                },
            ),
        },
    ),
    data_type=operations.ConfigureSupplementalDataDataType.INVOICES,
    platform_key='gbol',
)

res = s.supplemental_data.configure(req)

if res.status_code == 200:
    # handle response
    pass
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
import codatcommon
from codatcommon.models import operations, shared

s = codatcommon.CodatCommon(
    auth_header="",
)

req = operations.GetSupplementalDataConfigurationRequest(
    data_type=operations.GetSupplementalDataConfigurationDataType.INVOICES,
    platform_key='gbol',
)

res = s.supplemental_data.get_configuration(req)

if res.supplemental_data_configuration is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetSupplementalDataConfigurationRequest](../../models/operations/getsupplementaldataconfigurationrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |


### Response

**[operations.GetSupplementalDataConfigurationResponse](../../models/operations/getsupplementaldataconfigurationresponse.md)**

