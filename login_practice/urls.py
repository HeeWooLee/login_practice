"""login_practice URL Configuration

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
from django.urls import path, include
from rest_framework import routers

from login_app import views as login_app_views
#from login_practice import views as login_practice_views
from trip import views as trip_views
from friend import views as friend_views

router = routers.DefaultRouter()

router.register(r'tests', login_app_views.TestViewSet)
#router.register(r'heys', login_practice_views.HeyViewSet)
router.register(r'trip', trip_views.TripViewSet)
router.register(r'friend', friend_views.FriendViewSet)

urlpatterns = [
    path('login_app/', include('login_app.urls')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('trip/', include('trip.urls')),
    path('friend/', include('friend.urls'))
]
