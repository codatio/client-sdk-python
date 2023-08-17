# sync_flow_preferences

## Overview

Configure preferences for any given Sync for Commerce company using sync flow.

### Available Operations

* [get_config_text_sync_flow](#get_config_text_sync_flow) - Get preferences for text fields
* [get_visible_accounts](#get_visible_accounts) - List visible accounts
* [update_config_text_sync_flow](#update_config_text_sync_flow) - Update preferences for text fields
* [update_visible_accounts_sync_flow](#update_visible_accounts_sync_flow) - Update visible accounts

## get_config_text_sync_flow

Return preferences set for the text fields on sync flow.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)


res = s.sync_flow_preferences.get_config_text_sync_flow()

if res.localization_info is not None:
    # handle response
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetConfigTextSyncFlowResponse](../../models/operations/getconfigtextsyncflowresponse.md)**


## get_visible_accounts

Return accounts which are visible on sync flow.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetVisibleAccountsRequest(
    client_id='674e0f46-7cc8-4796-ad15-1a05dfc2ddf7',
    platform_key='cc78ca1b-a928-4fc8-9674-2cb739205929',
)

res = s.sync_flow_preferences.get_visible_accounts(req)

if res.visible_accounts is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetVisibleAccountsRequest](../../models/operations/getvisibleaccountsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.GetVisibleAccountsResponse](../../models/operations/getvisibleaccountsresponse.md)**


## update_config_text_sync_flow

Set preferences for the text fields on sync flow.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = {
    "natus": shared.Localization(
        required=False,
        text='laboriosam',
    ),
}

res = s.sync_flow_preferences.update_config_text_sync_flow(req)

if res.localization_info is not None:
    # handle response
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [dict[str, shared.Localization]](../../models//.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.UpdateConfigTextSyncFlowResponse](../../models/operations/updateconfigtextsyncflowresponse.md)**


## update_visible_accounts_sync_flow

Update which accounts are visible on sync flow.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateVisibleAccountsSyncFlowRequest(
    visible_accounts=shared.VisibleAccounts(
        visible_accounts=[
            'saepe',
            'fuga',
            'in',
            'corporis',
        ],
    ),
    commerce_key='96eb10fa-aa23-452c-9955-907aff1a3a2f',
)

res = s.sync_flow_preferences.update_visible_accounts_sync_flow(req)

if res.visible_accounts is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.UpdateVisibleAccountsSyncFlowRequest](../../models/operations/updatevisibleaccountssyncflowrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |


### Response

**[operations.UpdateVisibleAccountsSyncFlowResponse](../../models/operations/updatevisibleaccountssyncflowresponse.md)**

