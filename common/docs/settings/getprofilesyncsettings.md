# get_profile_sync_settings
Available in: `settings`

Retrieve the sync settings for your client. This includes how often data types should be queued to be updated, and how much history should be fetched.

## Example Usage
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