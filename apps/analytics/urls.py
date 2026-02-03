"""
URL routing for analytics app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserActivityViewSet, CourseAnalyticsViewSet, StudentAnalyticsViewSet

router = DefaultRouter()
router.register(r'user-activity', UserActivityViewSet, basename='user-activity')
router.register(r'course-analytics', CourseAnalyticsViewSet, basename='course-analytics')
router.register(r'student-analytics', StudentAnalyticsViewSet, basename='student-analytics')

urlpatterns = [
    path('', include(router.urls)),
]
