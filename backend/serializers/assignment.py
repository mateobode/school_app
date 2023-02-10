import datetime
from datetime import date
from rest_framework import serializers

from backend.models.assignment import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        exclude = ('student',)


class AssignmentDeadlineSerializer(serializers.ModelSerializer):
    deadline = serializers.SerializerMethodField()

    class Meta:
        model = Assignment
        fields = ['id', 'start_date', 'end_date', 'deadline']

    def get_deadline(self, obj):
        deadline = obj.end_date - date.today()
        return deadline.days


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['file']