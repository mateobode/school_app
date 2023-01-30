from rest_framework import viewsets
from backend.models.student import Student
from backend.serializers.student import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

