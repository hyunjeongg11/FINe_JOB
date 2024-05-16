from django.urls import path
from . import views

urlpatterns = [
    path('delete_user/', views.delete_user),
    path('edit_user_info/', views.edit_user_info),
]
