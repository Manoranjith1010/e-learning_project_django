"""
Pytest configuration and fixtures
"""

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from tests.factories import (
    UserFactory,
    StudentUserFactory,
    InstructorUserFactory,
    AdminUserFactory,
)

User = get_user_model()


@pytest.fixture
def api_client():
    """Fixture for API client"""
    return APIClient()


@pytest.fixture
def user():
    """Fixture for creating a regular user"""
    return UserFactory()


@pytest.fixture
def student_user():
    """Fixture for creating a student user"""
    return StudentUserFactory()


@pytest.fixture
def instructor_user():
    """Fixture for creating an instructor user"""
    return InstructorUserFactory()


@pytest.fixture
def admin_user():
    """Fixture for creating an admin user"""
    return AdminUserFactory()


@pytest.fixture
def authenticated_client(api_client, user):
    """Fixture for authenticated API client"""
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def student_client(api_client, student_user):
    """Fixture for authenticated student API client"""
    api_client.force_authenticate(user=student_user)
    return api_client


@pytest.fixture
def instructor_client(api_client, instructor_user):
    """Fixture for authenticated instructor API client"""
    api_client.force_authenticate(user=instructor_user)
    return api_client


@pytest.fixture
def admin_client(api_client, admin_user):
    """Fixture for authenticated admin API client"""
    api_client.force_authenticate(user=admin_user)
    return api_client
