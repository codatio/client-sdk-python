from __future__ import annotations

from enum import Enum


class Type(str, Enum):
    """Type enum (lifted from inline OAS enum)."""
    ABA = 'aba'
    APCA = 'apca'
    BANKCODE = 'bankcode'
    BLZ = 'blz'
    BSB = 'bsb'
    CLABE = 'clabe'
    IBAN = 'iban'
    IFSC = 'ifsc'
    NZ2 = 'nz2'
    RTN = 'rtn'
    SORTCODE = 'sortcode'
    SWIFT = 'swift'
    TRNO = 'trno'
