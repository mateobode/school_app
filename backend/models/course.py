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

    def get_avg_grade(self, student):
        grades = student.assignments.filter(course=self).values_list('grade', flat=True)
        grades = sum(grade for grade in grades if grade is not None)
        return grades/30

    def get_progress(self, student):
        grades = student.assignments.filter(course=self).values_list('grade', flat=True)
        grades = list(grade for grade in grades if grade is not None)
        percentage = str((len(grades)/3)*100)
        return percentage+'%'
