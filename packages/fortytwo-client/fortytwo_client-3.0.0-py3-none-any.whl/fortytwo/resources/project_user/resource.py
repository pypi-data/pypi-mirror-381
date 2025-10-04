"""
Resources for fetching project user data from the 42 API.
"""

from typing import Any, Self

from fortytwo.resources.project_user.project_user import ProjectUser
from fortytwo.resources.resource import Resource, ResourceTemplate


class GetProjectUsers(Resource[list[ProjectUser]]):
    """
    Resource for fetching all project users.

    Returns a list of project user records showing student progress
    on projects. Only includes records with associated teams.
    Supports pagination via parameters.
    """

    method: str = "GET"
    _url: str = "/projects_users"

    @property
    def url(self: Self) -> str:
        return self.config.request_endpoint + self._url

    def parse_response(self: Self, response_data: Any) -> ResourceTemplate:
        return [
            ProjectUser(project_user) for project_user in response_data if project_user["teams"]
        ]


class GetProjectUsersByProject(Resource[list[ProjectUser]]):
    """
    Resource for fetching project users for a specific project.

    Returns a list of project user records for students working on
    the specified project. Only includes records with associated teams.

    Args:
        project_id: The ID of the project to fetch project users for.
    """

    method: str = "GET"
    _url: str = "/projects/%s/projects_users"

    def __init__(self: Self, project_id: int) -> None:
        self.project_id = project_id

    @property
    def url(self: Self) -> str:
        return self.config.request_endpoint + self._url % self.project_id

    def parse_response(self: Self, response_data: Any) -> ResourceTemplate:
        return [
            ProjectUser(project_user) for project_user in response_data if project_user["teams"]
        ]
