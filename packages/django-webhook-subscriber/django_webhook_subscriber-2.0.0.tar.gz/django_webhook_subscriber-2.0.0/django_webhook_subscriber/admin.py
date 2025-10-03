"""Updated Admin configuration for Django Webhook Subscriber."""

from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from .models import WebhookDeliveryLog, WebhookSubscriber, WebhookSubscription
from .delivery import clear_webhook_cache, get_webhook_cache_stats
from .tasks import test_webhook_connectivity, cleanup_webhook_logs


# Inline Admin Classes
class WebhookSubscriptionInline(admin.TabularInline):
    """Inline for managing subscriptions within subscriber admin."""

    model = WebhookSubscription
    extra = 1
    fields = [
        "event_name",
        "custom_endpoint",
        "is_active",
        "success_rate_display",
        "total_deliveries",
        "consecutive_failures",
    ]
    readonly_fields = ["success_rate_display"]

    def success_rate_display(self, obj):
        """Display success rate with color coding."""
        if obj.pk and obj.success_rate is not None:
            rate = obj.success_rate
            if rate >= 90:
                color = "green"
            elif rate >= 70:
                color = "orange"
            else:
                color = "red"
            return format_html(
                '<span style="color: {};">{:.1f}%</span>', color, rate
            )
        return "-"

    success_rate_display.short_description = _("Success Rate")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("subscriber")


class WebhookDeliveryLogInline(admin.StackedInline):
    """Inline for recent delivery logs."""

    model = WebhookDeliveryLog
    extra = 0
    max_num = 5  # Show last 5 deliveries
    fields = [
        "created_at",
        "response_status_display",
        "attempt_number",
        "delivery_duration_ms",
        "error_message_short",
    ]
    readonly_fields = [
        "created_at",
        "response_status_display",
        "attempt_number",
        "delivery_duration_ms",
        "error_message_short",
    ]
    can_delete = False
    ordering = ["-created_at"]

    def has_add_permission(self, request, obj=None):
        return False

    def response_status_display(self, obj):
        """Display response status with color coding."""
        if obj.response_status:
            if obj.is_success:
                return format_html(
                    '<span style="color: green;">✓ {}</span>',
                    obj.response_status,
                )
            elif obj.is_client_error:
                return format_html(
                    '<span style="color: orange;">⚠ {}</span>',
                    obj.response_status,
                )
            else:
                return format_html(
                    '<span style="color: red;">✗ {}</span>',
                    obj.response_status,
                )
        elif obj.error_message:
            return format_html('<span style="color: red;">✗ Exception</span>')
        return "?"

    response_status_display.short_description = _("Status")

    def error_message_short(self, obj):
        """Truncated error message for inline display."""
        if obj.error_message:
            return (
                obj.error_message[:100] + "..."
                if len(obj.error_message) > 100
                else obj.error_message
            )
        return "-"

    error_message_short.short_description = _("Error")


