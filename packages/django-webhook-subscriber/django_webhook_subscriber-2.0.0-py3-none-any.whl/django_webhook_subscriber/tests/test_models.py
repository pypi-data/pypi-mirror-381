from django.core.exceptions import ValidationError
from django.test import TestCase

from django_webhook_subscriber import managers, models, validators

from .factories import (
    ContentTypeFactory,
    WebhookSubscriberFactory,
    WebhookSubscriptionFactory,
)


class WebhookSubscriberModelTests(TestCase):
    def setUp(self):
        self.content_type = ContentTypeFactory()
        self.subscriber = models.WebhookSubscriber.objects.create(
            name="Test Subscriber",
            target_url="https://example.com/webhook",
            secret="supersecret",
            content_type=self.content_type,
        )

    def test_subscriber_model_is_created_successfully(self):
        self.subscriber.full_clean()
        self.assertIsNotNone(self.subscriber.id)
        self.assertEqual(self.subscriber.name, "Test Subscriber")
        self.assertEqual(
            self.subscriber.target_url,
            "https://example.com/webhook",
        )
        self.assertEqual(self.subscriber.secret, "supersecret")
        self.assertEqual(self.subscriber.content_type, self.content_type)
        # Asserting Default Values
        self.assertTrue(self.subscriber.is_active)
        self.assertEqual(self.subscriber.description, "")
        self.assertEqual(self.subscriber.headers, {})
        self.assertIsNone(self.subscriber.last_success)
        self.assertIsNone(self.subscriber.last_failure)
        self.assertEqual(self.subscriber.max_retries, 3)
        self.assertEqual(self.subscriber.retry_delay, 60)
        # Asserting Meta Fields
        self.assertIsNotNone(self.subscriber.created_at)
        self.assertIsNotNone(self.subscriber.updated_at)

    def test_subscriber_model_unique_together_constraint(self):
        with self.assertRaises(Exception) as context:
            models.WebhookSubscriber.objects.create(
                name="Duplicate Subscriber",
                content_type=self.content_type,
                target_url="https://example.com/webhook",
                secret="anothersecret",
            )
        self.assertIn("already exists", str(context.exception).lower())

    def test_subscriber_model_str_representation(self):
        self.assertEqual(
            str(self.subscriber),
            "Test Subscriber (https://example.com/webhook)",
        )

    def test_subscriber_model_clean_method_validates_timeout(self):
        invalid_subscriber = models.WebhookSubscriber(
            name="Invalid Timeout Subscriber",
            target_url="https://example.com/webhook",
            secret="secret",
            content_type=self.content_type,
            timeout=301,  # Invalid timeout (> 300)
        )
        with self.assertRaises(Exception) as context:
            invalid_subscriber.full_clean()
        self.assertIn(
            "timeout cannot exceed 300 seconds", str(context.exception).lower()
        )

    def test_subscriber_model_clean_method_validates_retry_delay(self):
        invalid_subscriber = models.WebhookSubscriber(
            name="Invalid Timeout Subscriber",
            target_url="https://example.com/webhook",
            secret="secret",
            content_type=self.content_type,
            retry_delay=3601,  # Invalid timeout (> 1 hour)
        )
        with self.assertRaises(Exception) as context:
            invalid_subscriber.full_clean()
        self.assertIn(
            "retry_delay cannot exceed 3600 seconds",
            str(context.exception).lower(),
        )

    def test_subscriber_model_model_class_property(self):
        self.assertEqual(
            self.subscriber.model_class,
            self.content_type.model_class(),
        )

    def test_subscriber_model_model_name_property(self):
        self.assertEqual(
            self.subscriber.model_name,
            f"{self.content_type.app_label}.{self.content_type.model}",
        )

    def test_subscriber_model_record_success_method(self):
        self.subscriber.record_success()
        self.subscriber.refresh_from_db()
        self.assertIsNotNone(self.subscriber.last_success)
        self.assertIsNone(self.subscriber.last_failure)

    def test_subscriber_model_record_failure_method(self):
        self.subscriber.record_failure()
        self.subscriber.refresh_from_db()
        self.assertIsNotNone(self.subscriber.last_failure)
        self.assertIsNone(self.subscriber.last_success)
        # Test consecutive failures increment
        self.subscriber.record_failure()
        self.subscriber.refresh_from_db()
        self.assertEqual(self.subscriber.consecutive_failures, 2)
        self.subscriber.auto_disable_after_failures = 3
        self.subscriber.record_failure()
        self.subscriber.refresh_from_db()
        self.assertFalse(self.subscriber.is_active)
        self.assertEqual(self.subscriber.consecutive_failures, 3)


