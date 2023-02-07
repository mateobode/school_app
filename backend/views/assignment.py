from rest_framework import viewsets

from backend.models.assignment import Assignment
from backend.serializers.assignment import AssignmentSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
