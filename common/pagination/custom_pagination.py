"""
Custom pagination classes for API
"""

from rest_framework.pagination import PageNumberPagination
from common.constants import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE


class StandardResultsSetPagination(PageNumberPagination):
    """Standard pagination for API results"""
    
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = "page_size"
    page_size_query_description = "Number of results to return per page"
    max_page_size = MAX_PAGE_SIZE
    page_query_description = "A page number within the paginated result set"


class LargeResultsSetPagination(PageNumberPagination):
    """Large pagination for API results"""
    
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = MAX_PAGE_SIZE
