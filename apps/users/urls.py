"""
URL routing for the users app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentProfileViewSet, RecruiterProfileViewSet, AdminProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'student-profiles', StudentProfileViewSet)
router.register(r'recruiter-profiles', RecruiterProfileViewSet)
router.register(r'admin-profiles', AdminProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
