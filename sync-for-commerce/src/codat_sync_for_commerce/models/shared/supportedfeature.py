"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .featurestate import FeatureState
from .featuretype import FeatureType
from codat_sync_for_commerce.types import BaseModel
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class SupportedFeatureTypedDict(TypedDict):
    feature_state: FeatureState
    r"""The current release state of the feature."""
    feature_type: FeatureType
    r"""The type of feature."""


class SupportedFeature(BaseModel):
    feature_state: Annotated[FeatureState, pydantic.Field(alias="featureState")]
    r"""The current release state of the feature."""

    feature_type: Annotated[FeatureType, pydantic.Field(alias="featureType")]
    r"""The type of feature."""
