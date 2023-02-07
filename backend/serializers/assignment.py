from rest_framework import serializers

from backend.models.assignment import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        exclude = ('student',)
