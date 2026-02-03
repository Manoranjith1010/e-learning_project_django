"""
Views for documents
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Document, CourseResource
from .serializers import DocumentSerializer, CourseResourceSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Document.objects.filter(models.Q(uploader=self.request.user) | models.Q(is_public=True))
        return Document.objects.filter(is_public=True)
    
    def perform_create(self, serializer):
        serializer.save(uploader=self.request.user)


class CourseResourceViewSet(viewsets.ModelViewSet):
    queryset = CourseResource.objects.all()
    serializer_class = CourseResourceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
