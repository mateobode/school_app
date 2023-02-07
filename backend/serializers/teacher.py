import json

from rest_framework import serializers

from backend.models.student import Student
from backend.models.course import Course
from backend.models.teacher import Teacher
from backend.serializers.course import CourseSerializer
from backend.serializers.student import StudentSerializer


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherCourseSerializer(serializers.Serializer):
    courses = CourseSerializer(many=True, read_only=True)
