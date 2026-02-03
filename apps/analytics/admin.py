"""
Admin configuration for analytics
"""

from django.contrib import admin
from .models import UserActivity, CourseAnalytics, StudentAnalytics


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'timestamp']
    list_filter = ['activity_type', 'timestamp']
    search_fields = ['user__username', 'activity_type']


@admin.register(CourseAnalytics)
class CourseAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'total_enrollments', 'total_completions', 'average_rating']
    search_fields = ['course_id']


@admin.register(StudentAnalytics)
class StudentAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['student', 'total_courses_enrolled', 'total_courses_completed', 'average_score']
    search_fields = ['student__username']
