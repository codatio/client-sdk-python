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


s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


res = s.sync_flow_preferences.get_config_text_sync_flow()

if res.localization_info is not None:
    # handle response
```

## get_sync_flow_url

Get a URL for Sync Flow including a one time passcode.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSyncFlowURLRequest(
    accounting_key="vel",
    commerce_key="error",
    merchant_identifier="deserunt",
)

res = s.sync_flow_preferences.get_sync_flow_url(req)

if res.sync_flow_url is not None:
    # handle response
```

## get_visible_accounts

Enable retrieval for accounts which are visible on sync flow.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetVisibleAccountsRequest(
    client_id="674e0f46-7cc8-4796-ad15-1a05dfc2ddf7",
    platform_key="cc78ca1b-a928-4fc8-9674-2cb739205929",
)

res = s.sync_flow_preferences.get_visible_accounts(req)

if res.visible_accounts is not None:
    # handle response
```

## update_config_text_sync_flow

To enable update of preferences set for the text fields on sync flow.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = {
    "natus": shared.Localization(
        required=False,
        text="laboriosam",
    ),
}

res = s.sync_flow_preferences.update_config_text_sync_flow(req)

if res.localization_info is not None:
    # handle response
```

## update_visible_accounts_sync_flow

To enable update of accounts visible preferences set on Sync Flow.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateVisibleAccountsSyncFlowRequest(
    visible_accounts=shared.VisibleAccounts(
        visible_accounts=[
            "saepe",
            "fuga",
            "in",
            "corporis",
        ],
    ),
    commerce_key="96eb10fa-aa23-452c-9955-907aff1a3a2f",
)

res = s.sync_flow_preferences.update_visible_accounts_sync_flow(req)

if res.visible_accounts is not None:
    # handle response
```