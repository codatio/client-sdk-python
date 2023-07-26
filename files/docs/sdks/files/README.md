# files

## Overview

Endpoints to manage uploaded files.

### Available Operations

* [download_files](#download_files) - Download all files for a company
* [list_files](#list_files) - List all files uploaded by a company
* [upload_files](#upload_files) - Upload files for a company

## download_files

The *Download files* endpoint downloads all files that have  been uploaded by to SMB to Codat. A `date` may be specified to download any files uploaded on the date provided.

### Example Usage

```python
import codatfiles
from codatfiles.models import operations, shared

s = codatfiles.CodatFiles(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadFilesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    date_='2022-10-23T00:00:00.000Z',
)

res = s.files.download_files(req)

if res.data is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DownloadFilesRequest](../../models/operations/downloadfilesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.DownloadFilesResponse](../../models/operations/downloadfilesresponse.md)**


## list_files

﻿The *List files* endpoint returns a list of all files uploaded to Codat by the SMB. 

### Example Usage

```python
import codatfiles
from codatfiles.models import operations, shared

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

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListFilesRequest](../../models/operations/listfilesrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |


### Response

**[operations.ListFilesResponse](../../models/operations/listfilesresponse.md)**


## upload_files

The *Upload files* endpoint uploads multiple files provided by the SMB to Codat. This may include personal identity documents, pitch decks, contracts, or files with accounting and banking data.

Uploaded files must meet the following requirements:

- Up to 20 files can be uploaded at a time.
- PDF, XLS, XLSX, XLSB, CSV, DOC, DOCX, PPT, PPTX, JPEG, JPG, and PNG files can be uploaded.
- Each file can be up to 10MB in size.

### Example Usage

```python
import codatfiles
from codatfiles.models import operations, shared

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

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.UploadFilesRequest](../../models/operations/uploadfilesrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |


### Response

**[operations.UploadFilesResponse](../../models/operations/uploadfilesresponse.md)**

