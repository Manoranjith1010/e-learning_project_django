"""
Middleware for logging HTTP requests
"""

import logging
import json
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest, HttpResponse

from common.utils.helpers import get_client_ip

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(MiddlewareMixin):
    """
    Middleware to log all HTTP requests and responses
    """

    def process_request(self, request: HttpRequest):
        """Log incoming request"""
        request._start_time = time.time()
        
        log_data = {
            "method": request.method,
            "path": request.path,
            "query_params": dict(request.GET),
            "client_ip": get_client_ip(request),
            "user": str(request.user) if request.user.is_authenticated else "Anonymous",
        }
        
        logger.info(f"Incoming request: {json.dumps(log_data)}")
        return None

    def process_response(self, request: HttpRequest, response: HttpResponse):
        """Log outgoing response"""
        if hasattr(request, "_start_time"):
            duration = time.time() - request._start_time
            
            log_data = {
                "method": request.method,
                "path": request.path,
                "status_code": response.status_code,
                "duration_ms": round(duration * 1000, 2),
            }
            
            logger.info(f"Response: {json.dumps(log_data)}")
        
        return response


import time
