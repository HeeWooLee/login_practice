import json

import trip
from .models import Friend
from .serializers import FriendSerializer
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

def get_friend(request, un):
    friend_dict = dict()
    selected = Friend.objects.filter(userName__exact = un)
    for i in range(len(selected)):
        friend_dict[i+1] = selected[i].userFriend
    return HttpResponse(json.dumps(friend_dict), content_type='application/json')


def get_friend_num(request, un):
    selected = Friend.objects.filter(userName__exact = un)
    return HttpResponse(json.dumps({"length": str(len(selected))}), content_type='application/json')


def create_friend(request, un, uf):
    friendOne = Friend(userName=un, userFriend=uf)
    friendTwo = Friend(userName=uf, userFriend=un)
    friendOne.save()
    friendTwo.save()
    return HttpResponse(json.dumps({un : uf, uf: un}), content_type='application/json')

def delete_friend(request, un, uf):
    deletedFriendOne = Friend.objects.filter(userName__exact = un).filter(userFriend__exact = uf)
    deletedFriendTwo = Friend.objects.filter(userName__exact = uf).filter(userFriend__exact = un)
    deletedFriendOne.delete()
    deletedFriendTwo.delete()
    return HttpResponse(json.dumps({un : uf, uf: un}), content_type='application/json')
