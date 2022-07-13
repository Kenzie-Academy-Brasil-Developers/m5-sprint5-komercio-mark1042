from django.shortcuts import render
from rest_framework import generics

from accounts.models import Account
from accounts.serializers import AccountSerializer


class ListCreateAccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer 
