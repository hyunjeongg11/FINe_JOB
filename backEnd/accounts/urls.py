from django.urls import path
from . import views

urlpatterns = [
    path('delete_user/', views.delete_user),
]
