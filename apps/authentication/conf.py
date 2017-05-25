from django.conf import settings
# Tiempo en días antes de expirar el registro temporal.
AUTH_REGISTER_EXPIRE_DAYS = getattr(settings, 'AUTH_REGISTER_EXPIRE_DAYS', 1)
