<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat()
s.config_security(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    )
)
   
req = operations.DownloadFilesRequest(
    path_params=operations.DownloadFilesPathParams(
        company_id="unde",
    ),
    query_params=operations.DownloadFilesQueryParams(
        date_="2022-07-30T14:41:22.972Z",
    ),
)
    
res = s.files.download_files(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->