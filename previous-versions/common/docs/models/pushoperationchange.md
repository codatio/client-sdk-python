# PushOperationChange


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `attachment_id`                                                    | *OptionalNullable[str]*                                            | :heavy_minus_sign:                                                 | Unique identifier for the attachment created otherwise null.       |
| `record_ref`                                                       | [Optional[models.PushOperationRef]](../models/pushoperationref.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `type`                                                             | [Optional[models.PushChangeType]](../models/pushchangetype.md)     | :heavy_minus_sign:                                                 | Type of change being applied to record in third party platform.    |