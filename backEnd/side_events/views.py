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

# @permission_classes([IsAdminUser])
@api_view(['POST'])
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

# @permission_classes([IsAdminUser])
@api_view(['GET'])
def save_faq(request):
    # faq_info = get_faq_info('2023-05-01', '2023-05-31')
    # print(faq_info.get('reponse').get('resultCnt'))
    # print(faq_info.get('reponse'))
    for year in range(2022, 2024):
        for month in range(1, 13):
            startDate = f'{year}-{month}-01'
            endDate = f'{year}-{month}-31'
            faq_info = get_faq_info(startDate, endDate)
            for i in range(faq_info.get('reponse').get('resultCnt')):
                subject = faq_info.get('reponse').get('result')[i].get('subject')
                url = faq_info.get('reponse').get('result')[i].get('originUrl')
                registerDate = faq_info.get('reponse').get('result')[i].get('regDate')

                save_data = {
                    'subject': subject,
                    'url': url,
                    'registerDate': registerDate,
                }

                if not FAQ.objects.filter(subject=subject):
                    serializer = FAQSerializer(data=save_data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
    return Response({'msg': 'save complete'}, status=status.HTTP_200_OK)