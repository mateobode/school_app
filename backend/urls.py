from backend.views.assignment import AssignmentViewSet
from backend.views.course import CourseViewSet
from backend.views.student import StudentViewSet
from backend.views.teacher import TeacherViewSet
from backend.views.adminportal import AdminViewSet
from backend.views.reports import export_student_grades, get_course_avg

from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
admin_router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
router.register(r'teachers', TeacherViewSet, basename='teachers')
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'assignments', AssignmentViewSet, basename='assignments')
router.register(r'admin-portal', AdminViewSet, basename='admin-portal')

urlpatterns = [
    path('grade-report/', export_student_grades),
    path('course-report/', get_course_avg),
]

urlpatterns += router.urls
