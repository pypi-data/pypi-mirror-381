# Django Webhook Subscriber

A Django package for managing webhook subscriptions and deliveries with robust retry logic, performance monitoring, and comprehensive admin interface.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Basic Usage](#basic-usage)
- [Models Reference](#models-reference)
- [API Reference](#api-reference)
- [Admin Interface](#admin-interface)
- [Management Commands](#management-commands)
- [Performance Testing](#performance-testing)
- [Production Deployment](#production-deployment)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Installation

### Requirements

- Python 3.8+
- Django 3.2+
- Django REST Framework 3.12+
- Celery 5.0+ (for async webhook delivery)
- Redis or another cache backend (recommended)

### Install Package

```bash
pip install django-webhook-subscriber
```

### Django Settings

Add to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    "django_webhook_subscriber",
    # ... your apps
]
```

### Database Migration

```bash
python manage.py migrate django_webhook_subscriber
```

### Celery Configuration

Configure Celery for async webhook delivery:

```python
# settings.py
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
```

```python
# celery.py
from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

app = Celery("myproject")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
```

## Quick Start

### 1. Create a Webhook Subscriber

```python
from django.contrib.contenttypes.models import ContentType
from django_webhook_subscriber.models import WebhookSubscriber, WebhookSubscription
from django.contrib.auth import get_user_model

User = get_user_model()

# Create subscriber for User model
user_content_type = ContentType.objects.get_for_model(User)

subscriber = WebhookSubscriber.objects.create(
    name="My External API",
    description="Receives user events",
    content_type=user_content_type,
    target_url="https://api.example.com/webhooks",
    max_retries=3,
    retry_delay=60,
    timeout=30
)

# Create subscription for 'created' events
subscription = WebhookSubscription.objects.create(
    subscriber=subscriber,
    event_name="created",
    is_active=True
)
```

### 2. Send Webhooks

```python
from django_webhook_subscriber import send_webhooks
from django.contrib.auth import get_user_model

User = get_user_model()

# Create a user and send webhook
user = User.objects.create(name="John Doe", email="john@example.com")

# Send webhook for "created" event
send_webhooks(user, "created")
```

### 3. Custom Serialization

```python
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserWebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]

# Update subscriber to use custom serializer
subscriber.serializer_class = "myapp.serializers.UserWebhookSerializer"
subscriber.save()
```

## Configuration

Configure the package in your Django settings:

<!-- TODO: confirm these are all the settings -->

```python
WEBHOOK_SUBSCRIBER = {
    # Log retention
    "LOG_RETENTION_DAYS": 30,
    "AUTO_CLEANUP": True,

    # Performance settings
    "MAX_WEBHOOK_BATCH_SIZE": 50,
    "WEBHOOK_CACHE_TTL": 300,

    # Defaults for new subscribers
    "DEFAULT_MAX_RETRIES": 3,
    "DEFAULT_RETRY_DELAY": 60,
    "REQUEST_TIMEOUT": 30,
}


# Recommended cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CONNECTION_POOL_KWARGS': {'max_connections': 20},
        }
    }
}


# Optional: Disable webhooks globally
DISABLE_WEBHOOKS = False  # Set to True to disable all webhook sending
```

## Basic Usage

### Sending Webhooks

The main API is the `send_webhooks()` function:

```python
from django_webhook_subscriber import send_webhooks

# Basic usage
send_webhooks(instance, 'event_name')
```

### Common Integration Patterns

#### Django Signals

```python
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_webhook_subscriber import send_webhooks
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def user_saved(sender, instance, created, **kwargs):
    event_name = "created" if created else "updated"
    send_webhooks(instance, event_name)

```

#### Django Lifecycle

```python
# models.py
from django_lifecycle import LifecycleModel, hook, AFTER_CREATE, AFTER_UPDATE
from django_webhook_subscriber import send_webhooks

class User(LifecycleModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    @hook(AFTER_CREATE)
    def on_create(self):
        send_webhooks(self, 'created')

    @hook(AFTER_UPDATE, when='email', has_changed=True)
    def on_email_update(self):
        send_webhooks(self, 'email_updated')
```

#### Manual Integration

```python
# myapp/views.py
from django_webhook_subscriber import send_webhooks

class UserViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        user = serializer.save()
        send_webhooks(user, "created")

    def perform_update(self, serializer):
        user = serializer.save()
        send_webhooks(user, "updated")
```

### Disabling Webhooks Temporarily

```python
from django_webhook_subscriber.utils import disable_webhooks

# Disable webhooks for bulk operations
with disable_webhooks():
    User.objects.bulk_create([...])  # No webhooks sent

# Webhooks resume normal operation after the context
```

## Models Reference

### WebhookSubscriber

Represents an external service that wants to receive webhooks.

**Key Fields:**

- `name`: Human-readable name for the subscriber
- `target_url`: Base URL for webhook delivery
- `content_type`: Django model this subscriber watches
- `serializer_class`: Optional custom DRF serializer
- `max_retries`: Maximum delivery attempts
- `retry_delay`: Seconds between retries
- `timeout`: Request timeout
- `auto_disable_after_failures`: Auto-disable threshold

**Methods:**

- `record_success()`: Mark successful delivery
- `record_failure()`: Mark failed delivery, handle auto-disable

### WebhookSubscription

Individual event subscription for a subscriber.

**Key Fields:**

- `subscriber`: Foreign key to WebhookSubscriber
- `event_name`: Event to subscribe to (e.g., 'created', 'updated')
- `custom_endpoint`: Optional endpoint override
- `success_rate`: Calculated property showing delivery success percentage

**Properties:**

- `endpoint`: Full URL for this subscription
- `success_rate`: Percentage of successful deliveries

**Methods:**

- `record_delivery_attempt(success, response_text)`: Track delivery stats

### WebhookDeliveryLog

Log of individual webhook delivery attempts.

**Key Fields:**

- `subscription`: Foreign key to WebhookSubscription
- `attempt_number`: Retry attempt number
- `response_status`: HTTP response status
- `response_body`: HTTP response body (truncated)
- `delivery_duration_ms`: Delivery time in milliseconds
- `error_message`: Exception details if delivery failed

**Properties:**

- `is_success`: True if delivery was successful (2xx status)
- `is_client_error`: True for 4xx status codes
- `is_server_error`: True for 5xx status codes

## API Reference

### Core Functions

#### `send_webhooks(instance, event_name, context=None, **kwargs)`

Send webhooks for a model instance and event.

**Parameters:**

- `instance`: Django model instance
- `event_name`: String event name
- `context`: Optional dict with additional data
- `**kwargs`: Additional arguments

**Returns:**

- Dict with processing summary

**Example:**

```python
result = send_webhooks(user, 'created')
# Returns: {'processed': 3, 'batches': 1, 'task_ids': [...]}
```

#### `clear_webhook_cache(content_type=None, event_name=None)`

Clear cached webhook subscription data.

**Parameters:**

- `content_type`: Optional ContentType to limit clearing
- `event_name`: Optional event name to limit clearing

#### `get_webhook_cache_stats()`

Get detailed cache statistics.

**Returns:**

- Dict with cache hit ratios, key counts, etc.

### Utility Functions

#### `webhooks_disabled()`

Check if webhooks are currently disabled.

#### `disable_webhooks()` (context manager)

Temporarily disable webhook sending.

#### `generate_secret()`

Generate a new webhook secret key.

## Admin Interface

The package provides a comprehensive Django admin interface:

### WebhookSubscriber Admin

- **Health indicators**: Visual status showing healthy/warning/critical
- **Performance tracking**: Success rates and failure counts
- **Connectivity testing**: Test endpoints via admin actions
- **Cache management**: Clear cache for specific subscribers

**Available Actions:**

- Activate/deactivate subscribers
- Test endpoint connectivity
- Reset failure counters
- Clear cache

### WebhookSubscription Admin

- **Performance metrics**: Success rates with color coding
- **Recent deliveries**: Visual icons showing last 5 attempts
- **Statistics management**: Reset performance counters

### WebhookDeliveryLog Admin

- **Detailed logging**: Formatted JSON payloads and responses
- **Performance analysis**: Delivery times and retry information
- **Error categorization**: Grouped error analysis

## Management Commands

### Cache Management

```bash
# Show cache statistics
python manage.py webhook_cache stats

# Clear all cache
python manage.py webhook_cache clear

# Clear specific content type
python manage.py webhook_cache clear --content-type=myapp.User

# Pre-warm cache
python manage.py webhook_cache warm
```

### Testing Endpoints

```bash
# Test all active subscribers
python manage.py webhook_test --all

# Test with custom payload
python manage.py webhook_test --subscriber-id=1 --method=POST --payload='{"test": true}'
```

### Log Management

```bash
# Clean up old logs
python manage.py webhook_logs cleanup --days=30

# Show statistics
python manage.py webhook_logs stats --days=7

# Show recent errors
python manage.py webhook_logs errors --limit=20
```

### System Status

```bash
# Overview
python manage.py webhook_status

# Detailed per-subscriber status
python manage.py webhook_status --detailed
```

### Manual Webhook Sending

```bash
# Send test webhook
python manage.py webhook_send myapp.User 123 created

# With custom context
python manage.py webhook_send myapp.Order 456 paid --context='{"payment_method": "stripe"}'
```

## Performance Testing

Test your webhook system under load:

```bash
# Basic performance test
python manage.py webhook_performance_test \
    --model=myapp.User \
    --event=created \
    --object-count=20 \
    --concurrent-webhooks=10

# High-load test with delivery measurement
python manage.py webhook_performance_test \
    --model=myapp.Order \
    --event=paid \
    --object-count=50 \
    --concurrent-webhooks=20 \
    --measure-delivery \
    --timeout=60 \
    --warmup

# Sustained load test
python manage.py webhook_performance_test \
    --model=myapp.Product \
    --event=updated \
    --object-count=15 \
    --batches=5 \
    --batch-delay=2.0
```

**Performance Metrics Provided:**

- Send throughput (webhooks/second)
- Delivery timing statistics
- Success/failure rates
- Error categorization
- Concurrency analysis

## Production Deployment

### Celery Setup

Ensure Celery is properly configured for production:

```python
# celery.py
from celery import Celery

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Configure for production
app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    worker_hijack_root_logger=False,
    worker_log_format='[%(asctime)s: %(levelname)s/%(processName)s] %(message)s',
)

app.autodiscover_tasks()
```

### Monitoring Setup

Configure logging for webhook monitoring:

```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'webhook_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/webhooks.log',
        },
    },
    'loggers': {
        'django_webhook_subscriber': {
            'handlers': ['webhook_file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### Automated Maintenance

Set up cron jobs for maintenance:

```bash
# Daily log cleanup at 2 AM
0 2 * * * cd /path/to/project && python manage.py webhook_logs cleanup

# Weekly health check report
0 9 * * 1 cd /path/to/project && python manage.py webhook_status --detailed

# Cache warming after deployments
@reboot cd /path/to/project && python manage.py webhook_cache warm
```

### Performance Optimization

1. **Use Redis for caching:**

   ```python
   CACHES = {
       'default': {
           'BACKEND': 'django.core.cache.backends.redis.RedisCache',
           'LOCATION': 'redis://127.0.0.1:6379/1',
       }
   }
   ```

2. **Configure appropriate batch sizes:**

   ```python
   WEBHOOK_SUBSCRIBER = {
       'MAX_WEBHOOK_BATCH_SIZE': 25,  # Adjust based on your load
       'WEBHOOK_CACHE_TTL': 600,      # 10 minutes
   }
   ```

3. **Monitor delivery performance:**
   ```bash
   # Regular performance testing
   python manage.py webhook_performance_test --model=myapp.User --event=test --object-count=10
   ```

## Troubleshooting

### Common Issues

#### 1. Webhooks Not Sending

**Check:**

- Webhooks globally enabled: `DISABLE_WEBHOOKS = False`
- Active subscriptions exist for the model/event
- Celery workers are running

**Debug:**

```bash
python manage.py webhook_status --detailed
python manage.py webhook_cache stats
```

#### 2. High Delivery Failures

**Check:**

- Endpoint accessibility
- Network connectivity
- Authentication headers

**Debug:**

```bash
python manage.py webhook_test --all
python manage.py webhook_logs errors --limit=50
```

#### 3. Performance Issues

**Check:**

- Cache hit ratios
- Batch sizes
- Celery worker count

**Debug:**

```bash
python manage.py webhook_cache stats
python manage.py webhook_performance_test --model=myapp.User --event=test --object-count=5
```

#### 4. Memory Usage

**Solutions:**

- Reduce `LOG_RETENTION_DAYS`
- Increase cleanup frequency
- Limit response body storage

```bash
python manage.py webhook_logs cleanup --days=7
```

### Error Reference

#### Common Error Messages

- **"No subscriptions found"**: No active subscriptions for model/event
- **"Webhook disabled"**: Global or context-specific disabling active
- **"Subscription not found"**: Subscription deleted during processing
- **"Connection error"**: Network connectivity issues
- **"Timeout"**: Endpoint response too slow

#### Performance Warnings

- **Cache miss ratio > 50%**: Consider warming cache more frequently
- **Delivery time > 5s**: Endpoint performance issues
- **Success rate < 95%**: Check endpoint reliability

### Debug Mode

Enable detailed logging for debugging:

```python
# settings.py
LOGGING = {
    'loggers': {
        'django_webhook_subscriber': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
}
```

## Contributing

### Development Setup

1. Clone the repository
2. Install development dependencies: `pip install -e .[dev]`
3. Run tests: `python -m pytest`
4. Run linting: `flake8 django_webhook_subscriber/`

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_delivery.py

# Run with coverage
python -m pytest --cov=django_webhook_subscriber
```

### Contributing Guidelines

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

### Reporting Issues

Please include:

- Django version
- Package version
- Full error traceback
- Minimal reproduction case

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
