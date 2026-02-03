"""
Practice/Exercise views for code exercises
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.lms.services.code_executor import CodeExecutor


class PracticeViewSet(viewsets.ViewSet):
    """
    ViewSet for practice exercises and code execution
    """
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['post'])
    def execute_code(self, request):
        """Execute submitted code"""
        code = request.data.get('code', '')
        language = request.data.get('language', 'python')
        input_data = request.data.get('input', '')
        
        result = CodeExecutor.execute_code(code, language, input_data)
        return Response(result, status=status.HTTP_200_OK if result['success'] else status.HTTP_400_BAD_REQUEST)
