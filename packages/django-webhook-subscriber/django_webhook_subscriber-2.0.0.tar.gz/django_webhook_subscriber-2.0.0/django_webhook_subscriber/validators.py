"""Validators for Django Webhook Subscriber."""

from django.core.exceptions import ValidationError
from django.utils.module_loading import import_string
from rest_framework import serializers


def validate_class_path(value):
    """Validator to check if the class path points to a valid class."""

    # Allow empty values
    if not value:
        return

    try:
        serializer_class = import_string(value)
        # Check that the serializer_class is a rest_framework serializer
        if not issubclass(serializer_class, serializers.Serializer):
            raise ValueError(
                "field_serializer must be a subclass of "
                f"{serializers.Serializer}."
            )

    except ImportError as e:
        raise ValidationError(f"Cannot import class from path: {value}") from e
    except (TypeError, AttributeError) as e:
        # Handles cases where imported object is not a class
        raise ValidationError(
            f"Path '{value}' does not point to a valid class"
        ) from e


def validate_headers(value):
    """
    Validator to ensure headers is a dict with string keys and string values.
    """

    if not isinstance(value, dict):
        raise ValidationError("Headers must be a dictionary.")

    for key, val in value.items():
        if not isinstance(key, str):
            raise ValidationError(f"Header key '{key}' must be a string.")

        # Allow string or None values (some headers might be empty)
        if val is not None and not isinstance(val, str):
            raise ValidationError(
                f"Header value for '{key}' must be a string or None."
            )

        # Optional: validate header name format (HTTP spec)
        if not key.replace("-", "").replace("_", "").isalnum():
            raise ValidationError(f"Invalid header name format: '{key}'")
