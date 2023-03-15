__doc__ = """ SDK Documentation: Bank Feeds API enables your SMB users to set up bank feeds from accounts in your application to supported accounting platforms.

A bank feed is a connection between a source bank account—in your application—and a target bank account in a supported accounting package.

[Read more...](https://docs.codat.io/bank-feeds-api/overview)

[See our OpenAPI spec](https://github.com/codatio/oas) """
import requests as requests_http
from . import utils
from .bank_account_transactions import BankAccountTransactions
from .bank_feed_accounts import BankFeedAccounts
from codat.models import shared

SERVERS = [
	"https://api.codat.io",
]

class Codat:
    r"""SDK Documentation: Bank Feeds API enables your SMB users to set up bank feeds from accounts in your application to supported accounting platforms.
    
    A bank feed is a connection between a source bank account—in your application—and a target bank account in a supported accounting package.
    
    [Read more...](https://docs.codat.io/bank-feeds-api/overview)
    
    [See our OpenAPI spec](https://github.com/codatio/oas) """
    bank_account_transactions: BankAccountTransactions
    bank_feed_accounts: BankFeedAccounts
    
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
        self.bank_account_transactions = BankAccountTransactions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.bank_feed_accounts = BankFeedAccounts(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    