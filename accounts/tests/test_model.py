from django.test import TestCase

from accounts.models import Account

class AccountModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Account.objects.create(email='testin123@test.com', first_name='Testin', last_name='McTestinson', password='1234', is_seller=True)

    def test_email_max_length(self):
        account = Account.objects.get(id=1)
        max_length = account._meta.get_field('email').max_length
        self.assertEquals(max_length, 128)
    
    def test_username_should_be_null(self):
        account = Account.objects.get(id=1)
        self.assertIsNone(account.username)
    
    def test_first_name_max_length(self):
        account = Account.objects.get(id=1)
        max_length = account._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 50)
    
    def test_last_name_max_length(self):
        account = Account.objects.get(id=1)
        max_length = account._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 50)
    
    def test_is_seller_should_be_true(self):
        account = Account.objects.get(id=1)
        self.assertEquals(account.is_seller, True)
    
    def test_is_seller_should_not_be_false(self):
        account = Account.objects.get(id=1)
        self.assertNotEquals(account.is_seller, False)
    
        

