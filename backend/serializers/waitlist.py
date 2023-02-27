from rest_framework import serializers
from backend.models.waitlist import WaitList
from backend.models.course import Course


class WaitlistSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()

    def create(self, validated_data):
        student = self.context['request'].user.student
        course_id = validated_data.get('course_id')

        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            raise serializers.ValidationError('Course not found!')

        if course.students.count() >= 10:
            WaitList.add_to_waitlist(student, course)
            return {'message': 'You have been added to the waitlist!'}
        else:
            return {'message': 'There is no waitlist for this course!'}
