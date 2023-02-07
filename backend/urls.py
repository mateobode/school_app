from backend.views.assignment import AssignmentViewSet
from backend.views.course import CourseViewSet
from backend.views.student import StudentViewSet
from backend.views.teacher import TeacherViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'assignments', AssignmentViewSet)

urlpatterns = router.urls
