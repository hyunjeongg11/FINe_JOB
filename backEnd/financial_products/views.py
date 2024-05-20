from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import requests
import random
from django.db.models import Q, Avg
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Deposit_Products, Saving_Products, Deposit_Options, Saving_Options
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingProductsSerializer, SavingOptionsSerializer,DepositProductDetailSerializer, SavingProductDetailSerializer

# from accounts.models import DetailUser

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

User = get_user_model()

# 예금 데이터
# 예금 상품 목록 및 옵션 DB 저장
# @permission_classes([IsAdminUser])

def isDepositSaved():
    if not Deposit_Products.objects.exists():
        return False
    return True


def isSavingSaved():
    if not Saving_Products.objects.exists():
        return False
    return True


def save_deposit_products():
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : settings.FINLIFE_API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()
    for li in response.get('result').get('baseList'):
        if not Deposit_Products.objects.filter(fin_prdt_cd=li.get('fin_prdt_cd')).exists():
            serializer = DepositProductsSerializer(data = li)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    for li in response.get('result').get('optionList'):
        deposit_product = Deposit_Products.objects.get(fin_prdt_cd = li.get('fin_prdt_cd'))
        serializer = DepositOptionsSerializer(data=li)
        if serializer.is_valid(raise_exception=True):
            serializer.save(deposit_product=deposit_product)

        
# 전체 예금 데이터 불러오기, 추가하기
# @permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == "GET":
        if not isDepositSaved():
            save_deposit_products()
        deposit_products = get_list_or_404(Deposit_Products)
        serializer = DepositProductsSerializer(deposit_products, many=True)
        return Response(serializer.data)
    else:
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)


# 특정 예금 상품 불러오기
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def deposit_product_detail(request, fin_prdt_cd):
    # deposit_product = Deposit_Products.objects.get(fin_prdt_cd=fin_prdt_cd)
    if not isDepositSaved():
        save_deposit_products()
    deposit_product = get_object_or_404(Deposit_Products, fin_prdt_cd=fin_prdt_cd)
    serializer = DepositProductDetailSerializer(deposit_product)
    return Response(serializer.data)


# 예금 옵션 불러오기
# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):    
    # deposit_product = Deposit_Products.objects.get(fin_prdt_cd=fin_prdt_cd)
    if not isDepositSaved():
        save_deposit_products()
    deposit_product = get_object_or_404(Deposit_Products, fin_prdt_cd=fin_prdt_cd)
    deposit_options = Deposit_Options.objects.filter(deposit_product=deposit_product)
    serializer = DepositOptionsSerializer(deposit_options, many=True)
    return Response(serializer.data)


# 예금 관심상품 등록
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_deposit(request, product_pk):
    # deposit = Deposit_Products.objects.get(pk=pk)
    deposit_product = get_object_or_404(Deposit_Products, pk=product_pk)

    if request.user in deposit_product.like_users.all():
        deposit_product.like_users.remove(request.user)
        liked = False
    else:
        deposit_product.like_users.add(request.user)
        liked = True
    return Response({'liked': liked})


# 관심상품 등록한 유저인지 확인
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_deposit_check(request, product_pk):
    # deposit = Deposit_Products.objects.get(pk=pk)
    deposit_product = get_object_or_404(Deposit_Products, pk=product_pk)

    if request.user in deposit_product.like_users.all():
        return Response({'user' : True})
    else:
        return Response({'user': False})

#------------------------------------------------------------#
# 적금 데이터
# 적금 상품 목록 및 옵션 DB 저장
# @permission_classes([IsAdminUser])
def save_saving_products():
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
        'auth' : settings.FINLIFE_API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()

    for li in response.get('result').get('baseList'):
        if not Saving_Products.objects.filter(fin_prdt_cd=li.get('fin_prdt_cd')).exists():
            serializer = SavingProductsSerializer(data = li)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    for li in response.get('result').get('optionList'):
        saving_product = Saving_Products.objects.get(fin_prdt_cd = li.get('fin_prdt_cd'))
        serializer = SavingOptionsSerializer(data=li)
        if serializer.is_valid(raise_exception=True):
            serializer.save(saving_product=saving_product)

                
# 전체 적금 데이터 불러오기, 추가하기
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def saving_products(request):
    if request.method == "GET":
        if not isSavingSaved():
            save_saving_products()
        saving_products = get_list_or_404(Saving_Products)
        serializer = SavingProductsSerializer(saving_products, many= True)
        return Response(serializer.data)
    else:
        serializer = SavingProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)


# 특정 적금 상품 불러오기
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def saving_product_detail(request, fin_prdt_cd):    
    if not isSavingSaved():
        save_saving_products()
    saving_product = get_object_or_404(Saving_Products, fin_prdt_cd=fin_prdt_cd)
    serializer = SavingProductDetailSerializer(saving_product)
    return Response(serializer.data)


# 적금 옵션만 불러오기
# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def saving_product_options(request, fin_prdt_cd):
    if not isSavingSaved():
        save_saving_products()
    saving_product = get_object_or_404(Saving_Products, fin_prdt_cd=fin_prdt_cd)
    options = Saving_Options.objects.filter(saving_product=saving_product)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)


