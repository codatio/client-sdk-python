# get_profile
Available in: `settings`

Fetch your Codat profile.

## Example Usage
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