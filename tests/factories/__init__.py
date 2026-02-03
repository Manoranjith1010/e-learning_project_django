"""
Test factories for creating test objects
"""

import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(DjangoModelFactory):
    """Factory for creating test users"""
    
    class Meta:
        model = User
    
    username = factory.Sequence(lambda n: f"user_{n}")
    email = factory.Sequence(lambda n: f"user_{n}@example.com")
    first_name = "Test"
    last_name = "User"
    role = "student"
    is_active = True
    is_email_verified = True
    
    @factory.post_generation
    def password(obj, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            obj.set_password(extracted)
        else:
            obj.set_password("testpass123")
        obj.save()


class StudentUserFactory(UserFactory):
    """Factory for creating student users"""
    role = "student"


class InstructorUserFactory(UserFactory):
    """Factory for creating instructor users"""
    role = "instructor"


class AdminUserFactory(UserFactory):
    """Factory for creating admin users"""
    role = "admin"
    is_staff = True
    is_superuser = True
