# Project User Resource

The Project User resource provides access to project completion data, tracking user progress, grades, and team information for 42 School projects.

## Overview

This module allows you to fetch project completion information from the 42 API, including grades, status, team details, and project progression data.

## Classes

### `ProjectUser`
Represents a user's completion record for a specific project.

**Properties:**
- `id` (int): Team ID for this project completion
- `name` (str): Team name
- `status` (str): Completion status ("finished", "in_progress", "waiting_for_correction", etc.)
- `final_mark` (int): Final grade received (0-100+)
- `created_at` (datetime): When the project was started
- `updated_at` (datetime): Last update to the project status

### Resource Classes

#### `GetProjectUsers`
Fetches project completion records with filtering options.
- **Endpoint:** `/projects_users`
- **Method:** GET
- **Returns:** `List[ProjectUser]`

#### `GetProjectUsersByProject`
Fetches all completions for a specific project.
- **Endpoint:** `/projects/{project_id}/projects_users`
- **Method:** GET
- **Returns:** `List[ProjectUser]`

## Usage Examples

### Using the Manager (Recommended)

```python
from fortytwo import Client

client = Client(
    ...
)

# Get all project completions with pagination
all_project_users = client.project_users.get_all(page=1, page_size=100)
print(f"Found {len(all_project_users)} project completions")

# Show grades
for project in all_project_users:
    status_emoji = "✅" if project.status == "finished" else "🔄"
    print(f"{status_emoji} {project.name}: {project.final_mark}/100")

# Get all completions for a specific project with pagination
project_completions = client.project_users.get_by_project_id(
    project_id=1,
    page=1,
    page_size=50
)
if project_completions:
    avg_grade = sum(p.final_mark for p in project_completions) / len(project_completions)
    print(f"Average grade for this project: {avg_grade:.1f}/100")
```

### Using Resources Directly

```python
from fortytwo.resources.project_user.resource import (
    GetProjectUsers,
    GetProjectUsersByProject
)

# Get all project users
all_completions = client.request(GetProjectUsers())

# Get completions for a specific project
project_completions = client.request(GetProjectUsersByProject(1))
```
user_completions = client.request(GetProjectUsersByUserId(12345))

# Get project completion statistics
project_stats = client.request(GetProjectUsersByProjectId(1))
```

## Data Structure

### Project User JSON Response
```json
{
  "id": 456789,
  "name": "team_name",
  "status": "finished",
  "final_mark": 95,
  "created_at": "2024-01-15T10:00:00Z",
  "updated_at": "2024-01-22T16:30:00Z"
}
```

## Parameters

For detailed information about filtering and ranging project_user queries, see the [ProjectUser Parameters Documentation](parameter/README.md).

> [!NOTE]
> Note: ProjectUser resources do not support sorting parameters.

## Error Handling

Methods raise exceptions on errors:

```python
from fortytwo import Client
from fortytwo.exceptions import FortyTwoRequestException

client = Client(
    ...
)

try:
    projects = client.project_users.get_all(page=1, page_size=100)
    if not projects:
        print("No project completions found")
    else:
        print(f"Found {len(projects)} project completions")
except FortyTwoRequestException as e:
    print(f"Request failed: {e}")
```
