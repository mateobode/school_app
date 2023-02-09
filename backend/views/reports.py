from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
import pandas as pd
from rest_framework.permissions import IsAdminUser

from backend.models.student import Student
from backend.models.assignment import Assignment


@api_view(['get'])
@permission_classes((IsAdminUser,))
def export_student_grades(request):

    if pk := request.GET.get('pk'):
        assignments = Assignment.objects.filter(student__pk=pk)
    else:
        assignments = Assignment.objects.all()

    data = []

    for assignment in assignments:
        data.append({
            "student": assignment.student.first_name,
            "description": assignment.description,
            "grade": assignment.grade
        })

    response = HttpResponse(pd.DataFrame(data).to_csv(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=grades_report.csv'
    return response


@api_view(['get'])
@permission_classes((IsAdminUser,))
def get_course_avg(request):
    students = Student.objects.all()
    student_grades = {}
    for student in students:
        student_grades[student.first_name]={}
        for course in student.courses.all():
            grades = Assignment.objects.filter(student=student, course=course).values_list("grade", flat=True)
            grades = sum(grade for grade in grades if grade is not None)
            student_grades[student.first_name][course.name] = grades/3

    response = HttpResponse(pd.DataFrame().from_dict(student_grades).to_csv(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=courses_average.csv'
    return response
