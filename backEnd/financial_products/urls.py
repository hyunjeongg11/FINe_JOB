from django.urls import path
from . import views

urlpatterns = [
    # -------------- 예,적금 DB에 저장 ------------------
    path('save_deposit_products/', views.save_deposit_products),
    path('save_saving_products/', views.save_saving_products),
    
    # ------------ 예,적금 옵션이랑 합친 데이터 불러오기 ----------
    # path('deposit_products/', views.deposit_products),
    # path('saving_products/', views.saving_products),
    # path('deposit_detail/<str:fin_prdt_cd>/', views.deposit_products_detail),
    # path('saving_detail/<str:fin_prdt_cd>/', views.saving_product_detail),
    
    # # ------------- 예,적금 옵션 데이터만 불러오기 ---------------
    # path('deposit_products-options/<str:fin_prdt_cd>/', views.deposit_products_options),
    # path('saving_products-options/<str:fin_prdt_cd>/', views.saving_products_options),
    
    # # ------------ 예,적금 관심상품 ----------
    # path('<int:pk>/likes_deposit/', views.deposit_likes),
    # path('<int:pk>/likes_check/', views.check_likes_user),
    # path('<int:pk>/likes_saving/', views.saving_likes),
    # path('<int:pk>/likes_check_saving/', views.check_likes_user_saving),
    # -------------- 상품 추천 -----------------
    # path('recommend/', views.recommend_products)
]