import datetime

from django.db import models
from django.utils import timezone

class Customers(models.Model):
    CustomerID = models.IntegerField(primary_key=True)
    CustomerName = models.CharField(max_length=200)
    OwnsRouter = models.BooleanField()

class CustomerWishList(models.Model):
    #WishID = models.IntegerField(primary_key=True)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    Type = models.CharField(max_length=200)
    AmmountOfItem = models.IntegerField()
    Price = models.DecimalField(decimal_places=2, max_digits=9)




