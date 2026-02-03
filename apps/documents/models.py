"""
Models for document management
"""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Document(models.Model):
    """
    Document model for storing course materials and resources
    """
    DOCUMENT_TYPE_CHOICES = (
        ('pdf', 'PDF'),
        ('doc', 'Document'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('other', 'Other'),
    )
    
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='documents/')
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES)
    file_size = models.BigIntegerField()  # in bytes
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'documents'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class CourseResource(models.Model):
    """
    Course resources/materials linked to courses
    """
    course_id = models.IntegerField()
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='course_resources')
    order = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'course_resources'
    
    def __str__(self):
        return f"{self.document.title} - Course {self.course_id}"
