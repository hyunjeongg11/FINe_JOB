import requests, random
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.conf import settings
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import TodayLuckSerializer
from .models import TodayLuck

@api_view(['POST'])
# @permission_classes([IsAdminUser])
def save_today_luck(request):
    serializer = TodayLuckSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_today_luck(request):
    todayLucks = get_list_or_404(TodayLuck)
    random_luck = random.choice(todayLucks)
    serializer = TodayLuckSerializer(random_luck)
    return Response(serializer.data, status=status.HTTP_200_OK)