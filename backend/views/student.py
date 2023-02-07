from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from backend.models.student import Student
from backend.serializers.student import StudentSerializer, StudentCourseSerializer, StudentAssignmentSerializer
from school_app.permissions import HasStudentPermission


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, HasStudentPermission]

    @action(detail=True)
    def get_courses(self, request, pk):
        student_instance = self.get_object()
        serializer = StudentCourseSerializer(student_instance)
        return Response(serializer.data)

    @action(detail=True)
    def get_assignments(self, request, pk):
        student_instance = self.get_object()
        serializer = StudentAssignmentSerializer(student_instance)
        return Response(serializer.data)

    @action(detail=True)
    def get_progress(self, request, pk):
        student_instance = self.get_object()
        serializer = StudentAssignmentSerializer(student_instance)
        courses = serializer.instance.courses.all()
        student_grades = {}
        for course in courses:
            grades = serializer.instance.assignments.filter(course=course).values_list('grade', flat=True)
            grades = list(grade for grade in grades if grade is not None)
            student_grades[course.name] = len(grades)/3 * 100
        return Response(student_grades)

    @action(detail=True)
    def get_avg_grade(self, request, pk):
        student_instance = self.get_object()
        serializer = StudentAssignmentSerializer(student_instance)
        courses = serializer.instance.courses.all()
        student_grades = {}
        for course in courses:
            grades = serializer.instance.assignments.filter(course=course).values_list('grade', flat=True)
            grades = sum(grade for grade in grades if grade is not None)
            student_grades[course.name] = grades/3
        return Response(student_grades)
