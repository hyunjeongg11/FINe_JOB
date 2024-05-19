"""
URL configuration for backEnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from naver_news import views as nnviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/jobs/', include('jobs.urls')),
    path('api/v1/exchange_rate/', include('exchange_rate.urls')),
    path('api/v1/boards/', include('boards.urls')),
    path('api/v1/accounts/', include('accounts.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('api/v1/financial_products/', include('financial_products.urls')),
    path('api/v1/side_events/', include('side_events.urls')),
    path('api/v1/mainpage/', nnviews.news),
    # path('api/v1/mainpage/kospi/', mpviews.kospi_info),
]
