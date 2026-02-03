"""
Custom decorators for views and functions
"""

import functools
import logging
from typing import Callable, List

from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


def rate_limit(calls: int, period: int):
    """
    Rate limiting decorator (calls per period in seconds)
    Requires Redis cache backend for production use
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Implementation would use cache backend
            return func(*args, **kwargs)
        return wrapper
    return decorator


def require_role(allowed_roles: List[str]):
    """
    Decorator to check user role before accessing view
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return JsonResponse(
                    {"error": "Authentication required"},
                    status=401,
                )
            
            if request.user.role not in allowed_roles:
                return JsonResponse(
                    {"error": "Insufficient permissions"},
                    status=403,
                )
            
            return func(request, *args, **kwargs)
        return wrapper
    return decorator


def handle_exceptions(func: Callable) -> Callable:
    """
    Decorator to handle common exceptions in views
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            logger.error(f"Error in {func.__name__}: {str(exc)}", exc_info=True)
            return JsonResponse(
                {"error": "An error occurred", "details": str(exc)},
                status=500,
            )
    return wrapper


def cache_view(timeout: int = 300):
    """
    Cache view response for specified timeout (in seconds)
    """
    return cache_page(timeout)
