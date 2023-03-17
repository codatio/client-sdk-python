from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from typing import Any, Optional


@dataclasses.dataclass
class ListJournalEntriesRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    page: int = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksLinksCurrent:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksLinksSelf:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksLinks:
    current: ListJournalEntriesLinksLinksCurrent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current') }})
    self_: ListJournalEntriesLinksLinksSelf = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('self') }})
    next: Optional[ListJournalEntriesLinksLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[ListJournalEntriesLinksLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksSourceModifiedDateJournalLinesAccountRef:
    r"""ListJournalEntriesLinksSourceModifiedDateJournalLinesAccountRef
    Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksSourceModifiedDateJournalLinesTracking:
    r"""ListJournalEntriesLinksSourceModifiedDateJournalLinesTracking
    List of record refs associated with the tracking information for the line (eg to a Tracking Category, or customer etc.)
    """
    
    record_refs: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRefs'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksSourceModifiedDateJournalLines:
    net_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('netAmount') }})
    account_ref: Optional[ListJournalEntriesLinksSourceModifiedDateJournalLinesAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    tracking: Optional[ListJournalEntriesLinksSourceModifiedDateJournalLinesTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksSourceModifiedDateJournalRef:
    r"""ListJournalEntriesLinksSourceModifiedDateJournalRef
    Links journal entries to the relevant journal in accounting integrations that use multi-book accounting (multiple journals).
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDeleted'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksSourceModifiedDateRecordRef:
    r"""ListJournalEntriesLinksSourceModifiedDateRecordRef
    Links to the underlying record or data type.
    
    Found on:
    
    - Journal entries
    - Account transactions
    - Invoices
    - Transfers
    """
    
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksSourceModifiedDateSupplementalData:
    r"""ListJournalEntriesLinksSourceModifiedDateSupplementalData
    Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more.
    """
    
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinksSourceModifiedDate:
    r"""ListJournalEntriesLinksSourceModifiedDate
    > **Language tip:** For the top-level record of a company's financial transactions, refer to the [Journals](https://docs.codat.io/accounting-api#/schemas/Journal) data type
    
    > View the coverage for journal entries in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A journal entry report shows the entries made in a company's general ledger, or [accounts](https://api.codat.io/swagger/index.html#/Accounts/get_companies__companyId__data_accounts), when transactions are approved. The journal line items for each journal entry should balance.
    
    A journal entry line item is a single transaction line on the journal entry. For example: 
    
    - When a journal entry is recording a receipt of cash, the credit to accounts receivable and the debit to cash are separate line items. 
    - When a company needs to recognise revenue from an annual contract on a monthly basis, on receipt of cash for month one, they make a debit to deferred income and a credit to revenue.
    
    In Codat a journal entry contains details of:
    
    - The date on which the entry was created and posted.
    - Itemised lines, including amounts and currency.
    - A reference to the associated accounts.
    - A reference to the underlying record. For example, the invoice, bill, or other data type that triggered the posting of the journal entry to the general ledger. 
    
    > **Pushing journal entries **  
    > Codat only supports journal entries in the base currency of the company that are pushed into accounts denominated in the same base currency.
    """
    
    created_on: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdOn'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    journal_lines: Optional[list[ListJournalEntriesLinksSourceModifiedDateJournalLines]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('journalLines'), 'exclude': lambda f: f is None }})
    journal_ref: Optional[ListJournalEntriesLinksSourceModifiedDateJournalRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('journalRef'), 'exclude': lambda f: f is None }})
    metadata: Optional[ListJournalEntriesLinksSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    posted_on: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postedOn'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    record_ref: Optional[ListJournalEntriesLinksSourceModifiedDateRecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRef'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    supplemental_data: Optional[ListJournalEntriesLinksSourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplementalData'), 'exclude': lambda f: f is None }})
    updated_on: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedOn'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListJournalEntriesLinks:
    r"""ListJournalEntriesLinks
    Codat's Paging Model
    """
    
    links: ListJournalEntriesLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_links') }})
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalResults') }})
    results: Optional[list[ListJournalEntriesLinksSourceModifiedDate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ListJournalEntriesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    links: Optional[ListJournalEntriesLinks] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    