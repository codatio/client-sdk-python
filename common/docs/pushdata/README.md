# push_data

## Overview

View push options and get push statuses.

### Available Operations

* [get_model_options](#get_model_options) - Get push options
* [get_operation](#get_operation) - Get push operation
* [list_operations](#list_operations) - List push operations

## get_model_options

This is the generic documentation for creation and updating of data. See the equivalent endpoint for a given data type for more specific information. 

Before pushing data into accounting software, it is often necessary to collect some details from the user as to how they would like the data to be inserted. This includes names and amounts on transactional entities, but also factors such as categorisation of entities, which is often handled differently between different accounting packages. A good example of this is specifying where on the balance sheet/profit and loss reports the user would like a newly-created nominal account to appear.

Codat tries not to limit users to pushing to a very limited number of standard categories, so we have implemented "options" endpoints, which allow us to expose to our clients the fields which are required to be pushed for a specific linked company, and the options which may be selected for each field.


> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/) for integrations that support push (POST/PUT methods).

### Example Usage

```python
import codatcommon
from codatcommon.models import operations, shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetCreateUpdateModelOptionsByDataTypeRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    data_type=shared.DataType.INVOICES,
)

res = s.push_data.get_model_options(req)

if res.push_option is not None:
    # handle response
```

## get_operation

Retrieve push operation.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetPushOperationRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    push_operation_key='4e0f467c-c879-46ed-951a-05dfc2ddf7cc',
)

res = s.push_data.get_operation(req)

if res.push_operation is not None:
    # handle response
```

## list_operations

List push operation records.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetCompanyPushHistoryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='esse',
)

res = s.push_data.list_operations(req)

if res.push_history_response is not None:
    # handle response
```
