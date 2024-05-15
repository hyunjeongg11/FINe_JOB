from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('delete_user/', views.delete_user),
]
