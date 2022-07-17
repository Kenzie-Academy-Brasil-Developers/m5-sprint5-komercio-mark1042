from rest_framework.test import APITestCase
from rest_framework.views import status
from accounts.models import Account
from rest_framework.authtoken.models import Token


class TestProductView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.seller_data = {'email': 'seller@mail.com', 'first_name': 'seller', 'last_name': 'seller', 'password': '1234', 'is_seller': True}
        cls.not_seller_data = {'email': 'notseller@mail.com', 'first_name': 'not', 'last_name': 'seller', 'password': '1234', 'is_seller': False}

        cls.seller = Account.objects.create_user(**cls.seller_data)
        cls.not_seller = Account.objects.create_user(**cls.not_seller_data)

        cls.seller_token = Token.objects.create(user=cls.seller)
        cls.not_seller_token = Token.objects.create(user=cls.not_seller)

        cls.product_data = {'description': 'test desc', 'price': 10, 'quantity': 1, 'user': cls.seller }

    def test_only_seller_can_create_product(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.seller_token.key)
        res = self.client.post('/api/products/', data=self.product_data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    def test_only_seller_can_create_product_fail(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.not_seller_token.key)
        res = self.client.post('/api/products/', data=self.product_data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        



