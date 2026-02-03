"""
Models for analytics and tracking
"""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserActivity(models.Model):
    """
    Track user activity on platform
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    course_id = models.IntegerField(null=True, blank=True)
    lesson_id = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'user_activities'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"


class CourseAnalytics(models.Model):
    """
    Analytics for courses
    """
    course_id = models.IntegerField(unique=True)
    total_enrollments = models.IntegerField(default=0)
    total_completions = models.IntegerField(default=0)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    completion_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'course_analytics'
    
    def __str__(self):
        return f"Analytics - Course {self.course_id}"


class StudentAnalytics(models.Model):
    """
    Analytics for individual students
    """
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name='analytics')
    total_courses_enrolled = models.IntegerField(default=0)
    total_courses_completed = models.IntegerField(default=0)
    total_challenges_solved = models.IntegerField(default=0)
    average_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_learning_hours = models.FloatField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'student_analytics'
    
    def __str__(self):
        return f"Analytics - {self.student.username}"
