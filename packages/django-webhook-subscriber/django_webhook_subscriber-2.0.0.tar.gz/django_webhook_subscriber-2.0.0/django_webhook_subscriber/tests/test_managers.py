from datetime import timedelta

from django.test import TestCase, override_settings
from django.utils import timezone
from django_webhook_subscriber import models

from .factories import WebhookSubscriptionFactory


class WebhookDeliveryLogManagerTests(TestCase):
    def setUp(self):
        self.subscription = WebhookSubscriptionFactory()

    def _create_log_entry(self, payload={}, delivery_url=None, **kwargs):
        created_at = kwargs.pop("created_at", None)
        subscription = kwargs.get("subscription", self.subscription)
        delivery_url = delivery_url or self.subscription.endpoint

        log = models.WebhookDeliveryLog.objects.create(
            subscription=subscription,
            payload=payload,
            delivery_url=delivery_url,
            **kwargs,
        )

        # setting created_at if provided
        if created_at:
            log.created_at = created_at
            log.save()

        return log

    def test_create_log_entry(self):
        log = models.WebhookDeliveryLog.objects.create(
            subscription=self.subscription,
            payload={"key": "value"},
            created_at=timezone.now(),
        )
        self.assertEqual(models.WebhookDeliveryLog.objects.count(), 1)
        self.assertEqual(log.subscription, self.subscription)

    @override_settings(WEBHOOK_SUBSCRIBER={"LOG_RETENTION_DAYS": 1})
    def test_cleanup_old_logs_deletes_old_entries(self):

        self._create_log_entry(created_at=timezone.now() - timedelta(days=2))
        self._create_log_entry()

        models.WebhookDeliveryLog.objects.cleanup_old_logs()

        self.assertEqual(models.WebhookDeliveryLog.objects.count(), 1)

    @override_settings(WEBHOOK_SUBSCRIBER={"LOG_RETENTION_DAYS": 1})
    def test_create_triggers_cleanup(self):
        # Create an old log
        old_log = self._create_log_entry(
            created_at=timezone.now() - timedelta(days=2),
        )
        # Manually update created_at to simulate old timestamp
        models.WebhookDeliveryLog.objects.filter(pk=old_log.pk).update(
            created_at=timezone.now() - timedelta(days=2)
        )

        # Create new log, triggering auto-cleanup
        self._create_log_entry()

        # Only one (new) log should remain
        self.assertEqual(models.WebhookDeliveryLog.objects.count(), 1)

    @override_settings(WEBHOOK_SUBSCRIBER={"AUTO_CLEANUP": False})
    def test_auto_cleanup_respects_setting(self):
        self._create_log_entry(created_at=timezone.now() - timedelta(days=40))
        self._create_log_entry(created_at=timezone.now())

        # Cleanup should not run because AUTO_CLEANUP is False
        self.assertEqual(models.WebhookDeliveryLog.objects.count(), 2)

    def test_auto_cleanup_respects_setting_default_values(self):
        self._create_log_entry(created_at=timezone.now() - timedelta(days=40))
        self._create_log_entry(created_at=timezone.now())

        # Cleanup should have run because AUTO_CLEANUP is True
        self.assertEqual(models.WebhookDeliveryLog.objects.count(), 1)
