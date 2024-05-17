from django.urls import path
from . import views

urlpatterns = [
    # -------------- 예,적금 DB에 저장 ------------------
    path('save_deposit_products/', views.save_deposit_products),
    path('save_saving_products/', views.save_saving_products),
    
    # ------------ 예,적금 옵션이랑 합친 데이터 불러오기 ----------
    path('deposit_products/', views.deposit_products),
    path('saving_products/', views.saving_products),
    path('deposit_product_detail/<str:fin_prdt_cd>/', views.deposit_product_detail),
    path('saving_product_detail/<str:fin_prdt_cd>/', views.saving_product_detail),
    
    # # ------------- 예,적금 옵션 데이터만 불러오기 ---------------
    path('deposit_product_options/<str:fin_prdt_cd>/', views.deposit_product_options),
    path('saving_product_options/<str:fin_prdt_cd>/', views.saving_product_options),
    
    # ------------ 예,적금 관심상품 ----------
    path('like_deposit/<int:product_pk>/', views.like_deposit),
    path('like_deposit_check/<int:product_pk>/', views.like_deposit_check),
    path('like_saving/<int:product_pk>/', views.like_saving),
    path('like_saving_check/<int:product_pk>/', views.like_saving_check),
    
    # -------------- 상품 추천 -----------------
    path('recommend_deposit_products/', views.recommend_deposit_products),
    path('recommend_saving_products/', views.recommend_saving_products),
]