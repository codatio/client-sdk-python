# data_integrity

## Overview

Data integrity is important

### Available Operations

* [get_data_integrity_details](#get_data_integrity_details) - Lists data integrity details for date type
* [get_data_integrity_status](#get_data_integrity_status) - Get data integrity status
* [get_data_integrity_summaries](#get_data_integrity_summaries) - Get data integrity summary

## get_data_integrity_details

Gets record-by-record match results for a given company and datatype, optionally restricted by a Codat query string.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDataIntegrityDetailsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    data_type=shared.DataIntegrityDataTypeEnum.BANKING_ACCOUNTS,
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='voluptatibus',
)

res = s.data_integrity.get_data_integrity_details(req)

if res.details is not None:
    # handle response
```

## get_data_integrity_status

Gets match status for a given company and datatype.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDataIntegrityStatusRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    data_type=shared.DataIntegrityDataTypeEnum.BANKING_ACCOUNTS,
)

res = s.data_integrity.get_data_integrity_status(req)

if res.status is not None:
    # handle response
```

## get_data_integrity_summaries

Gets match summary for a given company and datatype, optionally restricted by a Codat query string.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDataIntegritySummariesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    data_type=shared.DataIntegrityDataTypeEnum.BANKING_ACCOUNTS,
    query='ipsa',
)

res = s.data_integrity.get_data_integrity_summaries(req)

if res.summaries is not None:
    # handle response
```
