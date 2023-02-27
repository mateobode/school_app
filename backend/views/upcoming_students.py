import pandas as pd

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser


@api_view(['post'])
@permission_classes((IsAdminUser,))
def upcoming_students_csv(request):
    upcoming_students = request.FILES.get("new_students")
    upcoming_students_df = pd.read_csv(upcoming_students)
    filtered_df = upcoming_students_df.dropna(subset=["first_name"]).loc[upcoming_students_df["country"] != "Russia"]
    students_dict = filtered_df.to_dict(orient="records")

    return Response(students_dict, status=status.HTTP_200_OK)


"""
API example to import upcoming students through CSV file. Process CSV file to automatically
create student users and student record in the database.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.contrib.auth.models import User
from backend.models.student import Student


class StudentImportView(APIView):
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            
            upcoming_students = request.FILES['new_students']
            upcoming_students_df = pd.read_csv(upcoming_students)
            filtered_df = upcoming_students_df.dropna(
                subset=["first_name"]
            ).loc[
                upcoming_students_df["country"] != "Russia"
            ]
            
            student_data = df.to_dict(orient='records')

            for student in student_data:
                username = data['Email'].split('@')[0]
                user = User.objects.create_user(username=username, email=data['Email'])
                user.set_password('password')

                student = Student.objects.create(
                    student_user=user,
                    first_name=student['first_name'],
                    last_name=student['last_name'],
                    email=student['email'],
                    gender=student['gender'],
                    birth_date=student['birth_date'],
                    address=student['address'],
                    phone=student['phone'],
                    country=student['country']
                )
                student.save()

            return Response('Student records imported successfully, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
