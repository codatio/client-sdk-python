# ErrorStatus

The current status of a transient error. Null statuses indicate that the error is not transient.

## Example Usage

```python
from codat_sync_for_expenses.models.shared import ErrorStatus

value = ErrorStatus.ACTIVE
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `ACTIVE`   | Active     |
| `RESOLVED` | Resolved   |