# 적금 관심 상품 등록
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_saving(request, product_pk):
    # saving_product = Saving_Products.objects.get(pk=pk)
    saving_product = get_object_or_404(Saving_Products, pk=product_pk)
    if request.user in saving_product.like_users.all():
        saving_product.like_users.remove(request.user)
        liked = False
    else:
        saving_product.like_users.add(request.user)
        liked = True
    return Response({'liked': liked})


# 적금 관심상품 등록유저 확인
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_saving_check(request, product_pk):
    # saving_product = Saving_Products.objects.get(pk=pk)
    saving_product = get_object_or_404(Saving_Products, pk=product_pk)
    if request.user in saving_product.like_users.all():
        return Response({'user' : True})
    else:
        return Response({'user': False})


# 예금 단리 복리 계산기
def deposit_calculate_interest(deposit_amount, target_amount, interest_type, intr_rate, intr_rate2, save_trm):
    if interest_type == '단리':
        result = {}
        simple_interest = round(deposit_amount * (1 + (intr_rate / 100) * (save_trm / 12)))
        simple_interest2 = round(deposit_amount * (1 + (intr_rate2 / 100) * (save_trm / 12)))
        if simple_interest >= target_amount:
            result['amount'] = simple_interest
        if simple_interest2 >= target_amount:
            result['amount2'] = simple_interest2
        return result
    elif interest_type == '복리':
        result = {}
        compound_interest = round(deposit_amount * (1 + (intr_rate / 100))**(save_trm / 12))
        compound_interest2 = round(deposit_amount * (1 + (intr_rate2 / 100))**(save_trm / 12))
        if compound_interest >= target_amount:
            result['amount'] = compound_interest
        if compound_interest2 >= target_amount:
            result['amount2'] = compound_interest2
        return result
    return {}


# 예금 상품 추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_deposit_products(request):
    # deposit_amount = request.GET['depositAmount']
    # target_amount = request.GET['targetAmount']
    deposit_products = get_list_or_404(Deposit_Products)
    data = {}
    for deposit_product in deposit_products:
        options = Deposit_Options.objects.filter(deposit_product=deposit_product)
        for option in options:
            intr_rate_type_nm = option.intr_rate_type_nm
            intr_rate = option.intr_rate
            intr_rate2 = option.intr_rate2
            save_trm = option.save_trm
            result = deposit_calculate_interest(1000, 1050, intr_rate_type_nm, intr_rate, intr_rate2, save_trm)
            # result = calculate_interest(deposit_amount, target_amount, intr_rate_type_nm, intr_rate, intr_rate2, save_trm)
            if result:
                data[deposit_product.fin_prdt_cd] = (result, save_trm)
                break
    if data:
        return Response({'message': 'okay', 'data': data})
    return Response({'message': 'no data'})


# 적금 단리 복리 계산기
def saving_calculate_interest(monthly_amount, target_amount, interest_type, intr_rate, intr_rate2, save_trm):
    if interest_type == '단리':
        result = {}
        simple_interest = round(monthly_amount * (save_trm * (save_trm + 1) / 2 * (intr_rate / 100) / 12) + monthly_amount * save_trm)
        simple_interest2 = round(monthly_amount * (save_trm * (save_trm + 1) / 2 * (intr_rate2 / 100) / 12) + monthly_amount * save_trm)
        if simple_interest >= target_amount:
            result['amount'] = simple_interest
        if simple_interest2 >= target_amount:
            result['amount2'] = simple_interest2
        return result
    elif interest_type == '복리':
        result = {}
        compound_interest = round(monthly_amount * ((1 + (intr_rate / 100))**((save_trm + 1) / 12) - (1 + intr_rate / 100)**(1 / 12)) / ((1 + intr_rate / 100)**(1 / 12) - 1))
        compound_interest2 = round(monthly_amount * ((1 + (intr_rate2 / 100))**((save_trm + 1) / 12) - (1 + intr_rate2 / 100)**(1 / 12)) / ((1 + intr_rate2 / 100)**(1 / 12) - 1))
        if compound_interest >= target_amount:
            result['amount'] = compound_interest
        if compound_interest2 >= target_amount:
            result['amount2'] = compound_interest2
        return result
    return {}


# 적금 상품 추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_saving_products(request):
    # monthly_amount = request.GET['monthlyAmount']
    # target_amount = request.GET['targetAmount']
    saving_products = get_list_or_404(Saving_Products)
    data = {}
    for saving_product in saving_products:
        options = Saving_Options.objects.filter(saving_product=saving_product)
        for option in options:
            intr_rate_type_nm = option.intr_rate_type_nm
            intr_rate = option.intr_rate
            intr_rate2 = option.intr_rate2
            save_trm = option.save_trm
            result = saving_calculate_interest(1000000, 24000000, intr_rate_type_nm, intr_rate, intr_rate2, save_trm)
            # result = calculate_interest(deposit_amount, target_amount, intr_rate_type_nm, intr_rate, intr_rate2, save_trm)
            if result:
                data[saving_product.fin_prdt_cd] = (result, save_trm)
                break
    if data:
        return Response({'message': 'okay', 'data': data})
    return Response({'message': 'no data'})