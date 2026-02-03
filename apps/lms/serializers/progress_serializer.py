"""
Progress serializer
"""

from rest_framework import serializers
from apps.lms.models.progress import LessonProgress
from apps.lms.models.enrollment import Enrollment


class LessonProgressSerializer(serializers.ModelSerializer):
    lesson_title = serializers.CharField(source='lesson.title', read_only=True)
    
    class Meta:
        model = LessonProgress
        fields = ['id', 'lesson', 'lesson_title', 'is_completed', 'completion_date', 'time_spent_seconds', 'score']


class EnrollmentSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    
    class Meta:
        model = Enrollment
        fields = ['id', 'course', 'course_title', 'status', 'progress', 'completion_date', 'enrolled_at']
