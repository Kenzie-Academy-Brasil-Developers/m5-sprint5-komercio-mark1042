from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from products.serializers import CreateProductSerializer, ListProductSerializer
from rest_framework.authentication import TokenAuthentication
from products.mixins import SerializerByMethodMixin
from komercio import permissions

class ListCreateProductView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsSellerOrAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_map = {
        "POST" : CreateProductSerializer,
        "GET" : ListProductSerializer
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrievePatchProductView(SerializerByMethodMixin, generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsOwnerOrAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_map = {
        "PATCH": CreateProductSerializer,
        "GET": ListProductSerializer
    }