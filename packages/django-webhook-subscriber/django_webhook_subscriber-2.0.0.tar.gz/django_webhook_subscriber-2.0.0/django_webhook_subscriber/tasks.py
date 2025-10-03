"""Tasks for Django Webhook Subscriber."""

import logging
import time
from datetime import timedelta

import requests
from celery import group, shared_task
from django.utils import timezone

from .conf import rest_webhook_settings
from .http import webhook_session
from .utils import generate_headers

logger = logging.getLogger(__name__)


# =============================================================================
# Webhook delivery task with retry logic
# =============================================================================


@shared_task(bind=True)
def deliver_webhook(self, url, payload, subscription_id, attempt=1, **kwargs):
    """Deliver a webhook with proper retry logic and error handling."""

    from .models import WebhookDeliveryLog, WebhookSubscription

    # Load subscription with error handling
    try:
        subscription = WebhookSubscription.objects.select_related(
            "subscriber"
        ).get(id=subscription_id)

    except WebhookSubscription.DoesNotExist:
        logger.error(f"Subscription {subscription_id} not found")
        return {"error": "Subscription not found"}

    # Check if subscription is still active
    if not subscription.is_active or not subscription.subscriber.is_active:
        logger.info(
            f"Skipping delivery for inactive subscription {subscription_id}"
        )
        return {"skipped": "Subscription inactive"}

    start_time = time.time()

    # Create delivery log entry
    log = WebhookDeliveryLog.objects.create(
        subscription=subscription,
        payload=payload,
        delivery_url=url,
        attempt_number=attempt,
        is_retry=bool(attempt > 1),
    )

    try:
        with webhook_session() as session:
            # Generate headers for this specific request
            headers = generate_headers(subscription.subscriber)

            # Make the HTTP request
            response = session.post(
                url,
                json=payload,
                headers=headers,
                timeout=subscription.subscriber.timeout,
            )

            # Calculate delivery duration
            delivery_duration = int((time.time() - start_time) * 1000)

            # Update log with response data
            log.response_status = response.status_code
            log.response_body = response.text[:10240]  # Limit size
            log.response_headers = dict(response.headers)
            log.delivery_duration_ms = delivery_duration
            log.save()

            # Determine if delivery was successful
            is_success = 200 <= response.status_code < 300

            subscription.record_delivery_attempt(
                success=is_success,
                response_text=response.content,
            )

            # Update subscriber stats
            if is_success:
                subscription.subscriber.record_success()
                logger.info(
                    f"Webhook delivered successfully to {url} "
                    f"(attempt {attempt}, {delivery_duration}ms)"
                )
                return {
                    "success": True,
                    "status_code": response.status_code,
                    "duration_ms": delivery_duration,
                    "attempt": attempt,
                }

            else:
                # Handle HTTP error responses
                subscription.subscriber.record_failure()
                logger.warning(
                    f"Webhook delivery failed: {response.status_code} "
                    f"for {url} (attempt {attempt})"
                )

                should_retry = _should_retry_delivery(
                    subscription, attempt, response.status_code
                )

                if should_retry:
                    _schedule_retry(url, payload, subscription_id, attempt)

                return {
                    "success": False,
                    "status_code": response.status_code,
                    "duration_ms": delivery_duration,
                    "attempt": attempt,
                    "will_retry": should_retry,
                }
    except requests.exceptions.Timeout as e:
        error_msg = f"Timeout after {subscription.subscriber.timeout}s"
        _handle_delivery_exception(
            log, subscription, error_msg, url, payload, attempt
        )
        return {"error": f"Timeout error: {e=}", "attempt": attempt}

    except requests.exceptions.ConnectionError as e:
        error_msg = f"Connection error: {e=}"
        _handle_delivery_exception(
            log, subscription, error_msg, url, payload, attempt
        )
        return {"error": f"Connection error: {e=}", "attempt": attempt}

    except Exception as e:
        error_msg = f"Unexpected error: {e=}"
        _handle_delivery_exception(
            log, subscription, error_msg, url, payload, attempt
        )

        logger.error(
            f"Unexpected error delivering webhook: {e=}",
            exc_info=True,
        )
        return {"error": f"Unexpected error: {e=}", "attempt": attempt}


