from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.utils import AccountManager

class Account(AbstractUser):
    email = models.EmailField(unique=True, max_length=128)
    username = models.CharField(null=True, blank=True, max_length=32)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_seller = models.BooleanField()
    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
