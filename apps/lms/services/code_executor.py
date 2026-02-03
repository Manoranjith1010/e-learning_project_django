"""
Code executor service for running code exercises
"""

import subprocess
import json
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


class CodeExecutor:
    """
    Service to execute code and return results
    Supports Python, JavaScript, Java, C++
    """
    
    SUPPORTED_LANGUAGES = ['python', 'javascript', 'java', 'cpp']
    MAX_EXECUTION_TIME = 10  # seconds
    MAX_OUTPUT_SIZE = 50000  # characters
    
    @staticmethod
    def execute_code(code: str, language: str, input_data: str = '') -> Dict[str, Any]:
        """
        Execute code and return output
        """
        if language not in CodeExecutor.SUPPORTED_LANGUAGES:
            return {
                'success': False,
                'error': f'Language {language} not supported',
                'output': ''
            }
        
        try:
            if language == 'python':
                return CodeExecutor._execute_python(code, input_data)
            elif language == 'javascript':
                return CodeExecutor._execute_javascript(code, input_data)
            elif language == 'java':
                return CodeExecutor._execute_java(code, input_data)
            elif language == 'cpp':
                return CodeExecutor._execute_cpp(code, input_data)
        except Exception as e:
            logger.error(f'Code execution error: {str(e)}')
            return {
                'success': False,
                'error': str(e),
                'output': ''
            }
    
    @staticmethod
    def _execute_python(code: str, input_data: str) -> Dict[str, Any]:
        """Execute Python code"""
        try:
            result = subprocess.run(
                ['python', '-c', code],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=CodeExecutor.MAX_EXECUTION_TIME
            )
            output = result.stdout[:CodeExecutor.MAX_OUTPUT_SIZE]
            error = result.stderr[:CodeExecutor.MAX_OUTPUT_SIZE]
            
            return {
                'success': result.returncode == 0,
                'output': output,
                'error': error
            }
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': 'Execution timeout',
                'output': ''
            }
    
    @staticmethod
    def _execute_javascript(code: str, input_data: str) -> Dict[str, Any]:
        """Execute JavaScript code"""
        try:
            result = subprocess.run(
                ['node', '-e', code],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=CodeExecutor.MAX_EXECUTION_TIME
            )
            output = result.stdout[:CodeExecutor.MAX_OUTPUT_SIZE]
            error = result.stderr[:CodeExecutor.MAX_OUTPUT_SIZE]
            
            return {
                'success': result.returncode == 0,
                'output': output,
                'error': error
            }
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': 'Execution timeout',
                'output': ''
            }
    
    @staticmethod
    def _execute_java(code: str, input_data: str) -> Dict[str, Any]:
        """Execute Java code"""
        return {
            'success': False,
            'error': 'Java execution not yet implemented',
            'output': ''
        }
    
    @staticmethod
    def _execute_cpp(code: str, input_data: str) -> Dict[str, Any]:
        """Execute C++ code"""
        return {
            'success': False,
            'error': 'C++ execution not yet implemented',
            'output': ''
        }
