from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import requests
import random
from django.db.models import Q, Avg
 
from .models import Deposit_Products, Saving_Products, Deposit_Options, Saving_Options
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingProductsSerializer, SavingOptionsSerializer,DepositProductDetailSerializer, SavingProductDetailSerializer

# from accounts.models import DetailUser

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

User = get_user_model()

# 예금 데이터
# 예금 상품 목록 및 옵션 DB 저장
@api_view(['GET'])
def save_deposit_products(request):
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

    return JsonResponse({'message': 'okay'})

        
# # 전체 예금 데이터 불러오기, 추가하기
# @permission_classes([IsAuthenticated])
# @api_view(['GET', 'POST'])
# def deposit_products(request):
#     if request.method == "GET":
#         deposit_product = Deposit_Products.objects.all()
#         serializer = DepositProductsSerializer(deposit_product, many= True)
#         return Response(serializer.data)
#     else:
#         serializer = DepositProductsSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=201)

# # 특정 예금 상품 불러오기
# @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def deposit_products_detail(request, fin_prdt_cd):    
#     deposit_product = Deposit_Products.objects.get(fin_prdt_cd=fin_prdt_cd)
#     serializer = DepositProductDetailSerializer(deposit_product)
#     return Response(serializer.data)

# # 예금 옵션 불러오기
# # @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def deposit_products_options(request, fin_prdt_cd):    
#     deposit_product = Deposit_Products.objects.get(fin_prdt_cd=fin_prdt_cd)
#     deposit_options = Deposit_Options.objects.filter(deposit_product=deposit_product)
#     serializer = DepositOptionsSerializer(deposit_options, many=True)
#     return Response(serializer.data)

# # 예금 관심상품 등록
# @permission_classes([IsAuthenticated])
# @api_view(['POST'])
# def deposit_likes(request, pk):
#     deposit = Deposit_Products.objects.get(pk= pk)
#     if request.user in deposit.like_users.all():
#         deposit.like_users.remove(request.user)
#         liked = False
#     else:
#         deposit.like_users.add(request.user)
#         liked = True
#     return Response({'liked': liked})

# # 관심상품 등록한 유저인지 확인
# @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def check_likes_user(request, pk):
#     deposit = Deposit_Products.objects.get(pk= pk)
#     if request.user in deposit.like_users.all():
#         return Response({'user' : True})
#     else:
#         return Response({'user': False})


# 적금 데이터

# 적금 상품 목록 및 옵션 DB 저장
@api_view(['GET'])
def save_saving_products(request):
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

    return JsonResponse({'message': 'okay'})

                
# # 전체 적금 데이터 불러오기, 추가하기
# @permission_classes([IsAuthenticated])
# @api_view(['GET', 'POST'])
# def saving_products(request):
#     if request.method == "GET":
#         saving_product = Saving_Products.objects.all()
#         serializer = SavingProductsSerializer(saving_product, many= True)
#         return Response(serializer.data)
#     else:
#         serializer = SavingProductsSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=201)

# # 특정 적금 상품 불러오기
# @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def saving_product_detail(request, fin_prdt_cd):    
#     saving_product = Saving_Products.objects.get(fin_prdt_cd=fin_prdt_cd)
#     serializer = SavingProductDetailSerializer(saving_product)
#     return Response(serializer.data)


# # 적금 옵션만 불러오기
# # @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def saving_products_options(request, fin_prdt_cd):
#     print(fin_prdt_cd)    
#     product = Saving_Products.objects.get(fin_prdt_cd=fin_prdt_cd)
#     options = Saving_Options.objects.filter(saving_product=product)
#     serializer = DepositOptionsSerializer(options, many=True)
#     return Response(serializer.data)


# # 적금 관심 상품 등록
# @permission_classes([IsAuthenticated])
# @api_view(['POST'])
# def saving_likes(request, pk):
#     saving = Saving_Products.objects.get(pk= pk)
#     if request.user in saving.like_users.all():
#         saving.like_users.remove(request.user)
#         liked = False
#     else:
#         saving.like_users.add(request.user)
#         liked = True
#     return Response({'liked': liked})

# # 적금 관심상품 등록유저 확인
# @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def check_likes_user_saving(request, pk):
#     saving = Saving_Products.objects.get(pk= pk)
#     if request.user in saving.like_users.all():
#         return Response({'user' : True})
#     else:
#         return Response({'user': False})


