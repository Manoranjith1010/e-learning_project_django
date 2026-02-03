"""
Course views
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from apps.lms.models.course import Course
from apps.lms.models.enrollment import Enrollment
from apps.lms.serializers.course_serializer import CourseListSerializer, CourseDetailSerializer
from apps.lms.services.lecture_service import LectureService


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseListSerializer
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def enroll(self, request, slug=None):
        """Enroll student in course"""
        course = self.get_object()
        student = request.user
        
        enrollment, created = Enrollment.objects.get_or_create(
            student=student,
            course=course
        )
        
        if created:
            course.students_count += 1
            course.save()
            return Response({'message': 'Successfully enrolled in course'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Already enrolled in this course'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def content(self, request, slug=None):
        """Get complete course content structure"""
        course = self.get_object()
        content = LectureService.get_course_content(course.id)
        return Response(content)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_courses(self, request):
        """Get courses enrolled by current student"""
        enrollments = Enrollment.objects.filter(student=request.user).select_related('course')
        courses = [enrollment.course for enrollment in enrollments]
        serializer = CourseListSerializer(courses, many=True)
        return Response(serializer.data)
