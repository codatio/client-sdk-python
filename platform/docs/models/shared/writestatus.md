# WriteStatus

The current status of the write request, which is the same as the push operation status.

## Example Usage

```python
from codat_platform.models.shared import WriteStatus

value = WriteStatus.PENDING
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | Pending     |
| `FAILED`    | Failed      |
| `SUCCESS`   | Success     |
| `TIMED_OUT` | TimedOut    |