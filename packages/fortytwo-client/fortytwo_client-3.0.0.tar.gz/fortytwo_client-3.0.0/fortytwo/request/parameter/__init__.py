"""
Query parameter utilities for the FortyTwo API client.

This module provides base parameter classes and resource-specific parameter namespaces.
"""

from fortytwo.request.parameter.parameter import (
    Filter,
    PageNumber,
    PageSize,
    Parameter,
    Range,
    Sort,
)
from fortytwo.resources.location.parameter import LocationParameters
from fortytwo.resources.project.parameter import ProjectParameters
from fortytwo.resources.project_user.parameter import ProjectUserParameters
from fortytwo.resources.user.parameter import UserParameters


__all__ = [
    "Filter",
    "LocationParameters",
    "PageNumber",
    "PageSize",
    "Parameter",
    "ProjectParameters",
    "ProjectUserParameters",
    "Range",
    "Sort",
    "UserParameters",
]