def _should_retry_delivery(subscription, attempt, status_code=None):
    """Determine if a delivery should be retried."""

    # Don't retry if max attempts reached
    if attempt >= subscription.subscriber.max_retries + 1:
        return False

    # Don't retry client errors (4xx) - these won't succeed on retry
    if status_code and 400 <= status_code < 500:
        logger.info(f"Not retrying client error {status_code}")
        return False

    # Retry server errors (5xx) and network issues
    return True


def _schedule_retry(url, payload, subscription_id, current_attempt):
    """Schedule a retry for a failed delivery."""

    from .models import WebhookSubscription

    try:
        subscription = WebhookSubscription.objects.get(id=subscription_id)
        retry_delay = subscription.subscriber.retry_delay
        next_attempt = current_attempt + 1

        logger.info(
            f"Scheduling retry {next_attempt} for subscription "
            f"{subscription_id} in {retry_delay} seconds"
        )

        deliver_webhook.apply_async(
            args=(url, payload, subscription_id),
            kwargs={"attempt": next_attempt},
            countdown=retry_delay,
        )

    except Exception as e:
        logger.error(f"Failed to schedule retry: {e=}")


def _handle_delivery_exception(
    log, subscription, error_msg, url, payload, attempt
):
    """Handle exceptions during delivery."""

    # Update log with error details
    log.error_message = error_msg
    log.save()

    # Update subscription and subscriber
    subscription.record_delivery_attempt(success=False)
    subscription.subscriber.record_failure()

    logger.error(f"Webhook delivery error: {error_msg}")

    # schedule retry if appropriate
    should_retry = _should_retry_delivery(subscription, attempt)
    if should_retry:
        _schedule_retry(url, payload, subscription.id, attempt)


# =============================================================================
# Batch processing task
# =============================================================================


@shared_task
def process_webhook_delivery_batch(subscriptions):
    if not subscriptions:
        logger.warning("Empty subscription batch received")
        return {"processed": 0, "error": "Empty batch"}

    try:
        batch_size = len(subscriptions)
        batch_id = f"batch_{timezone.now().strftime('%Y%m%d_%H%M%S')}"

        logger.info(
            f"Processing webhook batch {batch_id} with {batch_size} deliveries"
        )

        # Validate subscriptions before processing
        valid_subscriptions = []
        for sub in subscriptions:
            if _validate_subscription_data(sub):
                valid_subscriptions.append(sub)

            else:
                logger.warning(f"Invalid subscription data: {sub}")

        if not valid_subscriptions:
            logger.error("No valid subscriptions in batch")
            return {"processed": 0, "error": "No valid subscriptions"}

        # Create delivery tasks
        delivery_tasks = []
        for sub in valid_subscriptions:
            delivery_tasks.append(
                deliver_webhook.s(
                    url=sub["url"],
                    payload=sub["payload"],
                    subscription_id=sub["id"],
                )
            )

        # Execute tasks in parallel with error handling
        job = group(delivery_tasks)
        result = job.apply_async()

        logger.info(
            f"Batch {batch_id} queued successfully with {len(delivery_tasks)} "
            "tasks"
        )

        return {
            "batch_id": batch_id,
            "processed": len(delivery_tasks),
            "total_requested": batch_size,
            "task_ids": (
                [task.id for task in delivery_tasks]
                if hasattr(result, "children")
                else []
            ),
        }

    except Exception as e:
        logger.error(
            f"Error processing webhook delivery batch: {e=}", exc_info=True
        )
        return {"processed": 0, "error": f"{e=}"}


def _validate_subscription_data(subscription):
    """Validate subscription data before processing."""

    required_fields = ["id", "url", "payload"]
    for field in required_fields:
        if field not in subscription:
            logger.warning(
                f"Missing required field '{field}' in subscription data"
            )
            return False

    return True


