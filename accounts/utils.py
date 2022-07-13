from django.contrib.auth.models import BaseUserManager

class AccountManager(BaseUserManager):
    def _create_user(self, email, first_name, last_name, password, is_seller, is_superuser, **extra_fields):
        email = self.normalize_email(email)
        account = self.model(email=email, first_name=first_name, last_name=last_name, is_seller=is_seller, is_superuser=is_superuser, **extra_fields)
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_user(self, email, first_name, last_name, password, is_seller, **extra_fields):
        return self._create_user(email, first_name, last_name, password, is_seller=is_seller, is_superuser=False, **extra_fields)
    
    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        return self._create_user(email, first_name, last_name, password, is_seller=False, is_superuser=True, **extra_fields)
