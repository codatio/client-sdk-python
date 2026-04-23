# EndUploadSessionRequestStatus

An indicator to cancel the dataset processing or trigger ingestion and enrichment of data.

## Example Usage

```python
from codat_lending.models.shared import EndUploadSessionRequestStatus

value = EndUploadSessionRequestStatus.CANCEL
```


## Values

| Name      | Value     |
| --------- | --------- |
| `CANCEL`  | Cancel    |
| `PROCESS` | Process   |