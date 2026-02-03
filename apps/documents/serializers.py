"""
Serializers for documents
"""

from rest_framework import serializers
from .models import Document, CourseResource


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'description', 'file', 'document_type', 'is_public', 'created_at']


class CourseResourceSerializer(serializers.ModelSerializer):
    document = DocumentSerializer(read_only=True)
    
    class Meta:
        model = CourseResource
        fields = ['id', 'course_id', 'document', 'order']
