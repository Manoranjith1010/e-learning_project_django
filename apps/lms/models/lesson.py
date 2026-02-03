"""
Lesson model for LMS - represents individual lessons within a module
"""

from django.db import models
from .module import Module


class Lesson(models.Model):
    """
    Individual lesson within a module
    """
    LESSON_TYPE_CHOICES = (
        ('video', 'Video'),
        ('text', 'Text'),
        ('quiz', 'Quiz'),
        ('assignment', 'Assignment'),
        ('code', 'Code Exercise'),
    )
    
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    lesson_type = models.CharField(max_length=20, choices=LESSON_TYPE_CHOICES)
    order = models.IntegerField()
    content = models.TextField()
    video_url = models.URLField(blank=True)
    video_duration = models.IntegerField(null=True, blank=True)  # in seconds
    attachment = models.FileField(upload_to='lesson_attachments/', null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'lessons'
        ordering = ['order']
        unique_together = ['module', 'order']
    
    def __str__(self):
        return f"{self.module.course.title} - {self.module.title} - {self.title}"
