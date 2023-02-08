from rest_framework import serializers

from backend.models.course import Course
from backend.models.student import Student
from backend.serializers.assignment import AssignmentSerializer
from backend.serializers.course import CourseStudentSerializer


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentCourseSerializer(serializers.Serializer):
    courses = CourseStudentSerializer(many=True)


class StudentAssignmentSerializer(serializers.Serializer):
    assignments = AssignmentSerializer(many=True)


class RegisterCourseSerializer(serializers.Serializer):
    courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.filter(semester='second'), many=True)
