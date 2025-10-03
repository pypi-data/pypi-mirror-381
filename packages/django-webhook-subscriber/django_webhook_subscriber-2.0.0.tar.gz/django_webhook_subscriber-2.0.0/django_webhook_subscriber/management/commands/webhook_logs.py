"""webhook_logs command for Django Webhook Subscriber."""

from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import models, transaction
from django.utils import timezone
from django_webhook_subscriber.conf import rest_webhook_settings
from django_webhook_subscriber.models import (
    WebhookDeliveryLog,
)


class Command(BaseCommand):
    help = "Manage webhook delivery logs"

    def add_arguments(self, parser):

        subparsers = parser.add_subparsers(dest="action", help="Log actions")

        # Cleanup command
        cleanup_parser = subparsers.add_parser(
            "cleanup", help="Clean up old logs"
        )
        cleanup_parser.add_argument(
            "--days",
            type=int,
            help="Keep logs newer than N days (overrides settings)",
        )
        cleanup_parser.add_argument(
            "--subscription-id",
            "-s",
            type=int,
            help="Clean logs for specific subscription by ID",
        )
        cleanup_parser.add_argument(
            "--dry-run",
            "-d",
            action="store_true",
            help="Show what would be deleted without actually deleting",
        )

        # Stats command
        stats_parser = subparsers.add_parser(
            "stats", help="Show log statistics"
        )
        stats_parser.add_argument(
            "--days",
            type=int,
            default=30,
            help="Show stats for last N days (default: 30)",
        )

        # Error command
        errors_parser = subparsers.add_parser(
            "errors", help="Show recent error logs"
        )
        errors_parser.add_argument(
            "--limit",
            type=int,
            default=10,
            help="Number of recent errors to show (default: 10)",
        )

    def handle(self, *args, **options):
        action = options.get("action")

        if not action:
            self.print_help("manage.py", "webhook_logs")
            return

        if action == "cleanup":
            self.handle_cleanup(options)
        elif action == "stats":
            self.handle_stats(options)
        elif action == "errors":
            self.handle_errors(options)

    def handle_cleanup(self, options):
        """Clean up old webhook logs."""
        retention_days = (
            options.get("days") or rest_webhook_settings.LOG_RETENTION_DAYS
        )
        cutoff_date = timezone.now() - timedelta(days=retention_days)

        query = WebhookDeliveryLog.objects.filter(created_at__lte=cutoff_date)

        if options.get("subscription_id"):
            query = query.filter(subscription_id=options["subscription_id"])

        total_count = query.count()
        if total_count == 0:
            self.stdout.write(self.style.SUCCESS("No old logs to clean up"))
            return

        if options.get("dry_run"):
            self.stdout.write(
                self.style.WARNING(
                    f"DRY RUN: Would delete {total_count} logs older than "
                    f"{cutoff_date}"
                )
            )
            return

        # Delete in batches to avoid memory issues
        batch_size = 1000
        total_deleted = 0
        with transaction.atomic():
            while True:
                batch_ids = list(
                    query.values_list("id", flat=True)[:batch_size]
                )
                if not batch_ids:
                    break

                deleted_count = WebhookDeliveryLog.objects.filter(
                    id__in=batch_ids
                ).delete()[0]
                total_deleted += deleted_count

                self.stdout.write(
                    f"Deleted {deleted_count} logs (total: {total_deleted})"
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Cleanup completed. Deleted {total_deleted} logs older than "
                f"{cutoff_date}"
            )
        )

    def handle_stats(self, options):
        """Show webhook log statistics."""

        days = options["days"]
        since_date = timezone.now() - timedelta(days=days)

        logs = WebhookDeliveryLog.objects.filter(created_at__gte=since_date)

        total_logs = logs.count()
        successful_logs = logs.filter(
            response_status__gte=200, response_status__lt=300
        ).count()
        error_logs = logs.exclude(
            response_status__gte=200, response_status__lt=300
        ).count()

        # Success rate
        success_rate = (
            (successful_logs / total_logs * 100) if total_logs > 0 else 0
        )

        # Top failing subscriptions
        failing_subs = (
            logs.exclude(response_status__gte=200, response_status__lt=300)
            .values(
                "subscription__subscriber__name", "subscription__event_name"
            )
            .annotate(error_count=models.Count("id"))
            .order_by("-error_count")[:5]
        )

        # Average response time
        avg_duration = (
            logs.exclude(delivery_duration_ms__isnull=True).aggregate(
                avg_duration=models.Avg("delivery_duration_ms")
            )["avg_duration"]
            or 0
        )

        self.stdout.write(
            self.style.SUCCESS(f"Webhook Statistics (Last {days} days)")
        )
        self.stdout.write("-" * 50)
        self.stdout.write(f"Total deliveries: {total_logs}")
        self.stdout.write(f"Successful: {successful_logs}")
        self.stdout.write(f"Failed: {error_logs}")
        self.stdout.write(f"Success rate: {success_rate:.1f}%")

        if avg_duration:
            self.stdout.write(f"Average response time: {avg_duration:.0f}ms")

        if failing_subs:
            self.stdout.write("\nTop failing subscriptions:")
            for sub in failing_subs:
                self.stdout.write(
                    f"  {sub['subscription__subscriber__name']} - "
                    f"{sub['subscription__event_name']}: {sub['error_count']} "
                    "errors"
                )

    def handle_errors(self, options):
        """Show recent webhook errors."""

        limit = options["limit"]

        error_logs = (
            WebhookDeliveryLog.objects.exclude(
                response_status__gte=200, response_status__lt=300
            )
            .select_related("subscription", "subscription__subscriber")
            .order_by("-created_at")[:limit]
        )

        if not error_logs:
            self.stdout.write(self.style.SUCCESS("No recent errors found"))
            return

        self.stdout.write(
            self.style.ERROR(f"Recent Webhook Errors (Last {limit})")
        )
        self.stdout.write("-" * 60)

        for log in error_logs:
            subscriber_name = log.subscription.subscriber.name
            event_name = log.subscription.event_name

            if log.error_message:
                error_info = f"Exception: {log.error_message[:100]}"
            else:
                error_info = f"HTTP {log.response_status}"

            self.stdout.write(
                f"{log.created_at.strftime('%Y-%m-%d %H:%M')} | "
                f"{subscriber_name} - {event_name} | {error_info}"
            )
