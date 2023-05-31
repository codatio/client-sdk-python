# files

## Overview

Endpoints to manage uploaded files.

### Available Operations

* [download_files](#download_files) - Download all files for a company
* [list_files](#list_files) - List all files uploaded by a company
* [upload_files](#upload_files) - Upload files for a company

## download_files

You can specify a date to download specific files for.

### Example Usage

```python
import codatfiles
from codatfiles.models import operations

s = codatfiles.CodatFiles(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadFilesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    date_='provident',
)

res = s.files.download_files(req)

if res.data is not None:
    # handle response
```

## list_files

Returns an array of files that have been uploaded for a given company.

### Example Usage

```python
import codatfiles
from codatfiles.models import operations

s = codatfiles.CodatFiles(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListFilesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.files.list_files(req)

if res.files is not None:
    # handle response
```

## upload_files

Upload files

### Example Usage

```python
import codatfiles
from codatfiles.models import operations

s = codatfiles.CodatFiles(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadFilesRequest(
    request_body=operations.UploadFilesRequestBody(
        content='distinctio'.encode(),
        request_body='quibusdam',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.files.upload_files(req)

if res.status_code == 200:
    # handle response
```
