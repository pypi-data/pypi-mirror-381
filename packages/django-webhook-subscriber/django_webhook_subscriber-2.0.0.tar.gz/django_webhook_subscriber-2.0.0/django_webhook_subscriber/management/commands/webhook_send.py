"""webhook_send command for Django Webhook Subscriber."""

import json

from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from django_webhook_subscriber.delivery import send_webhooks


class Command(BaseCommand):
    help = "Manually send webhooks for testing"

    def add_arguments(self, parser):
        parser.add_argument(
            "model",
            type=str,
            help="Model in format app_label.ModelName",
        )
        parser.add_argument(
            "object_id",
            type=int,
            help="ID of the object to send webhook for",
        )
        parser.add_argument(
            "event_name",
            type=str,
            help="Event name (e.g., created, updated, deleted)",
        )
        parser.add_argument(
            "--context",
            type=str,
            help="Additional context as JSON string",
        )
        parser.add_argument(
            "--async",
            action="store_true",
            help="Send webhooks asynchronously (default behavior)",
        )

    def handle(self, *args, **options):
        # Parse model
        try:
            app_label, model_name = options["model"].split(".")
            model_class = apps.get_model(app_label, model_name)
        except (ValueError, LookupError) as e:
            raise CommandError(f"Invalid model: {options['model']}: {e}")

        # Get object
        try:
            instance = model_class.objects.get(id=options["object_id"])
        except model_class.DoesNotExist:
            raise CommandError(
                f"{model_class.__name__} with ID {options['object_id']} not "
                "found"
            )

        # Parse context
        context = None
        if options.get("context"):
            try:
                context = json.loads(options["context"])
            except json.JSONDecodeError:
                raise CommandError("Invalid JSON in context")

        self.stdout.write(
            f"Sending webhook for {model_class.__name__} "
            f"(ID: {instance.id}) - Event: {options['event_name']}"
        )

        try:
            result = send_webhooks(
                instance=instance,
                event_name=options["event_name"],
                context=context,
            )

            if "error" in result:
                self.stdout.write(
                    self.style.ERROR(f"Error: {result['error']}")
                )
            elif "skipped" in result:
                self.stdout.write(
                    self.style.WARNING(f"Skipped: {result['skipped']}")
                )
            else:
                processed = result.get("processed", 0)
                batches = result.get("batches", 1)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Queued {processed} webhook deliveries in {batches} "
                        "batch(es)"
                    )
                )

        except Exception as e:
            raise CommandError(f"Error sending webhook: {e}")
