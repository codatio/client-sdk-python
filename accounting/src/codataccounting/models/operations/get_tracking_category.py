"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errormessage as shared_errormessage
from ..shared import trackingcategorytree as shared_trackingcategorytree
from typing import Optional



@dataclasses.dataclass
class GetTrackingCategoryRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    tracking_category_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'trackingCategoryId', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetTrackingCategoryResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    tracking_category_tree: Optional[shared_trackingcategorytree.TrackingCategoryTree] = dataclasses.field(default=None)
    r"""Success"""
    

