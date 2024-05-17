from django.urls import path
from . import views

urlpatterns = [
    path('get_exchange_rate/', views.get_exchange_rate),
    path('calculate/', views.calculate),
]
