<!-- Start SDK Example Usage [usage] -->
```python
import codatfiles
from codatfiles.models import operations

s = codatfiles.CodatFiles(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.DownloadFilesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    date_='2022-10-23T00:00:00Z',
)

res = s.files.download_files(req)

if res.data is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->