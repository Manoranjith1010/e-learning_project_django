"""
Lesson views
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.lms.models.lesson import Lesson
from apps.lms.serializers.lesson_serializer import LessonSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
