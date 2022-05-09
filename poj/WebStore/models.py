import datetime

from django.db import models
from django.utils import timezone

class Customers(models.Model):
    CustomerID = models.IntegerField(primary_key=True)
    CustomerName = models.CharField(max_length=200)
    OwnsRouter = models.BooleanField(default=False)


  

class CustomerWishList(models.Model):
    #WishID = models.IntegerField(primary_key=True)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    Type = models.CharField(max_length=200)
    AmmountOfItem = models.IntegerField(default=1)
    Price = models.DecimalField(decimal_places=2, max_digits=9)

class WishListPhone(models.Model):
    WishID = models.ForeignKey(CustomerWishList, on_delete=models.CASCADE)
    Brand = models.CharField(max_length=200)
    Quality = models.CharField(max_length=200)
    Generation = models.IntegerField()
    CameraQuality = models.IntegerField()
    PriorityList = models.IntegerField()

class WishListTV(models.Model):
    WishID = models.ForeignKey(CustomerWishList, on_delete=models.CASCADE)
    Brand = models.CharField(max_length=200)
    Hertz = models.IntegerField()
    ScreenType = models.CharField(max_length=200)
    ScreenSize = models.IntegerField()
    PriorityList = models.IntegerField()

class Vender(models.Model):
    VenderID = models.IntegerField(primary_key = True)
    Name = models.CharField(max_length = 200)

class Products(models.Model):
    ProductID = models.IntegerField(primary_key = True)
    Description = models.CharField(max_length=200)
    VenderID = models.ForeignKey(Vender, on_delete=models.CASCADE)
    Price = models.DecimalField(decimal_places=2, max_digits=9)    
    DeliveryCost = models.DecimalField(decimal_places =2, max_digits=9)
    DeliveryLength = models.IntegerField()
    Type = models.CharField(max_length=200)

class Service(models.Model):
    ServiceID = models.IntegerField(primary_key = True)
    Name = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)
    SubscriptionPrice = models.DecimalField(decimal_places=2, max_digits=9)
    SubscriptionLength = models.IntegerField()
    ContractLength = models.IntegerField()
    VenderID = models.ForeignKey(Vender, on_delete=models.CASCADE)

class InternetServices(models.Model):
    ServiceID = models.ForeignKey(Service, on_delete=models.CASCADE)
    Speed = models.IntegerField()
    DataCap = models.IntegerField()
    IncludesRouter = models.BooleanField()

class PhoneServices(models.Model):
    ServiceID = models.ForeignKey(Service, on_delete=models.CASCADE)
    Lines = models.IntegerField
    DataCap = models.IntegerField()
    HotSpot = models.BooleanField()
    Speed = models.IntegerField()

class Phones(models.Model):
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Brand = models.CharField(max_length=200)
    Quality = models.CharField(max_length=200)
    Generation = models.IntegerField()
    CameraQuality = models.IntegerField()

class TVs(models.Model):
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Brand = models.CharField(max_length=200)
    Hertz = models.IntegerField()
    ScreenType = models.CharField(max_length=200)
    ScreenSize = models.IntegerField()
