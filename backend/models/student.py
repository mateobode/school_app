from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    student_user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
