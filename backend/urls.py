from backend.views.student import StudentViewSet, StudentCourseViewSet, StudentAssignmentViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('students/', StudentViewSet.as_view({'get': 'list'}), name='students-list'),
    path('students/<int:pk>', StudentViewSet.as_view({'get': 'list'}), name='students-details'),
    path('students/<int:pk>/courses/', StudentCourseViewSet.as_view({'get': 'list'}), name='students-courses'),
    path('students/<int:pk>/courses/assignments/', StudentAssignmentViewSet.as_view({'get': 'list'})),
]

urlpatterns += router.urls
