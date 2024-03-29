"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountbalance import AccountBalance
from .items import Items
from .phonenumber_items import PhoneNumberItems
from .weblink_items import WebLinkItems
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CommerceCompanyInfo:
    r"""In the Codat system, company profile includes standard commercial details about
    a linked company, such as their address, phone number, and company registration.

    Explore our [data coverage](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=companyInfo) for this data type.
    """
    account_balances: Optional[List[AccountBalance]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountBalances'), 'exclude': lambda f: f is None }})
    r"""The available and current cash balances for the company's accounts"""
    addresses: Optional[List[Items]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addresses'), 'exclude': lambda f: f is None }})
    r"""Addresses associated with the company"""
    base_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('baseCurrency'), 'exclude': lambda f: f is None }})
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction. 

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    commerce_platform_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('commercePlatformRef'), 'exclude': lambda f: f is None }})
    r"""Identifier or reference for the company in the commerce platform"""
    company_legal_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyLegalName'), 'exclude': lambda f: f is None }})
    r"""The full legal name of the company"""
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyName'), 'exclude': lambda f: f is None }})
    r"""The name of the company"""
    created_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdDate'), 'exclude': lambda f: f is None }})
    r"""In Codat's data model, dates and times are represented using the <a class=\\"external\\" href=\\"https://en.wikipedia.org/wiki/ISO_8601\\" target=\\"_blank\\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```



    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:

    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`

    > Time zones
    > 
    > Not all dates from Codat will contain information about time zones.  
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    phone_numbers: Optional[List[PhoneNumberItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phoneNumbers'), 'exclude': lambda f: f is None }})
    r"""Phone numbers associated with the company"""
    registration_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('registrationNumber'), 'exclude': lambda f: f is None }})
    r"""The registration number of the company"""
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    source_urls: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceUrls'), 'exclude': lambda f: f is None }})
    r"""URL addresses for the originating system. For example, potential use cases include 'deeplinking' to the originating system"""
    web_links: Optional[List[WebLinkItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webLinks'), 'exclude': lambda f: f is None }})
    r"""Weblinks associated with the company"""
    

