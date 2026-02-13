# Settings

## Overview

Manage company profile configuration, sync settings, and API keys.

### Available Operations

* [create_api_key](#create_api_key) - Create API key
* [delete_api_key](#delete_api_key) - Delete API key
* [get](#get) - Get CORS settings
* [get_profile](#get_profile) - Get profile
* [get_sync_settings](#get_sync_settings) - Get sync settings
* [list_api_keys](#list_api_keys) - List API keys
* [set](#set) - Set CORS settings
* [update_profile](#update_profile) - Update profile
* [update_sync_settings](#update_sync_settings) - Update all sync settings

## create_api_key

Use the *Create API keys* endpoint to generate a new API key for your client.

[API keys](https://docs.codat.io/platform-api#/schemas/apiKeys) are tokens used to control access to the API. Include this token in the `Authorization` header parameter when making API calls, following the word "Basic" and a space with your API key.

You can [read more](https://docs.codat.io/using-the-api/authentication) about authentication at Codat and managing API keys via the Portal UI or API.

### Tips and pitfalls

* Your first API key is created for you. Access this key via [Codat's Portal](https://app.codat.io/developers/api-keys).
* If you require multiple API keys, perform multiple calls to the *Create API keys* endpoint. 
* The number of API keys is limited to 10. If you have reached the maximum amount of keys, use the *Delete API key* endpoint to delete an unused key first.

### Example Usage: API key details

<!-- UsageSnippet language="python" operationID="create-api-key" method="post" path="/apiKeys" example="API key details" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    })

    # Handle response
    print(res)

```
### Example Usage: API key details with name

<!-- UsageSnippet language="python" operationID="create-api-key" method="post" path="/apiKeys" example="API key details with name" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    })

    # Handle response
    print(res)

```
### Example Usage: Create API key with name

<!-- UsageSnippet language="python" operationID="create-api-key" method="post" path="/apiKeys" example="Create API key with name" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    })

    # Handle response
    print(res)

```
### Example Usage: Max length for name reached

<!-- UsageSnippet language="python" operationID="create-api-key" method="post" path="/apiKeys" example="Max length for name reached" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.CreateAPIKey](../../models/shared/createapikey.md)          | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[shared.APIKeyDetails](../../models/shared/apikeydetails.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 409, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_api_key

Use the *Delete API keys* endpoint to delete an existing API key, providing its valid `id` as a parameter. Note that this operation is not reversible.

[API keys](https://docs.codat.io/platform-api#/schemas/apiKeys) are tokens used to control access to the API. Include this token in the `Authorization` header parameter when making API calls, following the word "Basic" and a space with your API key.

You can [read more](https://docs.codat.io/using-the-api/authentication) about authentication at Codat and managing API keys via the Portal UI or API.

### Tips and pitfalls

* It is possible to delete the last remaining API key. If this happens, a new key can be created via the [API key management page](https://app.codat.io/developers/api-keys) of the Portal.
* It is possible to delete the API key used to authenticate the *Delete API key* request.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-api-key" method="delete" path="/apiKeys/{apiKeyId}" example="Conflict" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.delete_api_key(request={
        "api_key_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteAPIKeyRequest](../../models/operations/deleteapikeyrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[shared.ErrorMessage](../../models/shared/errormessage.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get

﻿The *Get CORS settings* endpoint returns the allowed origins (i.e. your domains) you want to allow cross-origin resource sharing ([CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)) with Codat. 

Enabling CORS with Codat is required by our embeddable UIs (such as [Connections SDK](https://docs.codat.io/auth-flow/optimize/connection-management) and [Link SDK](https://docs.codat.io/auth-flow/authorize-embedded-link)) to access Codat's API endpoints.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-cors-settings" method="get" path="/corsSettings" example="Allowed origins" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.get()

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

## get_profile

Fetch your Codat profile.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-profile" method="get" path="/profile" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.get_profile()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[shared.Profile](../../models/shared/profile.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.ErrorMessage | 401, 402, 403, 429  | application/json    |
| errors.ErrorMessage | 500, 503            | application/json    |
| errors.SDKError     | 4XX, 5XX            | \*/\*               |

## get_sync_settings

Retrieve the [sync settings](https://docs.codat.io/knowledge-base/advanced-sync-settings) for your client. This includes how often data types should be queued to be updated, and how much history should be fetched.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-profile-syncSettings" method="get" path="/profile/syncSettings" example="Example" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.get_sync_settings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[shared.SyncSettings](../../models/shared/syncsettings.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.ErrorMessage | 401, 402, 403, 429  | application/json    |
| errors.ErrorMessage | 500, 503            | application/json    |
| errors.SDKError     | 4XX, 5XX            | \*/\*               |

## list_api_keys

Use the *List API keys* endpoint to return a list of all API keys that currently exist for your client. This includes keys created via the Portal UI or the *Create API keys* endpoint.

[API keys](https://docs.codat.io/platform-api#/schemas/apiKeys) are tokens used to control access to the API. Include this token in the `Authorization` header parameter when making API calls, following the word "Basic" and a space with your API key.

You can [read more](https://docs.codat.io/using-the-api/authentication) about authentication at Codat and managing API keys via the Portal UI or API.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-api-keys" method="get" path="/apiKeys" example="Example" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.list_api_keys()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[shared.APIKeys](../../models/shared/apikeys.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.ErrorMessage | 401, 402, 403, 429  | application/json    |
| errors.ErrorMessage | 500, 503            | application/json    |
| errors.SDKError     | 4XX, 5XX            | \*/\*               |

## set

﻿The *Set CORS settings* endpoint allows you to register allowed origins (i.e. your domains) for use in cross-origin resource sharing ([CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)).
 
Enabling CORS with Codat is required by our embeddable UIs (such as [Connections SDK](https://docs.codat.io/auth-flow/optimize/connection-management) and [Link SDK](https://docs.codat.io/auth-flow/authorize-embedded-link)) to access Codat's API endpoints.

### Example Usage: Allowed origins

<!-- UsageSnippet language="python" operationID="set-cors-settings" method="post" path="/corsSettings" example="Allowed origins" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.set(request={
        "allowed_origins": [
            "https://www.bank-of-dave.com",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: Unauthorized

<!-- UsageSnippet language="python" operationID="set-cors-settings" method="post" path="/corsSettings" example="Unauthorized" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.set(request={
        "allowed_origins": [
            "https://www.bank-of-dave.com",
        ],
    })

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

## update_profile

Update your Codat profile

### Example Usage

<!-- UsageSnippet language="python" operationID="update-profile" method="put" path="/profile" example="Unauthorized" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.update_profile(request={
        "confirm_company_name": True,
        "icon_url": "https://client-images.codat.io/icon/042399f5-d104-4f38-9ce8-cac3524f4e88_3f5623af-d992-4c22-bc08-e58c520a8526.ico",
        "logo_url": "https://client-images.codat.io/logo/042399f5-d104-4f38-9ce8-cac3524f4e88_5806cb1f-7342-4c0e-a0a8-99bfbc47b0ff.png",
        "name": "Bob's Burgers",
        "redirect_url": "https://bobs-burgers.{countrySuffix}/{companyId}",
        "white_list_urls": [
            "https://bobs-burgers.com",
            "https://bobs-burgers.co.uk",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.Profile](../../models/shared/profile.md)                    | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[shared.Profile](../../models/shared/profile.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.ErrorMessage | 401, 402, 403, 429  | application/json    |
| errors.ErrorMessage | 500, 503            | application/json    |
| errors.SDKError     | 4XX, 5XX            | \*/\*               |

## update_sync_settings

Update sync settings for all data types.

### Example Usage

<!-- UsageSnippet language="python" operationID="update-profile-syncSettings" method="post" path="/profile/syncSettings" example="Unauthorized" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.settings.update_sync_settings(request={
        "client_id": "9807ce3e-cfa5-4370-b4f2-09c282b1598b",
        "settings": [
            {
                "data_type": shared.DataType.INVOICES,
                "fetch_on_first_link": True,
                "is_locked": True,
                "months_to_sync": 24,
                "sync_from_utc": "2020-01-01T12:00:00.000Z",
                "sync_from_window": 24,
                "sync_order": 0,
                "sync_schedule": 24,
            },
        ],
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.UpdateProfileSyncSettingsRequestBody](../../models/operations/updateprofilesyncsettingsrequestbody.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.ErrorMessage | 401, 402, 403, 429  | application/json    |
| errors.ErrorMessage | 500, 503            | application/json    |
| errors.SDKError     | 4XX, 5XX            | \*/\*               |