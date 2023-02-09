from backend.views.assignment import AssignmentViewSet
from backend.views.course import CourseViewSet
from backend.views.student import StudentViewSet
from backend.views.teacher import TeacherViewSet
from backend.views.reports import export_student_grades

from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'assignments', AssignmentViewSet)

urlpatterns = [
    path('grade-report/', export_student_grades),
]

urlpatterns += router.urls
