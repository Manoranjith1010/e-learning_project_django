"""
Management command to list all users
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "List all users in the system"

    def add_arguments(self, parser):
        parser.add_argument(
            "--role",
            type=str,
            help="Filter users by role (student, instructor, admin, recruiter)",
        )

    def handle(self, *args, **options):
        role_filter = options.get("role")
        
        if role_filter:
            users = User.objects.filter(role=role_filter)
            self.stdout.write(f"Users with role '{role_filter}':")
        else:
            users = User.objects.all()
            self.stdout.write("All users:")
        
        for user in users:
            self.stdout.write(
                f"  - {user.username} ({user.email}) - Role: {user.role}"
            )
        
        self.stdout.write(
            self.style.SUCCESS(f"\nTotal: {users.count()} users")
        )
