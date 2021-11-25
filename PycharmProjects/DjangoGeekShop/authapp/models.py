from django.db import models
from django.contrib.auth.models import AbstractUser




class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(default=18, verbose_name='age')