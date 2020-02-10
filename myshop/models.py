from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.IntegerField(default=0)