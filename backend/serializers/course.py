from rest_framework import serializers
from backend.models.student import Student
from backend.models.course import Course
from backend.models.teacher import Teacher


class CourseSerializer(serializers.ModelSerializer):

    students = serializers.SlugRelatedField(
        slug_field="first_name",
        queryset=Student.objects.all(),
        many=True
    )

    teachers = serializers.SlugRelatedField(
        slug_field="first_name",
        queryset=Teacher.objects.all(),
        many=True
    )

    class Meta:
        model = Course
        fields = "__all__"
