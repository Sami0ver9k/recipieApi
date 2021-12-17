from typing import ClassVar
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class UserManager(BaseUserManager):
    """new custom user model manager"""

    def create_user(self,email,password=None, **extrafields):

        """creates new user"""
        if not email:
            raise ValueError('no email')
        user=self.model(email=self.normalize_email(email), **extrafields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password=None):

        """creates new user"""
        
        user=self.create_user(email,password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser,PermissionsMixin):
    """custom user model it uses email not user name"""

    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD = 'email'










