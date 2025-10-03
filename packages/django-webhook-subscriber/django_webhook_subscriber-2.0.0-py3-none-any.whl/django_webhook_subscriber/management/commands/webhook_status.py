"""webhook_status command for Django Webhook Subscriber."""

from django.core.management.base import BaseCommand
from django.db import models
from django.utils import timezone
from datetime import timedelta

from django_webhook_subscriber.models import (
    WebhookSubscriber,
    WebhookSubscription,
    WebhookDeliveryLog,
)


class Command(BaseCommand):
    help = "Show overall webhook system status"

    def add_arguments(self, parser):
        parser.add_argument(
            "--detailed",
            action="store_true",
            help="Show detailed status for each subscriber",
        )

    def handle(self, *args, **options):
        self.show_overview()

        if options["detailed"]:
            self.show_detailed_status()

    def show_overview(self):
        """Show system overview."""
        # Basic counts
        total_subscribers = WebhookSubscriber.objects.count()
        active_subscribers = WebhookSubscriber.objects.filter(
            is_active=True
        ).count()
        total_subscriptions = WebhookSubscription.objects.count()
        active_subscriptions = WebhookSubscription.objects.filter(
            is_active=True
        ).count()

        # Health metrics
        failing_subscribers = WebhookSubscriber.objects.filter(
            consecutive_failures__gt=0
        ).count()

        critical_subscribers = WebhookSubscriber.objects.filter(
            consecutive_failures__gte=5
        ).count()

        # Recent activity (last 24 hours)
        last_24h = timezone.now() - timedelta(hours=24)
        recent_deliveries = WebhookDeliveryLog.objects.filter(
            created_at__gte=last_24h
        ).count()

        recent_successes = WebhookDeliveryLog.objects.filter(
            created_at__gte=last_24h,
            response_status__gte=200,
            response_status__lt=300,
        ).count()

        success_rate_24h = (
            (recent_successes / recent_deliveries * 100)
            if recent_deliveries > 0
            else 0
        )

        self.stdout.write(self.style.SUCCESS("Webhook System Status"))
        self.stdout.write("=" * 50)

        self.stdout.write(
            f"Subscribers: {active_subscribers}/{total_subscribers} active"
        )
        self.stdout.write(
            f"Subscriptions: {active_subscriptions}/{total_subscriptions} "
            "active"
        )
        self.stdout.write(
            f"Health: {failing_subscribers} failing, {critical_subscribers} "
            "critical"
        )

        self.stdout.write("\nLast 24 Hours:")
        self.stdout.write(f"Deliveries: {recent_deliveries}")
        self.stdout.write(f"Success rate: {success_rate_24h:.1f}%")

    def show_detailed_status(self):
        """Show detailed status for each subscriber."""
        subscribers = WebhookSubscriber.objects.prefetch_related(
            "subscriptions"
        ).annotate(
            total_subscriptions=models.Count("subscriptions"),
            active_subscriptions=models.Count(
                "subscriptions", filter=models.Q(subscriptions__is_active=True)
            ),
        )

        self.stdout.write("\n" + "=" * 80)
        self.stdout.write("DETAILED SUBSCRIBER STATUS")
        self.stdout.write("=" * 80)

        for subscriber in subscribers:
            # Health indicator
            if not subscriber.is_active:
                health = "DISABLED"
                style = self.style.WARNING
            elif subscriber.consecutive_failures == 0:
                health = "HEALTHY"
                style = self.style.SUCCESS
            elif subscriber.consecutive_failures < 5:
                health = (
                    f"WARNING ({subscriber.consecutive_failures} failures)"
                )
                style = self.style.WARNING
            else:
                health = (
                    f"CRITICAL ({subscriber.consecutive_failures} failures)"
                )
                style = self.style.ERROR

            self.stdout.write(style(f"\n{subscriber.name} - {health}"))
            self.stdout.write(f"  URL: {subscriber.target_url}")
            self.stdout.write(
                f"  Subscriptions: {subscriber.active_subscriptions}/"
                f"{subscriber.total_subscriptions} active"
            )

            if subscriber.last_success:
                self.stdout.write(
                    "  Last success: "
                    f"{subscriber.last_success.strftime('%Y-%m-%d %H:%M')}"
                )
            if subscriber.last_failure:
                self.stdout.write(
                    "  Last failure: "
                    f"{subscriber.last_failure.strftime('%Y-%m-%d %H:%M')}"
                )
