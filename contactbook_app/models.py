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
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  picture = models.FileField(null=True, upload_to='picture/')
  phone_number = models.CharField(max_length=15, blank=True, null=True)
  home_address = models.CharField(max_length=100, blank=True, null=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  class Meta:
    db_table = 'user'

class UserActiveTokensManager(models.Manager): 

  def active_user_using_token(self, token):
    user_active_token = self.filter(
      token=token,
      expired_time__gte=datetime.now()
    ).first()
    r_user = user_active_token.r_user
    r_user.is_active = True
    r_user.save()

class UserActiveTokens(models.Model): 
  token = models.UUIDField(db_index=True)
  expired_time = models.DateTimeField()
  r_user = models.ForeignKey(
    'User', on_delete=models.CASCADE
  )

  objects = UserActiveTokensManager()

  class Meta:
    db_table = 'user_active_tokens'


@receiver(post_save, sender=User) 
def publish_token(sender, instance, **kwargs):
  print(datetime.now() + timedelta(hours=5))
  user_active_token = UserActiveTokens.objects.create(
    r_user=instance, 
    token=str(uuid4()),
    expired_time=datetime.now() + timedelta(hours=5)
  )
  
  print(f'http://127.0.0.1:8000/contactbook_app/active_user/{user_active_token.token}')