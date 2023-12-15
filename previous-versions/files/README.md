# Files

<!-- Start Codat Library Description -->
﻿Use Codat's Files API to upload your SMB customers' files.
<!-- End Codat Library Description -->
Use Codat's Files API to upload your SMB customers' files.

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install codat-files
```
<!-- End SDK Installation [installation] -->

## Example Usage
<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [files](docs/sdks/files/README.md)

* [download_files](docs/sdks/files/README.md#download_files) - Download all files for a company
* [list_files](docs/sdks/files/README.md#list_files) - List all files uploaded by a company
* [upload_files](docs/sdks/files/README.md#upload_files) - Upload files for a company
<!-- End Available Resources and Operations [operations] -->



<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries.  If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API.  However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a retryConfig object to the call:
```python
import codatfiles
from codatfiles.models import operations
from codatfiles.utils import BackoffStrategy, RetryConfig

s = codatfiles.CodatFiles(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.DownloadFilesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    date_='2022-10-23T00:00:00Z',
)

res = s.files.download_files(req,
    RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False))

if res.data is not None:
    # handle response
    pass
```

If you'd like to override the default retry strategy for all operations that support retries, you can provide a retryConfig at SDK initialization:
```python
import codatfiles
from codatfiles.models import operations
from codatfiles.utils import BackoffStrategy, RetryConfig

s = codatfiles.CodatFiles(
    retry_config=RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False)
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
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.Schema                    | 400,401,402,404,429,500,503      | application/json                 |
| errors.DownloadFilesErrorMessage | 403                              | application/json                 |
| errors.SDKError                  | 400-600                          | */*                              |

### Example

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

res = None
try:
    res = s.files.download_files(req)
except errors.Schema as e:
    print(e)  # handle exception
    raise(e)
except errors.DownloadFilesErrorMessage as e:
    print(e)  # handle exception
    raise(e)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.data is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.codat.io` | None |

#### Example

```python
import codatfiles
from codatfiles.models import operations

s = codatfiles.CodatFiles(
    server_idx=0,
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


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import codatfiles
from codatfiles.models import operations

s = codatfiles.CodatFiles(
    server_url="https://api.codat.io",
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
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import codatfiles
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = codatfiles.CodatFiles(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `auth_header` | apiKey        | API key       |

To authenticate with the API the `auth_header` parameter must be set when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

<!-- Start Codat Support Notes -->
### Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance. 
You can raise any issues by contacting your dedicated Codat representative or reaching out to our [support team](mailto:support@codat.io).
We're here to help ensure a smooth experience for you.
<!-- End Codat Support Notes -->

<!-- Start Codat Generated By -->
### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
<!-- End Codat Generated By -->