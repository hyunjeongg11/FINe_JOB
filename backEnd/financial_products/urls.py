from django.urls import path
from . import views

urlpatterns = [
    # -------------- 예,적금 DB에 저장 ------------------
    path('save-deposit-products/', views.save_deposit_products),
    path('save-saving-products/', views.save_saving_products),
    
    # ------------ 예,적금 옵션이랑 합친 데이터 불러오기 ----------
    path('deposit-products/', views.deposit_products),
    path('saving-products/', views.saving_products),
    path('deposit-detail/<str:fin_prdt_cd>/', views.deposit_products_detail),
    path('saving-detail/<str:fin_prdt_cd>/', views.saving_product_detail),
    
    # ------------- 예,적금 옵션 데이터만 불러오기 ---------------
    path('deposit-products-options/<str:fin_prdt_cd>/', views.deposit_products_options),
    path('saving-products-options/<str:fin_prdt_cd>/', views.saving_products_options),
    
    # ------------ 예,적금 관심상품 ----------
    path('<int:pk>/likes-deposit/', views.deposit_likes),
    path('<int:pk>/likes-check/', views.check_likes_user),
    path('<int:pk>/likes-saving/', views.saving_likes),
    path('<int:pk>/likes-check-saving/', views.check_likes_user_saving),
    # -------------- 상품 추천 -----------------
    # path('recommend/', views.recommend_products)
]