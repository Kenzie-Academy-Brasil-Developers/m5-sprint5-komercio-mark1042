from rest_framework.test import APITestCase
from rest_framework.views import status
from accounts.models import Account
from rest_framework.authtoken.models import Token

class TestAccountView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.admin = {'email': 'admin@mail.com', 'first_name': 'admin', 'last_name': 'admin', 'password': '1234'}
        cls.seller = {'email': 'seller@mail.com', 'first_name': 'seller', 'last_name': 'seller', 'password': '1234', 'is_seller': True}
        cls.not_seller = {'email': 'notseller@mail.com', 'first_name': 'not', 'last_name': 'seller', 'password': '1234', 'is_seller': False}
        cls.field_required_msg = 'This field is required.'
        cls.forbidden_msg = 'You do not have permission to perform this action.'

    def test_create_seller(self):
        res = self.client.post('/api/accounts/', data=self.seller)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['first_name'], 'seller')
        self.assertTrue(res.data['is_seller'])
        self.assertNotIn('password', res.data)
    
    def test_create_not_seller(self):
        res = self.client.post('/api/accounts/', data=self.not_seller)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['first_name'], 'not')
        self.assertFalse(res.data['is_seller'])
        self.assertNotIn('password', res.data)
    
    def test_create_seller_missing_keys(self):
        res = self.client.post('/api/accounts/', data={'first_name': 'test', 'last_name': 'test'})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', res.data)
        self.assertEqual(str(res.data['email'][0]), self.field_required_msg)
        self.assertIn('password', res.data)
        self.assertEqual(str(res.data['password'][0]), self.field_required_msg)
        self.assertNotIn('first_name', res.data)
        self.assertNotIn('last_name', res.data)
    
    def test_create_not_seller_missing_keys(self):
        res = self.client.post('/api/accounts/', data={'email': 'test@mail.com', 'password': '1234'})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('first_name', res.data)
        self.assertEqual(str(res.data['first_name'][0]), self.field_required_msg)
        self.assertIn('last_name', res.data)
        self.assertEqual(str(res.data['last_name'][0]), self.field_required_msg)
        self.assertNotIn('email', res.data)
        self.assertNotIn('password', res.data)

    def test_seller_login_token(self):
        new_seller = Account.objects.create_user(**self.seller)
        res = self.client.post('/api/login/', data=self.seller)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(new_seller.auth_token.key, res.data['token'])
        
    def test_not_seller_login_token(self):
        not_seller_ = Account.objects.create_user(**self.not_seller)
        res = self.client.post('/api/login/', data=self.not_seller)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(not_seller_.auth_token.key, res.data['token'])
    
    def test_only_account_owner_can_patch(self):
        update_data = {'first_name': 'PATCH'}
        seller_ = Account.objects.create_user(**self.seller)
        not_seller_ = Account.objects.create_user(**self.not_seller)

        seller_token = Token.objects.create(user=seller_)
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + seller_token.key)
        res = self.client.patch(f'/api/accounts/{not_seller_.id}/', data=update_data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(res.data['detail'], self.forbidden_msg)

        res = self.client.patch(f'/api/accounts/{seller_.id}/', data=update_data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['first_name'], 'PATCH')
    
    def test_only_admin_can_deactivate(self):
        update_data = {'is_active': False}
        admin = Account.objects.create_superuser(**self.admin)
        seller_ = Account.objects.create_user(**self.seller)
        
        seller_token = Token.objects.create(user=seller_)
        admin_token = Token.objects.create(user=admin)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + seller_token.key)
        res = self.client.patch(f'/api/accounts/{seller_.id}/management/', data=update_data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(res.data['detail'], self.forbidden_msg)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + admin_token.key)
        res = self.client.patch(f'/api/accounts/{seller_.id}/management/', data=update_data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('is_active', res.data)
        self.assertFalse(res.data['is_active'])






        


    
    
    






    