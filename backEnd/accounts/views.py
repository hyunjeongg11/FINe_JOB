from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from django.http import JsonResponse 

from .models import  DetailUser, User
from .serializers import UserDetailSerializer 

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

# @permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete_user(request):
    user = request.user
    if DetailUser.objects.filter(user=user).exists():
        detail = DetailUser.objects.get(user=user)
        detail.delete()
    user.delete()
    return Response({'msg': 'delete complete'}, status=status.HTTP_200_OK)
