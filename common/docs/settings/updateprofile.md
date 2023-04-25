# update_profile
Available in: `settings`

Update your Codat profile

## Example Usage
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