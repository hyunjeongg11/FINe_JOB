from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from django.http import JsonResponse 

from .models import  DetailUser, User
from .serializers import UserDetailSerializer, UserLikeListSerializer 

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


User = get_user_model()


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_info(request):
    if not DetailUser.objects.filter(user=request.user).exists():
        DetailUser.objects.create(user=request.user)
        userdetail = DetailUser.objects.get(user=request.user)
    else:
        userdetail = DetailUser.objects.get(user=request.user)
    if request.method == 'GET':
        serializer = UserDetailSerializer(userdetail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = UserDetailSerializer(userdetail, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_list(request):
    serializer = UserLikeListSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    detail = DetailUser.objects.get(user=user)
    detail.delete()
    user.delete()
    return Response('{msg: delete complete}', status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_superuser(request):
    data = {'is_superuser': request.user.is_superuser}
    return JsonResponse(data, status=200)


@api_view(['POST'])
def check_userID(request):
    username = request.data['username']
    if User.objects.filter(username=username).exists():
        isExist = True
    else:
        isExist = False

    result = {'isExist': isExist}
    return JsonResponse(result, status=status.HTTP_200_OK)
