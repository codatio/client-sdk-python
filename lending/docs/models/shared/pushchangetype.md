# PushChangeType

Type of change being applied to record in third party platform.

## Example Usage

```python
from codat_lending.models.shared import PushChangeType

value = PushChangeType.UNKNOWN
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `UNKNOWN`             | Unknown               |
| `CREATED`             | Created               |
| `MODIFIED`            | Modified              |
| `DELETED`             | Deleted               |
| `ATTACHMENT_UPLOADED` | AttachmentUploaded    |