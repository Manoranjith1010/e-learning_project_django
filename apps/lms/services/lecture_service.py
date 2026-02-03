"""
Lecture service for managing course lectures and content
"""

from apps.lms.models.course import Course
from apps.lms.models.module import Module
from apps.lms.models.lesson import Lesson


class LectureService:
    """
    Service for managing lectures and course content
    """
    
    @staticmethod
    def get_course_content(course_id: int):
        """Get complete course structure with all modules and lessons"""
        try:
            course = Course.objects.get(id=course_id)
            modules = Module.objects.filter(course=course).prefetch_related('lessons')
            
            content = {
                'course': {
                    'id': course.id,
                    'title': course.title,
                    'description': course.description,
                },
                'modules': []
            }
            
            for module in modules:
                module_data = {
                    'id': module.id,
                    'title': module.title,
                    'description': module.description,
                    'lessons': []
                }
                
                for lesson in module.lessons.all():
                    lesson_data = {
                        'id': lesson.id,
                        'title': lesson.title,
                        'type': lesson.lesson_type,
                        'duration': lesson.video_duration,
                    }
                    module_data['lessons'].append(lesson_data)
                
                content['modules'].append(module_data)
            
            return content
        except Course.DoesNotExist:
            return None
    
    @staticmethod
    def create_course(instructor, title, slug, description, level, category, duration_weeks):
        """Create a new course"""
        course = Course.objects.create(
            instructor=instructor,
            title=title,
            slug=slug,
            description=description,
            level=level,
            category=category,
            duration_weeks=duration_weeks
        )
        return course
    
    @staticmethod
    def add_module_to_course(course_id, title, description, order):
        """Add module to course"""
        module = Module.objects.create(
            course_id=course_id,
            title=title,
            description=description,
            order=order
        )
        return module
    
    @staticmethod
    def add_lesson_to_module(module_id, title, lesson_type, order, content):
        """Add lesson to module"""
        lesson = Lesson.objects.create(
            module_id=module_id,
            title=title,
            lesson_type=lesson_type,
            order=order,
            content=content
        )
        return lesson
