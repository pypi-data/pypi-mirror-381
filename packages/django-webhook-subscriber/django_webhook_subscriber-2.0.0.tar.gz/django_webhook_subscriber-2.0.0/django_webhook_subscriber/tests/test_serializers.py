from django.test import TestCase
from rest_framework import serializers

from django_webhook_subscriber import models
from django_webhook_subscriber.serializers import serialize_webhook_instance

from .factories import WebhookDeliveryLogFactory


class SerializersTests(TestCase):
    def setUp(self):
        # creating instance to be serialized
        self.instance = WebhookDeliveryLogFactory()

    def test_default_serialization(self):
        # serializing the user instance
        data = serialize_webhook_instance(self.instance)

        # Check that fields are correct
        self.assertEqual(data["id"], self.instance.id)
        self.assertEqual(data["payload"], self.instance.payload)
        self.assertEqual(data["subscription"], self.instance.subscription.id)

    def test_serialization_with_custom_serializer(self):
        class CustomSerializer(serializers.ModelSerializer):
            class Meta:
                model = models.WebhookDeliveryLog
                fields = ["id", "payload"]

        # Test with DRF serializer
        data = serialize_webhook_instance(
            self.instance,
            field_serializer=CustomSerializer,
        )

        # Check the fields are correct
        self.assertEqual(data["id"], self.instance.id)
        self.assertEqual(data["payload"], self.instance.payload)
        self.assertNotIn("subscription", data)

    def test_serialization_with_invalid_serializer(self):
        class InvalidSerializer:
            pass

        # Test with invalid serializer
        msg = (
            "field_serializer must be a subclass of rest_framework.Serializer"
        )
        with self.assertRaisesMessage(ValueError, msg):
            serialize_webhook_instance(
                self.instance,
                field_serializer=InvalidSerializer,
            )
