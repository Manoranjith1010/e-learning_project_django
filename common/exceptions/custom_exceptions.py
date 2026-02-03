"""
Custom exception classes for the application
"""

from rest_framework import status


class APIException(Exception):
    """Base exception for API"""
    
    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        error_code: str = "API_ERROR",
        details: dict = None,
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}
        super().__init__(self.message)


class ValidationError(APIException):
    """Raised when validation fails"""
    
    def __init__(self, message: str, error_code: str = "VALIDATION_ERROR", details: dict = None):
        super().__init__(
            message,
            status_code=status.HTTP_400_BAD_REQUEST,
            error_code=error_code,
            details=details,
        )


class NotFoundError(APIException):
    """Raised when resource is not found"""
    
    def __init__(self, message: str = "Resource not found", error_code: str = "NOT_FOUND"):
        super().__init__(
            message,
            status_code=status.HTTP_404_NOT_FOUND,
            error_code=error_code,
        )


class PermissionDeniedError(APIException):
    """Raised when user lacks permissions"""
    
    def __init__(self, message: str = "Permission denied", error_code: str = "PERMISSION_DENIED"):
        super().__init__(
            message,
            status_code=status.HTTP_403_FORBIDDEN,
            error_code=error_code,
        )


class ConflictError(APIException):
    """Raised when there's a conflict (e.g., duplicate entry)"""
    
    def __init__(self, message: str, error_code: str = "CONFLICT"):
        super().__init__(
            message,
            status_code=status.HTTP_409_CONFLICT,
            error_code=error_code,
        )


class RateLimitError(APIException):
    """Raised when rate limit is exceeded"""
    
    def __init__(self, message: str = "Rate limit exceeded", error_code: str = "RATE_LIMIT"):
        super().__init__(
            message,
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            error_code=error_code,
        )
