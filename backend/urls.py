from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from backend.views.assignment import AssignmentViewSet
from backend.views.course import CourseViewSet
from backend.views.student import StudentViewSet
from backend.views.teacher import TeacherViewSet
from backend.views.adminportal import AdminViewSet
from backend.views.reports import export_student_grades, get_course_avg

from rest_framework.routers import DefaultRouter
from django.urls import path

from backend.views.upcoming_students import upcoming_students_csv
from backend.views.waitlist import add_to_waitlist

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
    path('register-waitlist/', add_to_waitlist),
    path('upcoming-students/', upcoming_students_csv),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += router.urls
