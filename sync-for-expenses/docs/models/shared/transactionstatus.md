# TransactionStatus

Status of the transaction.

## Example Usage

```python
from codat_sync_for_expenses.models.shared import TransactionStatus

value = TransactionStatus.UNKNOWN
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `UNKNOWN`          | Unknown            |
| `PENDING`          | Pending            |
| `VALIDATION_ERROR` | ValidationError    |
| `COMPLETED`        | Completed          |
| `PUSH_ERROR`       | PushError          |