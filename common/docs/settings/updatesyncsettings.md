# update_sync_settings
Available in: `settings`

Update sync settings for all data types.

## Example Usage
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
            sync_from_utc="2022-10-23T00:00:00Z",
            sync_from_window=24,
            sync_order=38425,
            sync_schedule=24,
        ),
        shared.SyncSetting(
            data_type="invoices",
            fetch_on_first_link=False,
            is_locked=False,
            months_to_sync=24,
            sync_from_utc="2022-10-23T00:00:00Z",
            sync_from_window=24,
            sync_order=438601,
            sync_schedule=24,
        ),
        shared.SyncSetting(
            data_type="invoices",
            fetch_on_first_link=False,
            is_locked=False,
            months_to_sync=24,
            sync_from_utc="2022-10-23T00:00:00Z",
            sync_from_window=24,
            sync_order=634274,
            sync_schedule=24,
        ),
    ],
)

res = s.settings.update_sync_settings(req)

if res.status_code == 200:
    # handle response
```