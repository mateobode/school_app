from django.db import models

from backend.models.student import Student
from backend.models.course import Course


class Assignment(models.Model):
    description = models.CharField(max_length=250)
    student = models.ForeignKey(Student, related_name='assignments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE, null=True)
    grade = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    feedback = models.CharField(max_length=250, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.description

