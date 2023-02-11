from datetime import date

from rest_framework import serializers

from backend.models.student import Student


class StudentAdminSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    gender = serializers.CharField(max_length=50)
    birth_date = serializers.DateField()
    country = serializers.CharField(max_length=50)

    def list(self, validated_data):
        return Student.objects.all(**validated_data)


class StudentAgeSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'birth_date', 'age']

    def get_age(self, obj):
        today = date.today()
        return today.year - obj.birth_date.year - ((today.month, today.day) < (obj.birth_date.month, obj.birth_date.day))
