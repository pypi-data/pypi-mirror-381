from copy import deepcopy

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

DEFAULTS = {
    "LOG_RETENTION_DAYS": 30,  # Number of days to keep logs
    "AUTO_CLEANUP": True,  # Automatically clean up old logs
    "WEBHOOK_CACHE_TTL": 300,  # Cache TTL for webhook configurations
    "MAX_BATCH_SIZE": 100,  # Max number of webhooks to send in a single batch
}

USER_SETTINGS = getattr(settings, "WEBHOOK_SUBSCRIBER", {})


# Merge user settings with defaults
class Settings:
    def __init__(self, user_settings, defaults):
        self._user_settings = user_settings
        self._defaults = defaults

    def __getattr__(self, attr):
        if attr not in self._defaults:
            raise AttributeError(f"Invalid setting: '{attr}'")

        val = self._user_settings.get(attr, deepcopy(self._defaults[attr]))

        if attr in [
            "LOG_RETENTION_DAYS",
            "WEBHOOK_CACHE_TTL",
            "MAX_BATCH_SIZE",
        ]:
            if not isinstance(val, int) or val <= 0:
                raise ImproperlyConfigured(
                    f"Invalid value for '{attr}': {val}. It should be a "
                    "positive integer."
                )

        return val


# Lazy loading of settings
# This allows settings to be accessed without importing them directly
# from the settings module. This is useful for testing and other
# scenarios where the settings module may not be available.
class LazySettings:
    def __getattr__(self, attr):
        from django.conf import settings

        user_settings = getattr(settings, "WEBHOOK_SUBSCRIBER", {})
        _settings = Settings(user_settings, DEFAULTS)
        return getattr(_settings, attr)


rest_webhook_settings = LazySettings()
