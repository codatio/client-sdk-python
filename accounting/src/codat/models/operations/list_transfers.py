from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from typing import Any, Optional


@dataclasses.dataclass
class ListTransfersPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListTransfersQueryParams:
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListTransfersSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class ListTransfersRequest:
    path_params: ListTransfersPathParams = dataclasses.field()
    query_params: ListTransfersQueryParams = dataclasses.field()
    security: ListTransfersSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinksLinksCurrent:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinksLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinksLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinksLinksSelf:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinksLinks:
    current: ListTransfersLinksLinksCurrent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('current') }})
    self: ListTransfersLinksLinksSelf = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('self') }})
    next: Optional[ListTransfersLinksLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[ListTransfersLinksLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinksSourceModifiedDateContactRef:
    r"""ListTransfersLinksSourceModifiedDateContactRef
    The customer or supplier for the transfer, if available.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinksSourceModifiedDateTransferAccountAccountRef:
    r"""ListTransfersLinksSourceModifiedDateTransferAccountAccountRef
    The account that the transfer is moving from or to.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinksSourceModifiedDateTransferAccount:
    r"""ListTransfersLinksSourceModifiedDateTransferAccount
    The details of the accounts the transfer is moving from.
    """
    
    account_ref: Optional[ListTransfersLinksSourceModifiedDateTransferAccountAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinksSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinksSourceModifiedDateSupplementalData:
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('content'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinksSourceModifiedDateTrackingCategoryRefs:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinksSourceModifiedDate:
    r"""ListTransfersLinksSourceModifiedDate
    > View the coverage for transfers in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers\" target=\"_blank\">Data coverage explorer</a>.
    
    From the **Transfers** endpoints, you can:
    
    - [Retrieve a list of all transfers for a specified company](https://api.codat.io/swagger/index.html#/Transfers/get_companies__companyId__connections__connectionId__data_transfers)
    - [Retrieve a single transfer for a specified company](https://api.codat.io/swagger/index.html#/Transfers/get_companies__companyId__connections__connectionId__data_transfers__transferId_) 
    - [Add a new transfer for a specified company](https://api.codat.io/swagger/index.html#/Transfers/post_companies__companyId__connections__connectionId__push_transfers) 
    
    **Transfers** is a child data type of [account transactions](https://docs.codat.io/accounting-api#/schemas/AccountTransaction).
    """
    
    contact_ref: Optional[ListTransfersLinksSourceModifiedDateContactRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contactRef'), 'exclude': lambda f: f is None }})
    date_: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    deposited_record_refs: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('depositedRecordRefs'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    from_: Optional[ListTransfersLinksSourceModifiedDateTransferAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('from'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    metadata: Optional[ListTransfersLinksSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    supplemental_data: Optional[ListTransfersLinksSourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplementalData'), 'exclude': lambda f: f is None }})
    to: Optional[ListTransfersLinksSourceModifiedDateTransferAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('to'), 'exclude': lambda f: f is None }})
    tracking_category_refs: Optional[list[ListTransfersLinksSourceModifiedDateTrackingCategoryRefs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trackingCategoryRefs'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTransfersLinks:
    r"""ListTransfersLinks
    Codat's Paging Model
    """
    
    links: ListTransfersLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('_links') }})
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    results: Optional[list[ListTransfersLinksSourceModifiedDate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ListTransfersResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    links: Optional[ListTransfersLinks] = dataclasses.field(default=None)
    