"""webhook command for Django Webhook Subscriber."""

import json
import time

from django.core.management.base import BaseCommand, CommandError
from django_webhook_subscriber.models import WebhookSubscriber
from django_webhook_subscriber.sessions import create_webhook_session
from django_webhook_subscriber.utils import generate_headers


class Command(BaseCommand):
    help = "Test webhook endpoints"

    def add_arguments(self, parser):

        parser.add_argument(
            "--subscriber-id",
            "-s",
            type=int,
            help="Test specific subscriber by ID",
        )
        parser.add_argument(
            "--all",
            "-a",
            action="store_true",
            help="Test all active subscribers",
        )
        parser.add_argument(
            "--timeout",
            "-t",
            type=int,
            default=10,
            help="Test timeout in seconds (default: 10)",
        )
        parser.add_argument(
            "--method",
            "-m",
            choices=["HEAD", "GET", "POST"],
            default="HEAD",
            help="HTTP method to use for testing (default: HEAD)",
        )
        parser.add_argument(
            "--payload",
            "-p",
            type=str,
            help="JSON payload for POST requests",
        )

    def handle(self, *args, **options):
        subscribers = self.get_subscribers(options)

        if not subscribers:
            raise CommandError("No subscribers found to test.")

        self.stderr.write(f"Testing {subscribers.count()} subscriber(s)...")

        results = []
        with create_webhook_session() as session:
            for subscriber in subscribers:
                result = self.test_subscriber(session, subscriber, options)
                results.append(result)

        self.print_results(results)

    def get_subscribers(self, options):
        qs = WebhookSubscriber.objects.filter(is_active=True)
        if options.get("subscriber_id"):
            qs = qs.filter(id=options["subscriber_id"])
        elif options.get("all"):
            return qs
        else:
            raise CommandError("Please specify --subscriber-id or --all.")

    def test_subscriber(self, session, subscriber, options):
        start_time = time.time()
        method = options["method"]
        timeout = min(options["timeout"], subscriber.timeout)

        self.stdout.write(
            f"Testing {subscriber.name} ({subscriber.target_url})..."
        )

        try:
            headers = generate_headers(subscriber)

            if method == "POST" and options.get("payload"):
                try:
                    payload = json.loads(options["payload"])
                except json.JSONDecodeError as e:
                    return {
                        "subscriber": subscriber,
                        "success": False,
                        "error": f"Invalid JSON payload: {e=}",
                        "duration_ms": 0,
                    }
                response = session.post(
                    subscriber.target_url,
                    json=payload,
                    headers=headers,
                    timeout=timeout,
                )
            elif method == "GET":
                response = session.get(
                    subscriber.target_url,
                    headers=headers,
                    timeout=timeout,
                )
            else:  # HEAD or default
                response = session.head(
                    subscriber.target_url,
                    headers=headers,
                    timeout=timeout,
                )

            duration_ms = int((time.time() - start_time) * 1000)

            return {
                "subscriber": subscriber,
                "success": True,
                "status_code": response.status_code,
                "duration_ms": duration_ms,
                "headers": dict(response.headers),
                "error": None,
            }

        except Exception as e:
            duration_ms = int((time.time() - start_time) * 1000)
            return {
                "subscriber": subscriber,
                "success": False,
                "status_code": None,
                "duration_ms": duration_ms,
                "error": f"{e=}",
            }

    def print_results(self, results):
        self.stdout.write("\n" + "=" * 60)
        self.stdout.write("TEST RESULTS")
        self.stdout.write("=" * 60)

        successful = 0
        failed = 0

        for result in results:
            subscriber = result["subscriber"]

            if result["success"]:
                successful += 1
                style = self.style.SUCCESS
                status = (
                    f"✓ {result['status_code']} ({result['duration_ms']}ms)"
                )
            else:
                failed += 1
                style = self.style.ERROR
                status = f"✗ {result['error']} ({result['duration_ms']}ms)"

            self.stdout.write(style(f"{subscriber.name}: {status}"))

        self.stdout.write("\n" + "-" * 60)
        self.stdout.write(
            f"Total: {len(results)} | Success: {successful} | Failed: {failed}"
        )

        if failed > 0:
            self.stdout.write(
                self.style.WARNING(f"⚠ {failed} endpoint(s) failed testing")
            )
