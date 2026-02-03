"""
Progress tracker service for tracking student progress
"""

from django.utils import timezone
from apps.lms.models.progress import LessonProgress
from apps.lms.models.enrollment import Enrollment


class ProgressTracker:
    """
    Service for tracking and updating student progress
    """
    
    @staticmethod
    def mark_lesson_complete(student, lesson):
        """Mark a lesson as completed"""
        progress, created = LessonProgress.objects.get_or_create(
            student=student,
            lesson=lesson
        )
        progress.is_completed = True
        progress.completion_date = timezone.now()
        progress.save()
        
        return progress
    
    @staticmethod
    def update_lesson_time(student, lesson, additional_seconds):
        """Update time spent on lesson"""
        progress, created = LessonProgress.objects.get_or_create(
            student=student,
            lesson=lesson
        )
        progress.time_spent_seconds += additional_seconds
        progress.save()
        
        return progress
    
    @staticmethod
    def get_course_progress(student, course):
        """Get student's overall progress in a course"""
        try:
            enrollment = Enrollment.objects.get(student=student, course=course)
            
            # Calculate completion percentage
            total_lessons = 0
            completed_lessons = 0
            
            for module in course.modules.all():
                for lesson in module.lessons.all():
                    total_lessons += 1
                    if LessonProgress.objects.filter(
                        student=student,
                        lesson=lesson,
                        is_completed=True
                    ).exists():
                        completed_lessons += 1
            
            progress_percentage = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
            
            enrollment.progress = progress_percentage
            enrollment.save()
            
            return {
                'completed_lessons': completed_lessons,
                'total_lessons': total_lessons,
                'progress_percentage': progress_percentage
            }
        except Enrollment.DoesNotExist:
            return None
    
    @staticmethod
    def get_lesson_progress(student, lesson):
        """Get student's progress on a specific lesson"""
        try:
            progress = LessonProgress.objects.get(student=student, lesson=lesson)
            return {
                'is_completed': progress.is_completed,
                'time_spent_seconds': progress.time_spent_seconds,
                'score': progress.score,
                'completion_date': progress.completion_date
            }
        except LessonProgress.DoesNotExist:
            return None
