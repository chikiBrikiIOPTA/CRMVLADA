"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from CRM import views

urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('Главная/', views.main, name='Главная'),
    path('Музыка/', views.music, name='Музыка'),
    path('Контакты/', views.contact, name='Контакты'),
    path('О-нас/', views.about, name='О-нас'),
    path('Трек1/', views.track1, name='Трек1'),
    path('Трек2/', views.track2, name='Трек2'),
    path('Трек3/', views.track3, name='Трек3'),
    path('Трек4/', views.track4, name='Трек4'),
    path('admin/', admin.site.urls),
]