class WebhookSubscriptionModelTests(TestCase):
    def setUp(self):
        self.subscriber = WebhookSubscriberFactory(name="Test Subscriber")
        self.subscription = models.WebhookSubscription.objects.create(
            subscriber=self.subscriber,
            event_name="created",
        )

    def test_subscription_model_is_created_successfully(self):
        self.subscription.full_clean()
        self.assertIsNotNone(self.subscription.id)
        self.assertEqual(self.subscription.subscriber, self.subscriber)
        self.assertEqual(self.subscription.event_name, "created")
        # Asserting Default Values
        self.assertEqual(self.subscription.custom_endpoint, "")
        self.assertTrue(self.subscription.is_active)
        # Asserting Meta Fields
        self.assertIsNotNone(self.subscription.created_at)
        self.assertIsNotNone(self.subscription.updated_at)

    def test_subscription_model_str_representation(self):
        self.assertEqual(
            str(self.subscription),
            "Test Subscriber - created",
        )

    def test_subscription_model_unique_together_constraint(self):
        with self.assertRaises(Exception) as context:
            models.WebhookSubscription.objects.create(
                subscriber=self.subscriber,
                event_name="created",
            )
        self.assertIn("unique constraint", str(context.exception).lower())

    def test_subscription_model_clean_method_validates_event_type(self):
        pass

    def test_subscription_model_endpoint_property(self):
        self.subscriber.target_url = "https://example.com/webhook/"
        self.subscriber.save()
        self.subscription.custom_endpoint = "/events/create"
        self.subscription.full_clean()
        self.assertEqual(
            self.subscription.endpoint,
            "https://example.com/webhook/events/create",
        )

        # Remove endpoint
        self.subscription.custom_endpoint = ""
        self.subscription.save()
        self.assertEqual(
            self.subscription.endpoint,
            "https://example.com/webhook/",
        )

        # Full endpoint
        self.subscription.custom_endpoint = "https://another.com/hook"
        self.subscription.full_clean()
        self.assertEqual(
            self.subscription.endpoint,
            "https://another.com/hook",
        )

    def test_subscription_model_model_name_property(self):
        self.assertEqual(
            self.subscription.model_name,
            self.subscriber.model_name,
        )

    def test_subscription_model_content_type_property(self):
        self.assertEqual(
            self.subscription.content_type,
            self.subscriber.content_type,
        )

    def test_subscription_model_serializer_class_property(self):
        self.assertEqual(
            self.subscription.serializer_class,
            self.subscriber.serializer_class,
        )

    def test_subscription_model_success_rate_property(self):
        self.assertIsNone(self.subscription.success_rate)
        self.subscription.total_deliveries = 10
        self.subscription.successful_deliveries = 7
        self.subscription.save()
        self.assertEqual(self.subscription.success_rate, 70.0)
        self.subscription.successful_deliveries = 10
        self.subscription.save()
        self.assertEqual(self.subscription.success_rate, 100.0)

    def test_subscription_model_record_delivery_attempt_method(self):
        self.subscription.record_delivery_attempt(success=True)
        self.subscription.refresh_from_db()
        self.assertEqual(self.subscription.total_deliveries, 1)
        self.assertEqual(self.subscription.successful_deliveries, 1)
        self.assertEqual(self.subscription.consecutive_failures, 0)

        self.subscription.record_delivery_attempt(
            success=False, response_text=str("s") * 1025
        )
        self.subscription.refresh_from_db()
        self.assertEqual(self.subscription.total_deliveries, 2)
        self.assertEqual(self.subscription.successful_deliveries, 1)
        self.assertEqual(self.subscription.consecutive_failures, 1)
        self.assertEqual(len(self.subscription.last_response), 1024)


