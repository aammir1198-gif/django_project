from django.contrib.auth.models import AbstractUser

from django.db import models

class User(AbstractUser):

    full_name = models.CharField(max_length=30)

    phone_number = models.CharField(max_length=11)

    age = models.IntegerField(default=18)