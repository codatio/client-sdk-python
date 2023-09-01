# sync_flow_preferences

## Overview

Configure preferences for any given Sync for Commerce company using sync flow.

### Available Operations

* [get_config_text_sync_flow](#get_config_text_sync_flow) - Retrieve preferences for text fields on Sync Flow
* [get_sync_flow_url](#get_sync_flow_url) - Retrieve sync flow url
* [get_visible_accounts](#get_visible_accounts) - List visible accounts
* [update_config_text_sync_flow](#update_config_text_sync_flow) - Update preferences for text fields on sync flow
* [update_visible_accounts_sync_flow](#update_visible_accounts_sync_flow) - Update the visible accounts on Sync Flow

## get_config_text_sync_flow

To enable retrieval of preferences set for the text fields on Sync Flow.

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


## get_sync_flow_url

Get a URL for Sync Flow including a one time passcode.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetSyncFlowURLRequest(
    accounting_key='voluptas',
    commerce_key='expedita',
    merchant_identifier='voluptas',
)

res = s.sync_flow_preferences.get_sync_flow_url(req)

if res.sync_flow_url is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetSyncFlowURLRequest](../../models/operations/getsyncflowurlrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.GetSyncFlowURLResponse](../../models/operations/getsyncflowurlresponse.md)**


## get_visible_accounts

Enable retrieval for accounts which are visible on sync flow.

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
    client_id='f66fef02-0e9f-4443-b425-7b992c8dbda6',
    platform_key='a61efa21-9825-48fd-8a9e-ba47f7d3ef04',
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

To enable update of preferences set for the text fields on sync flow.

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
    "aliquid": shared.Localization(
        required=False,
        text='dolore',
    ),
    "voluptatem": shared.Localization(
        required=False,
        text='illum',
    ),
    "laboriosam": shared.Localization(
        required=False,
        text='culpa',
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

To enable update of accounts visible preferences set on Sync Flow.

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
            'atque',
        ],
    ),
    platform_key='31c87adf-596f-4df1-ad83-7ae80c1c19c9',
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

