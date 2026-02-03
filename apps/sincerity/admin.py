"""
Admin configuration for sincerity
"""

from django.contrib import admin
from .models import IntegrityCheck


@admin.register(IntegrityCheck)
class IntegrityCheckAdmin(admin.ModelAdmin):
    list_display = ['student', 'cheating_score', 'status', 'checked_at']
    list_filter = ['status', 'plagiarism_detected', 'checked_at']
    search_fields = ['student__username']
