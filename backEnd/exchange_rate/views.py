from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status

import requests
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from datetime import datetime, timedelta, date

# api 키로 환율정보 가져오기
def get_exchange_rate_info(search_date):
    EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY
    base_url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"
    params = {
        'authkey': EXCHANGE_API_KEY,
        'searchdate': search_date,
        'data': 'AP01',
    }
    return requests.get(base_url, params=params).json()

# response 데이터를 받아서 DB에 저장
def save_exchange_rate(response, search_date):
    for result in response:
        cur_unit = result.get('cur_unit')
        cur_nm = result.get('cur_nm')
        ttb = result.get('ttb')
        tts = result.get('tts')
        deal_bas_r = result.get('deal_bas_r')

        save_data = {
            'search_date': search_date,
            'cur_unit': cur_unit,
            'cur_nm': cur_nm,
            'ttb': ttb,
            'tts': tts,
            'deal_bas_r': deal_bas_r,
        }

        serializer = ExchangeRateSerializer(data=save_data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


@api_view(['GET'])
def get_exchange_rate(request):
    EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY
    today = date.today()
    search_date = today.strftime('%Y-%m-%d')
    if not ExchangeRate.objects.filter(search_date=search_date):
        response = get_exchange_rate_info(search_date)
        if response:
            save_exchange_rate(response, search_date)

        else: # 비영업일이거나 영업 이전 시간이다
            while not response:
                now = datetime.strptime(search_date, '%Y-%m-%d')
                search_date = now - timedelta(days=1)
                search_date = search_date.strftime('%Y-%m-%d')
                response = get_exchange_rate_info(search_date)

            if not ExchangeRate.objects.filter(search_date=search_date): # 환율 데이터가 DB에 없다면 저장
                save_exchange_rate(response, search_date)

    return Response({'msg': 'save complete'}, status=status.HTTP_200_OK)