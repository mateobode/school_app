from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from backend.models.assignment import Assignment
from backend.serializers.assignment import AssignmentSerializer, FileSerializer
from school_app.permissions import HasAssignmentPermission


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, HasAssignmentPermission]

    def get_queryset(self):
        if hasattr(self.request.user, "student"):
            return self.queryset.filter(student=self.request.user.student)
        elif hasattr(self.request.user, "teacher"):
            return self.queryset.filter(course__teachers=self.request.user.teacher)

    @action(detail=True, methods=['put'])
    def submit_assignment(self, request, pk):
        assignment = self.get_object()
        serializer = FileSerializer(instance=assignment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # student_instance.assignments.add(*serializer.data["file"])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)