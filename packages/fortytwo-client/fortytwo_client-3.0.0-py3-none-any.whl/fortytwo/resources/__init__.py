"""
This module provides a base class for 42 API resources.
"""

from fortytwo.resources import (
    custom,
    location,
    project,
    project_user,
    token,
    user,
)
from fortytwo.resources.model import Model


__all__ = [
    "Model",
    "custom",
    "location",
    "project",
    "project_user",
    "token",
    "user",
]
