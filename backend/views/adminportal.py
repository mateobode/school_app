from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from backend.models.student import Student
from backend.serializers.adminportal import StudentAdminSerializer, StudentAgeSerializer


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentAdminSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    @action(detail=False)
    def students_country(self, request):
        students = Student.objects.all()
        serializer = StudentAdminSerializer(students, many=True)
        grouped_by_country = {}
        for student in serializer.data:
            country = student.pop("country")
            grouped_by_country[country] = grouped_by_country.get(country, []) + [student]

        return Response(grouped_by_country)

    @action(detail=False)
    def students_gender(self, request):
        students = Student.objects.all()
        serializer = StudentAdminSerializer(students, many=True)
        grouped_by_gender = {}
        for student in serializer.data:
            gender = student.pop("gender")
            grouped_by_gender[gender] = grouped_by_gender.get(gender, []) + [student]

        return Response(grouped_by_gender)

    @action(detail=False)
    def students_age(self, request):
        students = Student.objects.all()
        serializer = StudentAgeSerializer(students, many=True)
        grouped_by_age = {}
        for student in serializer.data:
            age = student.pop("age")
            grouped_by_age[age] = grouped_by_age.get(age, []) + [student]

        return Response(grouped_by_age)
