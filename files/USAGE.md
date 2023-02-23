<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()
s.config_security(
    security=shared.Security(
        api_key=shared.SchemeAPIKey(
            api_key="YOUR_API_KEY_HERE",
        ),
    )
)
   
req = operations.DownloadFilesRequest(
    security=operations.DownloadFilesSecurity(
        api_key=shared.SchemeAPIKey(
            api_key="YOUR_API_KEY_HERE",
        ),
    ),
    path_params=operations.DownloadFilesPathParams(
        company_id="unde",
    ),
    query_params=operations.DownloadFilesQueryParams(
        date_="2022-07-22T11:46:19.336Z",
    ),
)
    
res = s.files.download_files(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->