from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('user_info/', views.user_info),
    path('like_list/', views.like_list),
    path('delete_user/', views.delete_user),
    path('check_superuser/', views.check_superuser),
    path('check_userID/', views.check_userID)
]
