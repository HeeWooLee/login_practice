# seralizers that 1:1 match with model
from rest_framework import serializers
from login_app.models import Hey, Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        # write field which we want to denote
        fields = ('test', 'id')

class HeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hey
        # write field which we want to denote
        fields = ('userName', 'passWord')