"""Deliveries for Django Webhook Subscriber."""

import logging
from collections import defaultdict

from django.core.cache import cache
from django.utils import timezone
from django.utils.module_loading import import_string

from .conf import rest_webhook_settings as settings
from .serializers import serialize_webhook_instance
from .tasks import process_webhook_delivery_batch
from .utils import (
    clear_content_type_cache,
    get_content_type_id,
    webhooks_disabled,
)

logger = logging.getLogger(__name__)


class WebhookDeliveryProcessor:
    def __init__(self):
        self.cache_ttl = getattr(settings, "WEBHOOK_CACHE_TTL", 300)

    def send_webhook(self, instance, event_name, context=None, **kwargs):
        """Send webhooks for a given model instance and event."""

        try:
            # Check if webhooks are globally disabled
            if webhooks_disabled():
                logger.info(
                    "Webhooks are disabled, skipping delivery.",
                    extra={"instance": instance, "event_name": event_name},
                )
                return {"skipped": "Webhooks disabled"}

            # Get active subscriptions for this model and event
            subscriptions = self._get_subscriptions_cached(
                instance, event_name
            )

            if not subscriptions:
                logger.info(
                    "No subscriptions found, skipping delivery.",
                    extra={"instance": instance, "event_name": event_name},
                )
                return {"skipped": "No subscriptions"}

            # Optimize payload generation by grouping serializer
            subscription_groups = self._group_subscriptions_by_serializer(
                subscriptions
            )

            # Generate payloads for each serializer group
            for serializer_class, subs in subscription_groups.items():
                payload = self._generate_payload(
                    instance, event_name, serializer_class
                )

                # Assign payload to all subscriptions in this group
                for sub in subs:
                    sub["payload"] = payload

            # Deliver the webhooks
            result = self._deliver_webhooks(subscriptions)

            logger.info(
                f"Queued {len(subscriptions)} webhooks for {event_name}",
                extra={"instance": instance, "event_name": event_name},
            )

            return result

        except Exception as e:
            logger.error(
                f"Error sending webhook: {e=}",
                extra={"instance": instance, "event_name": event_name},
                exc_info=True,
            )
            return {"error": f"Error sending webhook: {e=}"}

    def _group_subscriptions_by_serializer(self, subscriptions):
        """Group subscriptions by their serializer class."""

        # Using defaultdict to avoid key errors
        groups = defaultdict(list)
        for sub in subscriptions:
            serializer_key = sub.get("serializer_class") or None
            groups[serializer_key].append(sub)

        return groups

    def _get_subscriptions_cached(self, instance, event_name):
        """Retrieve active subscriptions with optimized caching."""

        content_type_id = get_content_type_id(
            instance._meta.app_label,
            instance._meta.model_name,
        )

        if content_type_id is None:
            logger.error(
                f"Content type not found for {instance._meta.label}",
                extra={"instance": instance},
            )
            return []

        cache_key = f"webhook_subscriptions:{content_type_id}:{event_name}"

        # Try to get from cache
        subscriptions = cache.get(cache_key)

        if subscriptions is None:
            # Cache miss - fetch from database
            subscriptions = self._fetch_subscriptions_from_db(
                content_type_id, event_name
            )

            # Cache the result
            cache.set(cache_key, subscriptions, self.cache_ttl)

            logger.debug(
                f"Cached {len(subscriptions)} subscriptions for {cache_key} "
                "key"
            )
        else:
            logger.debug(
                f"Cache hit for {cache_key}: {len(subscriptions)} "
                "subscriptions"
            )

        return subscriptions

    def _fetch_subscriptions_from_db(self, content_type_id, event_name):
        """Fetch subscriptions from database with optimizations."""

        from .models import WebhookSubscription

        qs = (
            WebhookSubscription.objects.select_related("subscriber")
            .filter(
                is_active=True,
                event_name=event_name,
                subscriber__is_active=True,
                subscriber__content_type_id=content_type_id,
            )
            .only(
                # Only load fields we need
                "id",
                "custom_endpoint",
                "subscriber_id",
                "subscriber__target_url",
                "subscriber__serializer_class",
            )
        )

        # Converting to lightweight dict format for caching
        subscriptions = []
        for sub in qs:
            subscription_data = {
                "id": sub.id,
                "subscriber_id": sub.subscriber_id,
                "url": sub.endpoint,  # This property handles URL logic
                "serializer_class": sub.subscriber.serializer_class,
            }
            subscriptions.append(subscription_data)

        return subscriptions

    def _generate_payload(self, instance, event_name, serializer_class_path):
        """Generate webhook payload for a specific serializer."""

        try:
            serializer_class = None

            # Import serializer class if specified
            if serializer_class_path:
                serializer_class = import_string(serializer_class_path)

            # Serialize the instance
            fields_data = serialize_webhook_instance(
                instance, serializer_class
            )

            # Build standard payload structure
            payload = {
                "pk": instance.pk,
                "event_signal": event_name,
                "source": f"{instance._meta.app_label}."
                f"{instance._meta.model_name}",
                "timestamp": timezone.now().isoformat(),
                "fields": fields_data,
            }

            return payload

        except Exception as e:
            logger.error(
                f"Error generating payload: {e=}",
                extra={"instance": instance, "event_name": event_name},
                exc_info=True,
            )

            return {
                "pk": getattr(instance, "pk", None),
                "event_signal": event_name,
                "source": f"{instance._meta.app_label}."
                f"{instance._meta.model_name}",
                "timestamp": timezone.now().isoformat(),
                "error": f"Serialization failed: {e=}",
                "fields": {},
            }

    def _deliver_webhooks(self, subscriptions):
        """Deliver webhooks with batch processing and size limits."""

        if not subscriptions:
            return {"processed": 0}

        # Splitting large batches to avoid overwhelming Celery
        max_batch_size = getattr(settings, "MAX_BATCH_SIZE")

        if len(subscriptions) <= max_batch_size:
            # Single batch
            return self._process_single_batch(subscriptions)

        else:
            # Multiple batches
            return self._process_multiple_batches(
                subscriptions, max_batch_size
            )

    def _process_single_batch(self, subscriptions):
        """Process a single batch of webhook deliveries."""

        try:
            result = process_webhook_delivery_batch.delay(subscriptions)
            return {
                "processed": len(subscriptions),
                "batches": 1,
                "task_id": result.id,
            }

        except Exception as e:
            logger.error(f"Failed to queue webhook batch: {e=}", exc_info=True)
            return {"error": f"{e=}", "processed": 0}

    def _process_multiple_batches(self, subscriptions, batch_size):
        """Process multiple batches of webhook deliveries."""

        batches = []
        task_ids = []
        total_processed = 0

        # Splitting into chunks
        for i in range(0, len(subscriptions), batch_size):
            batch = subscriptions[i:i + batch_size]  # fmt: skip

            try:
                result = process_webhook_delivery_batch.delay(batch)
                batches.append({"size": len(batch), "task_id": result.id})
                task_ids.append(result.id)
                total_processed += len(batch)

            except Exception as e:
                logger.error(
                    f"Failed to queue webhook batch {i//batch_size + 1}: {e=}"
                )
                batches.append({"size": len(batch), "error": f"{e=}"})
        logger.info(
            f"Queued {len(batches)} batches for {total_processed} webhook "
            "deliveries"
        )

        return {
            "processed": total_processed,
            "batches": len(batches),
            "batch_details": batches,
            "task_ids": task_ids,
        }

    def clear_webhook_cache(self, content_type=None, event_name=None):
        """Clear cached webhook subscription data."""

        from .models import WebhookSubscription

        if content_type and event_name:
            # Clear specific cache key
            cache_key = f"webhook_subscriptions:{content_type.id}:{event_name}"
            cache.delete(cache_key)
            logger.debug(f"Cleared cache for {cache_key}")

        elif content_type:
            # Clear all cache keys for this content type
            event_names = (
                WebhookSubscription.objects.filter(
                    subscriber__content_type=content_type,
                )
                .values_list("event_name", flat=True)
                .distinct()
            )

            cleared_count = 0
            for event_name in event_names:
                cache_key = (
                    f"webhook_subscriptions:{content_type.id}:{event_name}"
                )
                cache.delete(cache_key)
                cleared_count += 1
            logger.debug(
                f"Cleared {cleared_count} cache keys for content type "
                f"{content_type}"
            )

        else:
            # Clear all webhook caches (use pattern-based deletion if
            # available)
            if hasattr(cache, "delete_pattern"):
                # Redis backend supports pattern deletion
                deleted = cache.delete_pattern("webhook_subscriptions:*")
                logger.debug(
                    f"Cleared {deleted} webhook cache keys using pattern"
                )
            else:
                # Fallback: clear entire cache
                cache.clear()
                logger.warning(
                    "Cleared entire cache (pattern deletion not supported)"
                )

    def get_cache_stats(self):
        """Get webhook cache statistics."""

        # Get all possible cache keys
        cache_keys = self._get_all_cache_keys()

        stats = {
            "total_possible_keys": len(cache_keys),
            "cached_keys": 0,
            "total_cached_subscriptions": 0,
            "cache_hit_ratio": 0.0,
            "key_details": [],
        }

        for key in cache_keys:
            cached_data = cache.get(key)

            key_info = {
                "key": key,
                "is_cached": cached_data is not None,
                "subscription_count": len(cached_data) if cached_data else 0,
            }

            if cached_data is not None:
                stats["cached_keys"] += 1
                stats["total_cached_subscriptions"] += len(cached_data)

            stats["key_details"].append(key_info)

        # Calculate hit ratio
        if stats["total_possible_keys"] > 0:
            stats["cache_hit_ratio"] = (
                stats["cached_keys"] / stats["total_possible_keys"]
            ) * 100

        return stats

    def _get_all_cache_keys(self):
        """Get all possible webhook cache keys."""

        # Query all unique content_type + event_name combinations
        from .models import WebhookSubscription

        combinations = WebhookSubscription.objects.values_list(
            "subscriber__content_type_id", "event_name"
        ).distinct()

        cache_keys = []
        for content_type_id, event_name in combinations:
            cache_key = f"webhook_subscriptions:{content_type_id}:{event_name}"
            cache_keys.append(cache_key)

        return cache_keys