# =============================================================================
# Cleanup and maintenance tasks
# =============================================================================


@shared_task
def cleanup_webhook_logs(subscription_id=None, days=None):
    """Cleanup old webhook delivery logs."""
    from .models import WebhookDeliveryLog

    try:
        # Get retention period
        retention_days = days or rest_webhook_settings.LOG_RETENTION_DAYS
        cutoff_date = timezone.now() - timedelta(days=retention_days)

        # Build query
        query = WebhookDeliveryLog.objects.filter(created_at__lt=cutoff_date)

        if subscription_id:
            query = query.filter(subscription_id=subscription_id)

        # Count before deletion
        count = query.count()

        if count == 0:
            logger.info("No old webhook logs to clean up")
            return {"deleted": 0, "cutoff_date": cutoff_date.isoformat()}

        # Delete in batches to avoid memory issues
        batch_size = 1000
        total_deleted = 0

        while True:
            batch_ids = list(query.values_list("id", flat=True)[:batch_size])
            if not batch_ids:
                break

            deleted_count = WebhookDeliveryLog.objects.filter(
                id__in=batch_ids
            ).delete()[0]
            total_deleted += deleted_count

            logger.info(
                f"Deleted {deleted_count} webhook logs (total: "
                f"{total_deleted})"
            )

        return {
            "deleted": total_deleted,
            "cutoff_date": cutoff_date.isoformat(),
            "retention_days": retention_days,
        }

    except Exception as e:
        logger.error(f"Error during webhook log cleanup: {e=}", exc_info=True)
        return {"error": f"{e=}"}


@shared_task
def test_webhook_connectivity(subscriber_ids=None):
    """Test connectivity to webhook endpoints."""

    from .models import WebhookSubscriber

    try:
        # Get subscribers to test
        query = WebhookSubscriber.objects.filter(is_active=True)
        if subscriber_ids:
            query = query.filter(id__in=subscriber_ids)

        subscribers = list(query)

        if not subscribers:
            return {
                "tested": 0,
                "results": [],
                "error": "No active subscribers found",
            }

        results = []

        with webhook_session() as session:
            for subscriber in subscribers:
                result = _test_single_endpoint(session, subscriber)
                results.append(result)

            success_count = sum(1 for r in results if r["success"])

            logger.info(
                "Connectivity test completed: "
                f"{success_count}/{len(subscribers)} successful"
            )

            return {
                "tested": len(results),
                "successful": success_count,
                "successful_responses": sum(
                    1
                    for r in results
                    if r["success"]
                    and r["status_code"]
                    and 200 <= r["status_code"] < 300
                ),
                "failed": len(results) - success_count,
                "results": results,
            }
    except Exception as e:
        logger.error(f"Error during connectivity test: {e=}", exc_info=True)
        return {"error": f"{e=}"}


def _test_single_endpoint(session, subscriber):
    """Test connectivity to a single subscriber endpoint."""

    start_time = time.time()

    try:
        # Use HEAD request for testing (less intrusive)
        headers = generate_headers(subscriber)

        response = session.head(
            subscriber.target_url,
            headers=headers,
            timeout=min(subscriber.timeout, 10),
        )

        duration_ms = int((time.time() - start_time) * 1000)

        return {
            "subscriber_id": subscriber.id,
            "subscriber_name": subscriber.name,
            "url": subscriber.target_url,
            "success": True,
            "status_code": response.status_code,
            "duration_ms": duration_ms,
            "error": None,
        }

    except Exception as e:
        duration_ms = int((time.time() - start_time) * 1000)

        logger.error(
            f"Error testing webhook endpoint {subscriber.id}: {e=}",
            exc_info=True,
        )

        return {
            "subscriber_id": subscriber.id,
            "subscriber_name": subscriber.name,
            "url": subscriber.target_url,
            "success": False,
            "status_code": None,
            "duration_ms": duration_ms,
            "error": f"{e=}",
        }
