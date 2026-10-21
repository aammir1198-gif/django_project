from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):

        return self.name

class Products(models.Model):

    name = models.CharField(max_length=60)

    price = models.FloatField()

    count = models.IntegerField()

    desciption = models.CharField(max_length=500)

    category = models.ForeignKey(Category , on_delete=models.CASCADE , null=True)