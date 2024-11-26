"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from codat_files import utils
from codat_files._hooks import SDKHooks
from codat_files.files import Files
from codat_files.models import shared
from codat_files.types import OptionalNullable, UNSET
import httpx
from typing import Any, Callable, Dict, Optional, Union


class CodatFiles(BaseSDK):
    r"""Files API: > ### New to Codat?
    >
    > Our Files API reference is relevant only to our existing clients.
    > Please reach out to your Codat contact so that we can find the right product for you.

    An API for uploading and downloading files from 'File Upload' Integrations.

    The Accounting file upload, Banking file upload, and Business documents file upload integrations provide simple file upload functionality.

    <!-- Start Codat Tags Table -->
    ## Endpoints

    | Endpoints | Description |
    | :- |:- |
    | Files | Endpoints to manage uploaded files. |
    <!-- End Codat Tags Table -->
    [Read more...](https://docs.codat.io/other/file-upload)

    [See our OpenAPI spec](https://github.com/codatio/oas)
    """

    files: Files
    r"""Endpoints to manage uploaded files."""

    def __init__(
        self,
        auth_header: Union[str, Callable[[], str]],
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param auth_header: The auth_header required for authentication
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        security: Any = None
        if callable(auth_header):
            security = lambda: shared.Security(auth_header=auth_header())  # pylint: disable=unnecessary-lambda-assignment
        else:
            security = shared.Security(auth_header=auth_header)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                async_client=async_client,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, self.sdk_configuration.client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()

    def _init_sdks(self):
        self.files = Files(self.sdk_configuration)