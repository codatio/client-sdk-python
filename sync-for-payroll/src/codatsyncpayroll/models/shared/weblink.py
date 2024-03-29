"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatsyncpayroll import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class Type(str, Enum):
    r"""The type of the weblink."""
    WEBSITE = 'Website'
    SOCIAL = 'Social'
    UNKNOWN = 'Unknown'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WebLink:
    r"""Weblink associated with the company."""
    type: Optional[Type] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The type of the weblink."""
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    r"""The full URL for the weblink."""
    

