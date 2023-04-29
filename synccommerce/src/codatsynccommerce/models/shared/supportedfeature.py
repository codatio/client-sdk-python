"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import featurestate_enum as shared_featurestate_enum
from ..shared import featuretype_enum as shared_featuretype_enum
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SupportedFeature:
    
    feature_state: shared_featurestate_enum.FeatureStateEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('featureState') }})
    feature_type: shared_featuretype_enum.FeatureTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('featureType') }})
    