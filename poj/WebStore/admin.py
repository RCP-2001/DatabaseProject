from django.contrib import admin

from .models import Customers, CustomerWishList, WishListPhone, WishListTV, Vender, Products, Service, InternetServices, PhoneServices, Phones, TVs

admin.site.register(Customers)
admin.site.register(CustomerWishList)
admin.site.register(WishListPhone)
admin.site.register(WishListTV)
admin.site.register(Vender)
admin.site.register(Products)
admin.site.register(Service)
admin.site.register(InternetServices)
admin.site.register(PhoneServices)
admin.site.register(Phones)
admin.site.register(TVs)