# # 상품 추천
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def recommend_products(request):
#     user = request.user
#     detailInfo = DetailUser.objects.get(user=user)
#     # 임의의 유저 선택
#     # detailInfo = DetailUser.objects.get(pk=1)
#     birthday = detailInfo.birthday
#     year = birthday[0:4]
#     year_range = [str(tmp) for tmp in range(int(year) - 3, int(year) + 3)]
#     salary = detailInfo.salary
#     asset = detailInfo.asset
#     main_bank = detailInfo.main_bank
#     goal = detailInfo.goal
#     gender = detailInfo.gender

#     # 자산과 연봉 범위에 따라 filter 범위 다르게 주기
#     salary_range = [[0, 20000000], [30000000, 40000000], [40000000, 60000000], [60000000, 100000000], [100000000, 150000000]]
#     salary_gap = [5000000, 2000000, 5000000, 10000000, 30000000]
#     asset_range = [[0, 20000000], [30000000, 60000000], [60000000, 150000000], [150000000, 500000000], [500000000, 1500000000]]
#     asset_gap = [5000000, 10000000, 20000000, 30000000, 50000000]
    
#     for si in range(len(salary_range)):
#         if salary_range[si][0] <= salary < salary_range[si][1]:
#             break
    
#     for ai in range(len(asset_range)):
#         if asset_range[si][0] <= asset < asset_range[si][1]:
#             break

#     # 비슷한 유저 찾기
#     # 해당 유저들이 가입한 상품 리스트 추출(user.like_deposits_set, user.like_savings_set 사용)
#     age_filtered_users = DetailUser.objects.filter(
#         (Q(birthday__icontains=year_range[0]) |
#         Q(birthday__icontains=year_range[1]) |
#         Q(birthday__icontains=year_range[2]) |
#         Q(birthday__icontains=year_range[3]) |
#         Q(birthday__icontains=year_range[4]) |
#         Q(birthday__icontains=year_range[5])) & 
#         Q(main_bank=main_bank, goal=goal))
        
#     all_filtered_users = age_filtered_users.filter(Q(salary__lte=salary + salary_gap[si], salary__gte=salary - salary_gap[si],
#                                                     asset__lte=asset + asset_gap[si], asset__gte=asset - asset_gap[ai]))


#     # print(all_filtered_users)
#     deposit_products = []
#     saving_products = []
#     average_salary = all_filtered_users.aggregate(avg_salary=Avg('salary'))['avg_salary']
#     average_asset = all_filtered_users.aggregate(avg_asset=Avg('asset'))['avg_asset']
#     for info in all_filtered_users:
#         filter = 'all'
#         if info.user.like_deposit.all().exists():
#             for item in info.user.like_deposit.all():
#                 deposit_products.append(item)
#         if info.user.like_saving.all().exists():
#             for item in info.user.like_saving.all():
#                 saving_products.append(item)

#     if (len(set(deposit_products)) < 5) or (len(set(saving_products)) < 5):
#         filter = 'age_only'
#         deposit_products = []
#         saving_products = []
#         average_salary = age_filtered_users.aggregate(avg_salary=Avg('salary'))['avg_salary']
#         average_asset = age_filtered_users.aggregate(avg_asset=Avg('asset'))['avg_asset']

#         for info in age_filtered_users:
#             if info.user.like_deposit.all().exists():
#                 for item in info.user.like_deposit.all():
#                     deposit_products.append(item)
#             if info.user.like_saving.all().exists():
#                 for item in info.user.like_saving.all():
#                     saving_products.append(item)


#     selected_deposit = random.sample(set(deposit_products), min(len(deposit_products), 5))
#     selected_saving = random.sample(set(saving_products), min(len(saving_products), 5))
    
#     serializer1 = DepositProductsSerializer(selected_deposit, many=True)
#     serializer2 = SavingProductsSerializer(selected_saving, many=True)

#     response_data = {
#         'deposit_products': serializer1.data,
#         'saving_products': serializer2.data,
#         'filter': filter,
#         'average_salary': average_salary,
#         'average_asset': average_asset
#     }
#     return JsonResponse(response_data, status=200)
