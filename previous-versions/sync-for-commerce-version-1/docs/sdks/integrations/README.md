# Integrations

## Overview

View useful information about codat's integrations.

### Available Operations

* [get_integration_branding](#get_integration_branding) - Get branding for an integration
* [list_integrations](#list_integrations) - List information on Codat's supported integrations

## get_integration_branding

Retrieve Integration branding assets.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetIntegrationBrandingRequest(
    platform_key='quis',
)

res = s.integrations.get_integration_branding(req)

if res.branding is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetIntegrationBrandingRequest](../../models/operations/getintegrationbrandingrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |


### Response

**[operations.GetIntegrationBrandingResponse](../../models/operations/getintegrationbrandingresponse.md)**


## list_integrations

Retrieve a list of available integrations support by datatype and state of release.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListIntegrationsRequest(
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='beatae',
)

res = s.integrations.list_integrations(req)

if res.integrations is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListIntegrationsRequest](../../models/operations/listintegrationsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.ListIntegrationsResponse](../../models/operations/listintegrationsresponse.md)**