# Global instance of the delivery processor
webhook_delivery_processor = WebhookDeliveryProcessor()


def send_webhooks(instance, event_name, context=None, **kwargs):
    """Send webhooks for a given model instance and event."""

    return webhook_delivery_processor.send_webhook(
        instance,
        event_name,
        context=context,
        **kwargs,
    )


def clear_webhook_cache(content_type=None, event_name=None):
    """Clear all cached data from the delivery process."""

    webhook_delivery_processor.clear_webhook_cache(
        content_type=content_type, event_name=event_name
    )
    # Clear cached data from get_content_type_id function
    clear_content_type_cache()


def get_webhook_cache_stats():
    """Get statistics about the webhook subscription cache."""

    return webhook_delivery_processor.get_cache_stats()


def warm_webhook_cache():
    """Pre-fill the webhook cache by loading all active subscription
    combinations."""

    processor = webhook_delivery_processor
    warmed_count = 0

    from django.contrib.contenttypes.models import ContentType

    from .models import WebhookSubscription

    # Get all unique combinations of active subscriptions
    combinations = (
        WebhookSubscription.objects.filter(
            is_active=True,
            subscriber__is_active=True,
        )
        .values_list("subscriber__content_type_id", "event_name")
        .distinct()
    )

    for content_type_id, event_name in combinations:
        try:

            content_type = ContentType.objects.get(id=content_type_id)
            model_class = content_type.model_class()

            if model_class:
                # Create a minimal dummy instance for cache warming
                dummy_instance = model_class()
                dummy_instance._meta = model_class._meta

                # This will populate the cache
                processor._get_subscriptions_cached(dummy_instance, event_name)
                warmed_count += 1

        except Exception as e:
            logger.warning(
                f"Could not warm cache for {content_type_id}:{event_name}: "
                f"{e=}"
            )

    logger.info(
        f"Warmed webhook cache for {warmed_count} subscription combinations"
    )
    return {"warmed": warmed_count}
