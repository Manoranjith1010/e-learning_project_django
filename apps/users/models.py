"""
Models for the users app - Authentication & roles
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import URLValidator

class User(AbstractUser):
    """
    Custom User model supporting multiple roles (Student, Recruiter, Admin)
    """
    
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('recruiter', 'Recruiter'),
        ('admin', 'Admin'),
        ('instructor', 'Instructor'),
    )
    
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.email})"


class StudentProfile(models.Model):
    """
    Extended profile for Student users
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    enrollment_number = models.CharField(max_length=50, unique=True)
    college = models.CharField(max_length=255, blank=True)
    branch = models.CharField(max_length=100, blank=True)
    semester = models.IntegerField(default=1)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    github_url = models.URLField(blank=True, validators=[URLValidator()])
    linkedin_url = models.URLField(blank=True, validators=[URLValidator()])
    skills = models.JSONField(default=list, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    
    class Meta:
        db_table = 'student_profiles'
    
    def __str__(self):
        return f"Student Profile - {self.user.get_full_name()}"


class RecruiterProfile(models.Model):
    """
    Extended profile for Recruiter users
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruiter_profile')
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField()
    company_website = models.URLField(blank=True, validators=[URLValidator()])
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    phone = models.CharField(max_length=20)
    industry = models.CharField(max_length=100, blank=True)
    company_description = models.TextField(blank=True)
    employees_count = models.CharField(max_length=100, blank=True)
    is_verified = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'recruiter_profiles'
    
    def __str__(self):
        return f"Recruiter - {self.company_name}"


class AdminProfile(models.Model):
    """
    Extended profile for Admin users
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    department = models.CharField(max_length=100, blank=True)
    permissions = models.JSONField(default=dict, blank=True)
    
    class Meta:
        db_table = 'admin_profiles'
    
    def __str__(self):
        return f"Admin - {self.user.get_full_name()}"
