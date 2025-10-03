"""Models for Django Webhook Subscriber."""

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import WebhookDeliveryLogManager
from .utils import generate_secret
from .validators import validate_class_path, validate_headers


class WebhookSubscriber(models.Model):
    """
    Represents an external service subscribing to receive webhooks from a
    specific model.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255, help_text=_("Name of this subscriber")
    )
    description = models.TextField(blank=True)

    # What model they're subscribing to
    content_type = models.ForeignKey(
        "contenttypes.ContentType",
        on_delete=models.CASCADE,
        help_text=_("The model this subscriber watches"),
    )

    # Endpoint configuration
    target_url = models.CharField(
        max_length=500,  # Increased length for long URLs
        help_text=_("The base URL for webhook delivery"),
    )
    secret = models.CharField(
        max_length=64,
        default=generate_secret,
        help_text=_(
            "Secret key for webhook authentication via X-Secret header"
        ),
    )

    serializer_class = models.CharField(
        max_length=512,
        blank=True,
        validators=[validate_class_path],
        help_text=_(
            "Dot path to DRF serializer class "
            "(e.g., 'myapp.serializers.MySerializer')"
        ),
    )

    # Headers and configuration
    headers = models.JSONField(
        default=dict,
        blank=True,
        validators=[validate_headers],
        help_text=_("Additional headers to send (JSON format)"),
    )

    # Delivery settings
    max_retries = models.PositiveIntegerField(
        default=3, help_text=_("Max delivery attempts")
    )
    retry_delay = models.PositiveIntegerField(
        default=60, help_text=_("Seconds between retries")
    )
    timeout = models.PositiveIntegerField(
        default=30, help_text=_("Request timeout in seconds")
    )

    # Auto-disable settings
    auto_disable_after_failures = models.PositiveIntegerField(
        default=10,
        help_text=_("Auto-disable after N consecutive failures (0 = never)"),
    )

    # Status tracking
    is_active = models.BooleanField(default=True)
    consecutive_failures = models.PositiveIntegerField(default=0)
    last_success = models.DateTimeField(null=True, blank=True)
    last_failure = models.DateTimeField(null=True, blank=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        db_table = "django_webhook_subscriber_webhook_subscriber"
        verbose_name = _("Webhook Subscriber")
        verbose_name_plural = _("Webhook Subscribers")
        unique_together = (("target_url", "content_type"),)
        indexes = [
            models.Index(fields=["content_type", "is_active"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["content_type"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.target_url})"

    def clean(self):
        """Additional validation."""
        super().clean()

        # Validate timeout is reasonable
        if self.timeout > 300:  # 5 minutes max
            raise ValidationError("timeout cannot exceed 300 seconds")

        # Validate retry settings
        if self.retry_delay > 3600:  # 1 hour max
            raise ValidationError("retry_delay cannot exceed 3600 seconds")

    @property
    def model_class(self):
        return self.content_type.model_class()

    @property
    def model_name(self):
        return f"{self.content_type.app_label}.{self.content_type.model}"

    def record_success(self):
        """Record a successful delivery."""
        from django.utils import timezone

        self.consecutive_failures = 0
        self.last_success = timezone.now()
        self.save(update_fields=["consecutive_failures", "last_success"])

    def record_failure(self):
        """Record a failed delivery and handle auto-disable."""

        self.consecutive_failures += 1
        self.last_failure = timezone.now()

        # Auto-disable if threshold reached
        if (
            self.auto_disable_after_failures > 0
            and self.consecutive_failures >= self.auto_disable_after_failures
        ):
            self.is_active = False

        self.save(
            update_fields=["consecutive_failures", "last_failure", "is_active"]
        )

    def save(self, *args, **kwargs):
        self.full_clean()  # Always validate
        super().save(*args, **kwargs)

        # Clear cache on save
        from .delivery import clear_webhook_cache

        clear_webhook_cache(content_type=self.content_type)


class WebhookSubscription(models.Model):
    """Individual event subscription for a subscriber."""

    id = models.AutoField(primary_key=True)
    subscriber = models.ForeignKey(
        WebhookSubscriber,
        on_delete=models.CASCADE,
        related_name="subscriptions",
        limit_choices_to=models.Q(is_active=True),
    )

    event_name = models.CharField(
        max_length=100,
        help_text=_("Event name (e.g., 'created', 'published', 'archived')"),
    )

    custom_endpoint = models.CharField(
        max_length=512,
        blank=True,
        help_text=_("Optional custom endpoint path or full URL"),
    )

    # Status
    is_active = models.BooleanField(default=True)

    # Response handling
    keep_last_response = models.BooleanField(
        default=True,
        help_text=_("Whether to store the last response received"),
    )
    last_response = models.TextField(
        blank=True,
        help_text=_("Last response received (truncated if too long)"),
    )
    last_success = models.DateTimeField(blank=True, null=True)
    last_failure = models.DateTimeField(blank=True, null=True)

    # Added tracking fields
    consecutive_failures = models.PositiveIntegerField(default=0)
    total_deliveries = models.PositiveIntegerField(default=0)
    successful_deliveries = models.PositiveIntegerField(default=0)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("subscriber__name", "event_name")
        db_table = "django_webhook_subscriber_subscription"
        verbose_name = _("Webhook Subscription")
        verbose_name_plural = _("Webhook Subscriptions")
        unique_together = (("subscriber", "event_name"),)
        indexes = [
            models.Index(fields=["subscriber", "event_name"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["subscriber", "is_active"]),
            models.Index(fields=["event_name", "is_active"]),
        ]

    def __str__(self):
        return f"{self.subscriber.name} - {self.event_name}"

    @property
    def endpoint(self):
        """Full URL endpoint for this subscription."""
        if not self.custom_endpoint:
            return self.subscriber.target_url

        # Check if custom_endpoint is a full URL
        if self.custom_endpoint.startswith(("http://", "https://")):
            return self.custom_endpoint

        # Join base URL with endpoint path
        base_url = self.subscriber.target_url.rstrip("/")
        endpoint = self.custom_endpoint.lstrip("/")
        return f"{base_url}/{endpoint}" if endpoint else base_url

    @property
    def success_rate(self):
        """Calculate success rate percentage."""
        if self.total_deliveries == 0:
            return None
        return (self.successful_deliveries / self.total_deliveries) * 100

    def record_delivery_attempt(self, success=False, response_text=None):
        """Record a delivery attempt."""

        self.total_deliveries += 1

        if success:
            self.successful_deliveries += 1
            self.consecutive_failures = 0
            self.last_success = timezone.now()
        else:
            self.consecutive_failures += 1
            self.last_failure = timezone.now()

        # Store response if requested and not too large
        if self.keep_last_response and response_text:
            self.last_response = response_text[:1024]  # Limit size

        self.save(
            update_fields=[
                "total_deliveries",
                "successful_deliveries",
                "consecutive_failures",
                "last_success",
                "last_failure",
                "last_response",
            ]
        )

    # Proxy properties for backward compatibility
    @property
    def model_name(self):
        return self.subscriber.model_name

    @property
    def content_type(self):
        return self.subscriber.content_type

    @property
    def serializer_class(self):
        return self.subscriber.serializer_class


class WebhookDeliveryLog(models.Model):
    """Log of webhook delivery attempts."""

    id = models.AutoField(primary_key=True)
    subscription = models.ForeignKey(
        WebhookSubscription,
        on_delete=models.CASCADE,
        related_name="delivery_logs",  # Better name
    )

    # Retry tracking
    attempt_number = models.PositiveSmallIntegerField(default=1)
    is_retry = models.BooleanField(default=False)

    # Payload and response data
    payload = models.JSONField(default=dict)
    response_status = models.PositiveIntegerField(null=True, blank=True)
    response_body = models.TextField(blank=True)
    response_headers = models.JSONField(default=dict, blank=True)

    # Error tracking
    error_message = models.TextField(blank=True)

    # Delivery metadata
    delivery_url = models.CharField(max_length=500)
    delivery_duration_ms = models.PositiveIntegerField(null=True, blank=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)

    # Manager
    objects = WebhookDeliveryLogManager()

    class Meta:
        ordering = ["-created_at"]
        db_table = "django_webhook_subscriber_webhook_delivery_log"
        verbose_name = _("Webhook Delivery Log")
        verbose_name_plural = _("Webhook Delivery Logs")
        indexes = [
            models.Index(fields=["subscription", "-created_at"]),
            models.Index(fields=["response_status"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["attempt_number"]),
        ]

    def __str__(self):
        status = f" ({self.response_status})" if self.response_status else ""
        retry_info = f" (retry {self.attempt_number})" if self.is_retry else ""
        return f"{self.subscription}{status}{retry_info}"

    @property
    def event_name(self):
        return self.subscription.event_name

    @property
    def is_success(self):
        """Check if delivery was successful."""

        # If there's an error message, it means an exception occurred
        if self.error_message:
            return False

        return self.response_status and 200 <= self.response_status < 300

    @property
    def is_client_error(self):
        """Check if error was client-side (4xx)."""
        return self.response_status and 400 <= self.response_status < 500

    @property
    def is_server_error(self):
        """Check if error was server-side (5xx)."""
        return self.response_status and 500 <= self.response_status < 600
