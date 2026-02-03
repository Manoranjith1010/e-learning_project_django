"""
URL routing for documents app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, CourseResourceViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'course-resources', CourseResourceViewSet, basename='course-resource')

urlpatterns = [
    path('', include(router.urls)),
]
