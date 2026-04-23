# BilledToType

Defines if the invoice or credit note is billed/rebilled to a project or customer.

## Example Usage

```python
from codat_lending.models.shared import BilledToType

value = BilledToType.UNKNOWN
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `UNKNOWN`        | Unknown          |
| `NOT_APPLICABLE` | NotApplicable    |
| `CUSTOMER`       | Customer         |
| `PROJECT`        | Project          |