from unittest.mock import Mock, patch

import requests
from django.test import TestCase
from django.utils import timezone

from django_webhook_subscriber import models, tasks

from .factories import (
    ContentTypeFactory,
    WebhookDeliveryLogFactory,
    WebhookSubscriberFactory,
    WebhookSubscriptionFactory,
)


class DeliverWebhookTasksTests(TestCase):
    def setUp(self):
        self.subscription = WebhookSubscriptionFactory()

    def mock_response(self, status_code=200, json_data=None):
        mock_resp = requests.Response()
        mock_resp.status_code = status_code
        mock_resp._content = (
            b'{"key": "value"}' if json_data is None else json_data
        )
        return mock_resp

    def test_deliver_webhook_on_subscription_does_not_exist_error(self):
        result = tasks.deliver_webhook("", {}, subscription_id=9999)
        self.assertIn("error", result)
        self.assertIn("Subscription not found", result["error"])

    def test_deliver_webhook_on_no_active_subscription_error(self):
        # deactivate subscription
        self.subscription.is_active = False
        self.subscription.save()
        result = tasks.deliver_webhook(
            url="",
            payload={},
            subscription_id=self.subscription.id,
        )
        self.assertIn("skipped", result)
        self.assertIn("Subscription inactive", result["skipped"])

    @patch("django_webhook_subscriber.tasks.webhook_session")
    def test_deliver_webhook_on_successful_delivery(
        self, mock_session_context
    ):
        # Mocking the session.post request to return a successful response
        mock_session = mock_session_context.return_value.__enter__.return_value
        mock_session.post.return_value = self.mock_response(200)

        result = tasks.deliver_webhook(
            url="http://example.com/webhook",
            payload={"key": "value"},
            subscription_id=self.subscription.id,
        )
        # Asserting result indicates success
        mock_session.post.assert_called_once_with(
            "http://example.com/webhook",
            json={"key": "value"},
            headers=tasks.generate_headers(self.subscription.subscriber),
            timeout=30,
        )
        # Asserting result indicates success
        self.assertTrue(result["success"])
        self.assertEqual(result["status_code"], 200)
        self.assertIn("duration_ms", result)
        self.assertEqual(result["attempt"], 1)

        # Asserting DeliveryLog was created
        log = models.WebhookDeliveryLog.objects.first()
        self.assertIsNotNone(log)
        self.assertEqual(log.subscription, self.subscription)
        self.assertEqual(log.response_status, 200)
        self.assertEqual(log.response_body, '{"key": "value"}')

    @patch("django_webhook_subscriber.tasks.webhook_session")
    def test_deliver_webhook_on_failed_delivery(self, mock_session_context):
        # Mocking the session.post request to return a successful response
        mock_session = mock_session_context.return_value.__enter__.return_value
        mock_session.post.return_value = self.mock_response(400)

        with patch(
            "django_webhook_subscriber.tasks._should_retry_delivery"
        ) as mock_should_retry:
            mock_should_retry.return_value = True
            result = tasks.deliver_webhook(
                url="http://example.com/webhook",
                payload={"key": "value"},
                subscription_id=self.subscription.id,
            )
            # Asserting result indicates success
            mock_session.post.assert_called_once_with(
                "http://example.com/webhook",
                json={"key": "value"},
                headers=tasks.generate_headers(self.subscription.subscriber),
                timeout=30,
            )
            # Asserting result indicates success
            self.assertFalse(result["success"])
            self.assertEqual(result["status_code"], 400)
            self.assertIn("duration_ms", result)
            self.assertEqual(result["attempt"], 1)
            self.assertTrue(result["will_retry"])

            # Asserting DeliveryLog was created
            log = models.WebhookDeliveryLog.objects.first()
            self.assertIsNotNone(log)
            self.assertEqual(log.subscription, self.subscription)
            self.assertEqual(log.response_status, 400)
            self.assertEqual(log.response_body, '{"key": "value"}')

    @patch("django_webhook_subscriber.tasks.webhook_session")
    def test_deliver_webhook_on_timeout_error_during_delivery(
        self, mock_session_context
    ):
        # Mocking the session.post request to return a successful response
        mock_session = mock_session_context.return_value.__enter__.return_value
        mock_session.post.side_effect = requests.exceptions.Timeout("Timeout!")

        result = tasks.deliver_webhook(
            url="http://example.com/webhook",
            payload={"key": "value"},
            subscription_id=self.subscription.id,
        )
        # Asserting result indicates success
        self.assertIn("error", result)
        self.assertIn("Timeout error", result["error"])
        self.assertEqual(result["attempt"], 1)
        # Asserting DeliveryLog was created
        log = models.WebhookDeliveryLog.objects.first()
        self.assertIsNotNone(log)
        self.assertEqual(log.subscription, self.subscription)
        self.assertEqual(log.error_message, "Timeout after 30s")

    @patch("django_webhook_subscriber.tasks.webhook_session")
    def test_deliver_webhook_on_connection_error_during_delivery(
        self, mock_session_context
    ):
        # Mocking the session.post request to return a successful response
        mock_session = mock_session_context.return_value.__enter__.return_value
        mock_session.post.side_effect = requests.exceptions.ConnectionError(
            "Connection error!"
        )

        result = tasks.deliver_webhook(
            url="http://example.com/webhook",
            payload={"key": "value"},
            subscription_id=self.subscription.id,
        )
        # Asserting result indicates success
        self.assertIn("error", result)
        self.assertIn("Connection error", result["error"])
        self.assertEqual(result["attempt"], 1)
        # Asserting DeliveryLog was created
        log = models.WebhookDeliveryLog.objects.first()
        self.assertIsNotNone(log)
        self.assertEqual(log.subscription, self.subscription)
        self.assertIn("Connection error", log.error_message)

    @patch("django_webhook_subscriber.tasks.webhook_session")
    def test_deliver_webhook_on_exception_during_delivery(
        self, mock_session_context
    ):
        # Mocking the session.post request to return a successful response
        mock_session = mock_session_context.return_value.__enter__.return_value
        mock_session.post.side_effect = Exception("Some error!")

        result = tasks.deliver_webhook(
            url="http://example.com/webhook",
            payload={"key": "value"},
            subscription_id=self.subscription.id,
        )
        # Asserting result indicates success
        self.assertIn("error", result)
        self.assertIn("Unexpected error", result["error"])
        self.assertEqual(result["attempt"], 1)
        # Asserting DeliveryLog was created
        log = models.WebhookDeliveryLog.objects.first()
        self.assertIsNotNone(log)
        self.assertEqual(log.subscription, self.subscription)
        self.assertIn("Unexpected error", log.error_message)

    def test_should_retry_delivery_on_max_retries_exceeded(self):
        should_retry = tasks._should_retry_delivery(
            self.subscription,
            attempt=self.subscription.subscriber.max_retries + 1,
        )
        self.assertFalse(should_retry)

    def test_should_retry_delivery_on_status_code_retryable(self):
        should_retry = tasks._should_retry_delivery(
            self.subscription, attempt=1, status_code=500
        )
        self.assertTrue(should_retry)

    def test_should_retry_delivery_on_status_code_not_retryable(self):
        should_retry = tasks._should_retry_delivery(
            self.subscription, attempt=1, status_code=429
        )
        self.assertFalse(should_retry)

    @patch("django_webhook_subscriber.tasks.deliver_webhook")
    def test_schedule_retry_on_successful_scheduling(self, mock_deliver):
        tasks._schedule_retry(
            url="http://example.com/webhook",
            payload={"key": "value"},
            subscription_id=self.subscription.id,
            current_attempt=1,
        )
        mock_deliver.apply_async.assert_called_once_with(
            args=(
                "http://example.com/webhook",
                {"key": "value"},
                self.subscription.id,
            ),
            kwargs={"attempt": 2},
            countdown=60,  # default
        )

    @patch("django_webhook_subscriber.tasks.deliver_webhook")
    def test_schedule_retry_on_failure(self, mock_deliver):
        mock_deliver.apply_async.side_effect = Exception("Some error!")
        # Asserting no raise
        tasks._schedule_retry(
            url="http://example.com/webhook",
            payload={"key": "value"},
            subscription_id=self.subscription.id,
            current_attempt=1,
        )
        mock_deliver.apply_async.assert_called_once()

    @patch("django_webhook_subscriber.tasks._schedule_retry")
    def test_handle_delivery_exception_on_retry(self, mock_schedule_retry):
        log = WebhookDeliveryLogFactory(subscription=self.subscription)
        with patch(
            "django_webhook_subscriber.tasks._should_retry_delivery"
        ) as mock_should_retry:
            mock_should_retry.return_value = True
            tasks._handle_delivery_exception(
                log,
                self.subscription,
                "Some error!",
                url="http://example.com/webhook",
                payload={"key": "value"},
                attempt=1,
            )
            mock_should_retry.assert_called_once_with(self.subscription, 1)
            mock_schedule_retry.assert_called_once_with(
                "http://example.com/webhook",
                {"key": "value"},
                self.subscription.id,
                1,
            )


