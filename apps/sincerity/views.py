"""
Views for sincerity/integrity checks
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import IntegrityCheck
from .serializers import IntegrityCheckSerializer


class IntegrityCheckViewSet(viewsets.ModelViewSet):
    serializer_class = IntegrityCheckSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return IntegrityCheck.objects.filter(student=self.request.user)
