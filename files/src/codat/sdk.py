__doc__ = """ SDK Documentation: An API for uploading and downloading files from 'File Upload' Integrations.

The Accounting file upload, Banking file upload, and Business documents file upload integrations provide simple file upload functionality.

[Read more...](https://docs.codat.io/other/file-upload)

[See our OpenAPI spec](https://github.com/codatio/oas) """
import requests
from . import utils
from .files import Files
from codat.models import shared

SERVERS = [
	"https://api.codat.io",
]

class Codat:
    r"""SDK Documentation: An API for uploading and downloading files from 'File Upload' Integrations.
    
    The Accounting file upload, Banking file upload, and Business documents file upload integrations provide simple file upload functionality.
    
    [Read more...](https://docs.codat.io/other/file-upload)
    
    [See our OpenAPI spec](https://github.com/codatio/oas) """
    files: Files
    
    _client: requests.Session
    _security_client: requests.Session
    _security: shared.Security
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.2.0"
    _gen_version: str = "1.8.2"

    def __init__(self) -> None:
        self._client = requests.Session()
        self._security_client = requests.Session()
        self._init_sdks()

    def config_server_url(self, server_url: str, params: dict[str, str] = None):
        if params is not None:
            self._server_url = utils.template_url(server_url, params)
        else:
            self._server_url = server_url

        self._init_sdks()
    
    

    def config_client(self, client: requests.Session):
        self._client = client
        
        if self._security is not None:
            self._security_client = utils.configure_security_client(self._client, self._security)
        self._init_sdks()
    
    def config_security(self, security: shared.Security):
        self._security = security
        self._security_client = utils.configure_security_client(self._client, security)
        self._init_sdks()
    
    def _init_sdks(self):
        self.files = Files(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    