import hashlib
from datetime import datetime
import requests, random
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.conf import settings
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import TodayLuckSerializer, FAQSerializer
from .models import TodayLuck, FAQ
from django.core.management import call_command

# @permission_classes([IsAdminUser])
@api_view(['POST'])
def save_today_luck(request):
    serializer = TodayLuckSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

def generate_hash(birthday, today):
    # 생일과 오늘 날짜를 문자열로 결합
    input_str = f"{birthday}-{today}"
    # SHA-256 해시 생성
    hash_object = hashlib.sha256(input_str.encode())
    # 해시 값을 16진수 문자열로 변환 후, 정수로 변환
    hash_value = int(hash_object.hexdigest(), 16)
    return hash_value

def hash(request, lenOfTodayLucks):
    birthday = datetime.strptime(request.user.birthday, '%Y-%m-%d').strftime('%Y-%m-%d')
    today = datetime.now().strftime('%Y-%m-%d')
    hash = generate_hash(birthday, today)
    # lenOfTodayLucks로 나눈 나머지 반환
    return hash % lenOfTodayLucks + 1

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_today_luck(request):
    if not TodayLuck.objects.exists():
        call_command('loaddata', 'today_luck/today_luck.json')
    serializer = TodayLuckSerializer(get_object_or_404(TodayLuck, id=hash(request, TodayLuck.objects.count())))
    return Response(serializer.data, status=status.HTTP_200_OK)


def get_faq_info(startDate, endDate):
    FAQ_API_KEY = settings.FAQ_API_KEY
    base_url = 'https://www.fss.or.kr/fss/kr/openApi/api/tip.jsp'
    params = {
        'apiType': 'json',
        'startDate': startDate,
        'endDate': endDate,
        'authKey': FAQ_API_KEY,
    }
    return requests.get(base_url, params=params).json()


@api_view(['GET'])
def save_faq(request):
    # faq_info = get_faq_info('2023-05-01', '2023-05-31')
    # for year in range(2022, 2024):
    for year in range(2022, 2023):
        # for month in range(1, 13):
        for month in range(12, 13):
            startDate = f'{year}-{month}-01'
            endDate = f'{year}-{month}-31'
            faq_info = get_faq_info(startDate, endDate)
            print(faq_info)
            for i in range(faq_info.get('reponse').get('resultCnt')):
                subject = faq_info.get('reponse').get('result')[i].get('subject')
                print(subject)
                url = faq_info.get('reponse').get('result')[i].get('originUrl')
                print(url)
                registerDate = faq_info.get('reponse').get('result')[i].get('regDate')
                print(registerDate)
                save_data = {
                    'subject': subject,
                    'url': url,
                    'registerDate': registerDate,
                }

                if not FAQ.objects.filter(subject=subject):
                    serializer = FAQSerializer(data=save_data)
                    print(serializer)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
    return Response({'msg': 'save complete'}, status=status.HTTP_200_OK)