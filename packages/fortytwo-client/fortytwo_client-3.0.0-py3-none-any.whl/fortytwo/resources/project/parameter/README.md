# Project Parameters

This document describes all available parameters for filtering, sorting, and ranging Project resources in the 42 API.

## Overview

Project parameters allow you to customize queries to the 42 API's project endpoint. You can:
- **Filter** - Find projects matching specific criteria
- **Sort** - Order results by specific fields
- **Range** - Retrieve projects within a specific range of values

## Usage

```python
from fortytwo import Client, parameter

client = Client(
    ...
)

# Using project-specific parameters
projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_visible(True),
    parameter.ProjectParameters.Sort.by_difficulty("asc"),
    parameter.PageSize(50)
)
```

## Filter Parameters

Filters narrow down results to match specific criteria.

### `by_id(project_id)`
Filter projects by their unique ID.

**Parameters:**
- `project_id` (str | int): The project ID to filter by

**Example:**
```python
projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_id(1337)
)
```

---

### `by_name(name)`
Filter projects by their exact name.

**Parameters:**
- `name` (str): The project name to filter by

**Example:**
```python
projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_name("ft_transcendence")
)
```

---

### `by_slug(slug)`
Filter projects by their URL-friendly slug.

**Parameters:**
- `slug` (str): The project slug to filter by

**Example:**
```python
projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_slug("42cursus-ft-transcendence")
)
```

---

### `by_created_at(created_at)`
Filter projects by their creation date.

**Parameters:**
- `created_at` (str | datetime): The creation date (ISO format string or datetime object)

**Example:**
```python
from datetime import datetime

projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_created_at("2024-01-01T00:00:00Z")
)
```

---

### `by_updated_at(updated_at)`
Filter projects by their last update date.

**Parameters:**
- `updated_at` (str | datetime): The update date (ISO format string or datetime object)

**Example:**
```python
projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_updated_at("2024-10-01T00:00:00Z")
)
```

---

### `by_visible(visible)`
Filter projects by visibility status.

**Parameters:**
- `visible` (str | bool): Visibility status (True/False or "true"/"false")

**Example:**
```python
# Get only visible projects
projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_visible(True)
)

# Get hidden projects
projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_visible(False)
)
```

---

### `by_exam(exam)`
Filter projects by whether they are exams.

**Parameters:**
- `exam` (str | bool): Exam status (True/False or "true"/"false")

**Example:**
```python
# Get only exam projects
exams = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_exam(True)
)

# Get non-exam projects
projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_exam(False)
)
```

---

### `by_parent_id(parent_id)`
Filter projects by their parent project ID.

**Parameters:**
- `parent_id` (str | int): The parent project ID

**Example:**
```python
# Get all child projects of a specific parent
child_projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_parent_id(100)
)
```

---

### `by_cursus_id(cursus_id)`
Filter projects belonging to a specific cursus.

**Parameters:**
- `cursus_id` (str | int): The cursus ID

**Example:**
```python
# Get all projects in the 42 cursus (ID: 21)
cursus_projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_cursus_id(21)
)
```

---

### `by_campus_id(campus_id)`
Filter projects available at a specific campus.

**Parameters:**
- `campus_id` (str | int): The campus ID

**Example:**
```python
# Get projects available at Paris campus (ID: 1)
campus_projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_campus_id(1)
)
```

---

## Sort Parameters

Sort parameters order the results by specific fields.

All sort methods accept a `direction` parameter:
- `"asc"` - Ascending order (A-Z, 0-9, easiest-hardest)
- `"desc"` - Descending order (Z-A, 9-0, hardest-easiest)

### `by_id(direction="desc")`
Sort by project ID.

**Default:** Descending (newest projects first)

**Example:**
```python
# Newest projects first
projects = client.projects.get_all(
    parameter.ProjectParameters.Sort.by_id()
)

# Oldest projects first
projects = client.projects.get_all(
    parameter.ProjectParameters.Sort.by_id("asc")
)
```

---

### `by_name(direction="asc")`
Sort alphabetically by project name.

**Default:** Ascending (A-Z)

**Example:**
```python
# A-Z
projects = client.projects.get_all(
    parameter.ProjectParameters.Sort.by_name()
)

# Z-A
projects = client.projects.get_all(
    parameter.ProjectParameters.Sort.by_name("desc")
)
```

---

### `by_slug(direction="asc")`
Sort alphabetically by project slug.

**Default:** Ascending (A-Z)

**Example:**
```python
projects = client.projects.get_all(
    parameter.ProjectParameters.Sort.by_slug()
)
```

---

### `by_difficulty(direction="asc")`
Sort by project difficulty level.

**Default:** Ascending (easiest to hardest)

**Example:**
```python
# Easiest projects first
projects = client.projects.get_all(
    parameter.ProjectParameters.Sort.by_difficulty()
)

# Hardest projects first
projects = client.projects.get_all(
    parameter.ProjectParameters.Sort.by_difficulty("desc")
)
```

---

### `by_created_at(direction="desc")`
Sort by creation date.

**Default:** Descending (newest first)

**Example:**
```python
# Recently created projects first
projects = client.projects.get_all(
    parameter.ProjectParameters.Sort.by_created_at()
)
```

---

### `by_updated_at(direction="desc")`
Sort by last update date.

**Default:** Descending (most recently updated first)

**Example:**
```python
# Recently updated projects first
projects = client.projects.get_all(
    parameter.ProjectParameters.Sort.by_updated_at()
)
```

---

## Range Parameters

Range parameters retrieve projects with values between a minimum and maximum.

All range methods accept optional `min` and `max` parameters. You can specify one or both.

### `id_range(min_id=None, max_id=None)`
Filter projects with IDs in a specific range.

**Parameters:**
- `min_id` (str | int, optional): Minimum ID (inclusive)
- `max_id` (str | int, optional): Maximum ID (inclusive)

**Example:**
```python
# Projects with IDs between 100 and 200
projects = client.projects.get_all(
    parameter.ProjectParameters.Range.id_range(100, 200)
)

# Projects with ID 100 or greater
projects = client.projects.get_all(
    parameter.ProjectParameters.Range.id_range(min_id=100)
)
```

---

### `name_range(min_name=None, max_name=None)`
Filter projects with names in alphabetical range.

**Parameters:**
- `min_name` (str, optional): Minimum name (inclusive)
- `max_name` (str, optional): Maximum name (inclusive)

**Example:**
```python
# Projects with names from 'a' to 'm'
projects = client.projects.get_all(
    parameter.ProjectParameters.Range.name_range("a", "m")
)
```

---

### `slug_range(min_slug=None, max_slug=None)`
Filter projects with slugs in alphabetical range.

**Parameters:**
- `min_slug` (str, optional): Minimum slug (inclusive)
- `max_slug` (str, optional): Maximum slug (inclusive)

**Example:**
```python
projects = client.projects.get_all(
    parameter.ProjectParameters.Range.slug_range("42", "ft")
)
```

---

### `difficulty_range(min_difficulty=None, max_difficulty=None)`
Filter projects by difficulty range.

**Parameters:**
- `min_difficulty` (str | int, optional): Minimum difficulty (inclusive)
- `max_difficulty` (str | int, optional): Maximum difficulty (inclusive)

**Example:**
```python
# Beginner to intermediate projects (difficulty 1-5)
projects = client.projects.get_all(
    parameter.ProjectParameters.Range.difficulty_range(1, 5)
)

# Advanced projects (difficulty 8+)
projects = client.projects.get_all(
    parameter.ProjectParameters.Range.difficulty_range(min_difficulty=8)
)
```

---

### `created_at_range(start_date=None, end_date=None)`
Filter projects created within a date range.

**Parameters:**
- `start_date` (str | datetime, optional): Start date (inclusive)
- `end_date` (str | datetime, optional): End date (inclusive)

**Example:**
```python
from datetime import datetime

# Projects created in 2024
projects = client.projects.get_all(
    parameter.ProjectParameters.Range.created_at_range(
        datetime(2024, 1, 1),
        datetime(2024, 12, 31)
    )
)
```

---

### `updated_at_range(start_date=None, end_date=None)`
Filter projects updated within a date range.

**Parameters:**
- `start_date` (str | datetime, optional): Start date (inclusive)
- `end_date` (str | datetime, optional): End date (inclusive)

**Example:**
```python
from datetime import datetime, timedelta

# Projects updated in the last 30 days
end_date = datetime.now()
start_date = end_date - timedelta(days=30)

projects = client.projects.get_all(
    parameter.ProjectParameters.Range.updated_at_range(start_date, end_date)
)
```

---

## Combining Parameters

You can combine multiple parameters to create complex queries:

```python
# Get visible, non-exam projects from the 42 cursus,
# sorted by difficulty
projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_visible(True),
    parameter.ProjectParameters.Filter.by_exam(False),
    parameter.ProjectParameters.Filter.by_cursus_id(21),
    parameter.ProjectParameters.Sort.by_difficulty("asc"),
    parameter.PageSize(50)
)

# Get beginner projects sorted by name
beginner_projects = client.projects.get_all(
    parameter.ProjectParameters.Range.difficulty_range(1, 3),
    parameter.ProjectParameters.Sort.by_name()
)

# Get recently updated projects in a specific difficulty range
recent_projects = client.projects.get_all(
    parameter.ProjectParameters.Range.difficulty_range(5, 10),
    parameter.ProjectParameters.Sort.by_updated_at("desc"),
    parameter.PageSize(20)
)
```

## Common Use Cases

### Find a project by name
```python
projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_name("ft_transcendence")
)
project = projects[0] if projects else None
```

### Get all projects in a cursus sorted by difficulty
```python
cursus_projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_cursus_id(21),
    parameter.ProjectParameters.Sort.by_difficulty("asc")
)
```

### Get all exam projects
```python
exams = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_exam(True),
    parameter.ProjectParameters.Sort.by_name()
)
```

### Get beginner-friendly projects
```python
beginner_projects = client.projects.get_all(
    parameter.ProjectParameters.Range.difficulty_range(1, 3),
    parameter.ProjectParameters.Filter.by_visible(True),
    parameter.ProjectParameters.Sort.by_difficulty("asc")
)
```

### Get projects updated recently
```python
from datetime import datetime, timedelta

cutoff_date = datetime.now() - timedelta(days=30)

recent_projects = client.projects.get_all(
    parameter.ProjectParameters.Range.updated_at_range(start_date=cutoff_date),
    parameter.ProjectParameters.Sort.by_updated_at("desc")
)
```

### Get all child projects of a parent
```python
child_projects = client.projects.get_all(
    parameter.ProjectParameters.Filter.by_parent_id(100),
    parameter.ProjectParameters.Sort.by_name()
)
```

## Examples

See the [`example/`](../../../../example/) directory for complete working examples.
