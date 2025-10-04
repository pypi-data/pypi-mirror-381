"""
This module provides resources for getting projects from the 42 API.
"""

from typing import TYPE_CHECKING, Any, Self

from dateutil.parser import parse as parse_date

from fortytwo.json import register_serializer
from fortytwo.resources.model import Model


if TYPE_CHECKING:
    from datetime import datetime


class Project(Model):
    """
    This class provides a representation of a 42 project.
    """

    def __init__(self: Self, data: Any) -> None:
        self.id: int = data["id"]

        self.name: str = data["name"]
        self.slug: str = data["slug"]

        self.difficulty: int = data["difficulty"]

        self.created_at: datetime = parse_date(data["created_at"])
        self.updated_at: datetime = parse_date(data["updated_at"])

        self.exam: bool = data["exam"]
        self.parent: Any | None = data["parent"]
        self.children: list[Any] = data["children"]

    def __repr__(self: Self) -> str:
        return f"<Project {self.name}>"

    def __str__(self: Self) -> str:
        return self.name


register_serializer(
    Project,
    lambda p: {
        "id": p.id,
        "name": p.name,
        "slug": p.slug,
        "difficulty": p.difficulty,
        "created_at": p.created_at.isoformat(),
        "updated_at": p.updated_at.isoformat(),
        "exam": p.exam,
        "parent": p.parent,
        "children": p.children,
    },
)
