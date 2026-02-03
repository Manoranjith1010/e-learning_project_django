"""
Utility helper functions for common operations
"""

import secrets
import string
from typing import Any, Dict, Optional

from django.core.mail import send_mail
from django.conf import settings
from django.utils.text import slugify


def get_client_ip(request) -> str:
    """
    Get client IP address from request
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def generate_token(length: int = 32) -> str:
    """
    Generate a secure random token
    """
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def send_email(
    subject: str,
    message: str,
    recipient_list: list,
    html_message: Optional[str] = None,
    from_email: Optional[str] = None,
) -> int:
    """
    Send email with optional HTML content
    """
    if from_email is None:
        from_email = settings.DEFAULT_FROM_EMAIL

    return send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        html_message=html_message,
        fail_silently=False,
    )


def format_error_response(
    message: str,
    error_code: str,
    details: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Format error response consistently
    """
    response = {
        "success": False,
        "message": message,
        "error_code": error_code,
    }
    if details:
        response["details"] = details
    return response


def format_success_response(
    message: str,
    data: Optional[Any] = None,
    meta: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Format success response consistently
    """
    response = {
        "success": True,
        "message": message,
    }
    if data is not None:
        response["data"] = data
    if meta:
        response["meta"] = meta
    return response


def truncate_string(text: str, max_length: int = 100) -> str:
    """
    Truncate text to max length with ellipsis
    """
    if len(text) > max_length:
        return text[: max_length - 3] + "..."
    return text


def generate_slug(text: str, max_length: int = 100) -> str:
    """
    Generate URL-safe slug from text
    """
    slug = slugify(text)
    if len(slug) > max_length:
        slug = slug[:max_length]
    return slug
