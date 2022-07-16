from rest_framework import serializers

from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=32, required=False, write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'is_seller', 'date_joined']

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)
        

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'is_seller']


class ToggleIsActiveSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Account
        all_fields = ['id', 'email', 'first_name', 'last_name', 'is_seller', 'date_joined', 'is_active']
        fields = all_fields
        read_only_fields = all_fields[:-1]
        

    