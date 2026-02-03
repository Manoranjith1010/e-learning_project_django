"""
URL routing for coding app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CodeChallengeViewSet, ChallengeSubmissionViewSet

router = DefaultRouter()
router.register(r'challenges', CodeChallengeViewSet, basename='challenge')
router.register(r'submissions', ChallengeSubmissionViewSet, basename='submission')

urlpatterns = [
    path('', include(router.urls)),
]
