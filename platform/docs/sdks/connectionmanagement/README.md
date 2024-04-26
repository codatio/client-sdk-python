# ConnectionManagement
(*connection_management*)

## Overview

Configure connection management UI and retrieve access tokens for authentication.

### Available Operations

* [get_access_token](#get_access_token) - Get access token

## get_access_token

﻿Use the *Get access token* endpoint to retrieve a new access token for use by the [connection management UI](https://docs.codat.io/auth-flow/optimize/connection-management).

The embedded [connection management UI](https://docs.codat.io/auth-flow/optimize/connection-management) lets your customers control access to their data by allowing them to manage their existing connections.

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetConnectionManagementAccessTokenRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.connection_management.get_access_token(req)

if res.connection_management_access_token is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetConnectionManagementAccessTokenRequest](../../models/operations/getconnectionmanagementaccesstokenrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |


### Response

**[operations.GetConnectionManagementAccessTokenResponse](../../models/operations/getconnectionmanagementaccesstokenresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |
