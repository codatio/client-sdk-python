# Files

<!-- Start Codat Library Description -->
﻿Use Codat's Files API to upload your SMB customers' files.
<!-- End Codat Library Description -->
Use Codat's Files API to upload your SMB customers' files.

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install codat-files
```
<!-- End SDK Installation -->

## Example Usage
<!-- Start SDK Example Usage -->
```python
import codatfiles
from codatfiles.models import operations, shared

s = codatfiles.CodatFiles(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.DownloadFilesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    date_='2022-10-23T00:00:00.000Z',
)

res = s.files.download_files(req)

if res.data is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [files](docs/sdks/files/README.md)

* [download_files](docs/sdks/files/README.md#download_files) - Download all files for a company
* [list_files](docs/sdks/files/README.md#list_files) - List all files uploaded by a company
* [upload_files](docs/sdks/files/README.md#upload_files) - Upload files for a company
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->