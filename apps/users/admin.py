"""
Admin configuration for the users app
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, StudentProfile, RecruiterProfile, AdminProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'role', 'profile_picture', 'bio', 'date_of_birth', 'is_email_verified', 'is_phone_verified')}),
    )


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'enrollment_number', 'college', 'branch', 'cgpa']
    search_fields = ['user__username', 'enrollment_number', 'college']


@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'user', 'phone', 'is_verified']
    search_fields = ['company_name', 'user__username']


@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'department']
    search_fields = ['user__username', 'department']
