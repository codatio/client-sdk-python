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
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.4.0"
    _gen_version: str = "1.11.0"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
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
        
    