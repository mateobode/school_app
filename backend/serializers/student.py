from rest_framework import serializers

from backend.models.course import Course
from backend.models.student import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentCourseSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['student', 'name']
