# TransactionDefinitionsStatus

Status of transaction.

## Example Usage

```python
from codat_sync_for_expenses.models.shared import TransactionDefinitionsStatus

value = TransactionDefinitionsStatus.UNKNOWN
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `UNKNOWN`    | Unknown      |
| `PUSH_ERROR` | PushError    |
| `COMPLETED`  | Completed    |
| `FAILED`     | Failed       |
| `PENDING`    | Pending      |