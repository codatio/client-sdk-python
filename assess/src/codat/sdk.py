__doc__ = """ SDK Documentation: Codat's Assess API enable you to make smarter credit decisions on your small business customers. Assess enriches your customer's accounting, commerce and banking data to surface actionable insights you didn't have before.

[Read more...](https://www.codat.io/assess/)

[See our OpenAPI spec](https://github.com/codatio/oas) """
import requests as requests_http
from . import utils
from .categories import Categories
from .data_integrity import DataIntegrity
from .excel_reports import ExcelReports
from .reports import Reports
from codat.models import shared

SERVERS = [
	"https://api.codat.io",
]

class Codat:
    r"""SDK Documentation: Codat's Assess API enable you to make smarter credit decisions on your small business customers. Assess enriches your customer's accounting, commerce and banking data to surface actionable insights you didn't have before.
    
    [Read more...](https://www.codat.io/assess/)
    
    [See our OpenAPI spec](https://github.com/codatio/oas) """
    categories: Categories
    data_integrity: DataIntegrity
    excel_reports: ExcelReports
    reports: Reports
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    _security: shared.Security
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.3.0"
    _gen_version: str = "1.9.1"

    def __init__(self) -> None:
        self._client = requests_http.Session()
        self._security_client = requests_http.Session()
        self._init_sdks()

    def config_server_url(self, server_url: str, params: dict[str, str] = None):
        if params is not None:
            self._server_url = utils.template_url(server_url, params)
        else:
            self._server_url = server_url

        self._init_sdks()
    
    

    def config_client(self, client: requests_http.Session):
        self._client = client
        
        if self._security is not None:
            self._security_client = utils.configure_security_client(self._client, self._security)
        self._init_sdks()
    
    def config_security(self, security: shared.Security):
        self._security = security
        self._security_client = utils.configure_security_client(self._client, security)
        self._init_sdks()
    
    def _init_sdks(self):
        self.categories = Categories(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.data_integrity = DataIntegrity(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.excel_reports = ExcelReports(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.reports = Reports(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    