from unittest.mock import Mock, patch

from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.test import TestCase, override_settings

from django_webhook_subscriber import delivery, models, utils

from .factories import (
    WebhookDeliveryLogFactory,
    WebhookSubscriberFactory,
    WebhookSubscriptionFactory,
)


class WebhookDeliveryProcessorTests(TestCase):
    def setUp(self):
        self.processor = delivery.WebhookDeliveryProcessor()
        # Clear cache before each test
        delivery.clear_webhook_cache()

        # Create test content type and model instance
        self.content_type = ContentType.objects.get_for_model(
            models.WebhookDeliveryLog
        )
        self.instance = WebhookDeliveryLogFactory()
        self.subscriber = WebhookSubscriberFactory(
            content_type=self.content_type
        )
        self.subscription = WebhookSubscriptionFactory(
            subscriber=self.subscriber, event_name="created"
        )

    def tearDown(self):
        cache.clear()
        delivery.clear_webhook_cache()

    def test_delivery_process_on_initialization(self):
        self.assertEqual(self.processor.cache_ttl, 300)
        with override_settings(WEBHOOK_SUBSCRIBER={"WEBHOOK_CACHE_TTL": 600}):
            processor = delivery.WebhookDeliveryProcessor()
            self.assertEqual(processor.cache_ttl, 600)

    def test_send_webhook_on_webhooks_disabled(self):
        with utils.disable_webhooks():
            result = self.processor.send_webhook(self.instance, "created")
            self.assertEqual(result, {"skipped": "Webhooks disabled"})

    def test_send_webhook_on_no_subscriptions(self):
        with patch.object(
            self.processor, "_get_subscriptions_cached"
        ) as mock_get_subs:
            mock_get_subs.return_value = []
            result = self.processor.send_webhook(self.instance, "created")
            self.assertEqual(result, {"skipped": "No subscriptions"})

    def test_send_webhook_on_successful_generation(self):
        # Generating subscription, and subscriber
        subscription = WebhookSubscriptionFactory(
            subscriber=self.subscriber,
            event_name="created",
        )
        with (
            patch.object(
                self.processor, "_get_subscriptions_cached"
            ) as mock_get_subs,
            patch.object(
                self.processor, "_group_subscriptions_by_serializer"
            ) as mock_group,
            patch.object(self.processor, "_generate_payload") as mock_generate,
            patch.object(self.processor, "_deliver_webhooks") as mock_deliver,
        ):
            mock_get_subs.return_value = [{"id": subscription.id}]
            mock_group.return_value = {None: [{"id": subscription.id}]}
            mock_generate.return_value = {"id": self.instance.id}
            mock_deliver.return_value = {"delivered": 1}

            self.processor.send_webhook(self.instance, "created")
            mock_get_subs.assert_called_once_with(self.instance, "created")
            mock_group.assert_called_once_with([{"id": subscription.id}])
            mock_generate.assert_called_once_with(
                self.instance, "created", None
            )
            mock_deliver.assert_called_once()
            args = mock_deliver.call_args[0][0]
            self.assertEqual(args[0]["id"], subscription.id)

    def test_send_webhook_on_exception_raised(self):
        # Generating subscription, and subscriber
        with patch.object(
            self.processor, "_get_subscriptions_cached"
        ) as mock_get_subs:
            mock_get_subs.side_effect = Exception("Test exception")
            results = self.processor.send_webhook(self.instance, "created")
            self.assertIn("error", results)
            self.assertIn("Error sending webhook", results["error"])

    def test_group_subscriptions_by_serializer(self):
        # Generating subscriptions with different serializers
        results = self.processor._group_subscriptions_by_serializer([])
        self.assertEqual(dict(results), {})
        # Creating subscriptions

        results = self.processor._group_subscriptions_by_serializer(
            [
                {"id": 1, "serializer_class": None},
                {"id": 2, "serializer_class": "some.path.SerializerA"},
            ]
        )
        self.assertEqual(
            dict(results),
            {
                None: [{"id": 1, "serializer_class": None}],
                "some.path.SerializerA": [
                    {"id": 2, "serializer_class": "some.path.SerializerA"}
                ],
            },
        )

    @patch("django_webhook_subscriber.delivery.get_content_type_id")
    def test_get_subscriptions_cached_on_cache_hit(self, mock_get_ct_id):
        mock_get_ct_id.return_value = 1
        cached_data = [{"id": 1, "url": "http://example.com"}]
        cache.set("webhook_subscriptions:1:created", cached_data)

        result = self.processor._get_subscriptions_cached(
            self.instance, "created"
        )

        self.assertEqual(result, cached_data)
        mock_get_ct_id.assert_called_once()

    @patch("django_webhook_subscriber.delivery.get_content_type_id")
    @patch.object(
        delivery.WebhookDeliveryProcessor, "_fetch_subscriptions_from_db"
    )
    def test_get_subscriptions_cached_on_cache_miss(
        self, mock_fetch, mock_get_ct_id
    ):
        mock_get_ct_id.return_value = 1
        db_data = [{"id": 1, "url": "http://example.com"}]
        mock_fetch.return_value = db_data

        result = self.processor._get_subscriptions_cached(
            self.instance, "created"
        )

        self.assertEqual(result, db_data)
        mock_fetch.assert_called_once_with(1, "created")
        # Verify it was cached
        cached = cache.get("webhook_subscriptions:1:created")
        self.assertEqual(cached, db_data)

    @patch("django_webhook_subscriber.delivery.get_content_type_id")
    @patch.object(
        delivery.WebhookDeliveryProcessor, "_fetch_subscriptions_from_db"
    )
    def test_get_subscriptions_cached_on_empty_cache(
        self, mock_fetch, mock_get_ct_id
    ):
        mock_get_ct_id.return_value = 1
        mock_fetch.return_value = []

        result = self.processor._get_subscriptions_cached(
            self.instance, "created"
        )

        self.assertEqual(result, [])
        mock_fetch.assert_called_once()

    def test_fetch_subscriptions_from_db_on_no_subscriptions(self):
        result = self.processor._fetch_subscriptions_from_db(
            999, "nonexistent"
        )

        self.assertEqual(result, [])

    def test_fetch_subscriptions_from_db_on_existing_subscriptions(self):
        # Create test data
        result = self.processor._fetch_subscriptions_from_db(
            self.content_type.id,
            "created",
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], self.subscription.id)
        self.assertEqual(result[0]["subscriber_id"], self.subscriber.id)
        self.assertEqual(result[0]["url"], self.subscriber.target_url)

    @patch("django_webhook_subscriber.delivery.serialize_webhook_instance")
    def test_generate_payload_on_successful_serialization(
        self, mock_serialize
    ):
        mock_serialize.return_value = {"field1": "value1", "field2": "value2"}

        result = self.processor._generate_payload(
            self.instance, "created", None
        )

        self.assertEqual(result["pk"], 1)
        self.assertEqual(result["event_signal"], "created")
        self.assertEqual(
            result["source"], "django_webhook_subscriber.webhookdeliverylog"
        )
        self.assertEqual(
            result["fields"], {"field1": "value1", "field2": "value2"}
        )
        self.assertIn("timestamp", result)

    @patch("django_webhook_subscriber.delivery.serialize_webhook_instance")
    def test_generate_payload_on_serialization_exception(self, mock_serialize):
        mock_serialize.side_effect = Exception("Serialization failed")

        result = self.processor._generate_payload(
            self.instance, "created", None
        )

        self.assertEqual(result["pk"], 1)
        self.assertEqual(result["event_signal"], "created")
        self.assertIn("error", result)
        self.assertEqual(result["fields"], {})

    def test_deliver_webhooks_on_no_subscriptions(self):
        result = self.processor._deliver_webhooks([])

        self.assertEqual(result, {"processed": 0})

    @patch("django_webhook_subscriber.delivery.process_webhook_delivery_batch")
    def test_deliver_webhooks_on_single_batch_processing(self, mock_task):
        mock_result = Mock()
        mock_result.id = "task-123"
        mock_task.delay.return_value = mock_result

        subscriptions = [{"id": i} for i in range(10)]
        result = self.processor._deliver_webhooks(subscriptions)

        self.assertEqual(result["processed"], 10)
        self.assertEqual(result["batches"], 1)
        self.assertEqual(result["task_id"], "task-123")
        mock_task.delay.assert_called_once()

    @patch("django_webhook_subscriber.delivery.process_webhook_delivery_batch")
    @override_settings(WEBHOOK_SUBSCRIBER={"MAX_BATCH_SIZE": 5})
    def test_deliver_webhooks_on_multiple_batch_processing(self, mock_task):
        mock_result1 = Mock()
        mock_result1.id = "task-1"
        mock_result2 = Mock()
        mock_result2.id = "task-2"
        mock_task.delay.side_effect = [mock_result1, mock_result2]

        # Create processor with new settings
        processor = delivery.WebhookDeliveryProcessor()
        subscriptions = [{"id": i} for i in range(10)]
        result = processor._deliver_webhooks(subscriptions)

        self.assertEqual(result["processed"], 10)
        self.assertEqual(result["batches"], 2)
        self.assertEqual(len(result["task_ids"]), 2)
        self.assertEqual(mock_task.delay.call_count, 2)

    @patch("django_webhook_subscriber.delivery.process_webhook_delivery_batch")
    def test_process_single_batch_on_successful_delivery(self, mock_task):
        mock_result = Mock()
        mock_result.id = "task-123"
        mock_task.delay.return_value = mock_result

        subscriptions = [{"id": 1}]
        result = self.processor._process_single_batch(subscriptions)

        self.assertEqual(result["processed"], 1)
        self.assertEqual(result["batches"], 1)
        self.assertEqual(result["task_id"], "task-123")

    @patch("django_webhook_subscriber.delivery.process_webhook_delivery_batch")
    def test_process_single_batch_on_delivery_exception(self, mock_task):
        mock_task.delay.side_effect = Exception("Celery error")

        subscriptions = [{"id": 1}]
        result = self.processor._process_single_batch(subscriptions)

        self.assertIn("error", result)
        self.assertEqual(result["processed"], 0)

    @patch("django_webhook_subscriber.delivery.process_webhook_delivery_batch")
    def test_process_multiple_batches_on_successful_delivery(self, mock_task):
        mock_result1 = Mock()
        mock_result1.id = "task-1"
        mock_result2 = Mock()
        mock_result2.id = "task-2"
        mock_task.delay.side_effect = [mock_result1, mock_result2]

        subscriptions = [{"id": i} for i in range(10)]
        result = self.processor._process_multiple_batches(subscriptions, 5)

        self.assertEqual(result["processed"], 10)
        self.assertEqual(result["batches"], 2)
        self.assertEqual(len(result["task_ids"]), 2)

    @patch("django_webhook_subscriber.delivery.process_webhook_delivery_batch")
    def test_process_multiple_batches_on_delivery_exception(self, mock_task):
        mock_result1 = Mock()
        mock_result1.id = "task-1"
        mock_task.delay.side_effect = [mock_result1, Exception("Celery error")]

        subscriptions = [{"id": i} for i in range(10)]
        result = self.processor._process_multiple_batches(subscriptions, 5)

        self.assertEqual(result["processed"], 5)
        self.assertEqual(result["batches"], 2)
        self.assertEqual(len(result["task_ids"]), 1)  # Only successful one
        # Check that one batch has error
        error_batch = next(b for b in result["batch_details"] if "error" in b)
        self.assertIn("error", error_batch)

    def test_clear_webhook_cache_on_no_parameters(self):
        # Set up some cache data
        cache.set("webhook_subscriptions:1:created", [{"id": 1}])
        cache.set("webhook_subscriptions:2:updated", [{"id": 2}])

        self.processor.clear_webhook_cache()

        # Verify cache is cleared
        self.assertIsNone(cache.get("webhook_subscriptions:1:created"))
        self.assertIsNone(cache.get("webhook_subscriptions:2:updated"))

    def test_clear_webhook_cache_on_content_type_only(self):
        # Create subscriptions for testing
        WebhookSubscriptionFactory(
            subscriber=self.subscriber, event_name="updated"
        )

        # Set up cache
        cache.set(
            f"webhook_subscriptions:{self.content_type.id}:created",
            [{"id": 1}],
        )
        cache.set(
            f"webhook_subscriptions:{self.content_type.id}:updated",
            [{"id": 2}],
        )

        self.processor.clear_webhook_cache(content_type=self.content_type)

        # Verify both are cleared
        self.assertIsNone(
            cache.get(f"webhook_subscriptions:{self.content_type.id}:created")
        )
        self.assertIsNone(
            cache.get(f"webhook_subscriptions:{self.content_type.id}:updated")
        )

    def test_clear_webhook_cache_on_content_type_and_event_name(self):
        cache_key = f"webhook_subscriptions:{self.content_type.id}:created"
        cache.set(cache_key, [{"id": 1}])

        self.processor.clear_webhook_cache(
            content_type=self.content_type, event_name="created"
        )

        self.assertIsNone(cache.get(cache_key))

    def test_get_cache_stats_on_no_cache(self):
        stats = self.processor.get_cache_stats()

        self.assertEqual(stats["cached_keys"], 0)
        self.assertEqual(stats["total_cached_subscriptions"], 0)
        self.assertEqual(stats["cache_hit_ratio"], 0.0)
        self.assertGreater(stats["total_possible_keys"], 0)

    def test_get_cache_stats_on_existing_cache(self):
        # Populate cache
        cache_key = f"webhook_subscriptions:{self.content_type.id}:created"
        cached_data = [{"id": 1}, {"id": 2}]
        cache.set(cache_key, cached_data)

        stats = self.processor.get_cache_stats()

        self.assertEqual(stats["cached_keys"], 1)
        self.assertEqual(stats["total_cached_subscriptions"], 2)
        self.assertEqual(stats["cache_hit_ratio"], 50.0)
        self.assertEqual(stats["total_possible_keys"], 2)


