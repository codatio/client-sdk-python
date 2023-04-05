"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import datatype_enum as shared_datatype_enum
from ..shared import supportedfeature as shared_supportedfeature
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DataTypeFeature:
    r"""Describes support for a given datatype and associated operations"""
    
    supported_features: list[shared_supportedfeature.SupportedFeature] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supportedFeatures') }})  
    data_type: Optional[shared_datatype_enum.DataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Available Data types"""  
    