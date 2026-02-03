"""
Development settings for eduhire project.
"""

from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

# CORS Configuration for development
CORS_ALLOW_ALL_ORIGINS = True

# Email configuration for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Celery configuration for development
CELERY_TASK_ALWAYS_EAGER = True  # Execute tasks synchronously in development

# Disable some security features for development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
