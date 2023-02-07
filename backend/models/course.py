from django.db import models

from backend.models.student import Student
from backend.models.teacher import Teacher
from backend.utils import SEMESTERS


class Course(models.Model):
    name = models.CharField(max_length=50)
    teachers = models.ManyToManyField(Teacher, related_name='courses')
    students = models.ManyToManyField(Student, related_name='courses')
    semester = models.CharField(choices=SEMESTERS, max_length=10)

    def __str__(self):
        return self.name
