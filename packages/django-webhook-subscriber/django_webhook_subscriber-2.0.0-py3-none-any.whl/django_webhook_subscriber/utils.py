"""Utility functions for Django Webhook Subscriber"""

import contextvars
import uuid
from contextlib import contextmanager
from functools import lru_cache

from django.conf import settings

# =============================================================================
# Header and secret generation
# =============================================================================


def generate_headers(subscriber):
    """Generate headers for webhook delivery, including custom headers."""

    headers = subscriber.headers.copy() if subscriber.headers else {}

    # Add content type header if not present
    if "Content-Type" not in headers:
        headers["Content-Type"] = "application/json"

    # Add secret key authentication header
    headers["X-Secret"] = subscriber.secret

    return headers


def generate_secret():
    """Generate a new secret key for webhook authentication."""

    return str(uuid.uuid4())


# =============================================================================
# Webhook enabling/disabling context manager
# =============================================================================

# We're using contextvars instead of thread locals because:
# - contextvars provide proper isolation in async environments (async tasks)
# - they automatically propagate through async/await boundaries
# - they work correctly with concurrent execution (asyncio, threading)
# - they ensure webhook state is isolated per request/task context

_webhooks_disabled = contextvars.ContextVar("webhooks_disabled", default=False)


def webhooks_disabled():
    """Check if webhooks are currently disabled in this context."""

    # Check context variable first
    check_disabled = _webhooks_disabled.get()

    # Check Django settings
    settings_disabled = getattr(settings, "DISABLE_WEBHOOKS", False)

    # Webhooks are disabled if either context or settings says so
    return check_disabled or settings_disabled


@contextmanager
def disable_webhooks():
    """Context manager to temporarily disable webhooks.

    Usage:
        with disable_webhooks():
            # Code that should not trigger webhooks
            ...
    """

    token = _webhooks_disabled.set(True)
    try:
        yield
    finally:
        _webhooks_disabled.reset(token)


# =============================================================================
# ContentType caching
# =============================================================================


@lru_cache(maxsize=128)
def get_content_type_id(app_label, model_name) -> int:
    """Cached lookup for content type ID"""

    from django.contrib.contenttypes.models import ContentType

    try:
        return ContentType.objects.get(
            app_label=app_label,
            model=model_name,
        ).id
    except ContentType.DoesNotExist:
        return None


def clear_content_type_cache():
    """Clear the content type cache"""

    get_content_type_id.cache_clear()
