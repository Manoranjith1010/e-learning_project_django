"""
Views for analytics
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserActivity, CourseAnalytics, StudentAnalytics
from .serializers import UserActivitySerializer, CourseAnalyticsSerializer, StudentAnalyticsSerializer


class UserActivityViewSet(viewsets.ModelViewSet):
    serializer_class = UserActivitySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return UserActivity.objects.filter(user=self.request.user)


class CourseAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = CourseAnalytics.objects.all()
    serializer_class = CourseAnalyticsSerializer
    permission_classes = [IsAuthenticated]


class StudentAnalyticsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentAnalyticsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return StudentAnalytics.objects.filter(student=self.request.user)
