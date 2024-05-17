from django.urls import path
from . import views

urlpatterns = [
    path('save_job_info/', views.save_job_info),
    path('get_job_info/', views.get_job_info),
    path('like_job_info/<job_info_pk>', views.like_job_info),
]