# BillStatus

Current state of the bill.

## Example Usage

```python
from codat_lending.models.shared import BillStatus

value = BillStatus.UNKNOWN
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `UNKNOWN`        | Unknown          |
| `OPEN`           | Open             |
| `PARTIALLY_PAID` | PartiallyPaid    |
| `PAID`           | Paid             |
| `VOID`           | Void             |
| `DRAFT`          | Draft            |