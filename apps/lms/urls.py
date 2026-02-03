"""
URL routing for LMS app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.course_views import CourseViewSet
from .views.lesson_views import LessonViewSet
from .views.practice_views import PracticeViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'practice', PracticeViewSet, basename='practice')

urlpatterns = [
    path('', include(router.urls)),
]
