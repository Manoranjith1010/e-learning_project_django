"""
Admin configuration for assessments
"""

from django.contrib import admin
from .models import Quiz, Question, QuizAttempt


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'total_questions', 'passing_score', 'created_at']
    search_fields = ['title', 'description']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'question_type', 'order']
    list_filter = ['quiz', 'question_type']
    search_fields = ['question_text']


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ['student', 'quiz', 'score', 'is_passed', 'completed_at']
    list_filter = ['is_passed', 'completed_at']
    search_fields = ['student__username', 'quiz__title']
