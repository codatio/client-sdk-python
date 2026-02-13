# ~~ConnectionManagement~~

> [!WARNING]
> This SDK is **DEPRECATED**

## Overview

Configure UI and retrieve access tokens for authentication used by **Connections SDK**.

### Available Operations

* [~~get~~](#get) - Get access token (old) :warning: **Deprecated** Use [get_access_token](docs/sdks/companies/README.md#get_access_token) instead.

## ~~get~~

﻿The new [Get company access token](https://docs.codat.io/platform-api#/operations/get-company-access-token) endpoint replaces this endpoint and includes additional functionality.

> :warning: **DEPRECATED**: The endpoint for generating company-specific connection management access tokens has been deprecated.
Codat now supports a global company access token, providing seamless access across multiple products.
Update your integration to use the global token for improved efficiency and consistency.
. Use `get_access_token` instead.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-connection-management-access-token" method="get" path="/companies/{companyId}/connectionManagement/accessToken" example="Access token" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.connection_management.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

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

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |