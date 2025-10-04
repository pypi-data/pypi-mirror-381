# User Resource

The User resource provides access to 42 School user data and operations.

## Overview

This module allows you to fetch user information from the 42 API, including basic profile data, authentication status, images, and more.

## Classes

### `User`
Represents a 42 School user with all their associated data.

**Properties:**
- `id` (int): Unique user identifier
- `login` (str): User's login name
- `kind` (str): User type/kind
- `alumni` (bool): Whether the user is an alumnus
- `active` (bool): Whether the user account is active
- `image` (dict): Profile images in different sizes
- `email` (str): User's email address
- `first_name` (str): User's first name
- `last_name` (str): User's last name
- `usual_full_name` (str): User's display name
- `phone` (str): User's phone number
- `created_at` (datetime): Account creation date
- `updated_at` (datetime): Last profile update date

### Resource Classes

#### `GetUserById`
Fetches a single user by their ID.
- **Endpoint:** `/users/{id}`
- **Method:** GET
- **Returns:** `User`

#### `GetUsers`
Fetches all users with optional filtering.
- **Endpoint:** `/users`
- **Method:** GET
- **Returns:** `List[User]`

## Usage Examples

### Using the Manager (Recommended)

```python
from fortytwo import Client
from fortytwo.exceptions import FortyTwoNotFoundException

client = Client(
    ...
)

# Get a specific user
try:
    user = client.users.get_by_id(user_id=12345)
    print(f"User: {user.login}")
    print(f"Name: {user.first_name} {user.last_name}")
    print(f"Alumni: {user.alumni}")
except FortyTwoNotFoundException:
    print("User not found")

# Get all users with pagination
users = client.users.get_all(page=1, page_size=50)
for user in users:
    print(f"{user.id}: {user.login}")
```

### Using Resources Directly

```python
from fortytwo.resources.user.resource import GetUserById, GetUsers

# Get a specific user
user = client.request(GetUserById(12345))

# Get all users
users = client.request(GetUsers())
```

## Data Structure

### User JSON Response
```json
{
  "id": 12345,
  "login": "jdoe",
  "first_name": "John",
  "last_name": "Doe",
  "usual_full_name": "John Doe",
  "email": "john.doe@student.42.fr",
  "kind": "student",
  "alumni?": false,
  "active?": true,
  "phone": "+1234567890",
  "image": {
    "versions": {
      "large": "https://cdn.intra.42.fr/users/large_jdoe.jpg",
      "medium": "https://cdn.intra.42.fr/users/medium_jdoe.jpg",
      "small": "https://cdn.intra.42.fr/users/small_jdoe.jpg",
      "micro": "https://cdn.intra.42.fr/users/micro_jdoe.jpg"
    }
  },
  "created_at": "2023-01-15T10:30:00Z",
  "updated_at": "2024-03-20T14:22:00Z"
}
```

## Parameters

For detailed information about filtering, sorting, and ranging user queries, see the [User Parameters Documentation](parameter/README.md).

## Error Handling

All methods raise exceptions on errors:

```python
from fortytwo import Client
from fortytwo.exceptions import (
    FortyTwoNotFoundException,
    FortyTwoUnauthorizedException,
    FortyTwoRateLimitException,
    FortyTwoNetworkException,
    FortyTwoRequestException
)

client = Client(
    ...
)

try:
    user = client.users.get_by_id(user_id=99999)
    print(f"Found user: {user.login}")
except FortyTwoNotFoundException:
    print("User not found")
except FortyTwoUnauthorizedException:
    print("Authentication failed")
except FortyTwoRateLimitException as e:
    print(f"Rate limit exceeded. Wait {e.wait_time} seconds")
except FortyTwoNetworkException:
    print("Network error occurred")
except FortyTwoRequestException as e:
    print(f"Request failed: {e}")
```
