"""
Models for coding challenges and exercises
"""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CodeChallenge(models.Model):
    """
    Coding challenge for students to solve
    """
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    problem_statement = models.TextField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    category = models.CharField(max_length=100)
    test_cases = models.JSONField(default=list)
    time_limit = models.IntegerField(default=5)  # seconds
    memory_limit = models.IntegerField(default=256)  # MB
    editorial = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'code_challenges'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class ChallengeSubmission(models.Model):
    """
    Student submission for a coding challenge
    """
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('wrong_answer', 'Wrong Answer'),
        ('runtime_error', 'Runtime Error'),
        ('time_limit', 'Time Limit Exceeded'),
    )
    
    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('cpp', 'C++'),
    )
    
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='challenge_submissions')
    challenge = models.ForeignKey(CodeChallenge, on_delete=models.CASCADE, related_name='submissions')
    code = models.TextField()
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    output = models.TextField(blank=True)
    error_message = models.TextField(blank=True)
    execution_time = models.FloatField(null=True, blank=True)  # seconds
    memory_used = models.FloatField(null=True, blank=True)  # MB
    test_cases_passed = models.IntegerField(default=0)
    total_test_cases = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'challenge_submissions'
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"{self.student.username} - {self.challenge.title}"
