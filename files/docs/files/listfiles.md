# list_files
Available in: `files`

Returns an array of files that have been uploaded for a given company.

## Example Usage
```python
import codatfiles
from codatfiles.models import operations

s = codatfiles.CodatFiles(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListFilesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.files.list_files(req)

if res.files is not None:
    # handle response
```