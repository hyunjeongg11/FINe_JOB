from django.urls import path
from ..naverNews import views

urlpatterns = [
    path('news/', views.news, name='news'),
]
