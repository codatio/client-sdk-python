# ErrorStatus

The current status of a transient error. Null statuses indicate that the error is not transient.

## Example Usage

```python
from codat_lending.models.shared import ErrorStatus

value = ErrorStatus.ACTIVE
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `ACTIVE`   | Active     |
| `RESOLVED` | Resolved   |