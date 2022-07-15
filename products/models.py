from django.db import models

class Product(models.Model):
    description = models.TextField(max_length=128)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='products')
