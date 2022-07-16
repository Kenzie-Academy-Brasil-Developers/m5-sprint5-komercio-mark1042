from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.views import APIView, Response, status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from accounts.models import Account
from accounts.serializers import AccountSerializer, LoginSerializer, AccountUpdateSerializer
from komercio.permissions import IsAccountOwner


class ListCreateAccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer 

class ListXNewestAccountsView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        accs_num = self.kwargs['num']
        return self.queryset.order_by('-date_joined')[0:accs_num]

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

class UpdateAccountView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = AccountUpdateSerializer
    queryset = Account.objects.all()

