"""
Project resource for the FortyTwo API.

This module provides the Project model and ProjectManager for interacting
with project data.
"""

from fortytwo.resources.project.manager import ProjectManager
from fortytwo.resources.project.project import Project


__all__ = [
    "Project",
    "ProjectManager",
]
