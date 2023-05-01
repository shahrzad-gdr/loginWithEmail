from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    email = models.EmailField(verbose_name='email address', unique=True)


    REQUIRED_FIELDS = []