from django.urls import path
from . import views

urlpatterns = [
    path('save_today_luck', views.save_today_luck),
    path('get_today_luck', views.get_today_luck),
    path('save_faq', views.save_faq),
]