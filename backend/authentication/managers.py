from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )



        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password,
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        
        return user