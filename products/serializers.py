from rest_framework import serializers
from products.models import Product
from accounts.models import Account

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'first_name', 'last_name', 'is_seller']

class CreateProductSerializer(serializers.ModelSerializer):
    user = SellerSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'description', 'price', 'quantity', 'is_active', 'user']

class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['description', 'price', 'quantity', 'is_active', 'user']