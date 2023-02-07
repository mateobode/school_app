from rest_framework import viewsets

from backend.models import Course
from backend.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
