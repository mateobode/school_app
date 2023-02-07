from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from backend.models.teacher import Teacher
from backend.serializers.teacher import TeacherSerializer, TeacherCourseSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    @action(detail=True)
    def get_courses(self, request, pk):
        teacher_instance = self.get_object()
        serializer = TeacherCourseSerializer(teacher_instance)
        return Response(serializer.data)
