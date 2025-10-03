"""Serializers for Django Webhook Subscriber"""

from rest_framework.serializers import Serializer, ModelSerializer


def serialize_webhook_instance(instance, field_serializer=None):
    """Default serializer for webhook events.

    This function receives an instance, and serializes all its fields into a
    dictionary using the provided serializer class. If the serializer class
    is not a subclass of Django REST Framework's Serializer, it raises a
    ValueError.
    """

    class DefaultWebhookSerializer(ModelSerializer):
        """Default serializer class for webhook events.

        This class is used to serialize all fields of a model instance into a
        dictionary format. It is a subclass of Django REST Framework's
        ModelSerializer.
        """

        class Meta:
            model = instance.__class__
            fields = "__all__"

    if field_serializer is None:
        field_serializer = DefaultWebhookSerializer

    # Check that the field_serializer is a rest_framework serializer
    if not issubclass(field_serializer, Serializer):
        raise ValueError(
            "field_serializer must be a subclass of rest_framework.Serializer"
        )

    # Create an instance of the serializer
    serializer = field_serializer(instance=instance)
    # Serialize the instance
    serialized_data = serializer.data
    # Return the serialized data
    return serialized_data
