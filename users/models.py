from django.db import models

class UserInfo(models.Model):

    full_name = models.CharField(max_length=30)

    email = models.CharField()

    phone_number = models.CharField(max_length=11)

    age = models.IntegerField()