"""
Admin configuration for LMS app
"""

from django.contrib import admin
from .models.course import Course
from .models.module import Module
from .models.lesson import Lesson
from .models.enrollment import Enrollment
from .models.progress import LessonProgress


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'level', 'status', 'students_count', 'rating']
    list_filter = ['level', 'status', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'is_published']
    list_filter = ['course', 'is_published']
    search_fields = ['title', 'course__title']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'lesson_type', 'order', 'is_published']
    list_filter = ['lesson_type', 'is_published', 'module__course']
    search_fields = ['title', 'module__title']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'status', 'progress', 'enrolled_at']
    list_filter = ['status', 'enrolled_at', 'course']
    search_fields = ['student__username', 'course__title']


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ['student', 'lesson', 'is_completed', 'score', 'time_spent_seconds']
    list_filter = ['is_completed', 'started_at']
    search_fields = ['student__username', 'lesson__title']
