from django.urls import path
from boards import views

urlpatterns = [
    path('age/', views.age_list),
    path('age/<int:age_pk>/', views.age_detail),
    path('age/<int:age_pk>/comments/', views.age_comment_create),
    path('age/comments/<int:comment_pk>', views.age_comment_detail),
    path('free/', views.free_list),
    path('free/<int:free_pk>/', views.free_detail),
    path('free/<int:free_pk>/comments/', views.free_comment_create),
    path('free/comments/<int:comment_pk>', views.free_comment_detail),
    # path('user_log/', views.show_logs)
]