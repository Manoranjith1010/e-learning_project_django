"""
Serializers for sincerity/integrity
"""

from rest_framework import serializers
from .models import IntegrityCheck


class IntegrityCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrityCheck
        fields = ['id', 'assessment_id', 'cheating_score', 'plagiarism_detected', 'ai_generated_probability', 'status']
