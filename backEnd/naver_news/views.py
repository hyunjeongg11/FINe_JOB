from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os
import sys
import json
import urllib.request
from django.conf import settings

# Create your views here.
@api_view(['GET'])
def news(request):
    encText = urllib.parse.quote('금융')
    url = "https://openapi.naver.com/v1/search/news.json?query=" + encText # JSON 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", settings.NAVER_CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", settings.NAVER_CLIENT_SECRET)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return Response(json.loads(response_body.decode('utf-8')), status=status.HTTP_200_OK)
    else:
        return Response({"message": "조회에 실패했습니다."}, status=status.HTTP_404_NOT_FOUND)