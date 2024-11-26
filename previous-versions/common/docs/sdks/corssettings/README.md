# CorsSettings
(*connection_management.cors_settings*)

## Overview

### Available Operations

* [get](#get) - Get CORS settings
* [set](#set) - Set CORS settings

## get

﻿The *Get CORS settings* endpoint returns the allowed origins (i.e. your domains) you want to allow cross-origin resource sharing ([CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)) with Codat. 

Enabling CORS with Codat is required by our embeddable [Connections SDK](https://docs.codat.io/auth-flow/optimize/connection-management) to access Codat's API endpoints.

The embeddable [Connections SDK](https://docs.codat.io/auth-flow/optimize/connection-management) lets your customers control access to their data by allowing them to manage their existing connections.

### Example Usage

```python
from codat_common import CodatCommon

s = CodatCommon(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.connection_management.cors_settings.get()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConnectionManagementAllowedOrigins](../../models/connectionmanagementallowedorigins.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| models.SDKError             | 4xx-5xx                     | */*                         |


## set

﻿The *Set CORS settings* endpoint allows you to register allowed origins (i.e. your domains) for use in cross-origin resource sharing ([CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)).
 
Enabling CORS with Codat is required by our embeddable [Connections SDK](https://docs.codat.io/auth-flow/optimize/connection-management) to access Codat's API endpoints. 

The embeddable [Connections SDK](https://docs.codat.io/auth-flow/optimize/connection-management) lets your customers control access to their data by allowing them to manage their existing connections.

### Example Usage

```python
from codat_common import CodatCommon

s = CodatCommon(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.connection_management.cors_settings.set(request={
    "allowed_origins": [
        "https://www.bank-of-dave.com",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.ConnectionManagementAllowedOrigins](../../models/connectionmanagementallowedorigins.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.ConnectionManagementAllowedOrigins](../../models/connectionmanagementallowedorigins.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| models.SDKError             | 4xx-5xx                     | */*                         |