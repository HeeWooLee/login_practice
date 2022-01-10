import json
from django.http.response import HttpResponse
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

def validate(request, usr, passwd):
    person = Hey.objects.filter(userName__exact=usr).filter(passWord__exact=passwd)
    if not person:
        return HttpResponse(json.dumps({"pk": "-1"}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({"pk": str(person.first().pk)}), content_type='application/json')


def register(request, usr, passwd):
    person = Hey.objects.filter(userName__exact=usr)
    if person:
        return HttpResponse(json.dumps({"pk": "-1"}), content_type='application/json')
    else:   
        newPerson = Hey(userName=usr, passWord=passwd)
        newPerson.save()
        return HttpResponse(json.dumps({"pk":str(newPerson.pk)}), content_type='application/json')


def uservalid(request, usr):
    person = Hey.objects.filter(userName__exact=usr)
    if not person:
        return HttpResponse(json.dumps({"pk": "-1"}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({"pk": "1"}), content_type='application/json')
