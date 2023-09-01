"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class FeatureState(str, Enum):
    RELEASE = 'Release'
    ALPHA = 'Alpha'
    BETA = 'Beta'
    DEPRECATED = 'Deprecated'
    NOT_SUPPORTED = 'NotSupported'
    NOT_IMPLEMENTED = 'NotImplemented'