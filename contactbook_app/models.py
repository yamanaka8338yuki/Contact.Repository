from django.db import models
from django.contrib.auth.models import (
  AbstractBaseUser,
  PermissionsMixin,
)
from django.db.models.signals import post_save 
from django.dispatch import receiver
from uuid import uuid4
from datetime import datetime, timedelta
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=100)
  email = models.EmailField(max_length=100, unique=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  picture = models.FileField(null=True, upload_to='picture/')
  phone_number = models.CharField(max_length=15, blank=True, null=True)
  home_address = models.CharField(max_length=100, blank=True, null=True)

  AUTH_CHOICES = [
        ('general', '保護者ユーザー'),
        ('admin', '保育士ユーザー'),
  ]
  auth = models.CharField(max_length=10, choices=AUTH_CHOICES, default='general')


  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  class Meta:
    db_table = 'user'



