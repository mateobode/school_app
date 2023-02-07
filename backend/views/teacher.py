from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from backend.models.teacher import Teacher
from backend.serializers.teacher import TeacherSerializer, TeacherCourseSerializer
from school_app.permissions import HasTeacherPermission


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, HasTeacherPermission]

    @action(detail=True)
    def get_courses(self, request, pk):
        teacher_instance = self.get_object()
        serializer = TeacherCourseSerializer(teacher_instance)
        return Response(serializer.data)
