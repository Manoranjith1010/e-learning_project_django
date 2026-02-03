"""
Custom validation functions
"""

import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value):
    """Validate phone number format"""
    pattern = r"^\+?1?\d{9,15}$"
    if not re.match(pattern, value.replace(" ", "").replace("-", "")):
        raise ValidationError(
            _("Please enter a valid phone number."),
            code="invalid_phone_number",
        )


def validate_image_size(file_obj, max_size_mb=5):
    """Validate image file size"""
    max_size = max_size_mb * 1024 * 1024
    if file_obj.size > max_size:
        raise ValidationError(
            _(f"Image size should not exceed {max_size_mb}MB."),
            code="image_too_large",
        )


def validate_video_format(file_obj):
    """Validate video file format"""
    allowed_formats = ["mp4", "avi", "mov", "mkv", "webm"]
    file_ext = file_obj.name.split(".")[-1].lower()
    
    if file_ext not in allowed_formats:
        raise ValidationError(
            _(f"Video format should be one of {', '.join(allowed_formats)}."),
            code="invalid_video_format",
        )
