# ConnectionManagement
(*connection_management*)

## Overview

Configure UI and retrieve access tokens for authentication used by **Connections SDK**.

### Available Operations

* [~~get~~](#get) - Get access token (old) :warning: **Deprecated** Use [get_access_token](docs/sdks/companies/README.md#get_access_token) instead.

## ~~get~~

﻿The new `/companies/{companyId}/accessToken` endpoint replaces this endpoint and includes additional functionality.

Use the *Get access token* endpoint to retrieve a new access token for use with the [Connections SDK](https://docs.codat.io/auth-flow/optimize/connection-management). The token is only valid for one hour and applies to a single company.

The embeddable [Connections SDK](https://docs.codat.io/auth-flow/optimize/connection-management) lets your customers control access to their data by allowing them to manage their existing connections.

> :warning: **DEPRECATED**: The endpoint for generating company-specific connection management access tokens has been deprecated.
Codat now supports a global company access token, providing seamless access across multiple products.
Update your integration to use the global token for improved efficiency and consistency.
. Use `get_access_token` instead.

### Example Usage

```python
from codat_platform import CodatPlatform
from codat_platform.models import shared

with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_platform:

    res = codat_platform.connection_management.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetConnectionManagementAccessTokenRequest](../../models/operations/getconnectionmanagementaccesstokenrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[shared.ConnectionManagementAccessToken](../../models/shared/connectionmanagementaccesstoken.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 401, 402, 403, 404, 429, 500, 503 | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |