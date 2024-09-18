# SyncFlowSettings
(*sync_flow_settings*)

## Overview

Control text and visibility settings for the Sync Flow.

### Available Operations

* [get_config_text_sync_flow](#get_config_text_sync_flow) - Get preferences for text fields
* [get_visible_accounts](#get_visible_accounts) - List visible accounts
* [update_config_text_sync_flow](#update_config_text_sync_flow) - Update preferences for text fields
* [update_visible_accounts_sync_flow](#update_visible_accounts_sync_flow) - Update visible accounts

## get_config_text_sync_flow

Return preferences set for the text fields on sync flow.

### Example Usage

```python
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared

s = CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.sync_flow_settings.get_config_text_sync_flow(request={
    "locale": shared.Locale.EN_US,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetConfigTextSyncFlowRequest](../../models/operations/getconfigtextsyncflowrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[Dict[str, shared.Localization]](../../models/.md)**

### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401,402,403,429,500,503 | application/json        |
| errors.SDKError         | 4xx-5xx                 | */*                     |


## get_visible_accounts

Return accounts which are visible on sync flow.

### Example Usage

```python
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared

s = CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.sync_flow_settings.get_visible_accounts(request={
    "client_id": "86fe9741-738d-4f2c-8e96-9c3f84156e91",
    "platform_key": "gbol",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetVisibleAccountsRequest](../../models/operations/getvisibleaccountsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[shared.VisibleAccounts](../../models/shared/visibleaccounts.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## update_config_text_sync_flow

Set preferences for the text fields on sync flow.

### Example Usage

```python
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared

s = CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.sync_flow_settings.update_config_text_sync_flow(request={
    "locale": shared.Locale.EN_US,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateConfigTextSyncFlowRequest](../../models/operations/updateconfigtextsyncflowrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[Dict[str, shared.Localization]](../../models/.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 400,401,402,403,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## update_visible_accounts_sync_flow

Update which accounts are visible on sync flow.

### Example Usage

```python
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared

s = CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.sync_flow_settings.update_visible_accounts_sync_flow(request={
    "platform_key": "gbol",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.UpdateVisibleAccountsSyncFlowRequest](../../models/operations/updatevisibleaccountssyncflowrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[shared.VisibleAccounts](../../models/shared/visibleaccounts.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |
