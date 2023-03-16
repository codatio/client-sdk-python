<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadFilesRequest(
    company_id="unde",
    date_="2022-08-11T14:41:47.787Z",
)
    
res = s.files.download_files(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->