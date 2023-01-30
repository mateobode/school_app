from rest_framework import viewsets

from backend.models.assignment import Assignment
from backend.models.student import Student
from backend.serializers.assignment import AssignmentSerializer
from backend.serializers.student import StudentSerializer, StudentCourseSerializer, StudentAssignmentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCourseViewSet(viewsets.ModelViewSet):
    serializer_class = StudentCourseSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        students = Student.objects.filter(pk=pk)

        for student in students:
            courses_student = student.courses.filter()

        return courses_student


class StudentAssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentAssignmentSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        students = Student.objects.filter(pk=pk)

        for student in students:
            student_assignment = student.assignments.filter()

        return student_assignment
