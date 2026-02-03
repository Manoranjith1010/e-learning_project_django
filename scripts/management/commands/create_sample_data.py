"""
Management command to create sample data
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.lms.models import Course

User = get_user_model()


class Command(BaseCommand):
    help = "Create sample data for testing"

    def handle(self, *args, **options):
        self.stdout.write("Creating sample data...")
        
        # Create sample instructor
        instructor, created = User.objects.get_or_create(
            username="instructor1",
            defaults={
                "email": "instructor@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "role": "instructor",
            },
        )
        if created:
            instructor.set_password("password123")
            instructor.save()
            self.stdout.write(
                self.style.SUCCESS(f"✓ Created instructor: {instructor.username}")
            )
        
        # Create sample course
        course, created = Course.objects.get_or_create(
            slug="python-basics",
            defaults={
                "title": "Python Basics",
                "description": "Learn Python fundamentals",
                "instructor": instructor,
                "category": "Programming",
                "level": "beginner",
                "duration_weeks": 4,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"✓ Created course: {course.title}")
            )
        
        self.stdout.write(
            self.style.SUCCESS("✓ Sample data creation completed!")
        )
