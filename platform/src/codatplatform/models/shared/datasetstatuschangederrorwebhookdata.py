"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .datatype import DataType
from codatplatform import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DatasetStatusChangedErrorWebhookData:
    data_type: Optional[DataType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Available data types"""
    dataset_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datasetId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for the dataset that completed its sync."""
    dataset_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datasetStatus'), 'exclude': lambda f: f is None }})
    r"""The current status of the dataset's sync."""
    

