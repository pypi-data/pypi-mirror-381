# Rate Limiter

The Rate Limiter provides flexible request rate limiting to comply with the 42 API's rate limits while preventing service interruptions. It supports both in-memory and distributed (Redis) rate limiting strategies.

## Overview

The 42 API has rate limits to prevent abuse:
- **Per-second limit**: Prevents bursts of requests
- **Hourly limit**: Typically 1200 requests per hour (may vary)

The rate limiter automatically:
- ✅ Tracks requests per hour and per second
- ✅ Enforces delays to respect limits
- ✅ Waits when limits are exceeded
- ✅ Resets counters at appropriate intervals

## Available Implementations

### MemoryRateLimiter

Stores rate limit state in memory. Suitable for single-process applications.

**Pros:**
- No external dependencies
- Fast and simple
- Good for development and single-instance deployments

**Cons:**
- State is lost on process restart
- Not suitable for multi-process or distributed deployments
- Each process has its own separate limits

**Usage:**
```python
from fortytwo import FortyTwoClient

# Method 1: Use default rate limiter (Memory)
client = FortyTwoClient(
    ...
)

# Method 2: Explicit configuration
config = FortyTwoClient.Config(
    rate_limiter=FortyTwoClient.RateLimiter.Memory(
        requests_per_hour=1200,
        requests_per_second=2,
    )
)
client = FortyTwoClient(
    ...
    config=config
)
```

### RedisRateLimiter

Stores rate limit state in Redis. Suitable for distributed applications.

**Pros:**
- Shared state across multiple processes/instances
- State survives process restarts
- Ideal for production distributed deployments
- Accurate rate limiting across your entire infrastructure

**Cons:**
- Requires Redis server
- Slightly more complex setup
- Network dependency

**Requirements:**
```bash
pip install redis
```

**Usage:**
```python
import redis
from fortytwo import FortyTwoClient

# Create Redis client
redis_client = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True,
)

# Configure FortyTwo client with Redis rate limiter
config = FortyTwoClient.Config(
    rate_limiter=FortyTwoClient.RateLimiter.Redis(
        redis_client=redis_client,
        requests_per_hour=1200,
        requests_per_second=2,
        key_prefix="fortytwo_api",  # Optional: namespace for Redis keys
    )
)

client = FortyTwoClient(
    ...
    config=config
)
```

## Configuration Parameters

Both rate limiters accept the following parameters:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `requests_per_hour` | `int` | `1200` | Maximum requests allowed per hour |
| `requests_per_second` | `int` | `2` | Maximum requests allowed per second |

### RedisRateLimiter Additional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `redis_client` | `redis.Redis` | Required | Authenticated Redis client instance |
| `key_prefix` | `str` | `"fortytwo_rate_limit"` | Prefix for Redis keys to avoid collisions |


## Behavior

### Per-Second Rate Limiting

The rate limiter enforces a delay between requests to respect the per-second limit:

```python
# With requests_per_second=2
client.users.get_by_id(1)  # Executes immediately
client.users.get_by_id(2)  # Waits 0.5 seconds
client.users.get_by_id(3)  # Waits 0.5 seconds
```

### Hourly Rate Limiting

When the hourly limit is reached, the rate limiter waits until the hour resets:

```python
# After making 1200 requests in an hour
client.users.get_by_id(1)  # Waits until next hour window
```

You'll see a log message:
```
WARNING - Hourly rate limit exceeded (1200/1200 requests used).
Waiting 245.3 seconds until next request is available...
```
