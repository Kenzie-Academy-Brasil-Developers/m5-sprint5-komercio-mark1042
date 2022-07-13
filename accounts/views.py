from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.views import APIView, Response, status
from rest_framework.authtoken.models import Token

from accounts.models import Account
from accounts.serializers import AccountSerializer, LoginSerializer


class ListCreateAccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer 

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(True)
        account = authenticate(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        if account:
            token = Token.objects.get_or_create(user=account)[0]
            return Response({'token': token.key })
        return Response({'message': "invalid email or password"}, status.HTTP_401_UNAUTHORIZED)
