"""
WebSocket routing configuration for eduhire project (optional).
"""

from django.urls import re_path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

# WebSocket URL patterns would go here
websocket_urlpatterns = [
    # Example: re_path(r'ws/notifications/', NotificationConsumer.as_asgi()),
]

# Optional: If using Django Channels
# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': URLRouter(websocket_urlpatterns),
# })
