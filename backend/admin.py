from django.contrib import admin
from backend.models.course import Course
from backend.models.student import Student
from backend.models.teacher import Teacher
from backend.models.assignment import Assignment

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Assignment)
