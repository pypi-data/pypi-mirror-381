"""webhook_send command for Django Webhook Subscriber."""

import statistics
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django_webhook_subscriber.delivery import send_webhooks
from django_webhook_subscriber.models import (
    WebhookDeliveryLog,
    WebhookSubscription,
)


class Command(BaseCommand):
    help = "Performance test webhook system with concurrent deliveries"

    def add_arguments(self, parser):
        # Test configuration
        parser.add_argument(
            "--model",
            type=str,
            required=True,
            help="Model in format app_label.ModelName",
        )
        parser.add_argument(
            "--event",
            type=str,
            required=True,
            help="Event name to test",
        )
        parser.add_argument(
            "--object-ids",
            type=str,
            help="Comma-separated list of object IDs to test "
            "(e.g., '1,2,3,4,5')",
        )
        parser.add_argument(
            "--object-count",
            type=int,
            help="Number of random objects to test (alternative to "
            "--object-ids)",
        )

        # Concurrency settings
        parser.add_argument(
            "--concurrent-webhooks",
            type=int,
            default=10,
            help="Number of concurrent webhook sends (default: 10)",
        )
        parser.add_argument(
            "--batches",
            type=int,
            default=1,
            help="Number of batches to run (default: 1)",
        )

        # Test options
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Show what would be tested without actually sending webhooks",
        )
        parser.add_argument(
            "--measure-delivery",
            action="store_true",
            help="Wait for and measure actual webhook delivery times.",
        )
        parser.add_argument(
            "--timeout",
            type=int,
            default=60,
            help="Timeout in seconds to wait for delivery when measuring "
            "(default: 60)",
        )
        parser.add_argument(
            "--warmup",
            action="store_true",
            help="Run a warmup round before the actual test",
        )

    def handle(self, *args, **options):
        # Validate and setup
        model_class, test_objects = self.setup_test(options)

        # Show test plan
        self.show_test_plan(model_class, test_objects, options)

        # Warmup if requested
        if options["warmup"]:
            self.run_warmup(test_objects, options)

        # Run the actual performance tests
        results = self.run_performance_test(test_objects, options)

        # Show results
        self.show_results(results, options)

    def setup_test(self, options):
        # Parse and validate model
        try:
            app_label, model_name = options["model"].split(".")
            model_class = apps.get_model(app_label, model_name)
        except (ValueError, LookupError) as e:
            raise CommandError(f"Invalid model: {options['model']}: {e}")

        # Get test objects
        if options.get("object_ids"):
            object_ids = [
                int(x.strip()) for x in options["object_ids"].split(",")
            ]
            test_objects = list(model_class.objects.filter(id__in=object_ids))

            if len(test_objects) != len(object_ids):
                found_ids = [obj.id for obj in test_objects]
                missing_ids = set(object_ids) - set(found_ids)
                raise CommandError(f"Objects not found: {missing_ids}")

        elif options.get("object_count"):
            count = options["object_count"]
            test_objects = list(model_class.objects.all()[:count])

            if len(test_objects) < count:
                raise CommandError(
                    f"Only {len(test_objects)} objects available, {count} "
                    "requested"
                )
        else:
            raise CommandError("Specify either --object-ids or --object-count")

        # Verify subscriptions exist
        content_type = ContentType.objects.get_for_model(model_class)
        subscription_count = WebhookSubscription.objects.filter(
            subscriber__content_type=content_type,
            event_name=options["event"],
            is_active=True,
            subscriber__is_active=True,
        ).count()

        if subscription_count == 0:
            raise CommandError(
                f"No active subscriptions found for {options['model']} - "
                f"{options['event']}"
            )

        return model_class, test_objects

    def show_test_plan(self, model_class, test_objects, options):

        total_webhooks = len(test_objects) * options["batches"]
        concurrent = options["concurrent_webhooks"]

        self.stdout.write(self.style.SUCCESS("Performance Test Plan"))
        self.stdout.write("-" * 40)
        self.stdout.write(f"Model: {model_class.__name__}")
        self.stdout.write(f"Event: {options['event']}")
        self.stdout.write(f"Objects to test: {len(test_objects)}")
        self.stdout.write(f"Batches: {options['batches']}")
        self.stdout.write(f"Total webhooks: {total_webhooks}")
        self.stdout.write(f"Concurrent sends: {concurrent}")

        if options["measure_delivery"]:
            self.stdout.write(f"Delivery timeout: {options['timeout']}s")

        if options["dry_run"]:
            self.stdout.write(
                self.style.WARNING("DRY RUN - No webhooks will be sent")
            )

    def run_warmup(self, test_objects, options):
        self.stdout.write("\nRunning warmup...")

        # Use first object for warmup
        warmup_object = test_objects[0]

        start_time = time.time()
        result = send_webhooks(warmup_object, options["event"])
        self.stdout.write(
            f"Warmup completed in {time.time() - start_time:.2f}s: {result}"
        )

        # Give systems time to settle
        time.sleep(2)

    def run_performance_test(self, test_objects, options):
        self.stdout.write("\nStarting performance test...")

        all_results = []

        for batch_num in range(options["batches"]):
            if options["batches"] > 1:
                self.stdout.write(
                    f"\nBatch {batch_num + 1}/{options['batches']}"
                )

            batch_results = self.run_single_batch(test_objects, options)
            all_results.extend(batch_results)

        return all_results

    def run_single_batch(self, test_objects, options):
        concurrent = options["concurrent_webhooks"]
        batch_results = []

        # Prepare tasks
        tasks = []
        for obj in test_objects:
            tasks.append(
                {
                    "object": obj,
                    "event": options["event"],
                    "start_logs": None,  # will be set before sending
                }
            )

        # Record initial log state if measuring delivery
        if options["measure_delivery"]:
            for task in tasks:
                task["start_logs"] = WebhookDeliveryLog.objects.filter(
                    subscription__subscriber__content_type__model=obj._meta.model_name.lower(),  # noqa: E501
                    created_at__gte=timezone.now(),
                ).count()

        # Execute concurrent webhook sends
        start_time = time.time()

        with ThreadPoolExecutor(max_workers=concurrent) as executor:
            # Submit all tasks
            future_to_task = {
                executor.submit(self.send_single_webhook, task): task
                for task in tasks
            }

            # Collect results
            for future in as_completed(future_to_task):
                task = future_to_task[future]
                try:
                    result = future.result()
                    task["send_result"] = result
                    task["send_duration"] = result.get("duration", 0)

                except Exception as e:
                    task["send_result"] = {"error": f"Exception: {e=}"}
                    task["send_duration"] = 0

        batch_send_duration = time.time() - start_time

        # Measure delivery times if requested
        if options["measure_delivery"]:
            self.stdout.write("Measuring delivery times...")
            self.measure_delivery_times(tasks, options["timeout"])

        # Compile batch results
        batch_summary = {
            "send_duration": batch_send_duration,
            "tasks": tasks,
            "concurrent_level": concurrent,
            "timestamp": timezone.now(),
        }

        batch_results.append(batch_summary)

        # Show batch summary
        successful_sends = sum(
            1 for task in tasks if not task["send_result"].get("error")
        )
        self.stdout.write(
            f"Batch completed: {successful_sends}/{len(tasks)} successful "
            f"in {batch_send_duration:.2f}s"
        )

        return batch_results

    def send_single_webhook(self, task):
        """Send a single webhook and measure timing."""
        obj = task["object"]
        event = task["event"]

        start_time = time.time()

        try:
            result = send_webhooks(obj, event)
            duration = time.time() - start_time

            return {
                "success": True,
                "result": result,
                "duration": duration,
                "object_id": obj.id,
            }
        except Exception as e:
            duration = time.time() - start_time

            return {
                "success": False,
                "error": str(e),
                "duration": duration,
                "object_id": obj.id,
            }

    def measure_delivery_times(self, tasks, timeout):
        """Measure actual webhook delivery times."""
        start_time = time.time()
        measured_count = 0

        while (time.time() - start_time) < timeout:
            for task in tasks:
                if task.get("delivery_measured"):
                    continue

                # Check for new delivery logs
                obj = task["object"]
                new_logs = WebhookDeliveryLog.objects.filter(
                    subscription__subscriber__content_type__model=obj._meta.model_name.lower(),  # noqa: E501
                    created_at__gte=task.get(
                        "send_start_time", timezone.now()
                    ),
                    payload__pk=obj.id,
                ).order_by("-created_at")

                if new_logs.exists():
                    latest_log = new_logs.first()
                    task["delivery_duration"] = latest_log.delivery_duration_ms
                    task["delivery_status"] = latest_log.response_status
                    task["delivery_measured"] = True
                    measured_count += 1

            # Check if all deliveries measured
            if measured_count >= len(tasks):
                break

            time.sleep(0.5)  # Check every 500ms

        measured_percentage = (measured_count / len(tasks)) * 100
        self.stdout.write(
            f"Measured {measured_count}/{len(tasks)} deliveries "
            f"({measured_percentage:.1f}%)"
        )

    def show_results(self, all_results, options):
        """Display comprehensive test results."""
        if not all_results:
            return

        self.stdout.write("\n" + "=" * 60)
        self.stdout.write("PERFORMANCE TEST RESULTS")
        self.stdout.write("=" * 60)

        # Aggregate statistics
        all_tasks = []
        total_send_time = 0

        for batch in all_results:
            all_tasks.extend(batch["tasks"])
            total_send_time += batch["send_duration"]

        successful_sends = sum(
            1 for task in all_tasks if not task["send_result"].get("error")
        )
        send_durations = [
            task["send_duration"]
            for task in all_tasks
            if task.get("send_duration")
        ]

        # Send performance metrics
        self.stdout.write("\nSend Performance:")
        self.stdout.write(f"  Total webhooks: {len(all_tasks)}")
        self.stdout.write(f"  Successful: {successful_sends}")
        self.stdout.write(f"  Failed: {len(all_tasks) - successful_sends}")
        self.stdout.write(
            f"  Success rate: {(successful_sends/len(all_tasks)*100):.1f}%"
        )
        self.stdout.write(f"  Total time: {total_send_time:.2f}s")
        self.stdout.write(
            f"  Throughput: {len(all_tasks)/total_send_time:.1f} webhooks/sec"
        )

        if send_durations:
            self.stdout.write(
                f"  Avg send time: {statistics.mean(send_durations):.3f}s"
            )
            self.stdout.write(f"  Min send time: {min(send_durations):.3f}s")
            self.stdout.write(f"  Max send time: {max(send_durations):.3f}s")

            if len(send_durations) > 1:
                self.stdout.write(
                    "  Send time std dev: "
                    f"{statistics.stdev(send_durations):.3f}s"
                )

        # Delivery performance metrics (if measured)
        delivery_tasks = [
            task for task in all_tasks if task.get("delivery_measured")
        ]

        if delivery_tasks:
            self.stdout.write("\nDelivery Performance:")
            delivery_times = [
                task["delivery_duration"]
                for task in delivery_tasks
                if task.get("delivery_duration")
            ]
            successful_deliveries = sum(
                1
                for task in delivery_tasks
                if task.get("delivery_status", 0) in range(200, 300)
            )

            self.stdout.write(f"  Measured deliveries: {len(delivery_tasks)}")
            self.stdout.write(
                f"  Successful deliveries: {successful_deliveries}"
            )
            self.stdout.write(
                "  Delivery success rate: "
                f"{(successful_deliveries/len(delivery_tasks)*100):.1f}%"
            )

            if delivery_times:
                self.stdout.write(
                    "  Avg delivery time: "
                    f"{statistics.mean(delivery_times):.0f}ms"
                )
                self.stdout.write(
                    f"  Min delivery time: {min(delivery_times)}ms"
                )
                self.stdout.write(
                    f"  Max delivery time: {max(delivery_times)}ms"
                )

                if len(delivery_times) > 1:
                    self.stdout.write(
                        "  Delivery time std dev: "
                        f"{statistics.stdev(delivery_times):.0f}ms"
                    )

        # Error analysis
        errors = defaultdict(int)
        for task in all_tasks:
            error = task["send_result"].get("error")
            if error:
                errors[error] += 1

        if errors:
            self.stdout.write("\nError Analysis:")
            for error, count in sorted(
                errors.items(), key=lambda x: x[1], reverse=True
            ):
                self.stdout.write(f"  {error}: {count} occurrences")

        # Concurrency analysis
        if len(all_results) > 1:
            self.stdout.write("\nBatch Analysis:")
            for i, batch in enumerate(all_results):
                batch_successful = sum(
                    1
                    for task in batch["tasks"]
                    if not task["send_result"].get("error")
                )
                self.stdout.write(
                    f"  Batch {i+1}: {batch_successful}/{len(batch['tasks'])} "
                    "successful "
                    f"in {batch['send_duration']:.2f}s"
                )
