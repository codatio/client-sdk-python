"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass
from typing import Dict, Tuple, Callable, Union
from .utils.retries import RetryConfig
from .utils import utils
from codatfiles.models import shared


SERVERS = [
    'https://api.codat.io',
    # Production
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests.Session
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '3.0.0'
    sdk_version: str = '0.2.0'
    gen_version: str = '2.214.3'
    user_agent: str = 'speakeasy-sdk/python 0.2.0 2.214.3 3.0.0 codat-files'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
