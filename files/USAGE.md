<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat()
s.config_security(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    )
)
   
req = operations.DownloadFilesRequest(
    security=operations.DownloadFilesSecurity(
        api_key="YOUR_API_KEY_HERE",
    ),
    path_params=operations.DownloadFilesPathParams(
        company_id="unde",
    ),
    query_params=operations.DownloadFilesQueryParams(
        date_="2022-07-28T14:41:43.209Z",
    ),
)
    
res = s.files.download_files(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->