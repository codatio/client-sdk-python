"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import errormessage as errors_errormessage
from typing import Optional


@dataclasses.dataclass
class DeleteAPIKeyRequest:
    api_key_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiKeyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for api key."""
    



@dataclasses.dataclass
class DeleteAPIKeyResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    error_message: Optional[errors_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Too many requests were made in a given amount of time. Wait a short period and then try again."""
    

