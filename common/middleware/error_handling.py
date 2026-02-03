"""
Middleware for handling errors
"""

import logging
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.conf import settings

from common.exceptions import APIException

logger = logging.getLogger(__name__)


class ErrorHandlingMiddleware(MiddlewareMixin):
    """
    Middleware to handle API exceptions and return consistent error responses
    """

    def process_exception(self, request, exception):
        """Handle exceptions and return JSON response"""
        
        if isinstance(exception, APIException):
            response_data = {
                "success": False,
                "message": exception.message,
                "error_code": exception.error_code,
            }
            
            if exception.details:
                response_data["details"] = exception.details
            
            logger.warning(
                f"API Exception: {exception.error_code} - {exception.message}",
                extra={"details": exception.details},
            )
            
            return JsonResponse(response_data, status=exception.status_code)
        
        # Log unexpected exceptions
        logger.error(
            f"Unexpected exception: {type(exception).__name__}",
            exc_info=True,
        )
        
        if settings.DEBUG:
            # In development, return detailed error info
            return JsonResponse(
                {
                    "success": False,
                    "message": str(exception),
                    "error_code": "INTERNAL_SERVER_ERROR",
                },
                status=500,
            )
        
        # In production, return generic error
        return JsonResponse(
            {
                "success": False,
                "message": "An error occurred",
                "error_code": "INTERNAL_SERVER_ERROR",
            },
            status=500,
        )
