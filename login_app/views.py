from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from login_app.models import Test, Hey
from login_app.serializers import TestSerializer, HeySerializer

class TestViewSet(viewsets.ModelViewSet):
    # include everything in Test Object in models.py
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    
class HeyViewSet(viewsets.ModelViewSet):
    # include everything in Test Object in models.py
    queryset = Hey.objects.all()
    serializer_class = HeySerializer