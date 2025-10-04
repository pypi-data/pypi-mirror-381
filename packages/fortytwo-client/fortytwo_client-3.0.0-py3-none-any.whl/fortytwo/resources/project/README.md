# Project Resource

The Project resource provides access to 42 School project data and curriculum information.

## Overview

This module allows you to fetch project information from the 42 API, including project details, difficulty levels, relationships, and curriculum structure.

## Classes

### `Project`
Represents a 42 School project with all associated metadata.

**Properties:**
- `id` (int): Unique project identifier
- `name` (str): Project name
- `slug` (str): URL-friendly project identifier
- `difficulty` (int): Project difficulty level (1-5)
- `exam` (bool): Whether this project is an exam
- `parent` (Optional[Any]): Parent project in curriculum tree
- `children` (List[Any]): Child projects in curriculum tree
- `created_at` (datetime): Project creation date
- `updated_at` (datetime): Last project update date

### Resource Classes

#### `GetProjectsById`
Fetches a single project by its ID.
- **Endpoint:** `/projects/{id}`
- **Method:** GET
- **Returns:** `Project`

#### `GetProjects`
Fetches all projects with optional filtering.
- **Endpoint:** `/projects`
- **Method:** GET
- **Returns:** `List[Project]`

#### `GetProjectsByCursus`
Fetches projects for a specific cursus.
- **Endpoint:** `/cursus/{cursus_id}/projects`
- **Method:** GET
- **Returns:** `List[Project]`

## Usage Examples

### Using the Manager (Recommended)

```python
from fortytwo import Client
from fortytwo.exceptions import FortyTwoNotFoundException

client = Client(
    ...
)

# Get a specific project
try:
    project = client.projects.get_by_id(project_id=1)
    print(f"Project: {project.name}")
    print(f"Difficulty: {project.difficulty}/5")
    print(f"Is Exam: {project.exam}")
except FortyTwoNotFoundException:
    print("Project not found")

# Get all projects with pagination
projects = client.projects.get_all(page=1, page_size=50)

# Get projects by cursus ID with pagination
cursus_projects = client.projects.get_by_cursus_id(cursus_id=21, page=1, page_size=25)
```

### Using Resources Directly

```python
from fortytwo.resources.project.resource import (
    GetProjectsById,
    GetProjects,
    GetProjectsByCursus
)

# Get a specific project
project = client.request(GetProjectsById(1))

# Get all projects
projects = client.request(GetProjects())

# Get projects by cursus
cursus_projects = client.request(GetProjectsByCursus(21))
```

## Data Structure

### Project JSON Response
```json
{
  "id": 1,
  "name": "libft",
  "slug": "libft",
  "difficulty": 2,
  "exam": false,
  "parent": {
    "id": 42,
    "name": "42cursus",
    "slug": "42cursus"
  },
  "children": [
    {
      "id": 15,
      "name": "get_next_line",
      "slug": "get_next_line"
    }
  ],
  "created_at": "2019-05-07T08:45:00Z",
  "updated_at": "2024-01-15T12:30:00Z"
}
```

## Parameters

For detailed information about filtering, sorting, and ranging project queries, see the [Project Parameters Documentation](parameter/README.md).

## Error Handling

All methods raise exceptions on errors:

```python
from fortytwo import Client
from fortytwo.exceptions import FortyTwoNotFoundException, FortyTwoRequestException

client = Client(
    ...
)

try:
    project = client.projects.get_by_id(project_id=99999)
    print(f"Found project: {project.name}")
except FortyTwoNotFoundException:
    print("Project not found")
except FortyTwoRequestException as e:
    print(f"Request failed: {e}")
```
