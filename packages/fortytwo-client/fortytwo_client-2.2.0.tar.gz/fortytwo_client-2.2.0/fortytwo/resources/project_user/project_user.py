"""
This module provides ressources for getting project users from the 42 API.
"""

from typing import TYPE_CHECKING, Any, List, Self

from dateutil.parser import parse as parse_date

from fortytwo.json import register_serializer

if TYPE_CHECKING:
    from datetime import datetime, timedelta


class FortyTwoProjectUser:
    """
    This class provides a representation of a 42 project user.
    """

    def __init__(self: Self, data: Any) -> None:
        latest_team: List[Any] = data["teams"][-1]

        self.id: int = latest_team["id"]
        self.name: str = latest_team["name"]

        self.status: str = latest_team["status"]
        self.final_mark: int = latest_team["final_mark"]

        self.created_at: datetime = parse_date(latest_team["created_at"])
        self.updated_at: datetime = parse_date(latest_team["updated_at"])
        self.duration: timedelta = self.updated_at - self.created_at

    def __repr__(self: Self) -> str:
        return f"<FortyTwoProjectUser {self.name}>"

    def __str__(self: Self) -> str:
        return self.name


register_serializer(
    FortyTwoProjectUser,
    lambda p: {
        "id": p.id,
        "name": p.name,
        "status": p.status,
        "final_mark": p.final_mark,
        "created_at": p.created_at.isoformat(),
        "updated_at": p.updated_at.isoformat(),
        "duration": p.duration.total_seconds(),
    },
)
