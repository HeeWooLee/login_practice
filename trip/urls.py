"""trip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views

urlpatterns = [
 #   path('', views.index, name='index'),
    path('get/<str:un>', views.get_detail , name='trip_detail'),    #ok
    path('getlen/<str:un>', views.get_detail_len , name='trip_detail'),
    path('get/<str:un>/<str:tn>', views.get_practice, name='trip_detail_practice'), #ok
    path('create/', views.create_new, name='create_new'),   #not ok
    path('create/<str:un>/<str:tn>/<str:data>/<int:len>', views.create_practice, name='create_new'),    #ok   
    path('delete/<str:un>/<str:tn>', views.delete, name='delete'),   #ok
]