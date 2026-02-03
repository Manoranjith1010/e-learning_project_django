"""
Course serializer
"""

from rest_framework import serializers
from apps.lms.models.course import Course


class CourseListSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source='instructor.get_full_name', read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'description', 'category', 'level', 'thumbnail', 'price', 'instructor_name', 'students_count', 'rating']


class CourseDetailSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source='instructor.get_full_name', read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'description', 'long_description', 'category', 'level', 'status', 'thumbnail', 'cover_image', 'price', 'duration_weeks', 'instructor_name', 'students_count', 'rating', 'tags', 'prerequisites', 'learning_outcomes', 'created_at', 'updated_at']
