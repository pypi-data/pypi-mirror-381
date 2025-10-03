from django.test import TestCase, override_settings

from django_webhook_subscriber import utils

from .factories import ContentTypeFactory, WebhookSubscriberFactory


class GenerateHeadersFunctionTests(TestCase):
    def setUp(self):
        self.subscriber = WebhookSubscriberFactory()

    def test_generate_headers_on_no_default_headers(self):
        headers = utils.generate_headers(self.subscriber)
        # Asserting both X-Secret and Content-Type headers are present
        self.assertIn("X-Secret", headers)
        self.assertIn("Content-Type", headers)
        self.assertEqual(headers["X-Secret"], self.subscriber.secret)
        self.assertEqual(headers["Content-Type"], "application/json")

    def test_generate_headers_on_custom_default_headers(self):
        self.subscriber.headers = {
            "Custom-Header": "Value",
            "Content-Type": "application/xml",
        }
        headers = utils.generate_headers(self.subscriber)
        # Asserting both X-Secret and Content-Type headers are present
        self.assertIn("X-Secret", headers)
        self.assertIn("Content-Type", headers)
        self.assertIn("Custom-Header", headers)
        self.assertEqual(headers["X-Secret"], self.subscriber.secret)
        self.assertEqual(headers["Content-Type"], "application/xml")
        self.assertEqual(headers["Custom-Header"], "Value")


class GenerateSecretFunctionTests(TestCase):
    def test_generate_secret_returns_uuid_string(self):
        secret = utils.generate_secret()
        self.assertIsInstance(secret, str)
        self.assertEqual(len(secret), 36)  # UUID string length


class WebhookDisableContextTests(TestCase):
    def test_webhook_disable_context_manager(self):
        # By default, webhooks should be enabled
        self.assertFalse(utils.webhooks_disabled())

        # Context manager should disable webhooks
        with utils.disable_webhooks():
            self.assertTrue(utils.webhooks_disabled())

            # Nested context managers should also work
            with utils.disable_webhooks():
                self.assertTrue(utils.webhooks_disabled())

            self.assertTrue(utils.webhooks_disabled())

        # After context manager, webhooks should be enabled again
        self.assertFalse(utils.webhooks_disabled())

    @override_settings(DISABLE_WEBHOOKS=True)
    def test_webhook_disable_context_manager_when_disabled_in_settings(self):
        # Webhooks should be disabled due to settings
        self.assertTrue(utils.webhooks_disabled())

        with utils.disable_webhooks():
            # Even inside the context manager, webhooks remain disabled
            self.assertTrue(utils.webhooks_disabled())

        self.assertTrue(utils.webhooks_disabled())


class ContentTypeCacheTests(TestCase):
    def setUp(self):
        self.content_type = ContentTypeFactory(
            app_label="test_app",
            model="testmodel",
        )
        # Clear cache to ensure fresh state
        utils.get_content_type_id.cache_clear()

    def test_get_content_type_id_caching(self):
        # First call should hit the database
        with self.assertNumQueries(1):
            ct_id_1 = utils.get_content_type_id("test_app", "testmodel")
            self.assertIsNotNone(ct_id_1)

        with self.assertNumQueries(0):
            # Second call should use the cache
            ct_id_2 = utils.get_content_type_id("test_app", "testmodel")
            self.assertEqual(ct_id_1, ct_id_2)

    def test_get_content_type_id_non_existent(self):
        with self.assertNumQueries(1):
            ct_id = utils.get_content_type_id(
                "nonexistent_app",
                "nonexistentmodel",
            )
            self.assertIsNone(ct_id)

    def test_clear_content_type_cache(self):
        with self.assertNumQueries(1):
            # First call should hit the database
            ct_id_1 = utils.get_content_type_id("test_app", "testmodel")
            self.assertIsNotNone(ct_id_1)

        # Clear the cache
        utils.clear_content_type_cache()

        # Next call should hit the database again (not cached)
        with self.assertNumQueries(1):
            ct_id_2 = utils.get_content_type_id("test_app", "testmodel")
            self.assertEqual(ct_id_1, ct_id_2)