class ProcessWebhookDeliveryBatchTasksTests(TestCase):
    def setUp(self):
        content_type = ContentTypeFactory()
        subscriber = WebhookSubscriberFactory(content_type=content_type)
        self.subscriptions = WebhookSubscriptionFactory.create_batch(
            3,
            subscriber=subscriber,
            event_name="created",
        )

    def test_process_webhook_delivery_batch_on_no_subscriptions(self):
        results = tasks.process_webhook_delivery_batch([])
        self.assertIn("processed", results)
        self.assertEqual(results["processed"], 0)
        self.assertIn("error", results)
        self.assertEqual(results["error"], "Empty batch")

    @patch("django_webhook_subscriber.tasks._validate_subscription_data")
    def test_process_webhook_delivery_batch_on_invalid_subscriptions(
        self, mock_validate
    ):
        mock_validate.return_value = False
        results = tasks.process_webhook_delivery_batch([{"id": 9999}])
        self.assertIn("processed", results)
        self.assertEqual(results["processed"], 0)
        self.assertIn("error", results)
        self.assertEqual(results["error"], "No valid subscriptions")

    @patch("django_webhook_subscriber.tasks._validate_subscription_data")
    @patch("django_webhook_subscriber.tasks.group")
    @patch("django_webhook_subscriber.tasks.deliver_webhook")
    def test_process_webhook_delivery_batch_on_successful_processing(
        self, mock_deliver, mock_group, mock_validate
    ):
        mock_validate.return_value = True

        # Mock the group execution to return successful results
        mock_job = mock_group.return_value
        mock_job.apply_async.return_value.get.return_value = [
            {"success": True, "status_code": 200} for _ in self.subscriptions
        ]

        results = tasks.process_webhook_delivery_batch(
            [
                {
                    "id": sub.id,
                    "url": "https://example.com/webhooks",
                    "payload": {"key": "value"},
                }
                for sub in self.subscriptions
            ]
        )

        # Verify signatures were created
        self.assertEqual(mock_deliver.s.call_count, 3)

        # Verify group was executed
        mock_group.assert_called_once()
        mock_job.apply_async.assert_called_once()

        # Assert results
        self.assertIn("batch_id", results)
        self.assertIn("task_ids", results)
        self.assertEqual(results["processed"], 3)
        self.assertEqual(results["total_requested"], 3)

    @patch("django_webhook_subscriber.tasks._validate_subscription_data")
    @patch("django_webhook_subscriber.tasks.group")
    @patch("django_webhook_subscriber.tasks.deliver_webhook")
    def test_process_webhook_delivery_batch_on_exception_during_processing(
        self, mock_deliver, mock_group, mock_validate
    ):
        mock_validate.return_value = True

        # Mock the group execution to raise an exception
        mock_job = mock_group.return_value
        mock_job.apply_async.side_effect = Exception("Some error!")

        results = tasks.process_webhook_delivery_batch(
            [
                {
                    "id": sub.id,
                    "url": "https://example.com/webhooks",
                    "payload": {"key": "value"},
                }
                for sub in self.subscriptions
            ]
        )

        # Verify signatures were created
        self.assertEqual(mock_deliver.s.call_count, 3)

        # Verify group was executed
        mock_group.assert_called_once()
        mock_job.apply_async.assert_called_once()

        # Assert results
        self.assertEqual(results["error"], "e=Exception('Some error!')")
        self.assertEqual(results["processed"], 0)

    def test_validate_subscription_data_on_valid_data(self):
        results = tasks._validate_subscription_data(
            {
                "id": self.subscriptions[0].id,
                "url": "https://example.com",
                "payload": {},
            }
        )
        self.assertTrue(results)

    def test_validate_subscription_data_on_invalid_data(self):
        results = tasks._validate_subscription_data(
            {
                "id": 9999,
                "payload": {},
            }
        )
        self.assertFalse(results)


