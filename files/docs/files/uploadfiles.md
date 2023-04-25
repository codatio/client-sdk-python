# upload_files
Available in: `files`

Upload files

## Example Usage
```python
import codatfiles
from codatfiles.models import operations

s = codatfiles.CodatFiles(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UploadFilesRequest(
    request_body=operations.UploadFilesRequestBody(
        content="corrupti".encode(),
        request_body="provident",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.files.upload_files(req)

if res.status_code == 200:
    # handle response
```