# Main Admin Classes
@admin.register(WebhookSubscriber)
class WebhookSubscriberAdmin(admin.ModelAdmin):
    """Enhanced admin interface for WebhookSubscriber."""

    list_display = [
        "name",
        "model_display",
        "target_url_display",
        "health_indicator",
        "subscriptions_count",
        "consecutive_failures",
        "last_activity_display",
        "created_at",
    ]
    list_display_links = ["name"]
    list_filter = [
        "is_active",
        "content_type",
        "consecutive_failures",
        "created_at",
        "last_success",
        "last_failure",
    ]
    search_fields = ["name", "description", "target_url"]
    readonly_fields = [
        "created_at",
        "updated_at",
        "last_success",
        "last_failure",
        "consecutive_failures",
        "model_class_display",
        "subscriptions_summary",
    ]

    fieldsets = (
        (
            _("Basic Information"),
            {"fields": ("name", "description", "content_type", "is_active")},
        ),
        (
            _("Endpoint Configuration"),
            {
                "fields": (
                    "target_url",
                    "secret",
                    "headers",
                    "serializer_class",
                ),
            },
        ),
        (
            _("Delivery Settings"),
            {
                "fields": (
                    "max_retries",
                    "retry_delay",
                    "timeout",
                    "auto_disable_after_failures",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            _("Status Information"),
            {
                "fields": (
                    "consecutive_failures",
                    "last_success",
                    "last_failure",
                    "model_class_display",
                    "subscriptions_summary",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            _("Metadata"),
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    inlines = [WebhookSubscriptionInline]
    actions = [
        "activate_subscribers",
        "deactivate_subscribers",
        "test_connectivity_action",
        "reset_failure_counters",
        "clear_cache_for_subscribers",
    ]

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related("content_type")
            .prefetch_related("subscriptions")
            .annotate(
                active_subscriptions_count=models.Count(
                    "subscriptions",
                    filter=models.Q(subscriptions__is_active=True),
                )
            )
        )

    def model_display(self, obj):
        """Display model information with app label."""
        return f"{obj.content_type.app_label}.{obj.content_type.model}"

    model_display.short_description = _("Model")
    model_display.admin_order_field = "content_type"

    def target_url_display(self, obj):
        """Display target URL with link."""
        if obj.target_url:
            return format_html(
                '<a href="{}" target="_blank" title="Open endpoint">{}</a>',
                obj.target_url,
                (
                    obj.target_url[:50] + "..."
                    if len(obj.target_url) > 50
                    else obj.target_url
                ),
            )
        return "-"

    target_url_display.short_description = _("Target URL")
    target_url_display.admin_order_field = "target_url"

    def health_indicator(self, obj):
        """Visual health indicator with status and failure count."""
        if not obj.is_active:
            return format_html('<span style="color: #999;">● Disabled</span>')

        # Health based on consecutive failures and recent activity
        if obj.consecutive_failures == 0:
            if obj.last_success:
                return format_html(
                    '<span style="color: green;">● Healthy</span>'
                )
            else:
                return format_html(
                    '<span style="color: orange;">● Untested</span>'
                )
        elif obj.consecutive_failures < 5:
            return format_html(
                '<span style="color: orange;">● Warning ({})</span>',
                obj.consecutive_failures,
            )
        else:
            return format_html(
                '<span style="color: red;">● Critical ({})</span>',
                obj.consecutive_failures,
            )

    health_indicator.short_description = _("Health")
    health_indicator.admin_order_field = "consecutive_failures"

    def subscriptions_count(self, obj):
        """Count of active subscriptions with link."""
        count = getattr(obj, "active_subscriptions_count", 0)
        if count > 0:
            url = reverse(
                "admin:django_webhook_subscriber_webhooksubscription_changelist"  # noqa: E501
            )
            return format_html(
                '<a href="{}?subscriber__id__exact={}">{}</a>',
                url,
                obj.pk,
                count,
            )
        return "0"

    subscriptions_count.short_description = _("Active Subscriptions")
    subscriptions_count.admin_order_field = "active_subscriptions_count"

    def last_activity_display(self, obj):
        """Display most recent activity (success or failure)."""
        last_activity = None
        activity_type = None

        if obj.last_success and obj.last_failure:
            if obj.last_success > obj.last_failure:
                last_activity = obj.last_success
                activity_type = "success"
            else:
                last_activity = obj.last_failure
                activity_type = "failure"
        elif obj.last_success:
            last_activity = obj.last_success
            activity_type = "success"
        elif obj.last_failure:
            last_activity = obj.last_failure
            activity_type = "failure"

        if last_activity:
            color = "green" if activity_type == "success" else "red"
            icon = "✓" if activity_type == "success" else "✗"
            return format_html(
                '<span style="color: {};" title="{}">{} {}</span>',
                color,
                last_activity.strftime("%Y-%m-%d %H:%M:%S"),
                icon,
                last_activity.strftime("%m/%d %H:%M"),
            )

        return format_html('<span style="color: #999;">No activity</span>')

    last_activity_display.short_description = _("Last Activity")

    def model_class_display(self, obj):
        """Display the actual model class information."""
        model_class = obj.model_class
        if model_class:
            return f"{model_class.__module__}.{model_class.__name__}"
        return "Model not found"

    model_class_display.short_description = _("Model Class")

    def subscriptions_summary(self, obj):
        """Summary of all subscriptions with success rates."""
        subscriptions = obj.subscriptions.all()
        if not subscriptions:
            return "No subscriptions"

        summary_lines = []
        for sub in subscriptions:
            status = "✓" if sub.is_active else "✗"
            rate = (
                f" ({sub.success_rate:.1f}%)"
                if sub.success_rate is not None
                else ""
            )
            summary_lines.append(f"{status} {sub.event_name}{rate}")

        return mark_safe("<br>".join(summary_lines))

    subscriptions_summary.short_description = _("Subscriptions Summary")

    # Custom Actions
    @admin.action(description=_("Activate selected subscribers"))
    def activate_subscribers(self, request, queryset):
        """Bulk activate subscribers."""
        updated = queryset.update(is_active=True)
        self.message_user(request, f"{updated} subscriber(s) activated.")

    @admin.action(description=_("Deactivate selected subscribers"))
    def deactivate_subscribers(self, request, queryset):
        """Bulk deactivate subscribers."""
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} subscriber(s) deactivated.")

    @admin.action(description=_("Test endpoint connectivity"))
    def test_connectivity_action(self, request, queryset):
        """Test connectivity to subscriber endpoints."""
        subscriber_ids = list(queryset.values_list("id", flat=True))

        # Queue the test task
        result = test_webhook_connectivity.delay(subscriber_ids)

        self.message_user(
            request,
            f"Connectivity test queued for {len(subscriber_ids)} "
            f"subscriber(s). Task ID: {result.id}",
            messages.INFO,
        )

    @admin.action(description=_("Reset failure counters"))
    def reset_failure_counters(self, request, queryset):
        """Reset consecutive failure counters."""
        updated = queryset.update(consecutive_failures=0)
        self.message_user(
            request, f"Reset failure counters for {updated} subscriber(s)."
        )

    @admin.action(description=_("Clear cache for selected subscribers"))
    def clear_cache_for_subscribers(self, request, queryset):
        """Clear cache for selected subscribers."""
        for subscriber in queryset:
            clear_webhook_cache(content_type=subscriber.content_type)

        self.message_user(
            request, f"Cache cleared for {queryset.count()} subscriber(s)."
        )


@admin.register(WebhookSubscription)
class WebhookSubscriptionAdmin(admin.ModelAdmin):
    """Admin interface for WebhookSubscription."""

    list_display = [
        "subscriber_name",
        "event_name",
        "endpoint_display",
        "status_indicator",
        "performance_display",
        "recent_deliveries",
        "created_at",
    ]
    list_display_links = ["subscriber_name", "event_name"]
    list_filter = [
        "is_active",
        "event_name",
        "subscriber__content_type",
        "subscriber__is_active",
        "consecutive_failures",
        "created_at",
    ]
    search_fields = [
        "subscriber__name",
        "event_name",
        "custom_endpoint",
        "subscriber__target_url",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
        "full_endpoint_display",
        "success_rate",
        "total_deliveries",
        "successful_deliveries",
        "consecutive_failures",
    ]

    fieldsets = (
        (
            _("Subscription Details"),
            {"fields": ("subscriber", "event_name", "is_active")},
        ),
        (
            _("Endpoint Configuration"),
            {
                "fields": ("custom_endpoint", "full_endpoint_display"),
            },
        ),
        (
            _("Performance Statistics"),
            {
                "fields": (
                    "success_rate",
                    "total_deliveries",
                    "successful_deliveries",
                    "consecutive_failures",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            _("Response Handling"),
            {
                "fields": ("keep_last_response", "last_response"),
                "classes": ("collapse",),
            },
        ),
        (
            _("Metadata"),
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    inlines = [WebhookDeliveryLogInline]
    actions = [
        "activate_subscriptions",
        "deactivate_subscriptions",
        "reset_subscription_stats",
        "clear_cache_action",
    ]

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related("subscriber", "subscriber__content_type")
            .prefetch_related("delivery_logs")
        )

    def subscriber_name(self, obj):
        """Display subscriber name with link."""
        url = reverse(
            "admin:django_webhook_subscriber_webhooksubscriber_change",
            args=[obj.subscriber.pk],
        )
        return format_html('<a href="{}">{}</a>', url, obj.subscriber.name)

    subscriber_name.short_description = _("Subscriber")
    subscriber_name.admin_order_field = "subscriber__name"

    def endpoint_display(self, obj):
        """Display the effective endpoint."""
        endpoint = obj.endpoint
        return format_html(
            '<a href="{}" target="_blank" title="Test endpoint">{}</a>',
            endpoint,
            endpoint[:40] + "..." if len(endpoint) > 40 else endpoint,
        )

    endpoint_display.short_description = _("Endpoint")

    def status_indicator(self, obj):
        """Visual status indicator."""
        if not obj.is_active:
            return format_html('<span style="color: #999;">● Disabled</span>')
        elif not obj.subscriber.is_active:
            return format_html(
                '<span style="color: orange;">● Subscriber Disabled</span>'
            )
        elif obj.consecutive_failures == 0:
            return format_html('<span style="color: green;">● Active</span>')
        elif obj.consecutive_failures < 3:
            return format_html('<span style="color: orange;">● Warning</span>')
        else:
            return format_html('<span style="color: red;">● Failing</span>')

    status_indicator.short_description = _("Status")

    def performance_display(self, obj):
        """Display performance metrics."""
        if obj.total_deliveries == 0:
            return format_html(
                '<span style="color: #999;">No deliveries</span>'
            )

        success_rate = obj.success_rate or 0
        if success_rate >= 95:
            color = "green"
        elif success_rate >= 80:
            color = "orange"
        else:
            color = "red"

        return format_html(
            '<span style="color: {};" title="{} successful / {} total">{}% '
            "({}/{})</span>",
            color,
            obj.successful_deliveries,
            obj.total_deliveries,
            success_rate,
            obj.successful_deliveries,
            obj.total_deliveries,
        )

    performance_display.short_description = _("Performance")

    def recent_deliveries(self, obj):
        """Show recent delivery status with timing."""
        recent_logs = obj.delivery_logs.order_by("-created_at")[:5]
        if not recent_logs:
            return format_html('<span style="color: #999;">None</span>')

        status_icons = []
        for log in recent_logs:
            if log.is_success:
                icon = "✅"
                title = f"Success ({log.response_status})"
            elif log.error_message:
                icon = "❌"
                title = f"Exception: {log.error_message[:50]}"
            elif log.response_status:
                if log.is_client_error:
                    icon = "⚠️"
                    title = f"Client Error ({log.response_status})"
                else:
                    icon = "❌"
                    title = f"Server Error ({log.response_status})"
            else:
                icon = "❓"
                title = "Unknown status"

            # Add timing info if available
            if log.delivery_duration_ms:
                title += f" - {log.delivery_duration_ms}ms"

            status_icons.append(f'<span title="{title}">{icon}</span>')

        return format_html(" ".join(status_icons))

    recent_deliveries.short_description = _("Recent Deliveries")

    def full_endpoint_display(self, obj):
        """Display the complete endpoint URL."""
        return obj.endpoint

    full_endpoint_display.short_description = _("Full Endpoint URL")

    # Custom Actions
    @admin.action(description=_("Activate selected subscriptions"))
    def activate_subscriptions(self, request, queryset):
        """Bulk activate subscriptions."""
        updated = queryset.update(is_active=True)
        self.message_user(request, f"{updated} subscription(s) activated.")

    @admin.action(description=_("Deactivate selected subscriptions"))
    def deactivate_subscriptions(self, request, queryset):
        """Bulk deactivate subscriptions."""
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} subscription(s) deactivated.")

    @admin.action(description=_("Reset performance statistics"))
    def reset_subscription_stats(self, request, queryset):
        """Reset performance statistics for subscriptions."""
        updated = queryset.update(
            consecutive_failures=0, total_deliveries=0, successful_deliveries=0
        )
        self.message_user(
            request, f"Reset statistics for {updated} subscription(s)."
        )

    @admin.action(description=_("Clear cache for selected subscriptions"))
    def clear_cache_action(self, request, queryset):
        """Clear cache for selected subscriptions."""
        for sub in queryset:
            clear_webhook_cache(
                content_type=sub.subscriber.content_type,
                event_name=sub.event_name,
            )
        self.message_user(
            request, f"Cache cleared for {queryset.count()} subscription(s)."
        )


@admin.register(WebhookDeliveryLog)
class WebhookDeliveryLogAdmin(admin.ModelAdmin):
    """Comprehensive admin interface for WebhookDeliveryLog."""

    list_display = [
        "__str__",
        "subscription_display",
        "event_name_display",
        "response_status_display",
        "performance_display",
        "created_at_display",
    ]
    list_display_links = ["__str__", "subscription_display"]
    list_filter = [
        "response_status",
        "subscription__event_name",
        "subscription__subscriber__content_type",
        "is_retry",
        "attempt_number",
        "created_at",
        ("delivery_duration_ms", admin.EmptyFieldListFilter),
    ]
    search_fields = [
        "subscription__subscriber__name",
        "subscription__event_name",
        "delivery_url",
        "error_message",
    ]
    readonly_fields = [
        "subscription",
        "attempt_number",
        "is_retry",
        "payload_display",
        "response_body_display",
        "response_headers_display",
        "error_message",
        "delivery_url",
        "delivery_duration_ms",
        "created_at",
    ]

    fieldsets = (
        (
            _("Delivery Information"),
            {
                "fields": (
                    "subscription",
                    "delivery_url",
                    "attempt_number",
                    "is_retry",
                    "delivery_duration_ms",
                    "created_at",
                )
            },
        ),
        (
            _("Request Data"),
            {
                "fields": ("payload_display",),
                "classes": ("collapse",),
            },
        ),
        (
            _("Response Data"),
            {
                "fields": (
                    "response_status",
                    "response_body_display",
                    "response_headers_display",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            _("Error Information"),
            {
                "fields": ("error_message",),
                "classes": ("collapse",),
            },
        ),
    )

    actions = ["cleanup_old_logs", "show_cache_stats"]
    date_hierarchy = "created_at"

    def has_add_permission(self, request):
        """Delivery logs are created automatically."""
        return False

    def has_change_permission(self, request, obj=None):
        """Delivery logs are read-only."""
        return False

    def subscription_display(self, obj):
        """Display subscription with link."""
        url = reverse(
            "admin:django_webhook_subscriber_webhooksubscription_change",
            args=[obj.subscription.pk],
        )
        return format_html(
            '<a href="{}">{} - {}</a>',
            url,
            obj.subscription.subscriber.name,
            obj.subscription.event_name,
        )

    subscription_display.short_description = _("Subscription")
    subscription_display.admin_order_field = "subscription__subscriber__name"

    def event_name_display(self, obj):
        """Display event name."""
        return obj.subscription.event_name

    event_name_display.short_description = _("Event")
    event_name_display.admin_order_field = "subscription__event_name"

    def response_status_display(self, obj):
        """Display response status with detailed color coding."""
        if obj.is_success:
            return format_html(
                '<span style="color: green; font-weight: bold;">✅ {} Success'
                "</span>",
                obj.response_status,
            )
        elif obj.error_message:
            return format_html(
                '<span style="color: red; font-weight: bold;">❌ Exception'
                "</span>"
            )
        elif obj.response_status:
            if obj.is_client_error:
                return format_html(
                    '<span style="color: orange; font-weight: bold;">⚠️ {} '
                    "Client Error</span>",
                    obj.response_status,
                )
            elif obj.is_server_error:
                return format_html(
                    '<span style="color: red; font-weight: bold;">❌ {} Server '
                    "Error</span>",
                    obj.response_status,
                )
            else:
                return format_html(
                    '<span style="color: purple;">❓ {} Unknown</span>',
                    obj.response_status,
                )
        else:
            return format_html(
                '<span style="color: #999;">❓ No Response</span>'
            )

    response_status_display.short_description = _("Status")
    response_status_display.admin_order_field = "response_status"

    def performance_display(self, obj):
        """Display performance metrics."""
        parts = []

        # Retry info
        if obj.is_retry:
            parts.append(f"Retry #{obj.attempt_number}")
        elif obj.attempt_number > 1:
            parts.append(f"Attempt #{obj.attempt_number}")

        # Duration
        if obj.delivery_duration_ms is not None:
            if obj.delivery_duration_ms < 1000:
                parts.append(f"{obj.delivery_duration_ms}ms")
            else:
                parts.append(f"{obj.delivery_duration_ms/1000:.1f}s")

        return " | ".join(parts) if parts else "-"

    performance_display.short_description = _("Performance")

    def created_at_display(self, obj):
        """Display creation time with relative info."""
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    created_at_display.short_description = _("Delivered At")
    created_at_display.admin_order_field = "created_at"

    def payload_display(self, obj):
        """Display formatted payload."""
        import json

        try:
            formatted = json.dumps(obj.payload, indent=2, ensure_ascii=False)
            return format_html(
                '<pre style="white-space: pre-wrap; max-height: 300px; '
                'overflow-y: auto; font-size: 12px;">{}</pre>',
                formatted,
            )
        except Exception:
            return str(obj.payload)

    payload_display.short_description = _("Payload")

    def response_body_display(self, obj):
        """Display formatted response body."""
        if obj.response_body:
            # Try to format as JSON if possible
            try:
                import json

                parsed = json.loads(obj.response_body)
                formatted = json.dumps(parsed, indent=2, ensure_ascii=False)
                content = formatted
            except (json.JSONDecodeError, TypeError):
                content = obj.response_body

            # Truncate if too long
            if len(content) > 3000:
                content = content[:3000] + "\n... [TRUNCATED]"

            return format_html(
                '<pre style="white-space: pre-wrap; max-height: 300px; '
                "overflow-y: auto; font-size: 12px; "
                'padding: 10px; border-radius: 4px;">{}</pre>',
                content,
            )
        return "-"

    response_body_display.short_description = _("Response Body")

    def response_headers_display(self, obj):
        """Display formatted response headers."""
        if obj.response_headers:
            import json

            try:
                formatted = json.dumps(
                    obj.response_headers, indent=2, ensure_ascii=False
                )
                return format_html(
                    '<pre style="white-space: pre-wrap; font-size: 12px;">{}'
                    "</pre>",
                    formatted,
                )
            except Exception:
                return str(obj.response_headers)
        return "-"

    response_headers_display.short_description = _("Response Headers")

    # Custom Actions
    @admin.action(description=_("Clean up old delivery logs"))
    def cleanup_old_logs(self, request, queryset):
        """Clean up old delivery logs."""
        result = cleanup_webhook_logs.delay()
        self.message_user(
            request,
            f"Log cleanup task queued. Task ID: {result.id}",
            messages.INFO,
        )

    @admin.action(description=_("Show webhook cache statistics"))
    def show_cache_stats(self, request, queryset):
        """Show cache statistics."""
        try:
            stats = get_webhook_cache_stats()
            message = (
                f"Cache Statistics: "
                f"{stats['cached_keys']}/{stats['total_possible_keys']} keys "
                f"cached ({stats['cache_hit_ratio']:.1f}% hit ratio), "
                f"{stats['total_cached_subscriptions']} total subscriptions "
                "cached"
            )
            self.message_user(request, message, messages.INFO)
        except Exception as e:
            self.message_user(
                request, f"Error getting cache stats: {e}", messages.ERROR
            )
