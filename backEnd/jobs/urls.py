from django.urls import path
from . import views

urlpatterns = [
    path('get_job_info/', views.get_job_info),
]