from rest_framework.permissions import BasePermission, SAFE_METHODS

class HasStudentPermission(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS and hasattr(request.user, 'student')

    def has_object_permission(self, request, view, obj):
        return obj.pk == request.user.student.pk


class HasTeacherPermission(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS and hasattr(request.user, 'teacher')

    def has_object_permission(self, request, view, obj):
        return obj.pk == request.user.teacher.pk


class HasAssignmentPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS and (hasattr(request.user, 'teacher') or hasattr(request.user, 'student'))

    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, "teacher") and request.user.teacher in obj.course.teachers.all():
            return True

        if hasattr(request.user, "student") and request.user.student == obj.student:
            return True
        return False
