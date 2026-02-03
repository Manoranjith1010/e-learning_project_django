"""
Custom permission classes for API views
"""

from rest_framework import permissions


class IsStudent(permissions.BasePermission):
    """Allow only users with student role"""
    
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "student"
        )


class IsInstructor(permissions.BasePermission):
    """Allow only users with instructor role"""
    
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "instructor"
        )


class IsAdminUser(permissions.BasePermission):
    """Allow only admin users"""
    
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsOwner(permissions.BasePermission):
    """Allow only the owner of an object to access it"""
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class IsStudentOrReadOnly(permissions.BasePermission):
    """Allow students to read and write, others to read only"""
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "student"
        )
