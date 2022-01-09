from django.urls import path, include
from . import views

app_name = 'login_app'

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework_category')),
    path('validate/<str:usr>/<str:passwd>', views.validate , name='validate'), 
    path('register/<str:usr>/<str:passwd>', views.register , name='register')   #ok
]