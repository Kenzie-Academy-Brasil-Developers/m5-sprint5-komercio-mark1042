from rest_framework.test import APITestCase
from rest_framework.views import status
from accounts.models import Account

class TestAccountView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.seller = {'email': 'seller@mail.com', 'first_name': 'seller', 'last_name': 'seller', 'password': '1234', 'is_seller': True}

    




        # cls.seller = Account.objects.create_user(email='seller@mail.com', first_name='seller', last_name='mcseller', password='1234', is_seller=True)
        # cls.notseller = Account.objects.create_user(email='notseller@mail.com', first_name='not', last_name='seller', password='1234', is_seller=False)