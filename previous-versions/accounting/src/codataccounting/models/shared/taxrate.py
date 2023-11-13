"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .metadata import Metadata
from .supplementaldata import SupplementalData
from .taxratecomponent import TaxRateComponent
from .taxratestatus import TaxRateStatus
from .validdatatypelinks import ValidDataTypeLinks
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxRate:
    r"""> View the coverage for tax rates in the <a className=\\"external\\" href=\\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=taxRates\\" target=\\"_blank\\">Data coverage explorer</a>.

    ## Overview

    Accounting systems typically store a set of taxes and associated rates within the accounting package. This means that users don't have to look up or remember the rates for each type of tax. For example, applying the tax \"UK sales VAT\" to line items of an invoice adds the correct rate of 20%.

    ### Tax components

    In some cases, a tax is made up of multiple sub taxes, often called _components_ of the tax.  For example, you may have an item that is charged a tax rate called \"City import tax (8%)\" that has two components:

    - A city tax of 5%
    - An import tax of 3%

    > **Effective tax rates**
    > - Where there are multiple components of a tax, each component may be calculated on the original amount and added together. Alternatively, one tax may be calculated on the sub-total of the original amount plus another tax, which is referred to as _compounding_. When there is compounding, the effective tax rate is the rate that, if applied to the original amount, would result in the total amount of tax with compounding.
    >
    > **Example:**  
    > A tax has two components. Both components have a rate of 10%, and one component is compound. In this case, there is a total tax rate of 20% but an effective tax rate of 21%.
    >
    > - For QuickBooks Online, Codat doesn't use compound rates. Instead, the calculated effective tax rate for each component is shown. This means that the effective and total rates are the same because the total tax rate is a sum of the component rates.
    """
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code') }})
    r"""Code for the tax rate from the accounting platform."""
    components: Optional[List[TaxRateComponent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('components') }})
    effective_tax_rate: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('effectiveTaxRate'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""See Effective tax rates description."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the tax rate, unique for the company in the accounting platform."""
    metadata: Optional[Metadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Codat-augmented name of the tax rate in the accounting platform."""
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    status: Optional[TaxRateStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Status of the tax rate in the accounting platform.
    - `Active` - An active tax rate in use by a company.  
    - `Archived` - A tax rate that has been archived or is inactive in the accounting platform.  
    - `Unknown` - Where the status of the tax rate cannot be determined from the underlying platform.
    """
    supplemental_data: Optional[SupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplementalData'), 'exclude': lambda f: f is None }})
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting platform. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    total_tax_rate: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalTaxRate'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Total (not compounded) sum of the components of a tax rate."""
    valid_datatype_links: Optional[List[ValidDataTypeLinks]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validDatatypeLinks') }})
    

