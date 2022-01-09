from .models import Trip
from rest_framework import serializers

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('userName', 'tripName', 'data' , 'totalLength')