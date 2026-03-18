# DataConnectionStatus

The current authorization status of the data connection.

## Example Usage

```python
from codat_sync_for_expenses.models.shared import DataConnectionStatus

value = DataConnectionStatus.PENDING_AUTH
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `PENDING_AUTH` | PendingAuth    |
| `LINKED`       | Linked         |
| `UNLINKED`     | Unlinked       |
| `DEAUTHORIZED` | Deauthorized   |