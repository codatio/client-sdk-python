"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from ._hooks import SDKHooks
from .httpclient import AsyncHttpClient, HttpClient
from .utils import Logger, RetryConfig, remove_suffix
from codat_bankfeeds.models import shared
from codat_bankfeeds.types import OptionalNullable, UNSET
from dataclasses import dataclass
from pydantic import Field
from typing import Callable, Dict, Optional, Tuple, Union


SERVERS = [
    "https://api.codat.io",
    # Production
]
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: HttpClient
    async_client: AsyncHttpClient
    debug_logger: Logger
    security: Optional[Union[shared.Security, Callable[[], shared.Security]]] = None
    server_url: Optional[str] = ""
    server_idx: Optional[int] = 0
    language: str = "python"
    openapi_doc_version: str = "3.0.0"
    sdk_version: str = "9.0.1"
    gen_version: str = "2.474.15"
    user_agent: str = "speakeasy-sdk/python 9.0.1 2.474.15 3.0.0 codat-bankfeeds"
    retry_config: OptionalNullable[RetryConfig] = Field(default_factory=lambda: UNSET)
    timeout_ms: Optional[int] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url:
            return remove_suffix(self.server_url, "/"), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}

    def get_hooks(self) -> SDKHooks:
        return self._hooks
