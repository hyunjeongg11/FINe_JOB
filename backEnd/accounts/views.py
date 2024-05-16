from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from django.http import JsonResponse 
from .serializers import CustomUserEditSerializer
from .models import User

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response({'msg': 'delete complete'}, status=status.HTTP_200_OK)

# edit user info
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_user_info(request):
    user = request.user
    serializer = CustomUserEditSerializer(user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)