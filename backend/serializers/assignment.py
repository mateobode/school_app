from rest_framework import serializers
from backend.models.student import Student
from backend.models.assignment import Assignment


class AssignmentSerializer(serializers.ModelSerializer):

    students = serializers.SlugRelatedField(
        slug_field="first_name",
        queryset=Student.objects.all(),
        many=True
    )

    class Meta:
        model = Assignment
        fields = "__all__"
