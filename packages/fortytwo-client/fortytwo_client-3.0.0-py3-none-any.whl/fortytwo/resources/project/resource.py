"""
Resources for fetching project data from the 42 API.
"""

from typing import Any, Self

from fortytwo.resources.project.project import Project
from fortytwo.resources.resource import Resource, ResourceTemplate


class GetProjects(Resource[list[Project]]):
    """
    Resource for fetching all projects.

    Returns a list of projects from the /projects endpoint.
    Supports pagination via parameters.
    """

    method: str = "GET"
    _url: str = "/projects"

    @property
    def url(self: Self) -> str:
        return self.config.request_endpoint + self._url

    def parse_response(self: Self, response_data: Any) -> ResourceTemplate:
        return [Project(project) for project in response_data]


class GetProjectsById(Resource[Project]):
    """
    Resource for fetching a specific project by ID.

    Args:
        project_id: The ID of the project to fetch.
    """

    method: str = "GET"
    _url: str = "/projects/%s"

    def __init__(self: Self, project_id: int) -> None:
        self.project_id = project_id

    @property
    def url(self: Self) -> str:
        return self.config.request_endpoint + self._url % self.project_id

    def parse_response(self: Self, response_data: Any) -> ResourceTemplate:
        return Project(response_data)


class GetProjectsByCursus(Resource[list[Project]]):
    """
    This class provides a resource for getting all projects for a cursus.
    """

    method: str = "GET"
    _url: str = "/cursus/%s/projects"

    def __init__(self: Self, cursus_id: int) -> None:
        self.cursus_id = cursus_id

    @property
    def url(self: Self) -> str:
        return self.config.request_endpoint + self._url % self.cursus_id

    def parse_response(self: Self, response_data: Any) -> ResourceTemplate:
        return [Project(project) for project in response_data]
