from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from backend.serializers.waitlist import WaitlistSerializer
from school_app.permissions import HasStudentPermission


@api_view(['POST'])
@permission_classes((HasStudentPermission,))
def add_to_waitlist(request):
    serializer = WaitlistSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    response_data = serializer.create(serializer.validated_data)
    return Response(response_data, status=status.HTTP_200_OK)
