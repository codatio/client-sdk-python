"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class PushOptionType(str, Enum):
    r"""The option type."""
    ARRAY = 'Array'
    OBJECT = 'Object'
    STRING = 'String'
    NUMBER = 'Number'
    BOOLEAN = 'Boolean'
    DATE_TIME = 'DateTime'
    FILE = 'File'
    MULTI_PART = 'MultiPart'
