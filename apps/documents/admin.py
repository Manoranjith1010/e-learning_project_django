"""
Admin configuration for documents
"""

from django.contrib import admin
from .models import Document, CourseResource


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploader', 'document_type', 'is_public', 'created_at']
    list_filter = ['document_type', 'is_public', 'created_at']
    search_fields = ['title', 'uploader__username']


@admin.register(CourseResource)
class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'document', 'order']
    list_filter = ['course_id']
    search_fields = ['document__title']
