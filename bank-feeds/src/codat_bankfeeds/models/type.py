from __future__ import annotations

from enum import Enum


class Type(str, Enum):
    """Type enum (lifted from inline OAS enum)."""
    RTN = 'rtn'
    ABA = 'aba'
    SWIFT = 'swift'
    BSB = 'bsb'
    IBAN = 'iban'
    NZ2 = 'nz2'
    TRNO = 'trno'
    SORTCODE = 'sortcode'
    BLZ = 'blz'
    IFSC = 'ifsc'
    BANKCODE = 'bankcode'
    APCA = 'apca'
    CLABE = 'clabe'
