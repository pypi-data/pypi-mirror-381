"""HTTP session management for webhook delivery."""

from contextlib import contextmanager

import requests
from requests.adapters import HTTPAdapter


def create_webhook_session():
    """Create an optimized session for webhook delivery."""

    session = requests.Session()

    # Configure adapter for connection pooling
    adapter = HTTPAdapter(
        pool_connections=2,
        pool_maxsize=5,  # Max connections per host
        max_retries=0,  # We handle the retries
    )

    # Mount adapter for both HTTP and HTTPS
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    # Set default handlers
    session.headers.update(
        {
            "User-Agent": "Django-Webhook-Subscriber/2.0",
            "Content-Type": "application/json",
        }
    )

    return session


@contextmanager
def webhook_session():
    """Context manager for webhook session.

    Usage:
        with webhook_session() as session:
            # Use session to send requests like
            response = session.post(url, json=payload)
            ...
    """

    session = create_webhook_session()
    try:
        yield session
    finally:
        session.close()
