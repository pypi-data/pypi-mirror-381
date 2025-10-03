from __future__ import annotations

import enum
import pathlib
from collections.abc import Callable, Generator
from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum, IntEnum, StrEnum
from _decimal import Decimal
from typing import NamedTuple

from pydantic import HttpUrl
import pythoncom

RowFilter = Callable[[Generator[dict[str, str], None, None]], Generator[dict[str, str], None, None]]


class RowInfo(NamedTuple):
    category: str
    id: str


class RowData(NamedTuple):
    row_info: RowInfo
    data: dict[str, str]

    @classmethod
    def from_data(cls, category: str, row_id: str, data: dict[str, str]) -> RowData:
        """Create a RowData instance from category, row_id, and data."""
        return cls(row_info=RowInfo(category=category, id=row_id), data=data)


class NoneFoundHandler(StrEnum):
    ignore = 'IGNORE'
    error = 'ERROR'


class SeekBookmark(Enum):
    """Starting point for cursor seek operations."""

    BEGINNING = 0
    CURRENT = 1
    END = 2


@dataclass
class Connection1:
    name: str
    from_table: str
    to_table: str


@dataclass
class Connection:
    name: str
    category: str
    column: str


CmcDateFormat = '%Y%m%d'
CmcTimeFormat = '%H:%M'


def to_cmc_date(datecheck: date):
    return datecheck.strftime(CmcDateFormat)


def get_cmc_date(v: str) -> date | None:
    """Use CMC Cannonical flag"""
    if isinstance(v, datetime):
        return v.date()
    elif isinstance(v, date):
        return v
    elif isinstance(v, str):
        if v.isdigit():
            if len(v) == 8:
                return datetime.strptime(v, CmcDateFormat).date()
        if len(v) in [7, 10]:
            return datetime.fromisoformat(v).date()
    print(f'No date found: {v}')
    return None


def get_cmc_time(time_str: str):
    """Use CMC Cannonical flag"""
    return datetime.strptime(time_str, CmcTimeFormat).time()


class CursorType(IntEnum):
    """Commence Cursor Types to view based on category, view, or preferences."""

    # open based on a category, columns = all supported fields in the category (in no particular order).
    CATEGORY = 0

    # Valid view-types: report, grid, report viewer, and book/address book.
    # inherit the view's filter, sort, and column set.
    # ICommenceCursor methods can be used to change these attributes.
    VIEW = 1

    # All Pilot* cursor column-sets =  defined by the Commence preferences (in no particular order).
    # It is not possible to change the filter, sort, or column set.

    # Category and fields defined by Preferences-> Other Apps -> 3Com Pilot Address Book.
    PILOT_ADDRESS = 2

    # Category and fields defined by Preferences-> Other Apps -> 3Com Pilot Memo Pad.
    PILOT_MEMO = 3

    # Category and fields defined by Preferences -> Other Apps -> 3Com Pilot To Do List.
    PILOT_TODO = 5

    # Category and fields defined by Preferences -> Other Apps -> 3Com Pilot Date Book.
    PILOT_APPOINT = 6

    # MS Outlook contacts preference
    OUTLOOK_ADDRESS = 7

    # MS Outlook calendar preference
    OUTLOOK_APPOINT = 8

    # MS Outlook Email Log preference
    OUTLOOK_EMAIL_LOG = 9

    # MS Outlook Task preference
    OUTLOOK_TASK = 10

    # open based on the view data used with the Send Letter command
    LETTER_MERGE = 11


class Bookmark(Enum):
    """Starting point for cursor seek operations."""

    BEGINNING = 0
    CURRENT = 1
    END = 2


class OptionFlag(Enum):
    """Flags for get_record and get_value methods."""

    NONE = 0
    FIELD_NAME = 0x0001
    ALL = 0x0002
    SHARED = 0x0004
    PILOT = 0x0008
    CANONICAL = 0x0010
    INTERNET = 0x0020


class OptionFlagInt(IntEnum):
    """Flags for get_record and get_value methods."""

    NONE = 0
    FIELD_NAME = 0x0001
    ALL = 0x0002
    SHARED = 0x0004
    PILOT = 0x0008
    CANONICAL = 0x0010
    INTERNET = 0x0020


FLAGS_UNUSED = 0


class CmcFieldType(enum.Enum):
    TEXT = 0  # Text field.
    NUMBER = 1  # Number field.
    DATE = 2  # Date field.
    TELEPHONE = 3  # Telephone field.
    CHECKBOX = 7  # Check Box field.
    NAME = 11  # Name field (= primary key).
    DATAFILE = 12  # Data File field (= filepath).
    IMAGE = 13  # Image field.
    TIME = 14  # Time field.
    EXCEL_CELL = 15  # Excel cell. (OBSOLETE)
    CALCULATION = 20  # Calculation field.
    SEQUENCE = 21  # Sequence number field.
    SELECTION = 22  # Selection field.
    EMAIL = 23  # E-mail address field.
    URL = 24  # Internet address field.


class CmcFieldDataType(enum.Enum):
    TEXT = str
    NUMBER = Decimal
    DATE = datetime.date
    TELEPHONE = str
    CHECKBOX = bool
    NAME = str
    DATAFILE = pathlib.Path
    IMAGE = pathlib.Path
    TIME = datetime.time
    EXCEL_CELL = str
    CALCULATION = str
    SEQUENCE = int
    SELECTION = str
    EMAIL = str
    URL = HttpUrl


@dataclass
class CmcFieldDefinition:
    type: CmcFieldType
    combobox: bool
    shared: bool
    mandatory: bool
    recurring: bool
    max_chars: int
    default_string: str = ''

    @classmethod
    def from_field_info(cls, field_info: str):
        pythoncom.CoInitialize()  # Initialize COM library on this thread

        parts = field_info.split(DELIM)
        field_type, flags, max_chars, default_string = parts[0], parts[1], parts[2], parts[3]

        return cls(
            type=CmcFieldType(int(field_type)),
            combobox=flags[6] == '1',
            shared=flags[7] == '1',
            mandatory=flags[8] == '1',
            recurring=flags[9] == '1',
            max_chars=int(max_chars),
            default_string=default_string,
        )


DELIM = r';*;%'


@dataclass
class MoreAvailable:
    n_more: int

    def __bool__(self):
        return self.n_more > 0


@dataclass
class Pagination:
    offset: int = 0
    limit: int = 0

    def __bool__(self):
        return any([self.limit, self.offset])

    def __str__(self):
        return f'Pagination: offset={self.offset}, limit={self.limit or "None"}'

    def next_page(self):
        return Pagination(offset=self.offset + self.limit, limit=self.limit)

    def prev_page(self):
        return Pagination(offset=max(0, self.offset - self.limit), limit=self.limit)



