# 42 Client

A Python client library for the 42 School API that simplifies authentication and data retrieval.

## Features

- 🔐 **Easy authentication** - OAuth2 handled automatically
- 📊 **Resource managers** - Convenient methods for users, projects, locations, and more
- 🚦 **Rate limiting** - Built-in support for Memory and Redis-based rate limiting
- 🔑 **Secret management** - Flexible credential storage (Memory, HashiCorp Vault)
- 🛡️ **Error handling** - Automatic retry and error management
- 📝 **Type hints** - Full type annotation support
- ⚙️ **Customizable** - Flexible configuration and parameters
- 🔄 **Pagination** - Easy iteration over paginated results

## Installation

### From PyPI (recommended)

```bash
# Using pip
pip install fortytwo-client

# Using uv (recommended)
uv add fortytwo-client
```

### From source

```bash
git clone https://github.com/lucas-ht/fortytwo-client.git
cd fortytwo-client
uv sync
```

### Development installation

```bash
git clone https://github.com/lucas-ht/fortytwo-client.git
cd fortytwo-client
uv sync --group dev
```

## Quick Start

### 1. Get your API credentials

First, you need to create an application on the [42 API](https://api.intra.42.fr/apidoc) to get your client ID and secret.

### 2. Basic usage

```python
from fortytwo import FortyTwoClient

# Create client instance with credentials
client = FortyTwoClient(
    client_id="your_client_id",
    client_secret="your_client_secret"
)

# Fetch user information
user = client.users.get_by_id(user_id=12345)
print(f"User: {user['login']}")

# Fetch projects
projects = client.projects.get_by_cursus_id(cursus_id=21)
```

### 3. Advanced usage with custom parameters

```python
from fortytwo import FortyTwoClient, parameter

client = FortyTwoClient(
    client_id="your_client_id",
    client_secret="your_client_secret"
)

# Use custom parameters for filtering and pagination
users = client.users.get_all(
    parameter.UserParameters.Filter.by_login("example"),
    parameter.PageSize(50),
    parameter.PageNumber(1)
)
```

## Examples

See the `example/` directory for more detailed usage examples:

- [`fetch_user_by_id.py`](example/fetch_user_by_id.py) - Fetching user information by ID
- [`fetch_user_by_login.py`](example/fetch_user_by_login.py) - Fetching user information by login
- [`fetch_project.py`](example/fetch_project.py) - Working with projects
- [`fetch_location.py`](example/fetch_location.py) - Location data retrieval
- [`redis_rate_limiter.py`](example/redis_rate_limiter.py) - Redis-based distributed rate limiting
- [`vault_secret_manager.py`](example/vault_secret_manager.py) - HashiCorp Vault secret management

## Documentation

### Core Features

- **[Resources Overview](fortytwo/resources/README.md)** - API resource documentation
- **[Rate Limiter](fortytwo/request/rate_limiter/README.md)** - Request rate limiting strategies (Memory, Redis)
- **[Secret Manager](fortytwo/request/secret_manager/README.md)** - Credential management strategies (Memory, Vault)

### API Resources

The client provides managers for accessing different 42 API resources:

- **[Users](fortytwo/resources/user/README.md)** - `client.users.*` - User information and profiles
- **[Projects](fortytwo/resources/project/README.md)** - `client.projects.*` - Project data and details
- **[Locations](fortytwo/resources/location/README.md)** - `client.locations.*` - Campus location tracking
- **[Project Users](fortytwo/resources/project_user/README.md)** - `client.project_users.*` - User-project relationships
- **[Tokens](fortytwo/resources/token/README.md)** - `client.tokens.*` - API token management

Each resource manager provides methods like:
- `get_by_id(id)` - Fetch a single resource by ID
- `get_all(*params)` - Fetch multiple resources with filtering
- Custom methods specific to each resource type

See individual resource documentation in [`fortytwo/resources/`](fortytwo/resources/) for details.

## Advanced Configuration

### Rate Limiting

The client supports both in-memory and Redis-based rate limiting:

```python
from fortytwo import FortyTwoClient

# Memory-based rate limiter (default)
config = FortyTwoClient.Config(
    rate_limiter=FortyTwoClient.RateLimiter.Memory(
        requests_per_hour=1200,
        requests_per_second=2
    )
)

# Redis-based rate limiter (for distributed systems)
import redis
redis_client = redis.Redis(host='localhost', port=6379)
config = FortyTwoClient.Config(
    rate_limiter=FortyTwoClient.RateLimiter.Redis(
        redis_client=redis_client,
        requests_per_hour=1200,
        requests_per_second=2
    )
)

client = FortyTwoClient(
    client_id="your_client_id",
    client_secret="your_client_secret",
    config=config
)
```

See [Rate Limiter Documentation](fortytwo/request/rate_limiter/README.md) for details.

### Secret Management

The client supports multiple secret storage backends:

```python
from fortytwo import FortyTwoClient
import hvac

# Memory-based secrets (default)
client = FortyTwoClient(
    client_id="your_client_id",
    client_secret="your_client_secret"
)

# HashiCorp Vault integration
vault_client = hvac.Client(url='https://vault.example.com', token='...')
config = FortyTwoClient.Config(
    secret_manager=FortyTwoClient.SecretManager.Vault(
        vault_client=vault_client,
        secret_path='fortytwo/api'
    )
)
client = FortyTwoClient(config=config)
```

See [Secret Manager Documentation](fortytwo/request/secret_manager/README.md) for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see the LICENSE file for details.

## Links

- [42 API Documentation](https://api.intra.42.fr/apidoc)
- [GitHub Repository](https://github.com/lucas-ht/fortytwo-client)
- [Issue Tracker](https://github.com/lucas-ht/fortytwo-client/issues)
