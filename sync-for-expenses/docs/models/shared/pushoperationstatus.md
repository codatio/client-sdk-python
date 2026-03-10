# PushOperationStatus

The current status of the push operation.

## Example Usage

```python
from codat_sync_for_expenses.models.shared import PushOperationStatus

value = PushOperationStatus.PENDING
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | Pending     |
| `FAILED`    | Failed      |
| `SUCCESS`   | Success     |
| `TIMED_OUT` | TimedOut    |