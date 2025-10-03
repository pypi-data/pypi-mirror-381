"""webhook_cache command for Django Webhook Subscriber."""

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from django_webhook_subscriber.delivery import (
    clear_webhook_cache,
    get_webhook_cache_stats,
    warm_webhook_cache,
)


class Command(BaseCommand):
    help = "Manage webhook cache operations"

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(dest="action", help="Cache actions")

        # Clear command
        clear_parser = subparsers.add_parser(
            "clear", help="Clear webhook cache"
        )
        clear_parser.add_argument(
            "--content-type",
            "-c",
            type=str,
            help="Clear cache for specific content type "
            "(app_label.model_name)",
        )
        clear_parser.add_argument(
            "--event",
            "-e",
            type=str,
            help="Clear cache for specific event name",
        )

        # Stats command
        subparsers.add_parser("stats", help="Show cache statistics")

        # List command
        list_parser = subparsers.add_parser("list", help="List cached keys")
        list_parser.add_argument(
            "--show-empty",
            action="store_true",
            help="Show keys that are not cached",
        )

        # Warm command
        subparsers.add_parser("warm", help="Pre-warm the cache")

    def handle(self, *args, **options):
        """Handle the command based on the provided action."""

        action = options.get("action")

        if not action:
            self.print_help("manage.py", "webhook_cache")
            return

        if action == "clear":
            self.handle_clear(options)
        elif action == "stats":
            self.handle_stats()
        elif action == "list":
            self.handle_list(options)
        elif action == "warm":
            self.handle_warm()

    def handle_clear(self, options):
        """Clear webhook cache with optional filtering."""

        content_type = None
        if options["content_type"]:
            try:
                app_label, model_name = options["content_type"].split(".")
                content_type = ContentType.objects.get(
                    app_label=app_label, model=model_name
                )

            except (ValueError, ContentType.DoesNotExist):
                raise CommandError(
                    f'Invalid content type: {options["content_type"]}'
                )

        clear_webhook_cache(
            content_type=content_type,
            event_name=options.get("event"),
        )

        if content_type and options.get("event"):
            self.stdout.write(
                self.style.SUCCESS(
                    f"Cleared cache for {content_type} - {options['event']}"
                )
            )
        elif content_type:
            self.stdout.write(
                self.style.SUCCESS(f"Cleared cache for {content_type}")
            )
        elif options.get("event"):
            self.stdout.write(
                self.style.SUCCESS(
                    f"Cleared cache for event '{options['event']}'"
                )
            )
        else:
            self.stdout.write(self.style.SUCCESS("Cleared all webhook cache"))

    def handle_stats(self):
        """Show detailed cache statistics."""
        try:
            stats = get_webhook_cache_stats()

            self.stdout.write(self.style.SUCCESS("Webhook Cache Statistics"))

            self.stdout.write("-" * 40)
            self.stdout.write(
                f"Total possible keys: {stats['total_possible_keys']}"
            )
            self.stdout.write(f"Actually cached keys: {stats['cached_keys']}")
            self.stdout.write(
                f"Cache hit ratio: {stats['cache_hit_ratio']:.1f}"
            )
            self.stdout.write(
                "Total cached subscriptions: "
                f"{stats['total_cached_subscriptions']}"
            )

            if stats["key_details"]:
                self.stdout.write("\nDetailed breakdown:")
                for detail in stats["key_details"]:
                    status = "CACHED" if detail["is_cached"] else "NOT CACHED"
                    self.stdout.write(
                        f"  {detail['key']}: {status} "
                        f"({detail['subscription_count']} subscriptions)"
                    )

        except Exception as e:
            raise CommandError(f"Error getting cache stats: {e=}")

    def handle_list(self, options):
        """List all webhook cache keys."""

        try:
            stats = get_webhook_cache_stats()
            show_empty = options.get("show_empty", False)

            for detail in stats["key_details"]:
                if not show_empty and not detail["is_cached"]:
                    continue

                status = "CACHED" if detail["is_cached"] else "NOT CACHED"
                self.stdout.write(
                    f"{detail['key']}: {status} "
                    f"({detail['subscription_count']} subscriptions)"
                )

        except Exception as e:
            raise CommandError(f"Error listing cache keys: {e=}")

    def handle_warm(self):
        """Pre-warm the webhook cache."""

        try:
            result = warm_webhook_cache()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Cache warmed for {result['warmed']} subscription "
                    "combinations."
                )
            )

        except Exception as e:
            raise CommandError(f"Error warming cache: {e=}")
