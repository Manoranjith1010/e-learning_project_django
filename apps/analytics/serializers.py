"""
Serializers for analytics
"""

from rest_framework import serializers
from .models import UserActivity, CourseAnalytics, StudentAnalytics


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ['id', 'activity_type', 'description', 'timestamp']


class CourseAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAnalytics
        fields = ['course_id', 'total_enrollments', 'total_completions', 'average_rating', 'completion_rate']


class StudentAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnalytics
        fields = ['total_courses_enrolled', 'total_courses_completed', 'total_challenges_solved', 'average_score', 'total_learning_hours']
