# PushOperationChange


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `attachment_id`                                                       | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Unique identifier for the attachment created otherwise null.          |
| `record_ref`                                                          | [Optional[PushOperationRef]](../../models/shared/pushoperationref.md) | :heavy_minus_sign:                                                    | N/A                                                                   |
| `type`                                                                | [Optional[PushChangeType]](../../models/shared/pushchangetype.md)     | :heavy_minus_sign:                                                    | Type of change being applied to record in third party platform.       |