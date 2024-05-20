from django.urls import path
from . import views

urlpatterns = [
    path('delete_user/', views.delete_user),
    path('edit_user_info/', views.edit_user_info),
    path('user_detail/<search_name>', views.user_detail),
    path('like_list/', views.like_list),
]
