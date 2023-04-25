# settings

## Overview

Manage your Codat instance.

### Available Operations

* [get_profile](#get_profile) - Get profile
* [get_profile_sync_settings](#get_profile_sync_settings) - Get sync settings
* [update_profile](#update_profile) - Update profile
* [update_sync_settings](#update_sync_settings) - Update all sync settings

## get_profile

Fetch your Codat profile.

### Example Usage

```python
import codatcommon


s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


res = s.settings.get_profile()

if res.profile is not None:
    # handle response
```

## get_profile_sync_settings

Retrieve the sync settings for your client. This includes how often data types should be queued to be updated, and how much history should be fetched.

### Example Usage

```python
import codatcommon


s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


res = s.settings.get_profile_sync_settings()

if res.sync_settings is not None:
    # handle response
```

## update_profile

Update your Codat profile

### Example Usage

```python
import codatcommon
from codatcommon.models import shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = shared.Profile(
    alert_auth_header="explicabo",
    api_key="nobis",
    confirm_company_name=False,
    icon_url="enim",
    logo_url="omnis",
    name="Bob's Burgers",
    redirect_url="nemo",
    white_list_urls=[
        "https://bobs-burgers.com/redirect",
        "https://bobs-burgers.com/redirect",
    ],
)

res = s.settings.update_profile(req)

if res.profile is not None:
    # handle response
```

## update_sync_settings

Update sync settings for all data types.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations, shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateSyncSettingsRequestBody(
    client_id="367f7975-267b-439b-90c6-a6040ee680f3",
    overrides_defaults=False,
    settings=[
        shared.SyncSetting(
            data_type="invoices",
            fetch_on_first_link=False,
            is_locked=False,
            months_to_sync=24,
            sync_from_utc="accusantium",
            sync_from_window=24,
            sync_order=438601,
            sync_schedule=24,
        ),
        shared.SyncSetting(
            data_type="invoices",
            fetch_on_first_link=False,
            is_locked=False,
            months_to_sync=24,
            sync_from_utc="culpa",
            sync_from_window=24,
            sync_order=988374,
            sync_schedule=24,
        ),
        shared.SyncSetting(
            data_type="invoices",
            fetch_on_first_link=False,
            is_locked=False,
            months_to_sync=24,
            sync_from_utc="sapiente",
            sync_from_window=24,
            sync_order=102044,
            sync_schedule=24,
        ),
    ],
)

res = s.settings.update_sync_settings(req)

if res.status_code == 200:
    # handle response
```
