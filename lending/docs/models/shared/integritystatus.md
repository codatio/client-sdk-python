# IntegrityStatus

The current status of the most recently run matching algorithm.

## Example Usage

```python
from codat_lending.models.shared import IntegrityStatus

value = IntegrityStatus.UNKNOWN
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `UNKNOWN`        | Unknown          |
| `DOES_NOT_EXIST` | DoesNotExist     |
| `ERROR`          | Error            |
| `COMPLETE`       | Complete         |