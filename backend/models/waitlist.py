from django.db import models
from backend.models.student import Student
from backend.models.course import Course


class WaitList(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="waitlisted_courses")
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="waitlisted_students")

    @classmethod
    def add_to_waitlist(cls, students, courses):
        waitlist_entry = cls.objects.get_or_create(students=students, courses=courses)
        return waitlist_entry
