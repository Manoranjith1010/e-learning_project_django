"""
Permission classes for the users app
"""

from rest_framework import permissions


class IsStudentOrReadOnly(permissions.BasePermission):
    """
    Permission to check if user is student or allow read-only access
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.role == 'student'


class IsRecruiterOrReadOnly(permissions.BasePermission):
    """
    Permission to check if user is recruiter or allow read-only access
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.role == 'recruiter'


class IsAdminUser(permissions.BasePermission):
    """
    Permission to check if user is admin
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and (request.user.role == 'admin' or request.user.is_staff)
