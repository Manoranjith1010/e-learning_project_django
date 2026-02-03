"""
URL routing for sincerity app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IntegrityCheckViewSet

router = DefaultRouter()
router.register(r'integrity-checks', IntegrityCheckViewSet, basename='integrity-check')

urlpatterns = [
    path('', include(router.urls)),
]
