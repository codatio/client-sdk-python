from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from typing import Any, Optional


@dataclasses.dataclass
class GetJournalEntryPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    journal_entry_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'journalEntryId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetJournalEntrySecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetJournalEntryRequest:
    path_params: GetJournalEntryPathParams = dataclasses.field()
    security: GetJournalEntrySecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetJournalEntrySourceModifiedDateJournalLinesAccountRef:
    r"""GetJournalEntrySourceModifiedDateJournalLinesAccountRef
    Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetJournalEntrySourceModifiedDateJournalLinesTracking:
    r"""GetJournalEntrySourceModifiedDateJournalLinesTracking
    List of record refs associated with the tracking information for the line (eg to a Tracking Category, or customer etc.)
    """
    
    record_refs: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('recordRefs'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetJournalEntrySourceModifiedDateJournalLines:
    net_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('netAmount') }})
    account_ref: Optional[GetJournalEntrySourceModifiedDateJournalLinesAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    tracking: Optional[GetJournalEntrySourceModifiedDateJournalLinesTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tracking'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetJournalEntrySourceModifiedDateJournalRef:
    r"""GetJournalEntrySourceModifiedDateJournalRef
    Links journal entries to the relevant journal in accounting integrations that use multi-book accounting (multiple journals).
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetJournalEntrySourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetJournalEntrySourceModifiedDateRecordRef:
    r"""GetJournalEntrySourceModifiedDateRecordRef
    Links to the underlying record or data type.
    
    Found on:
    
    - Journal entries
    - Account transactions
    - Invoices
    - Transfers
    """
    
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetJournalEntrySourceModifiedDateSupplementalData:
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('content'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetJournalEntrySourceModifiedDate:
    r"""GetJournalEntrySourceModifiedDate
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
    
    created_on: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdOn'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    journal_lines: Optional[list[GetJournalEntrySourceModifiedDateJournalLines]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('journalLines'), 'exclude': lambda f: f is None }})
    journal_ref: Optional[GetJournalEntrySourceModifiedDateJournalRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('journalRef'), 'exclude': lambda f: f is None }})
    metadata: Optional[GetJournalEntrySourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    posted_on: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('postedOn'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    record_ref: Optional[GetJournalEntrySourceModifiedDateRecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('recordRef'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    supplemental_data: Optional[GetJournalEntrySourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplementalData'), 'exclude': lambda f: f is None }})
    updated_on: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('updatedOn'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetJournalEntryResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    source_modified_date: Optional[GetJournalEntrySourceModifiedDate] = dataclasses.field(default=None)
    