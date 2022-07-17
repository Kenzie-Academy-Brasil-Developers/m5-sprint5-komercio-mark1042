from django.test import TestCase
from accounts.models import Account

from products.models import Product

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.account = Account.objects.create(email='testin123@test.com', first_name='Testin', last_name='McTestinson', password='1234', is_seller=True) 
        cls.product = Product.objects.create(description='Product description test', price=10, quantity=1, user=cls.account)
        cls.product_2 = Product.objects.create(description='Product 2', price=10, quantity=1, user=cls.account)
        cls.prodx = [cls.product, cls.product_2]

    def test_description_max_length(self):
        max_length = self.product._meta.get_field('description').max_length
        self.assertEquals(max_length, 128)
    
    def test_description_value(self):
        self.assertEquals(self.product.description, 'Product description test')
    
    def test_price_value(self):
        self.assertEquals(self.product.price, 10)
    
    def test_quantity_value(self):
        self.assertEquals(self.product.quantity, 1)
    
    def test_user_value(self):
        self.assertIs(self.product.user, self.account)
    
    def test_user_may_have_multiple_products(self):
        self.assertEquals(self.account.products.count(), len(self.prodx))
    
