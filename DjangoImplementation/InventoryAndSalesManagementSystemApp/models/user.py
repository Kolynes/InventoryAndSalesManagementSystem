#-*- coding: utf-8 -*-

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

class Manager(BaseUserManager):
    def create_superuser(self, email, first_name, last_name, password):
        user = User(
            email=email,
            first_name=first_name.title().strip(),
            last_name=last_name.title().strip()
        )
        user.set_password(password)
        user.is_superuser = True
        user.save()

    def create_user(self, email, first_name, last_name, password):
        user = User(
            email=email,
            first_name=first_name.title().strip(),
            last_name=last_name.title().strip()
        )
        user.set_password(password)
        user.save()

class User(AbstractBaseUser):
    class Meta:
        pass

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = Manager()

    def get_dict(self, ):
        return {
            "email": self.email,
            "firstName": self.first_name,
            "last_name": self.last_name
        }




    


