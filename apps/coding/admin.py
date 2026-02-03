"""
Admin configuration for coding app
"""

from django.contrib import admin
from .models import CodeChallenge, ChallengeSubmission


@admin.register(CodeChallenge)
class CodeChallengeAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'category', 'created_at']
    list_filter = ['difficulty', 'category']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ChallengeSubmission)
class ChallengeSubmissionAdmin(admin.ModelAdmin):
    list_display = ['student', 'challenge', 'status', 'test_cases_passed', 'submitted_at']
    list_filter = ['status', 'language', 'submitted_at']
    search_fields = ['student__username', 'challenge__title']
