from rest_framework import serializers

from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=32, required=False, write_only=True)
    class Meta:
        model = Account
        fields = ['email', 'username', 'first_name', 'last_name', 'is_seller', 'date_joined']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()



    