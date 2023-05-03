# settings

## Overview

Manage your Codat instance.

### Available Operations

* [get_profile](#get_profile) - Get profile
* [get_sync_settings](#get_sync_settings) - Update all sync settings
* [update_profile](#update_profile) - Update profile

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

## get_sync_settings

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
    client_id='367f7975-267b-439b-90c6-a6040ee680f3',
    overrides_defaults=False,
    settings=[
        shared.SyncSetting(
            data_type=shared.SyncSettingDataTypeEnum.INVOICES,
            fetch_on_first_link=False,
            is_locked=False,
            months_to_sync=24,
            sync_from_utc='nobis',
            sync_from_window=24,
            sync_order=315428,
            sync_schedule=24,
        ),
    ],
)

res = s.settings.get_sync_settings(req)

if res.status_code == 200:
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
    alert_auth_header='Bearer tXEiHiRK7XCtI8TNHbpGs1LI1pumdb4Cl1QIo7B2',
    api_key='sartANTjHAkLdbyDfaynoTQb7pkmj6hXHmnQKMrB',
    confirm_company_name=False,
    icon_url='https://client-images.codat.io/icon/042399f5-d104-4f38-9ce8-cac3524f4e88_3f5623af-d992-4c22-bc08-e58c520a8526.ico',
    logo_url='https://client-images.codat.io/logo/042399f5-d104-4f38-9ce8-cac3524f4e88_5806cb1f-7342-4c0e-a0a8-99bfbc47b0ff.png',
    name='Bob's Burgers',
    redirect_url='https://bobs-burgers.{countrySuffix}/{companyId}',
    white_list_urls=[
        'https://bobs-burgers.com',
        'https://bobs-burgers.com',
        'https://bobs-burgers.com',
    ],
)

res = s.settings.update_profile(req)

if res.profile is not None:
    # handle response
```
