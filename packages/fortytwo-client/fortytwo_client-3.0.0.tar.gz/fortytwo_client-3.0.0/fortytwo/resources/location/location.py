"""
This module provides resources for location of users from the 42 API.
"""

from typing import TYPE_CHECKING, Any, Self

from dateutil.parser import parse as parse_date

from fortytwo.json import register_serializer
from fortytwo.resources.model import Model


if TYPE_CHECKING:
    from datetime import datetime


class Location(Model):
    """
    This class provides a representation of a 42 location.
    """

    def __init__(self: Self, data: Any) -> None:
        self.id: int = data["id"]
        self.host: str = data["host"]

        self.begin_at: datetime = parse_date(data["begin_at"])
        self.end_at: datetime | None = parse_date(data["end_at"]) if data["end_at"] else None

    def __repr__(self: Self) -> str:
        return f"<Location {self.id}>"

    def __str__(self: Self) -> str:
        return str(self.id)


register_serializer(
    Location,
    lambda u: {
        "id": u.id,
        "begin_at": u.begin_at.isoformat(),
        "end_at": u.end_at.isoformat() if u.end_at else None,
    },
)
