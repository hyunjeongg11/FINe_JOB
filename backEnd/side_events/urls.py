from django.urls import path
from . import views

urlpatterns = [
    # path('get_faq/', views.get_faq),
    path('save_today_luck', views.save_today_luck),
    path('get_today_luck', views.get_today_luck),
]