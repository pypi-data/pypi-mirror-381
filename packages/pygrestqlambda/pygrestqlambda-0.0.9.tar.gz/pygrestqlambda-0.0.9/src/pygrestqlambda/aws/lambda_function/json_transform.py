"""
JSON output transformer for non-serialisable values
"""

from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

def to_string(value: object) -> str | float:
    """
    Calculates the string version of an object to return in a JSON response
    """

    if isinstance(value, UUID):
        # Handle UUIDs
        value = str(value)
    elif isinstance(value, datetime):
        # Handle date/timestamps
        value = value.isoformat()
    elif isinstance(value, date):
        value = value.isoformat()
    elif isinstance(value, Decimal):
        # Handle decimals
        value = float(value)
    elif not isinstance(value, str):
        # Handle non-string case
        raise TypeError('Unhandled type')

    return value
