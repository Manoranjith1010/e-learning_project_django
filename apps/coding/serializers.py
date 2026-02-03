"""
Serializers for coding challenges
"""

from rest_framework import serializers
from .models import CodeChallenge, ChallengeSubmission


class CodeChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeChallenge
        fields = ['id', 'title', 'slug', 'description', 'difficulty', 'category', 'created_at']


class ChallengeSubmissionSerializer(serializers.ModelSerializer):
    challenge_title = serializers.CharField(source='challenge.title', read_only=True)
    
    class Meta:
        model = ChallengeSubmission
        fields = ['id', 'challenge', 'challenge_title', 'code', 'language', 'status', 'test_cases_passed', 'total_test_cases', 'submitted_at']
