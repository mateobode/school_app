from rest_framework import serializers
from backend.models.student import Student
from backend.models.course import Course
from backend.models.teacher import Teacher
from backend.serializers.assignment import AssignmentSerializer
#from backend.serializers.student import StudentAssignmentSerializer


class CourseSerializer(serializers.ModelSerializer):

    students = serializers.SlugRelatedField(
        slug_field="first_name",
        queryset=Student.objects.all(),
        many=True
    )

    class Meta:
        model = Course
        fields = ['id', 'name', 'semester', 'students']


class CourseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'semester']
