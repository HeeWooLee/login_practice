from .models import Trip
from .serializers import TripSerializer
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

#     def perform_create(self, serializer):
#         serializer.save()

def get_general(request, un):
    list_trips = Trip.objects.filter(userName__exact=un)
    context = {un : list_trips}
    return HttpResponse(context, content_type='application/json')


def get_detail(request, un, tn):
    list_trips_general = Trip.objects.filter(userName__exact=un)
    list_trips_detail = list_trips_general.filter(tripName__exact=tn)
    context = {tn: list_trips_detail}
    return HttpResponse(context, content_type='application/json')