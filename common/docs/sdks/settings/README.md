# settings

## Overview

Manage your Codat instance.

### Available Operations

* [~~get_profile~~](#get_profile) - Get profile :warning: **Deprecated**
* [get_sync_settings](#get_sync_settings) - Get sync settings
* [update_profile](#update_profile) - Update profile
* [update_sync_settings](#update_sync_settings) - Update all sync settings

## ~~get_profile~~

Fetch your Codat profile.

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import codatcommon


s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="",
    ),
)


res = s.settings.get_profile()

if res.profile is not None:
    # handle response
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetProfileResponse](../../models/operations/getprofileresponse.md)**


## get_sync_settings

Retrieve the sync settings for your client. This includes how often data types should be queued to be updated, and how much history should be fetched.

### Example Usage

```python
import codatcommon


s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="",
    ),
)


res = s.settings.get_sync_settings()

if res.sync_settings is not None:
    # handle response
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetProfileSyncSettingsResponse](../../models/operations/getprofilesyncsettingsresponse.md)**


## update_profile

Update your Codat profile

### Example Usage

```python
import codatcommon
from codatcommon.models import shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="",
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
        'https://bobs-burgers.com',
    ],
)

res = s.settings.update_profile(req)

if res.profile is not None:
    # handle response
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.Profile](../../models/shared/profile.md)                    | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.UpdateProfileResponse](../../models/operations/updateprofileresponse.md)**


## update_sync_settings

Update sync settings for all data types.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations, shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.UpdateProfileSyncSettingsRequestBody(
    client_id='367f7975-267b-439b-90c6-a6040ee680f3',
    overrides_defaults=False,
    settings=[
        shared.SyncSetting(
            data_type=shared.SyncSettingDataType.INVOICES,
            fetch_on_first_link=False,
            is_locked=False,
            months_to_sync=24,
            sync_from_utc='2022-10-23T00:00:00.000Z',
            sync_from_window=24,
            sync_order=449950,
            sync_schedule=24,
        ),
        shared.SyncSetting(
            data_type=shared.SyncSettingDataType.INVOICES,
            fetch_on_first_link=False,
            is_locked=False,
            months_to_sync=24,
            sync_from_utc='2022-10-23T00:00:00.000Z',
            sync_from_window=24,
            sync_order=613064,
            sync_schedule=24,
        ),
        shared.SyncSetting(
            data_type=shared.SyncSettingDataType.INVOICES,
            fetch_on_first_link=False,
            is_locked=False,
            months_to_sync=24,
            sync_from_utc='2022-10-23T00:00:00.000Z',
            sync_from_window=24,
            sync_order=902349,
            sync_schedule=24,
        ),
        shared.SyncSetting(
            data_type=shared.SyncSettingDataType.INVOICES,
            fetch_on_first_link=False,
            is_locked=False,
            months_to_sync=24,
            sync_from_utc='2022-10-23T00:00:00.000Z',
            sync_from_window=24,
            sync_order=99280,
            sync_schedule=24,
        ),
    ],
)

res = s.settings.update_sync_settings(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.UpdateProfileSyncSettingsRequestBody](../../models/operations/updateprofilesyncsettingsrequestbody.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |


### Response

**[operations.UpdateProfileSyncSettingsResponse](../../models/operations/updateprofilesyncsettingsresponse.md)**

