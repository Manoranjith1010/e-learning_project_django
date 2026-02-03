"""
WSGI config for eduhire project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduhire.settings.dev')

application = get_wsgi_application()