class WebhookDeliveryProcessorFunctionsTests(TestCase):
    def setUp(self):
        self.processor = delivery.webhook_delivery_processor

    def test_send_webhook_function_on_calling_the_right_method(self):
        with patch.object(self.processor, "send_webhook") as mock_send:
            mock_send.return_value = Mock()
            result = delivery.send_webhooks(
                instance=self, event_name="created", extra_context={}
            )
            mock_send.assert_called_once_with(
                self, "created", context=None, extra_context={}
            )
            self.assertEqual(result, mock_send.return_value)

    def test_clear_webhook_cache_function_on_calling_the_right_functions(self):
        with (
            patch.object(self.processor, "clear_webhook_cache") as mock_clear,
            patch(
                "django_webhook_subscriber.delivery.clear_content_type_cache"
            ) as mock_clear_content_cache,
        ):
            mock_clear.return_value = None
            mock_clear_content_cache.return_value = None
            result = delivery.clear_webhook_cache()
            mock_clear.assert_called_once_with(
                content_type=None, event_name=None
            )
            mock_clear_content_cache.assert_called_once_with()
            self.assertIsNone(result)

    def test_get_webhook_cache_stats_function_on_calling_the_right_method(
        self,
    ):
        with patch.object(self.processor, "get_cache_stats") as mock_stats:
            mock_stats.return_value = {"key": "value"}
            result = delivery.get_webhook_cache_stats()
            mock_stats.assert_called_once_with()
            self.assertEqual(result, {"key": "value"})

    def test_warm_webhook_cache_on_warming_all_subscriptions(self):
        # Generating subscription, and subscriber
        content_type = ContentType.objects.get(
            app_label="django_webhook_subscriber", model="webhooksubscriber"
        )
        subscriber = WebhookSubscriberFactory(content_type=content_type)
        WebhookSubscriptionFactory(subscriber=subscriber, event_name="created")

        with patch.object(
            self.processor, "_get_subscriptions_cached"
        ) as mock_cache:
            results = delivery.warm_webhook_cache()
            mock_cache.assert_called_once()
            args = mock_cache.call_args[0]
            self.assertEqual(len(args), 2)
            self.assertIsInstance(args[0], models.WebhookSubscriber)
            self.assertEqual(args[1], "created")
            self.assertEqual(results["warmed"], 1)

    def test_warm_webhook_cache_on_exception_raised(self):
        # Generating subscription, and subscriber
        content_type = ContentType.objects.get(
            app_label="django_webhook_subscriber", model="webhooksubscriber"
        )
        subscriber = WebhookSubscriberFactory(content_type=content_type)
        WebhookSubscriptionFactory(subscriber=subscriber, event_name="created")
        with patch.object(
            self.processor, "_get_subscriptions_cached"
        ) as mock_cache:
            mock_cache.side_effect = Exception("Test exception")
            results = delivery.warm_webhook_cache()
            mock_cache.assert_called_once()
            args = mock_cache.call_args[0]
            self.assertEqual(len(args), 2)
            self.assertIsInstance(args[0], models.WebhookSubscriber)
            self.assertEqual(args[1], "created")
            self.assertEqual(results["warmed"], 0)
