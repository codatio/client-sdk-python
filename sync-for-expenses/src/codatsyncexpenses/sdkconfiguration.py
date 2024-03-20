"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from ._hooks import SDKHooks
from .utils import utils
from .utils.retries import RetryConfig
from codatsyncexpenses.models import shared
from dataclasses import dataclass
from typing import Callable, Dict, Tuple, Union


SERVERS = [
    'https://api.codat.io',
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests_http.Session
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = 'prealpha'
    sdk_version: str = '6.1.0'
    gen_version: str = '2.286.2'
    user_agent: str = 'speakeasy-sdk/python 6.1.0 2.286.2 prealpha codat-sync-for-expenses'
    retry_config: RetryConfig = None
    _hooks: SDKHooks = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}


    def get_hooks(self) -> SDKHooks:
        return self._hooks
