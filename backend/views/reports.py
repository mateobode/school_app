from django.http import HttpResponse
from rest_framework.decorators import api_view
import pandas as pd
from backend.models.assignment import Assignment


@api_view(['get'])
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
