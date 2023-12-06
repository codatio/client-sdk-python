"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatsyncpayables import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SupplementalData:
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting platform. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    content: Optional[Dict[str, Dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content') }})
    

