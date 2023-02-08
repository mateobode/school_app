from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from backend.models.assignment import Assignment
from backend.serializers.assignment import AssignmentSerializer
from school_app.permissions import HasAssignmentPermission, HasTeacherPermission


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, HasAssignmentPermission]

    def get_queryset(self):
        if hasattr(self.request.user, "student"):
            return self.queryset.filter(student=self.request.user.student)
        elif hasattr(self.request.user, "teacher"):
            return self.queryset.filter(course__teachers=self.request.user.teacher)
