# Cors
(*cors*)

## Overview

### Available Operations

* [~~get~~](#get) - Get CORS settings (old) :warning: **Deprecated** Use [get](docs/sdks/settings/README.md#get) instead.
* [~~set~~](#set) - Set CORS settings (old) :warning: **Deprecated** Use [set](docs/sdks/settings/README.md#set) instead.

## ~~get~~

﻿The *Get CORS settings* endpoint returns the allowed origins (i.e. your domains) you want to allow cross-origin resource sharing ([CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)) with Codat. 

Enabling CORS with Codat is required by our embeddable UIs (such as [Connections SDK](https://docs.codat.io/auth-flow/optimize/connection-management) and [Link SDK](https://docs.codat.io/auth-flow/authorize-embedded-link)) to access Codat's API endpoints.

> :warning: **DEPRECATED**: The new [Get CORS settings](https://docs.codat.io/platform-api#/operations/get-cors-settings) endpoint replaces this endpoint and includes additional functionality.
Update your integrations to use the new path `/corsSettings` as the existing route will be removed in a future release.
. Use `get` instead.

### Example Usage

```python
from codat_platform import CodatPlatform
from codat_platform.models import shared

with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.cors.get()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[shared.ConnectionManagementAllowedOrigins](../../models/shared/connectionmanagementallowedorigins.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## ~~set~~

﻿The *Set CORS settings* endpoint allows you to register allowed origins (i.e. your domains) for use in cross-origin resource sharing ([CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)).
 
Enabling CORS with Codat is required by our embeddable UIs (such as [Connections SDK](https://docs.codat.io/auth-flow/optimize/connection-management) and [Link SDK](https://docs.codat.io/auth-flow/authorize-embedded-link)) to access Codat's API endpoints. 

> :warning: **DEPRECATED**: The new [Set CORS settings](https://docs.codat.io/platform-api#/operations/set-cors-settings) endpoint replaces this endpoint and includes additional functionality.
Update your integrations to use the new path `/corsSettings` as the existing route will be removed in a future release.
. Use `set` instead.

### Example Usage

```python
from codat_platform import CodatPlatform
from codat_platform.models import shared

with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.cors.set(request={
        "allowed_origins": [
            "https://www.bank-of-dave.com",
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [shared.ConnectionManagementAllowedOrigins](../../models/shared/connectionmanagementallowedorigins.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[shared.ConnectionManagementAllowedOrigins](../../models/shared/connectionmanagementallowedorigins.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |