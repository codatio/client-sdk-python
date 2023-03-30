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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    date_="2022-10-23T00:00:00Z",
)
    
res = s.files.download_files(req)

if res.data is not None:
    # handle response
```
<!-- End SDK Example Usage -->