class WebhookDeliveryLogsModelTests(TestCase):
    def setUp(self):
        self.subscription = WebhookSubscriptionFactory(event_name="created")
        self.log = models.WebhookDeliveryLog.objects.create(
            subscription=self.subscription,
            payload={"key": "value"},
            delivery_url=self.subscription.endpoint,
        )

    def test_delivery_log_model_is_created_successfully(self):
        self.log.full_clean()
        self.assertIsNotNone(self.log.id)
        self.assertEqual(self.log.subscription, self.subscription)
        self.assertEqual(self.log.payload, {"key": "value"})
        self.assertIsNotNone(self.log.delivery_url, self.subscription.endpoint)
        # Asserting Default Values
        self.assertIsNone(self.log.response_status)
        self.assertEqual(self.log.response_body, "")
        self.assertEqual(self.log.response_headers, {})
        self.assertEqual(self.log.error_message, "")
        # Asserting Meta Fields
        self.assertIsNotNone(self.log.created_at)

    def test_delivery_log_model_str_representation(self):
        self.assertEqual(str(self.log), f"{self.subscription}")
        self.log.response_status = 200
        self.assertEqual(str(self.log), f"{self.subscription} (200)")
        self.log.is_retry = True
        self.log.attempt_number = 2
        self.assertEqual(str(self.log), f"{self.subscription} (200) (retry 2)")

    def test_delivery_log_model_uses_custom_manager(self):
        self.assertIsInstance(
            models.WebhookDeliveryLog.objects,
            managers.WebhookDeliveryLogManager,
        )

    def test_delivery_log_model_event_name_property(self):
        self.assertEqual(self.log.event_name, "created")

    def test_delivery_log_model_is_success_property(self):
        self.assertFalse(self.log.is_success)
        self.log.response_status = 200
        self.assertTrue(self.log.is_success)
        self.log.response_status = 404
        self.assertFalse(self.log.is_success)
        self.log.error_message = "Timeout"
        self.log.response_status = 200
        self.assertFalse(self.log.is_success)  # Exceptions are not successes

    def test_delivery_log_model_is_client_error_property(self):
        self.assertFalse(self.log.is_client_error)
        self.log.response_status = 404
        self.assertTrue(self.log.is_client_error)
        self.log.response_status = 500
        self.assertFalse(self.log.is_client_error)
        self.log.error_message = "Timeout"
        self.assertFalse(
            self.log.is_client_error
        )  # Exceptions are not client errors

    def test_delivery_log_model_is_server_error_property(self):
        self.assertFalse(self.log.is_server_error)
        self.log.response_status = 500
        self.assertTrue(self.log.is_server_error)
        self.log.response_status = 404
        self.assertFalse(self.log.is_server_error)
        self.log.error_message = "Timeout"
        self.assertFalse(
            self.log.is_server_error
        )  # Exceptions are not server errors


class ValidateClassPathValidatorTests(TestCase):
    def test_validate_class_path_on_valid_path(self):
        try:
            validators.validate_class_path(
                "rest_framework.serializers.ModelSerializer"
            )
        except ValidationError:
            self.fail(
                "validate_class_path raised ValidationError unexpectedly!"
            )

    def test_validate_class_path_on_empty_value(self):
        try:
            validators.validate_class_path("")
        except ValidationError:
            self.fail(
                "validate_class_path raised ValidationError unexpectedly!"
            )

    def test_validate_class_path_on_invalid_path(self):
        with self.assertRaises(ValidationError) as context:
            validators.validate_class_path("non.existent.ClassName")

        self.assertIn("Cannot import class from path", str(context.exception))

    def test_validate_class_path_on_non_serializer_class(self):
        with self.assertRaises(ValueError) as context:
            validators.validate_class_path(
                "django.core.validators.URLValidator"
            )

        self.assertIn(
            "field_serializer must be a subclass of",
            str(context.exception),
        )


class ValidateHeadersValidatorTests(TestCase):
    def test_validate_headers_on_valid_dict(self):
        try:
            validators.validate_headers(
                {
                    "Content-Type": "application/json",
                    "X-Custom-Header": "Value",
                    "X-Empty-Header": None,
                }
            )
        except ValidationError:
            self.fail("validate_headers raised ValidationError unexpectedly!")

    def test_validate_headers_on_empty_dict(self):
        try:
            validators.validate_headers({})
        except ValidationError:
            self.fail("validate_headers raised ValidationError unexpectedly!")

    def test_validate_headers_on_non_dict(self):
        with self.assertRaises(ValidationError) as context:
            validators.validate_headers(["Not", "a", "dict"])

        self.assertIn("Headers must be a dictionary", str(context.exception))

    def test_validate_headers_on_non_string_key(self):
        with self.assertRaises(ValidationError) as context:
            validators.validate_headers({123: "value"})

        self.assertIn(
            "Header key '123' must be a string", str(context.exception)
        )

    def test_validate_headers_on_non_string_value(self):
        with self.assertRaises(ValidationError) as context:
            validators.validate_headers({"X-Header": 456})

        self.assertIn(
            "Header value for 'X-Header' must be a string or None",
            str(context.exception),
        )

    def test_validate_headers_on_invalid_header_name_format(self):
        with self.assertRaises(ValidationError) as context:
            validators.validate_headers({"Invalid Header!": "value"})

        self.assertIn(
            "Invalid header name format: 'Invalid Header!'",
            str(context.exception),
        )
