from django.db import models

class Product(models.Model):
    name = models.CharField()
    inPrice = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    desc = models.TextField()
    def __str__(self):
        return self.name
# Create your models here.
