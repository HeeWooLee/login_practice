import json

import trip
from .models import Trip
from .serializers import TripSerializer
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from rest_framework import viewsets

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

#     def perform_create(self, serializer):
#         serializer.save()

def get_detail(request, un):
    d = dict()
    i = 1
    st = Trip.objects.filter(userName__exact=un)
    print(st)
    print(type(st))
    for i in range(len(st)):
        x = st[i]
        d[i+1] = {"tripName":x.tripName,"data":x.data,"totalLength":x.totalLength}
    return HttpResponse(json.dumps(d), content_type='application/json')

def get_detail_len(request, un):
    st = Trip.objects.filter(userName__exact=un).count()
    return HttpResponse(json.dumps({"length": str(st)}), content_type='application/json')



def create_new(request):
    userName = request.GET.get('userName')
    tripName = request.GET.get('tripName')
    data = request.GET.get('data')
    totalLength = request.GET.get('totalLength')
    
    newTrip = Trip(userName=userName, tripName= tripName, data = data, totalLength = totalLength)
    newTrip.save()

    return HttpResponse(json.dumps({"pk": str(newTrip.pk)}), content_type='application/json')

def delete(request, un, tn):
    deleteTrip = Trip.objects.filter(userName__exact=un).filter(tripName__exact=tn).first()
    deleteTrip.delete()
    return HttpResponse(json.dumps({"pk": str(pk)}), content_type='application/json')


def get_practice(request, un, tn):
    st = Trip.objects.filter(userName__exact=un).filter(tripName__exact=tn).first()
    d = {"userName": st.userName,"tripName":st.tripName,"data":st.data,"totalLength":st.totalLength}
    return HttpResponse(json.dumps(d), content_type='application/json')


def create_practice(request, un, tn, data, len):
    newTrip = Trip(userName=un, tripName= tn, data = data, totalLength = len)
    newTrip.save()
    return HttpResponse(json.dumps({"pk": str(newTrip.pk)}), content_type='application/json')