class TaskMaintenanceTasksTests(TestCase):
    def setUp(self):
        # Default 30 days retention
        self.timestamp_created = timezone.now() - timezone.timedelta(days=30)
        self.log = WebhookDeliveryLogFactory()
        self.subscription = self.log.subscription
        self.subscriber = self.subscription.subscriber

    def mock_response(self, status_code=200, json_data=None):
        mock_resp = requests.Response()
        mock_resp.status_code = status_code
        mock_resp._content = (
            b'{"key": "value"}' if json_data is None else json_data
        )
        return mock_resp

    def test_cleanup_webhook_logs_on_empty_query(self):
        results = tasks.cleanup_webhook_logs(30)
        self.assertIn("deleted", results)
        self.assertEqual(results["deleted"], 0)
        self.assertIn("cutoff_date", results)

    def test_cleanup_webhook_logs_on_successful_deletion(self):
        # Changing created timestamp to older than 30 days
        self.log.created_at = self.timestamp_created
        self.log.save()
        results = tasks.cleanup_webhook_logs(days=1)
        self.assertIn("deleted", results)
        self.assertEqual(results["deleted"], 1)
        self.assertIn("cutoff_date", results)
        # Assert logs are deleted
        remaining_logs = models.WebhookDeliveryLog.objects.count()
        self.assertEqual(remaining_logs, 0)

    def test_cleanup_webhook_logs_passing_subscription(self):
        # Changing created timestamp to older than 30 days
        self.log.created_at = self.timestamp_created
        self.log.save()
        results = tasks.cleanup_webhook_logs(
            days=1, subscription_id=self.subscription.id
        )
        self.assertIn("deleted", results)
        self.assertEqual(results["deleted"], 1)
        self.assertIn("cutoff_date", results)
        # Assert logs are deleted
        remaining_logs = models.WebhookDeliveryLog.objects.count()
        self.assertEqual(remaining_logs, 0)

    def test_cleanup_webhook_logs_on_exception_during_cleanup(self):
        # Setting exception raise
        with patch(
            "django_webhook_subscriber."
            "models.WebhookDeliveryLog.objects.filter"
        ) as mock_filter:
            mock_filter.side_effect = Exception("Some error!")
            results = tasks.cleanup_webhook_logs(30)
            self.assertIn("error", results)
            self.assertIn("Some error!", results["error"])

    def test_webhook_connectivity_check_on_no_subscribers(self):
        results = tasks.test_webhook_connectivity([9999])
        self.assertEqual(results["tested"], 0)
        self.assertEqual(results["results"], [])
        self.assertEqual(results["error"], "No active subscribers found")

    @patch("django_webhook_subscriber.tasks._test_single_endpoint")
    def test_webhook_connectivity_check_on_successful_check(self, mock_test):
        # Mocking the session.post request to return a successful response
        mock_test.return_value = {
            "subscriber_id": self.subscriber.id,
            "subscriber_name": self.subscriber.name,
            "url": self.subscriber.target_url,
            "success": True,
            "status_code": 400,
            "duration_ms": 123,
            "error": None,
        }
        results = tasks.test_webhook_connectivity([self.subscriber.id])

        self.assertEqual(results["tested"], 1)
        self.assertEqual(results["successful_responses"], 0)
        self.assertEqual(results["successful"], 1)
        self.assertEqual(results["failed"], 0)
        self.assertIn("results", results)

    @patch("django_webhook_subscriber.tasks._test_single_endpoint")
    def test_webhook_connectivity_check_on_exception_raise(self, mock_test):
        # Mocking the session.post request to return a successful response
        mock_test.side_effect = Exception("Some error!")
        results = tasks.test_webhook_connectivity([self.subscriber.id])

        self.assertIn("error", results)
        self.assertIn("Some error!", results["error"])

    def test_single_endpoint_check_on_successful_check(self):
        session = Mock()
        session.head.return_value = self.mock_response(200)
        result = tasks._test_single_endpoint(session, self.subscriber)
        self.assertEqual(result["subscriber_id"], self.subscriber.id)
        self.assertEqual(result["subscriber_name"], self.subscriber.name)
        self.assertEqual(result["url"], self.subscriber.target_url)
        self.assertTrue(result["success"])
        self.assertEqual(result["status_code"], 200)
        self.assertIn("duration_ms", result)
        self.assertIsNone(result["error"])

    def test_single_endpoint_check_on_failed_check(self):
        session = Mock()
        session.head.return_value = self.mock_response(500)
        result = tasks._test_single_endpoint(session, self.subscriber)
        self.assertEqual(result["subscriber_id"], self.subscriber.id)
        self.assertEqual(result["subscriber_name"], self.subscriber.name)
        self.assertEqual(result["url"], self.subscriber.target_url)
        self.assertTrue(result["success"])
        self.assertEqual(result["status_code"], 500)
        self.assertIn("duration_ms", result)
        self.assertIsNone(result["error"])

    def test_single_endpoint_check_on_exception_check(self):
        session = Mock()
        session.head.side_effect = Exception("Some error!")
        result = tasks._test_single_endpoint(session, self.subscriber)
        self.assertEqual(result["subscriber_id"], self.subscriber.id)
        self.assertEqual(result["subscriber_name"], self.subscriber.name)
        self.assertEqual(result["url"], self.subscriber.target_url)
        self.assertFalse(result["success"])
        self.assertIsNone(result["status_code"])
        self.assertIn("duration_ms", result)
        self.assertIn("Some error!", result["error"])
