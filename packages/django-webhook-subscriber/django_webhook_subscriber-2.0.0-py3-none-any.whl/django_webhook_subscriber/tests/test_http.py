import requests
from requests.adapters import HTTPAdapter
from django.test import TestCase

from django_webhook_subscriber.http import webhook_session


class CreateWebhookSessionFunctionTests(TestCase):
    def test_webhook_session_context_manager(self):
        with webhook_session() as session:
            # Asserting session is a requests.Session instance
            self.assertIsInstance(session, requests.Session)

            # Asserting pool_connections and pool_maxsize
            adapter = session.get_adapter("http://")
            self.assertEqual(adapter._pool_connections, 2)
            self.assertEqual(adapter._pool_maxsize, 5)

            # Asserting max_retries is 0
            self.assertEqual(adapter.max_retries.total, 0)

            # Asserting default headers are set
            self.assertIn("User-Agent", session.headers)
            self.assertIn("Content-Type", session.headers)

            # Asserting adapter is mounted
            adapter = session.get_adapter("http://")
            self.assertIsNotNone(adapter)
            self.assertIsInstance(adapter, HTTPAdapter)
            adapter = session.get_adapter("https://")
            self.assertIsNotNone(adapter)
            self.assertIsInstance(adapter, HTTPAdapter)
