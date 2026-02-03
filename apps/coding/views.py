"""
Views for coding challenges
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import CodeChallenge, ChallengeSubmission
from .serializers import CodeChallengeSerializer, ChallengeSubmissionSerializer


class CodeChallengeViewSet(viewsets.ModelViewSet):
    queryset = CodeChallenge.objects.all()
    serializer_class = CodeChallengeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


class ChallengeSubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = ChallengeSubmissionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return ChallengeSubmission.objects.filter(student=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
