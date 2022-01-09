from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 #   path('get/<int:pk>', views.get_detail , name='trip_detail'),    #ok
 #   path('get/<str:un>/<str:tn>', views.get_practice, name='trip_detail_practice'), #ok
 #    path('create/', views.create_new, name='create_new'),   #not ok
 #   path('create/<str:un>/<str:tn>/<str:data>/<int:len>', views.create_practice, name='create_new'),    #ok   
 #   path('delete/<int:pk>', views.delete, name='delete'),   #ok

    path('get/<str:un>', views.get_friend, name='get_friend'),  #ok
    path('getlen/<str:un>', views.get_friend_num, name='get_friend_num'),   #ok
    path('create/<str:un>/<str:uf>', views.create_friend, name='create_friend'),    #ok
    path('delete/<str:un>/<str:uf>', views.delete_friend, name='delete_friend'),    #ok
]