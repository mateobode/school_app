from rest_framework import serializers

from backend.models.assignment import Assignment
from backend.models.course import Course
from backend.models.student import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentCourseSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['student', 'name']

    def to_representation(self, instance):
        rep = super(StudentCourseSerializer, self).to_representation(instance)

        student_pk = self.context['request'].parser_context.get('kwargs').get('pk')
        student = Student.objects.get(pk=student_pk)
        avg_grade = instance.get_avg_grade(student)
        progress = instance.get_progress(student)

        rep["name"] = f"{rep['name']} - Progress: {progress} - Average Grade: {avg_grade}"
        #assignments = []

        # for pk in rep["assignments"]:
        #     assignment = Assignment.objects.get(pk=pk)
        #     assignments.append(f"{assignment.description} - {assignment.grade}")
        # rep["assignments"] = assignments

        return rep


class StudentAssignmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer

    class Meta:
        model = Assignment
        fields = ['description', 'grade', 'feedback']
