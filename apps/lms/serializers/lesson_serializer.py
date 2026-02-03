"""
Lesson serializer
"""

from rest_framework import serializers
from apps.lms.models.lesson import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'lesson_type', 'order', 'content', 'video_url', 'video_duration', 'is_published', 'created_at', 'updated_at']
