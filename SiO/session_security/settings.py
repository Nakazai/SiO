from django.conf import settings

__all__ = ['EXPIRE_AFTER', 'WARN_AFTER', 'PASSIVE_URLS']

EXPIRE_AFTER = getattr(settings, 'SESSION_SECURITY_EXPIRE_AFTER', 600)

WARN_AFTER = getattr(settings, 'SESSION_SECURITY_WARN_AFTER', 540)

PASSIVE_URLS = getattr(settings, 'SESSION_SECURITY_PASSIVE_URLS', [])

PASSIVE_URL_NAMES = getattr(settings, 'SESSION_SECURITY_PASSIVE_URL_NAMES', [])

expire_at_browser_close = getattr(
    settings,
    'SESSION_EXPIRE_AT_BROWSER_CLOSE',
    False
)
force_insecurity = getattr(
    settings,
    'SESSION_SECURITY_INSECURE',
    False
)

if not (expire_at_browser_close or force_insecurity):
    raise Exception(
        'Enable SESSION_EXPIRE_AT_BROWSER_CLOSE or SESSION_SECURITY_INSECURE'
    )
