"""Managers for Django Webhook Subscriber."""

import logging

from django.db import models
from django.utils import timezone

from .conf import rest_webhook_settings

logger = logging.getLogger(__name__)


class WebhookDeliveryLogManager(models.Manager):
    """Custom manager for WebhookDeliveryLog model.

    This manager provides methods to filter logs based on their status,
    age, and to clean up old logs based on retention settings.
    """

    def cleanup_old_logs(self, subscription=None):
        """This method will cleanup old logs based on retention settings."""

        # Get retention period from settings
        days = getattr(rest_webhook_settings, "LOG_RETENTION_DAYS")

        # Calculate cutoff date
        cutoff_date = timezone.now() - timezone.timedelta(days=days)

        # Build query
        query = self.filter(created_at__lt=cutoff_date)

        logger.debug("Cleaning up logs older than: %s...", cutoff_date)

        if subscription:
            # If a subscription is provided, filter by it
            query = query.filter(subscription=subscription)

        logger.debug("Found a total of %d old logs.", query.count())

        # Delete old logs
        deleted, _ = query.delete()

        logger.info("Deleted a total of %d old logs.", deleted)

    def create(self, **kwargs):
        """
        This method will create a new log entry, and proceed to cleanup old
        logs if necessary.
        """

        # create the log entry
        log = super().create(**kwargs)

        # Checking if AUTO_CLEANUP is set to True
        auto_cleanup = getattr(rest_webhook_settings, "AUTO_CLEANUP")

        # cleanup old logs if necessary
        if (
            auto_cleanup
            and "subscription" in kwargs
            and kwargs["subscription"]
        ):
            # Using a try/except block to prevent any errors during cleanup
            # from affecting the log creation process
            try:
                logger.debug(
                    "Cleaning up old logs for subscription: %s...",
                    kwargs["subscription"],
                )

                self.cleanup_old_logs(subscription=kwargs["subscription"])
            except Exception as e:
                logger.error("Error cleaning up old logs: %s", str(e))

        return log
