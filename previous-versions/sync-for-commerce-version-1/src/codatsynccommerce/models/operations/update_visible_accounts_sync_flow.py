"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errormessage as shared_errormessage
from ..shared import visibleaccounts as shared_visibleaccounts
from typing import Optional


@dataclasses.dataclass
class UpdateVisibleAccountsSyncFlowRequest:
    platform_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'platformKey', 'style': 'simple', 'explode': False }})
    r"""A unique 4-letter key to represent a platform in each integration. View [accounting](https://docs.codat.io/integrations/accounting/overview#platform-keys), [banking](https://docs.codat.io/integrations/banking/overview#platform-keys), and [commerce](https://docs.codat.io/integrations/commerce/overview#platform-keys) platform keys."""
    visible_accounts: Optional[shared_visibleaccounts.VisibleAccounts] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateVisibleAccountsSyncFlowResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""The request made is not valid."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    visible_accounts: Optional[shared_visibleaccounts.VisibleAccounts] = dataclasses.field(default=None)
    r"""Success"""
    

