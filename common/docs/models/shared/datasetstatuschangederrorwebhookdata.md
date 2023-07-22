# DatasetStatusChangedErrorWebhookData


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `data_type`                                                | *Optional[str]*                                            | :heavy_minus_sign:                                         | Data type the sync completed for.                          |
| `dataset_id`                                               | *Optional[str]*                                            | :heavy_minus_sign:                                         | Unique identifier for the dataset that completed its sync. |
| `dataset_status`                                           | *Optional[str]*                                            | :heavy_minus_sign:                                         | The current status of the dataset's sync.                  |